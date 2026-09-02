"""Solution agent: reads research.md → crafts solution with RICE/AARRR → cases/{company}/solution.md.

Runs Opus 5 with adaptive thinking to synthesize research into a structured
solution: problem statement, target segment, 3 proposals, RICE prioritization,
proposed solution pick, success metrics, rollout plan, and risks.
"""

import json
import anthropic
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

from src.config import SOLUTION_MODEL, PROMPTS_DIR
from src.tools.file_tools import make_solution_tools, _case_dir

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
                if name == "save_solution":
                    console.print("  [green]Saving solution...[/green]")
                elif name == "read_file":
                    console.print(f"  [dim]Reading: {block.get('input', {}).get('filename', '')}[/dim]")
        else:
            if block.type == "text" and block.text.strip():
                console.print(Markdown(block.text))
            elif block.type == "tool_use":
                if block.name == "save_solution":
                    console.print("  [green]Saving solution...[/green]")
                elif block.name == "read_file":
                    console.print(f"  [dim]Reading: {block.input.get('filename', '')}[/dim]")


def _replay_cached(company: str, archetype: str, cache_path: Path):
    """Replay a cached transcript: re-execute file tools and display output."""
    console.print(Panel("[yellow][CACHED] Replaying saved transcript — no API calls[/yellow]", border_style="yellow"))

    transcript = json.loads(cache_path.read_text())
    tools = make_solution_tools(company, archetype)
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

    console.print("\n[bold green]Solution complete.[/bold green] [yellow](from cache)[/yellow]")


def run_solution(client: anthropic.Anthropic, company: str, question: str, archetype: str, dev: bool = False):
    """Run the solution agent: read research → craft solution → save solution.md."""
    cache_dir = _cache_dir(company)
    cache_path = cache_dir / "solution_transcript.json"

    if dev and cache_path.exists():
        _replay_cached(company, archetype, cache_path)
        return

    if dev:
        console.print("[yellow]No cache found, running live API call...[/yellow]")

    research_path = _case_dir(company) / "research.md"
    if not research_path.exists():
        console.print("[red]Error: research.md not found. Run the research agent first.[/red]")
        return

    system_prompt = (PROMPTS_DIR / "solver.md").read_text()
    system_prompt += f"\n\n## Current Case\n- **Company**: {company}\n- **Case Question**: {question}\n- **Archetype**: {archetype}\n"

    tools = make_solution_tools(company, archetype)

    user_message = (
        f"Create a solution for the following PM case question.\n\n"
        f"**Company**: {company}\n"
        f"**Question**: {question}\n"
        f"**Archetype**: {archetype}\n\n"
        f"Start by reading research.md and data_points.json to understand the research. "
        f"Then craft a compelling solution and save it using the save_solution tool."
    )

    messages = [{"role": "user", "content": user_message}]

    console.print(Panel(f"[bold]Solving:[/bold] {question}", title=f"{company} | {archetype}", border_style="green"))
    console.print("[dim]Reading research and crafting solution...[/dim]\n")

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

    console.print("\n[bold green]Solution complete.[/bold green]")
