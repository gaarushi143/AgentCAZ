"""Central configuration: model choices, directory paths, API client factory."""

import os
from pathlib import Path

import anthropic

# Directory paths
PROJECT_ROOT = Path(__file__).parent.parent
CASES_DIR = PROJECT_ROOT / "cases"
PROMPTS_DIR = Path(__file__).parent / "prompts"
TEMPLATES_DIR = PROJECT_ROOT / "templates"

# Model assignments — Opus for reasoning-heavy agents, Sonnet for volume/search
RESEARCH_MODEL = "claude-sonnet-5"
SOLUTION_MODEL = "claude-opus-5"
EVALUATOR_MODEL = "claude-opus-5"
CLASSIFIER_MODEL = "claude-sonnet-5"


def get_client() -> anthropic.Anthropic:
    """Create an Anthropic client, attaching workspace-id header if the key is identity-linked."""
    workspace_id = os.environ.get("ANTHROPIC_WORKSPACE_ID")
    if workspace_id:
        return anthropic.Anthropic(
            default_headers={"anthropic-workspace-id": workspace_id},
        )
    return anthropic.Anthropic()

# The 6 PM case archetypes the classifier can return
ARCHETYPES = [
    "improve_product",
    "build_new_product",
    "enter_market",
    "strategic_bet",
    "diagnose_problem",
    "monetize_asset",
]
