"""AgentCAZ web UI — a minimal Flask front end for the case prep pipeline.

Two modes:
  * Demo: replays saved cases from demo/ (no API calls, free).
  * Live: runs the real agents; needs ACCESS_CODE and is capped per day.

Run locally:
    python -m web.app            # http://localhost:5000
"""

from __future__ import annotations

import datetime as dt
import hmac
import json
import os
import re
import sys
from pathlib import Path

import markdown
from dotenv import load_dotenv
from flask import Flask, abort, jsonify, render_template, request

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
load_dotenv(ROOT / ".env")

from src.config import ARCHETYPES  # noqa: E402
from web.runner import JOBS, STAGES, Job  # noqa: E402

DEMO_DIR = ROOT / "demo"
OUTPUT_FILES = {
    "research": "research.md",
    "data_points": "data_points.json",
    "solution": "solution.md",
    "outline": "deck_outline.md",
}
MAX_RUNS_PER_DAY = int(os.environ.get("MAX_LIVE_RUNS_PER_DAY", "5"))
_runs_today = {"date": None, "count": 0}

app = Flask(__name__)


# -- helpers --------------------------------------------------------------------

_CITE_OPEN = re.compile(r'[(<]cite index="[^"]*">')


def clean_md(text: str) -> str:
    """Strip web-search citation markup and raw HTML before rendering."""
    text = _CITE_OPEN.sub("", text).replace("</cite>", "")
    return text.replace("<", "&lt;")


def render_outputs(folder: Path) -> dict:
    """Return rendered HTML + raw text for each output file that exists."""
    out = {}
    for key, name in OUTPUT_FILES.items():
        path = folder / name
        if not path.exists():
            continue
        raw = path.read_text()
        if key == "data_points":
            try:
                points = json.loads(raw)
            except json.JSONDecodeError:
                points = []
            out[key] = {"points": points, "raw": raw, "name": name}
        else:
            cleaned = clean_md(raw)
            html = markdown.markdown(cleaned, extensions=["tables", "fenced_code", "sane_lists"])
            out[key] = {"html": html, "raw": _CITE_OPEN.sub("", raw).replace("</cite>", ""), "name": name}
    return out


def demo_cases() -> list[dict]:
    return json.loads((DEMO_DIR / "cases.json").read_text())


def live_enabled() -> bool:
    return bool(os.environ.get("ACCESS_CODE")) and bool(os.environ.get("ANTHROPIC_API_KEY"))


def _check_daily_limit() -> bool:
    today = dt.date.today().isoformat()
    if _runs_today["date"] != today:
        _runs_today.update(date=today, count=0)
    if _runs_today["count"] >= MAX_RUNS_PER_DAY:
        return False
    _runs_today["count"] += 1
    return True


# -- pages ----------------------------------------------------------------------

@app.get("/")
def index():
    return render_template(
        "index.html",
        demos=demo_cases(),
        archetypes=ARCHETYPES,
        live_enabled=live_enabled(),
    )


@app.get("/healthz")
def healthz():
    return "ok"


# -- demo -----------------------------------------------------------------------

@app.get("/api/demo/<slug>")
def demo(slug: str):
    case = next((c for c in demo_cases() if c["slug"] == slug), None)
    if case is None:
        abort(404)
    outputs = render_outputs(DEMO_DIR / slug)
    return jsonify({**case, "outputs": outputs, "stages": STAGES})


# -- live -----------------------------------------------------------------------

@app.post("/api/run")
def start_run():
    if not live_enabled():
        return jsonify(error="Live runs aren't enabled on this deployment."), 403
    body = request.get_json(force=True) or {}
    code = str(body.get("code", ""))
    if not hmac.compare_digest(code, os.environ["ACCESS_CODE"]):
        return jsonify(error="That access code isn't right."), 403

    company = str(body.get("company", "")).strip()[:80]
    question = str(body.get("question", "")).strip()[:500]
    if not company or not question:
        return jsonify(error="Add a company and a case question."), 400
    archetype = body.get("archetype") if body.get("archetype") in ARCHETYPES else None

    if not _check_daily_limit():
        return jsonify(error=f"Daily limit of {MAX_RUNS_PER_DAY} live runs reached. Try the demo."), 429

    job = Job(company, question, archetype, pause=bool(body.get("pause", True)))
    JOBS[job.id] = job
    job.start()
    return jsonify(job.to_dict())


@app.get("/api/run/<job_id>")
def run_status(job_id: str):
    job = JOBS.get(job_id) or abort(404)
    data = job.to_dict()
    # Only show files this run produced (the case folder may hold older runs).
    produced = {"research": "research", "data_points": "research", "solution": "solution", "outline": "outline"}
    outputs = render_outputs(job.case_dir())
    data["outputs"] = {k: v for k, v in outputs.items() if job.stages[produced[k]] == "done"}
    return jsonify(data)


@app.post("/api/run/<job_id>/continue")
def run_continue(job_id: str):
    job = JOBS.get(job_id) or abort(404)
    if job.state != "checkpoint" or not job.next_stage:
        return jsonify(error="This run isn't waiting for review."), 409
    job.start(job.next_stage)
    return jsonify(job.to_dict())


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
