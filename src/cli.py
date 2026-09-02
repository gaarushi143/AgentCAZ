"""CLI interface — Click commands for running agents individually or as a full pipeline."""

from __future__ import annotations

import click
from dotenv import load_dotenv
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

from src.config import CASES_DIR, get_client
from src.agents.research import classify_archetype, run_research
from src.agents.solution import run_solution
from src.agents.outline import run_outline

console = Console()


@click.group()
def cli():
    """AgentCAZ - PM Interview Case Prep System"""
    load_dotenv()


@cli.command()
@click.option("--company", "-c", required=True, help="Company name")
@click.option("--question", "-q", required=True, help="Case question")
@click.option("--archetype", "-a", default=None, help="Force archetype (auto-detected if omitted)")
@click.option("--dev", is_flag=True, help="Use cached responses instead of calling the API")
def research(company: str, question: str, archetype: str | None, dev: bool):
    """Run the research agent on a case question."""
    client = get_client()

    if archetype is None:
        console.print("[dim]Classifying case archetype...[/dim]")
        archetype = classify_archetype(client, question, dev=dev)
        console.print(f"[bold]Detected archetype:[/bold] {archetype}\n")

    run_research(client, company, question, archetype, dev=dev)

    case_dir = CASES_DIR / company.lower().replace(" ", "_").replace("/", "_")
    research_path = case_dir / "research.md"
    if research_path.exists():
        console.print(f"\n[bold]Research saved to:[/bold] {research_path}")
        console.print("[dim]Review the file and edit as needed before proceeding to solution.[/dim]")


@cli.command("run")
@click.option("--company", "-c", required=True, help="Company name")
@click.option("--question", "-q", required=True, help="Case question")
@click.option("--archetype", "-a", default=None, help="Force archetype")
@click.option("--auto", is_flag=True, help="Skip user checkpoint")
@click.option("--dev", is_flag=True, help="Use cached responses instead of calling the API")
def run_case(company: str, question: str, archetype: str | None, auto: bool, dev: bool):
    """Run the full case pipeline (research -> checkpoint -> solution -> deck + eval)."""
    client = get_client()

    if archetype is None:
        console.print("[dim]Classifying case archetype...[/dim]")
        archetype = classify_archetype(client, question, dev=dev)
        console.print(f"[bold]Detected archetype:[/bold] {archetype}\n")

    # Step 1: Research
    run_research(client, company, question, archetype, dev=dev)

    case_dir = CASES_DIR / company.lower().replace(" ", "_").replace("/", "_")
    research_path = case_dir / "research.md"

    if not auto:
        console.print(Panel(
            f"Research saved to: {research_path}\n\n"
            "Review the research and edit if needed.\n"
            "Press Enter to continue to solution, or Ctrl+C to stop.",
            title="Checkpoint",
            border_style="yellow",
        ))
        input()

    # Step 2: Solution
    run_solution(client, company, question, archetype, dev=dev)

    solution_path = case_dir / "solution.md"

    if not auto:
        console.print(Panel(
            f"Solution saved to: {solution_path}\n\n"
            "Review the solution and edit if needed.\n"
            "Press Enter to continue to deck outline, or Ctrl+C to stop.",
            title="Checkpoint",
            border_style="yellow",
        ))
        input()

    # Step 3: Deck Outline
    run_outline(client, company, question, archetype, dev=dev)

    outline_path = case_dir / "deck_outline.md"
    if outline_path.exists():
        console.print(f"\n[bold]Deck outline saved to:[/bold] {outline_path}")

    console.print("[dim]Deck creation and evaluation agents not yet implemented.[/dim]")


@cli.command()
@click.option("--company", "-c", required=True, help="Company name")
@click.option("--question", "-q", required=True, help="Case question")
@click.option("--archetype", "-a", default=None, help="Force archetype (auto-detected if omitted)")
@click.option("--dev", is_flag=True, help="Use cached responses instead of calling the API")
def solution(company: str, question: str, archetype: str | None, dev: bool):
    """Run the solution agent on existing research."""
    client = get_client()

    if archetype is None:
        console.print("[dim]Classifying case archetype...[/dim]")
        archetype = classify_archetype(client, question, dev=dev)
        console.print(f"[bold]Detected archetype:[/bold] {archetype}\n")

    run_solution(client, company, question, archetype, dev=dev)

    case_dir = CASES_DIR / company.lower().replace(" ", "_").replace("/", "_")
    solution_path = case_dir / "solution.md"
    if solution_path.exists():
        console.print(f"\n[bold]Solution saved to:[/bold] {solution_path}")
        console.print("[dim]Review the file and edit as needed before proceeding to deck.[/dim]")


@cli.command()
@click.option("--company", "-c", required=True, help="Company name")
@click.option("--question", "-q", required=True, help="Case question")
@click.option("--archetype", "-a", default=None, help="Force archetype (auto-detected if omitted)")
@click.option("--dev", is_flag=True, help="Use cached responses instead of calling the API")
def outline(company: str, question: str, archetype: str | None, dev: bool):
    """Generate a slide-by-slide deck outline from existing research and solution."""
    client = get_client()

    if archetype is None:
        console.print("[dim]Classifying case archetype...[/dim]")
        archetype = classify_archetype(client, question, dev=dev)
        console.print(f"[bold]Detected archetype:[/bold] {archetype}\n")

    run_outline(client, company, question, archetype, dev=dev)

    case_dir = CASES_DIR / company.lower().replace(" ", "_").replace("/", "_")
    outline_path = case_dir / "deck_outline.md"
    if outline_path.exists():
        console.print(f"\n[bold]Deck outline saved to:[/bold] {outline_path}")
        console.print("[dim]Review the outline and edit as needed before creating the deck.[/dim]")


@cli.command("list")
def list_cases():
    """List all case directories."""
    if not CASES_DIR.exists():
        console.print("[dim]No cases yet.[/dim]")
        return
    for d in sorted(CASES_DIR.iterdir()):
        if d.is_dir():
            files = [f.name for f in d.iterdir() if f.is_file()]
            console.print(f"  [bold]{d.name}[/bold] — {', '.join(files) or 'empty'}")


if __name__ == "__main__":
    cli()
