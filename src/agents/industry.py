"""Industry research agent: web search + Tool Runner loop → industries/{industry}/industry_research.md.

Runs Sonnet 5 with Anthropic's web_search server tool to gather real-time
industry data covering market sizing, competitive dynamics, financial benchmarks,
supply chain, technology trends, and regulatory landscape.
"""

import json
import anthropic
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from src.config import RESEARCH_MODEL, PROMPTS_DIR
from src.tools.file_tools import make_industry_tools, _industry_dir

console = Console()

WEB_SEARCH_TOOL = {"type": "web_search_20260209", "name": "web_search", "max_uses": 20}


def _cache_dir(industry: str) -> Path:
    d = _industry_dir(industry) / ".cache"
    d.mkdir(parents=True, exist_ok=True)
    return d


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
                elif name == "save_industry_research":
                    console.print("  [green]Saving industry research...[/green]")
                elif name == "save_data_point":
                    console.print(f"  [dim]Data point: {inp.get('fact', '')}[/dim]")
        else:
            if block.type == "text" and block.text.strip():
                console.print(Markdown(block.text))
            elif block.type == "tool_use":
                if block.name == "web_search":
                    console.print(f"  [dim]Searching: {block.input.get('query', '')}[/dim]")
                elif block.name == "save_industry_research":
                    console.print("  [green]Saving industry research...[/green]")
                elif block.name == "save_data_point":
                    console.print(f"  [dim]Data point: {block.input.get('fact', '')}[/dim]")


def _replay_cached(industry: str, cache_path: Path):
    """Replay a cached transcript: re-execute file tools and display output."""
    console.print(Panel("[yellow][CACHED] Replaying saved transcript — no API calls[/yellow]", border_style="yellow"))

    transcript = json.loads(cache_path.read_text())
    file_tools = make_industry_tools(industry)
    tool_map = {tool._name: tool for tool in file_tools}

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

    console.print("\n[bold green]Industry research complete.[/bold green] [yellow](from cache)[/yellow]")


def run_industry_research(client: anthropic.Anthropic, industry: str, dev: bool = False):
    """Run the industry research agent: web search loop → save industry_research.md and data_points.json."""
    cache_dir = _cache_dir(industry)
    cache_path = cache_dir / "industry_transcript.json"

    if dev and cache_path.exists():
        _replay_cached(industry, cache_path)
        return

    if dev:
        console.print("[yellow]No cache found, running live API call...[/yellow]")

    system_prompt = (PROMPTS_DIR / "industry_researcher.md").read_text()
    system_prompt += f"\n\n## Current Industry\n- **Industry**: {industry}\n"

    file_tools = make_industry_tools(industry)
    tools = [WEB_SEARCH_TOOL] + file_tools

    user_message = (
        f"Research the following industry thoroughly.\n\n"
        f"**Industry**: {industry}\n\n"
        f"Use web search to find real, current data. Cover all three categories: "
        f"core market & financial topics, dynamics & competition, and trends & external forces. "
        f"When you have enough research, save it using the save_industry_research tool. "
        f"Also save individual data points with sources using save_data_point."
    )

    messages = [{"role": "user", "content": user_message}]

    console.print(Panel(f"[bold]Researching industry:[/bold] {industry}", title="Industry Research", border_style="cyan"))
    console.print("[dim]Starting industry research with web search...[/dim]\n")

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

    cache_path.write_text(json.dumps(transcript, indent=2, default=str))

    console.print("\n[bold green]Industry research complete.[/bold green]")
