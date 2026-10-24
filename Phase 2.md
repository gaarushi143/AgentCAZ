# AgentCAZ — Phase 2 Plan: Evals First

Goal: measure how good AgentCAZ actually is (and whether it beats plain Claude), then improve it one lever at a time.

---

## Part 1: How AgentCAZ is wired

### The map

```
run.py  ──►  src/cli.py  (the orchestrator: fixed order, your checkpoints)
                │
                ├─ 1. classify_archetype()    research.py   single call, no tools
                │
                ├─ 2. run_research()          research.py   AGENT: web_search + save tools
                │        writes → cases/<company>/research.md, data_points.json
                │   ⏸ you review (press Enter)
                │
                ├─ 3. run_solution()          solution.py   reads research → save_solution
                │        writes → cases/<company>/solution.md
                │   ⏸ you review
                │
                └─ 4. run_outline()           outline.py    reads both → save_outline
                         writes → cases/<company>/deck_outline.md
```

### The folders

| Path | What lives there |
|---|---|
| `run.py` | Entry point. Just launches the CLI |
| `src/cli.py` | Commands (`run`, `research`, `solution`, `outline`, `industry`, `list`) and the stage order |
| `src/config.py` | Which model each stage uses, folder paths, the 6 archetypes |
| `src/agents/*.py` | One file per stage: builds the prompt, gives tools, runs the loop, saves a transcript |
| `src/tools/file_tools.py` | The tools each stage gets. Each agent gets its own set |
| `src/prompts/*.md` | The system prompts. **Most of the agent's "behavior" lives here** |
| `cases/<company>/` | Outputs. `.cache/` inside holds transcripts for `--dev` replay |

### Two design details worth knowing

- **Stages talk through files, not code.** Research doesn't hand anything to the solution agent directly; it writes `research.md`, and the solution agent calls `read_file` to load it. That's why you can edit the file at a checkpoint and the next stage picks up your changes.
- **The save tools enforce structure.** `save_solution` requires 8 fields (problem, segment, 3 proposals, RICE…). Claude can't skip a section, because the tool won't accept it. The tool schema doubles as the output template.

### Problems found (these block evals)

| Issue | Where | Why it matters |
|---|---|---|
| **Outputs are saved per company, not per question** | `_case_dir()` | Two Spotify cases overwrite each other. You can't eval 10 cases if 3 are Spotify |
| **Dev-mode classifier returns the wrong archetype** | `classify_archetype()` | With `--dev`, it returns the first cached archetype from *any* company's folder, not this question's |
| **Bad classifier output silently becomes `improve_product`** | same | Hides classification errors; you'll never know it failed |
| **No cost or step logging** | all agents | You can't report "this run cost ₹X and used 14 searches" |
| **No saved runs in the repo** | `.gitignore` | You'll need fresh runs to build a baseline |
| **The evaluator was planned but never built** | `cli.py` prints "evaluation agents not yet implemented"; `EVALUATOR_MODEL` unused | This is the next step anyway |

### How to explore a codebase yourself

1. **Start at the entry point** (`run.py` → `cli.py`) and follow one command end to end
2. **Read the config** to see what's tunable
3. **Read the prompts**; in agent projects, they're half the logic
4. **Run it once** in `--dev` mode or on a cheap case and watch the output
5. **Ask Claude Code** in the repo: "trace what happens when I run `python run.py run -c Spotify -q ...`"

---

## Part 2: The plan

### Step 1: Get it running again

1. Clone the repo locally and `pip install -e .`
2. Copy `.env.example` to `.env`, add your API key
3. **Update model names** in `config.py` to current ones (check the Anthropic docs)
4. Run one cheap case end to end with `--auto` and read all 4 output files
5. Ask yourself: *if a friend handed me this deck outline, would I present it?* Write down 3 things that feel weak. That's your first, informal eval

### Step 2: Fix the foundations

1. **Save outputs per case:** `cases/<company>_<short-hash-of-question>/` so cases never overwrite each other
2. **Fix the dev-mode classifier** to read the cache from *this* case's folder only
3. **Log unknown archetypes** instead of silently defaulting
4. **Add a `run_log.json` per case:** model used per stage, input/output tokens, number of searches, time taken, estimated cost
5. **Add a `CLAUDE.md`** explaining the project, so AI coding tools (and you, in 6 months) understand it fast

### Step 3: Build the eval dataset

1. **Pick 10 cases**, at least 1 per archetype, mixing companies (e.g. Spotify improve, Razorpay monetize, Zomato enter-market)
2. Save them in `evals/cases.json`, each with:
   - `company`, `question`
   - `expected_archetype` (your label)
   - `must_cover`: 2–4 things a good answer must include (e.g. "creator economics" for a Spotify podcasts case)
3. Prefer cases you've already practiced, so you know what good looks like

### Step 4: Run the baseline (paid once, reused forever)

1. Run AgentCAZ on all 10 with `--auto` and keep every output and `run_log.json`
2. **Plain-Claude baseline:** send the same 10 questions to Claude with one simple prompt ("prepare research, a solution and a deck outline for this PM case"). Save those too
3. Total spend is fixed now. Every later eval reuses these files

### Step 5: Write the scorers, cheapest first

| Order | Scorer | Type | Cost |
|---|---|---|---|
| 1 | **Classifier accuracy:** predicted vs. your label | Code | Free |
| 2 | **Structure checks:** every data point has a URL, 3+ competitors, market size present, RICE for all 3 features | Code | Free |
| 3 | **`must_cover` check:** did the solution address the items you listed? | Cheap LLM judge | Very low |
| 4 | **Source verification:** fetch each data-point URL, ask "does this page support this number?" | Cheap LLM judge | Low |
| 5 | **Quality rubric (1–5):** data accuracy, insight, defensibility, deck clarity | **You, by hand**, on all 10 | Free, ~2 hours |
| 6 | **LLM judge for the rubric:** score the same 10, check agreement with your scores | LLM judge | Low |

Put this in `evals/run_evals.py`, outputting `evals/results/<date>.json`. Same shape as WatsRAG.

### Step 6: Read the results and pick one problem

1. Build a simple table: case × scorer, AgentCAZ vs. plain Claude
2. Answer three questions:
   - **Does AgentCAZ beat plain Claude?** Where, and where not?
   - **Which stage is weakest?** (e.g. sources fail 30% of the time → research)
   - **Does the LLM judge agree with you?** If not, don't trust it yet
3. Pick **one** fix, using the 7 levers below

The 7 levers: knowledge/context, tools, instructions, self-checking, architecture (stages looping back), memory across runs, evals.

### Step 7: Improve, re-measure, repeat

1. Make one change (e.g. a critic loop on the solution stage)
2. Re-run **only the affected stage**, reusing cached earlier stages
3. Re-score and compare to the baseline
4. Keep a `CHANGELOG.md`: change → score before → after → kept or reverted

### Step 8: Add tracing and package it

1. **Tracing:** add W&B Weave or Langfuse once the plain script works, so you can show a dashboard of runs and scores
2. **Skills:** turn `prompts/*.md` into skills (`case-research`, `case-solution`, `deck-outline`)
3. **Plugin:** bundle skills + a `/case-prep` command so it runs inside Claude Code
4. **Optional MCP server:** expose `save_data_point` / `read_case` so any Claude client can work with your case files

### Step 9: Write it up

1. README sections: problem → architecture → eval setup → **results vs. plain Claude** → what didn't work → next steps
2. One chart: scores before vs. after your best change
3. A 2-minute demo video
4. A LinkedIn/Substack post: "I evaluated my own AI agent against plain Claude. Here's what I found."

---

## Keeping evals cheap

- Start with 10 cases, not 200
- Code checks before LLM judges
- Evaluate stages separately and reuse saved outputs (`.cache/`, `--dev` replay)
- Use a small, cheap model as the judge, validated against your own scores
- Batch API for overnight eval runs; prompt caching for long system prompts
- Run the full eval only when something changes
- Score the subjective parts by hand on a small set; those labels become the judge's test set

---

## Guardrails

- **Steps 1–6 are the real project.** Steps 7–9 are polish. Getting through Step 6 alone is already a strong story.
- **Expect plain Claude to win some cases.** Don't hide that. "My agent wins on sourcing and structure, loses on creativity, and here's why" is a great interview answer.
- **Resist adding features before Step 6.** That's how projects end up with 4 half-built agents and no evidence.
