"""Research agent: web search + Tool Runner loop → cases/{company}/research.md.

Runs Sonnet 5 with Anthropic's web_search server tool to gather real-time
company data, market sizing, competitors, and user insights. Supports
--dev mode to replay cached transcripts without API calls.
"""

import json
import anthropic
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from src.config import RESEARCH_MODEL, CLASSIFIER_MODEL, PROMPTS_DIR, ARCHETYPES
from src.tools.file_tools import make_file_tools, _case_dir

console = Console()

# Anthropic's built-in server tool for live web search
WEB_SEARCH_TOOL = {"type": "web_search_20260209", "name": "web_search", "max_uses": 20}


def _cache_dir(company: str) -> Path:
    d = _case_dir(company) / ".cache"
    d.mkdir(parents=True, exist_ok=True)
    return d


def classify_archetype(client: anthropic.Anthropic, question: str, dev: bool = False) -> str:
    """Classify a case question into one of 6 PM archetypes via a single API call."""
    if dev:
        # Check all case dirs for a cached archetype matching this question
        from src.config import CASES_DIR
        for d in (CASES_DIR).iterdir() if CASES_DIR.exists() else []:
            cache_file = d / ".cache" / "archetype.txt"
            if cache_file.exists():
                cached = cache_file.read_text().strip()
                if cached in ARCHETYPES:
                    console.print(f"[yellow][CACHED][/yellow] archetype: {cached}")
                    return cached

    prompt = (PROMPTS_DIR / "classifier.md").read_text()
    response = client.messages.create(
        model=CLASSIFIER_MODEL,
        max_tokens=50,
        system=prompt,
        messages=[{"role": "user", "content": question}],
    )
    result = response.content[0].text.strip().lower()
    if result not in ARCHETYPES:
        result = "improve_product"
    return result


def _display_message(message_data):
    """Display a message's content blocks through Rich console."""
    content = message_data if isinstance(message_data, list) else message_data.get("content", [])
    for block in content:
        if isinstance(block, dict):
            block_type = block.get("type", "")
            if block_type == "text" and block.get("text", "").strip():
                console.print(Markdown(block["text"]))
            elif block_type == "tool_use":
                name = block.get("name", "")
                inp = block.get("input", {})
                if name == "web_search":
                    console.print(f"  [dim]Searching: {inp.get('query', '')}[/dim]")
                elif name == "save_research":
                    console.print("  [green]Saving research...[/green]")
                elif name == "save_data_point":
                    console.print(f"  [dim]Data point: {inp.get('fact', '')}[/dim]")
        else:
            if block.type == "text" and block.text.strip():
                console.print(Markdown(block.text))
            elif block.type == "tool_use":
                if block.name == "web_search":
                    console.print(f"  [dim]Searching: {block.input.get('query', '')}[/dim]")
                elif block.name == "save_research":
                    console.print("  [green]Saving research...[/green]")
                elif block.name == "save_data_point":
                    console.print(f"  [dim]Data point: {block.input.get('fact', '')}[/dim]")


def _replay_cached(company: str, archetype: str, cache_path: Path):
    """Replay a cached transcript: re-execute file tools and display output."""
    console.print(Panel("[yellow][CACHED] Replaying saved transcript — no API calls[/yellow]", border_style="yellow"))

    transcript = json.loads(cache_path.read_text())
    file_tools = make_file_tools(company, archetype)
    tool_map = {}
    for tool in file_tools:
        tool_map[tool._name] = tool

    for message_data in transcript:
        content = message_data.get("content", [])
        _display_message(content)

        for block in content:
            if isinstance(block, dict) and block.get("type") == "tool_use":
                name = block.get("name", "")
                inp = block.get("input", {})
                if name in tool_map:
                    try:
                        tool_map[name](**inp)
                    except Exception:
                        pass

    console.print("\n[bold green]Research complete.[/bold green] [yellow](from cache)[/yellow]")


def run_research(client: anthropic.Anthropic, company: str, question: str, archetype: str, dev: bool = False) -> str:
    """Run the research agent: web search loop → save research.md and data_points.json."""
    cache_dir = _cache_dir(company)
    cache_path = cache_dir / "research_transcript.json"

    if dev and cache_path.exists():
        _replay_cached(company, archetype, cache_path)
        return archetype

    if dev:
        console.print("[yellow]No cache found, running live API call...[/yellow]")

    system_prompt = (PROMPTS_DIR / "researcher.md").read_text()
    system_prompt += f"\n\n## Current Case\n- **Company**: {company}\n- **Case Question**: {question}\n- **Archetype**: {archetype}\n"

    file_tools = make_file_tools(company, archetype)
    tools = [WEB_SEARCH_TOOL] + file_tools

    user_message = (
        f"Research the following PM case question thoroughly.\n\n"
        f"**Company**: {company}\n"
        f"**Question**: {question}\n"
        f"**Archetype**: {archetype}\n\n"
        f"Use web search to find real, current data. When you have enough research, "
        f"save it using the save_research tool. Also save individual data points "
        f"with sources using save_data_point."
    )

    messages = [{"role": "user", "content": user_message}]

    console.print(Panel(f"[bold]Researching:[/bold] {question}", title=f"{company} | {archetype}", border_style="blue"))
    console.print("[dim]Starting research with web search...[/dim]\n")

    max_restarts = 5
    restarts = 0
    last = None
    transcript = []

    while True:
        runner = client.beta.messages.tool_runner(
            model=RESEARCH_MODEL,
            max_tokens=16000,
            system=system_prompt,
            tools=tools,
            messages=messages,
        )

        for message in runner:
            last = message
            messages.append({"role": "assistant", "content": message.content})
            tool_response = runner.generate_tool_call_response()
            if tool_response is not None:
                messages.append(tool_response)

            transcript.append(message.to_dict())
            _display_message(message.content)

        if last is None or last.stop_reason != "pause_turn":
            break
        restarts += 1
        if restarts > max_restarts:
            console.print("[yellow]Warning: search hit iteration limit, continuing with available data[/yellow]")
            break

    # Save cache
    cache_path.write_text(json.dumps(transcript, indent=2, default=str))
    archetype_cache = cache_dir / "archetype.txt"
    archetype_cache.write_text(archetype)

    console.print("\n[bold green]Research complete.[/bold green]")
    return archetype
