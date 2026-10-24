"""Background job runner for the web UI.

Runs the existing AgentCAZ stages (classify -> research -> solution -> outline)
in a background thread, one stage at a time, and records progress so the
browser can poll it. The agent code in src/ is reused unchanged: we only swap
each agent module's console printer for a hook that records events.
"""

from __future__ import annotations

import io
import threading
import time
import uuid

from rich.console import Console

from src.agents import outline as outline_mod
from src.agents import research as research_mod
from src.agents import solution as solution_mod
from src.config import ARCHETYPES, get_client
from src.tools.file_tools import _case_dir

STAGES = ["classify", "research", "solution", "outline"]

JOBS: dict[str, "Job"] = {}

# Agent modules use module-level printers, so only one stage runs at a time.
_STAGE_LOCK = threading.Lock()


def _get(block, key, default=None):
    """Read a field from a content block that may be a dict or an SDK object."""
    if isinstance(block, dict):
        return block.get(key, default)
    return getattr(block, key, default)


class Job:
    def __init__(self, company: str, question: str, archetype: str | None, pause: bool):
        self.id = uuid.uuid4().hex[:12]
        self.company = company
        self.question = question
        self.archetype = archetype
        self.pause = pause
        self.stages = {s: "waiting" for s in STAGES}
        self.state = "running"  # running | checkpoint | done | error
        self.next_stage: str | None = None
        self.log: list[str] = []
        self.searches = 0
        self.data_points = 0
        self.error: str | None = None
        self.started = time.time()
        self.finished: float | None = None

    # -- progress hook ---------------------------------------------------------
    def add_log(self, line: str):
        self.log.append(line)
        self.log = self.log[-60:]

    def display_hook(self, message_data):
        content = message_data if isinstance(message_data, list) else _get(message_data, "content", []) or []
        for block in content:
            btype = _get(block, "type", "")
            name = _get(block, "name", "")
            inp = _get(block, "input", {}) or {}
            if btype == "server_tool_use" and name == "web_search":
                self.searches += 1
                self.add_log(f"Searching “{inp.get('query', '')}”")
            elif btype == "tool_use":
                if name == "save_data_point":
                    self.data_points += 1
                    self.add_log(f"Saved: {inp.get('fact', '')} = {inp.get('value', '')}")
                elif name == "read_file":
                    self.add_log(f"Reading {inp.get('filename', '')}")
                elif name.startswith("save_"):
                    self.add_log(f"Saving {name.replace('save_', '').replace('_', ' ')}…")

    # -- running ---------------------------------------------------------------
    def _run_stage(self, stage: str):
        client = get_client()
        quiet = Console(file=io.StringIO())
        with _STAGE_LOCK:
            for mod in (research_mod, solution_mod, outline_mod):
                mod._display_message = self.display_hook
                mod.console = quiet
            self.stages[stage] = "running"
            if stage == "classify":
                if self.archetype in ARCHETYPES:
                    self.add_log(f"Archetype set by you: {self.archetype}")
                else:
                    self.archetype = research_mod.classify_archetype(client, self.question)
                    self.add_log(f"Detected archetype: {self.archetype}")
            elif stage == "research":
                research_mod.run_research(client, self.company, self.question, self.archetype)
            elif stage == "solution":
                solution_mod.run_solution(client, self.company, self.question, self.archetype)
            elif stage == "outline":
                outline_mod.run_outline(client, self.company, self.question, self.archetype)
            self.stages[stage] = "done"

    def run_from(self, start: str):
        """Run stages from `start`, stopping at a checkpoint if pause is on."""
        self.state = "running"
        self.next_stage = None
        try:
            for i, stage in enumerate(STAGES[STAGES.index(start):], start=STAGES.index(start)):
                self._run_stage(stage)
                nxt = STAGES[i + 1] if i + 1 < len(STAGES) else None
                # Pause after research and solution (classify is too quick to review).
                if nxt and self.pause and stage in ("research", "solution"):
                    self.state = "checkpoint"
                    self.next_stage = nxt
                    return
            self.state = "done"
            self.finished = time.time()
        except Exception as e:  # surface the error in the UI instead of crashing
            for s, st in self.stages.items():
                if st == "running":
                    self.stages[s] = "error"
            self.state = "error"
            self.error = f"{type(e).__name__}: {str(e)[:300]}"
            self.finished = time.time()

    def start(self, stage: str = "classify"):
        self.state = "running"  # set now so a double click can't start it twice
        self.next_stage = None
        threading.Thread(target=self.run_from, args=(stage,), daemon=True).start()

    def to_dict(self) -> dict:
        end = self.finished or time.time()
        return {
            "id": self.id,
            "company": self.company,
            "question": self.question,
            "archetype": self.archetype,
            "stages": self.stages,
            "state": self.state,
            "next_stage": self.next_stage,
            "log": self.log[-8:],
            "searches": self.searches,
            "data_points": self.data_points,
            "elapsed": int(end - self.started),
            "error": self.error,
        }

    def case_dir(self):
        return _case_dir(self.company)
