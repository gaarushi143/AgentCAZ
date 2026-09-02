"""Outline agent: reads research + solution → designs slide-by-slide deck outline → cases/{company}/deck_outline.md.

Runs Opus 5 with adaptive thinking. The model decides slide count and order
based on content strength (typically 8-14 slides). Each slide gets a headline,
purpose, takeaway, content structure, and recommended visuals.
"""

import json
import anthropic
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from src.config import SOLUTION_MODEL, PROMPTS_DIR
from src.tools.file_tools import make_outline_tools, _case_dir

console = Console()


def _cache_dir(company: str) -> Path:
    """Return (and create) the .cache directory inside the company's case dir."""
    d = _case_dir(company) / ".cache"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _display_message(message_data):
    """Display a message's content blocks (text and tool use) through Rich console."""
    content = message_data if isinstance(message_data, list) else message_data.get("content", [])
    for block in content:
        if isinstance(block, dict):
            block_type = block.get("type", "")
            if block_type == "text" and block.get("text", "").strip():
                console.print(Markdown(block["text"]))
            elif block_type == "tool_use":
                name = block.get("name", "")
                if name == "save_outline":
                    console.print("  [green]Saving deck outline...[/green]")
                elif name == "read_file":
                    console.print(f"  [dim]Reading: {block.get('input', {}).get('filename', '')}[/dim]")
        else:
            if block.type == "text" and block.text.strip():
                console.print(Markdown(block.text))
            elif block.type == "tool_use":
                if block.name == "save_outline":
                    console.print("  [green]Saving deck outline...[/green]")
                elif block.name == "read_file":
                    console.print(f"  [dim]Reading: {block.input.get('filename', '')}[/dim]")


def _replay_cached(company: str, archetype: str, cache_path: Path):
    """Replay a cached transcript: re-execute file tools and display output."""
    console.print(Panel("[yellow][CACHED] Replaying saved transcript — no API calls[/yellow]", border_style="yellow"))

    transcript = json.loads(cache_path.read_text())
    tools = make_outline_tools(company, archetype)
    tool_map = {tool._name: tool for tool in tools}

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

    console.print("\n[bold green]Deck outline complete.[/bold green] [yellow](from cache)[/yellow]")


def run_outline(client: anthropic.Anthropic, company: str, question: str, archetype: str, dev: bool = False):
    """Run the outline agent: read research + solution → design slide narrative → save deck_outline.md."""
    cache_dir = _cache_dir(company)
    cache_path = cache_dir / "outline_transcript.json"

    if dev and cache_path.exists():
        _replay_cached(company, archetype, cache_path)
        return

    if dev:
        console.print("[yellow]No cache found, running live API call...[/yellow]")

    solution_path = _case_dir(company) / "solution.md"
    if not solution_path.exists():
        console.print("[red]Error: solution.md not found. Run the solution agent first.[/red]")
        return

    system_prompt = (PROMPTS_DIR / "outliner.md").read_text()
    system_prompt += f"\n\n## Current Case\n- **Company**: {company}\n- **Case Question**: {question}\n- **Archetype**: {archetype}\n"

    tools = make_outline_tools(company, archetype)

    user_message = (
        f"Create a slide-by-slide deck outline for the following PM case.\n\n"
        f"**Company**: {company}\n"
        f"**Question**: {question}\n"
        f"**Archetype**: {archetype}\n\n"
        f"Start by reading research.md and solution.md. "
        f"Then design the narrative arc and save the outline using the save_outline tool."
    )

    messages = [{"role": "user", "content": user_message}]

    console.print(Panel(f"[bold]Outlining deck:[/bold] {question}", title=f"{company} | {archetype}", border_style="magenta"))
    console.print("[dim]Reading research and solution, designing slide narrative...[/dim]\n")

    last = None
    transcript = []

    runner = client.beta.messages.tool_runner(
        model=SOLUTION_MODEL,
        max_tokens=16000,
        system=system_prompt,
        tools=tools,
        messages=messages,
        thinking={"type": "adaptive"},
    )

    for message in runner:
        last = message
        messages.append({"role": "assistant", "content": message.content})
        tool_response = runner.generate_tool_call_response()
        if tool_response is not None:
            messages.append(tool_response)

        transcript.append(message.to_dict())
        _display_message(message.content)

    cache_path.write_text(json.dumps(transcript, indent=2, default=str))

    console.print("\n[bold green]Deck outline complete.[/bold green]")
