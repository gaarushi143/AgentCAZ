"""@beta_tool definitions for reading/writing case files.

Each make_*_tools() factory returns a list of tools scoped to a specific
company's case directory. The tool docstrings and Args serve double duty:
they document the code AND generate the JSON schema the model sees.
"""

import json
from pathlib import Path

from anthropic import beta_tool

from src.config import CASES_DIR


def _case_dir(company: str) -> Path:
    """Return (and create) the case directory for a company, e.g. cases/spotify/."""
    safe_name = company.lower().replace(" ", "_").replace("/", "_")
    d = CASES_DIR / safe_name
    d.mkdir(parents=True, exist_ok=True)
    return d


def make_file_tools(company: str, archetype: str = ""):
    """Build the research agent's tool set: save_research, save_data_point, read_file."""
    case_dir = _case_dir(company)

    @beta_tool
    def save_research(
        company_context: str,
        business_model_flywheel: str,
        market_analysis: str,
        competitor_landscape: str,
        user_segments: str,
        user_journey: str,
        key_insights: str,
        data_points: str,
    ) -> str:
        """Save the completed research to a structured markdown file.

        Args:
            company_context: Company overview including mission, revenue, key products, and recent strategic moves.
            business_model_flywheel: How the company makes money and what reinforcing loops drive growth (e.g. more users -> more data -> better recommendations -> more users).
            market_analysis: Market sizing (TAM/SAM/SOM) with growth rates, trends, and sources.
            competitor_landscape: Competitor matrix comparing features, pricing, positioning, and market share.
            user_segments: 2-3 user segments with Jobs-to-be-Done analysis and pain points.
            user_journey: Step-by-step map of the current user experience for the primary segment — from discovery/entry through core action to outcome. Identify friction points, drop-off moments, and unmet needs at each step.
            key_insights: 3-5 non-obvious insights that could drive a differentiated solution.
            data_points: All verified numbers with source URLs, formatted as a list.
        """
        content = f"""# Research: {company}

## Case Archetype
{archetype}

## Company Context
{company_context}

## Business Model / Flywheel
{business_model_flywheel}

## Market Analysis
{market_analysis}

## Competitor Landscape
{competitor_landscape}

## User Segments
{user_segments}

## User Journey
{user_journey}

## Key Insights
{key_insights}

## Data Points
{data_points}
"""
        path = case_dir / "research.md"
        path.write_text(content)
        return f"Research saved to {path}"

    @beta_tool
    def save_data_point(fact: str, value: str, source_url: str) -> str:
        """Store a verified data point with its source for use in the deck.

        Args:
            fact: What the data point describes, e.g. "Spotify monthly active users".
            value: The numeric value, e.g. "626 million".
            source_url: URL where this data was found.
        """
        path = case_dir / "data_points.json"
        data = []
        if path.exists():
            data = json.loads(path.read_text())
        data.append({"fact": fact, "value": value, "source": source_url})
        path.write_text(json.dumps(data, indent=2))
        return f"Saved: {fact} = {value}"

    @beta_tool
    def read_file(filename: str) -> str:
        """Read a file from the current case directory.

        Args:
            filename: Name of the file to read, e.g. "research.md" or "data_points.json".
        """
        path = case_dir / filename
        if not path.exists():
            return f"File not found: {filename}"
        return path.read_text()

    return [save_research, save_data_point, read_file]


def make_solution_tools(company: str, archetype: str = ""):
    """Build the solution agent's tool set: read_file, save_solution."""
    case_dir = _case_dir(company)

    @beta_tool
    def read_file(filename: str) -> str:
        """Read a file from the current case directory.

        Args:
            filename: Name of the file to read, e.g. "research.md" or "data_points.json".
        """
        path = case_dir / filename
        if not path.exists():
            return f"File not found: {filename}"
        return path.read_text()

    @beta_tool
    def save_solution(
        problem_statement: str,
        target_segment: str,
        solution_proposals: str,
        rice_prioritization: str,
        proposed_solution: str,
        success_metrics: str,
        rollout_plan: str,
        risks_and_mitigations: str,
    ) -> str:
        """Save the completed solution to a structured markdown file.

        Args:
            problem_statement: Specific, scoped problem restatement grounded in research data.
            target_segment: The primary user segment chosen, with justification and data.
            solution_proposals: 3 proposed features, each with a name, description, pain point addressed, and how it strengthens the flywheel.
            rice_prioritization: RICE scoring (Reach, Impact, Confidence, Effort) for each feature with reasoning and final recommendation.
            proposed_solution: The single recommended solution to implement, with a compelling argument for why this one wins over the other two. Include what makes it the highest-impact choice, why the others fall short, and how it aligns with the company's flywheel.
            success_metrics: Metrics mapped to AARRR framework with specific targets and timeframes for the proposed solution.
            rollout_plan: Phased GTM plan covering MVP, iteration, and full rollout.
            risks_and_mitigations: 3-4 risks with concrete mitigations.
        """
        content = f"""# Solution: {company}

## Case Archetype
{archetype}

## Problem Statement
{problem_statement}

## Target Segment
{target_segment}

## Solution Proposals
{solution_proposals}

## RICE Prioritization
{rice_prioritization}

## Proposed Solution
{proposed_solution}

## Success Metrics (AARRR)
{success_metrics}

## Rollout Plan
{rollout_plan}

## Risks & Mitigations
{risks_and_mitigations}
"""
        path = case_dir / "solution.md"
        path.write_text(content)
        return f"Solution saved to {path}"

    return [read_file, save_solution]


def make_outline_tools(company: str, archetype: str = ""):
    """Build the outline agent's tool set: read_file, save_outline."""
    case_dir = _case_dir(company)

    @beta_tool
    def read_file(filename: str) -> str:
        """Read a file from the current case directory.

        Args:
            filename: Name of the file to read, e.g. "research.md", "solution.md", or "data_points.json".
        """
        path = case_dir / filename
        if not path.exists():
            return f"File not found: {filename}"
        return path.read_text()

    @beta_tool
    def save_outline(outline_content: str) -> str:
        """Save the completed deck outline to a markdown file.

        Args:
            outline_content: The full deck outline in markdown format, with each slide's headline, purpose, convey, content, and visuals.
        """
        path = case_dir / "deck_outline.md"
        path.write_text(outline_content)
        return f"Deck outline saved to {path}"

    return [read_file, save_outline]
