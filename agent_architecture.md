# AgentCAZ — PM Interview Case Prep Multi-Agent System

## Context
Preparing for PM campus interviews where companies give case questions (6 archetypes: improve product, build new product, enter market, strategic bet, diagnose problem, monetize asset). Need to produce solutions, Canva decks, and prototypes for ~3 companies in a week. This system automates the research, solutioning, deck creation, and evaluation pipeline.

## Architecture Overview

```
User (CLI)
    │
    ▼
Orchestrator (Python)
    │
    ├─ Step 1 ──► Classifier call (single API call, classifies archetype)
    │
    ├─ Step 2 ──► Research Agent (Tool Runner loop w/ web search)
    │                  │
    │                  ▼
    │             cases/{company}/research.md
    │
    ├─ PAUSE ──► User reviews research, approves/edits solution direction
    │
    ├─ Step 3 ──► Solution Agent (Tool Runner, drafts solution.md)
    │
    ├─ PAUSE ──► User reviews solution, approves/edits
    │
    ├─ Step 4 ──► Outline Agent (Tool Runner, drafts deck_outline.md)
    │
    ├─ PAUSE ──► User reviews deck outline, approves/edits slide structure
    │
    ├─ Step 5 ──► [parallel via asyncio]
    │               ├── Deck Agent (Tool Runner + Canva API) → Canva design
    │               └── Evaluator Agent (Tool Runner) → evaluation.md
    │
    └─ Step 6 ──► Refinement (if evaluator flags critical gaps → re-run targeted research)
```

**Stack**: Python + `anthropic` SDK (Tool Runner — `client.beta.messages.tool_runner`)
**No Managed Agents beta needed** — each agent is a separate Tool Runner call with its own system prompt, model, and tools. Python `asyncio` handles parallelism.
**Deck output**: Canva API (via `canva-api` Python package or direct REST)
**Web search**: Anthropic's built-in server tool (`web_search_20260209`)
**Storage**: Local filesystem, organized per company/case

---

## How Tool Runner Multi-Agent Works

Each "agent" is a function that runs `client.beta.messages.tool_runner(...)` with:
- A specific **system prompt** (loaded from `prompts/`)
- A specific **model** (Opus or Sonnet)
- A specific **tool set** (custom `@beta_tool` functions + server tools)

Python code orchestrates the sequence — no framework needed:

```python
async def run_case(company: str, question: str):
    # Step 1: Classify
    archetype = await classify_archetype(question)
    
    # Step 2: Research
    await run_research_agent(company, question, archetype)
    
    # Step 3: User checkpoint
    print(f"Research complete. Review: cases/{company}/research.md")
    input("Press Enter to continue, or edit the file first...")
    
    # Step 4: Solution
    await run_solution_agent(company, archetype)
    
    # Step 5: User checkpoint
    print(f"Solution complete. Review: cases/{company}/solution.md")
    input("Press Enter to continue, or edit the file first...")
    
    # Step 6: Deck Outline
    await run_outline_agent(company, question, archetype)
    
    # Step 7: User checkpoint
    print(f"Outline complete. Review: cases/{company}/deck_outline.md")
    input("Press Enter to continue, or edit the file first...")
    
    # Step 8: Deck + Eval in parallel
    await asyncio.gather(
        run_deck_agent(company, archetype),
        run_evaluator_agent(company)
    )
    
    # Step 9: Refinement if needed
    eval_result = read_evaluation(company)
    if eval_result.has_critical_gaps:
        await run_refinement(company, eval_result.gaps)
```

---

## Agent Definitions

### 1. Research Agent
- **Model**: `claude-sonnet-5` (cost-efficient for high-volume search)
- **Role**: Deep research on the company, market, competitors, users
- **Tools**:
  - `web_search_20250305` (Anthropic built-in server tool) — for live search
  - `@beta_tool save_research` — writes structured output to `cases/{company}/research.md`
  - `@beta_tool save_data_point` — stores verified numbers (revenue, MAU, market size) with sources
- **System prompt includes**: CIRCLES framework for problem decomposition, TAM/SAM/SOM for market sizing
- **Output format** — structured markdown:
  ```
  # Research: {Company} — {Case Question}
  ## Case Archetype: {type}
  ## Company Context (mission, revenue, key products, recent moves)
  ## Market Analysis (TAM/SAM/SOM with sources)
  ## Competitor Landscape (matrix: feature/pricing/positioning)
  ## User Segments (personas, pain points, JTBD)
  ## Key Insights (3-5 non-obvious findings)
  ## Data Points (verified numbers with source URLs)
  ```

### 2. Solution Agent
- **Model**: `claude-opus-5` (needs strong reasoning for creative solutioning)
- **Role**: Reads research, proposes solution with prioritization
- **Tools**:
  - `@beta_tool read_file` — reads research.md and archetype template
  - `@beta_tool save_solution` — writes solution.md
- **System prompt includes**: RICE prioritization, AARRR metrics, archetype-specific solution patterns
- **Output**: `cases/{company}/solution.md` with:
  - Problem restatement (specific, scoped)
  - Target user segment (one primary)
  - Solution proposal (3 features, prioritized via RICE)
  - Success metrics (AARRR-mapped)
  - GTM / rollout plan
  - Risks and mitigations

### 3. Outline Agent
- **Model**: `claude-opus-5` (needs strong reasoning for narrative structure)
- **Role**: Designs a slide-by-slide deck outline from research + solution
- **Tools**:
  - `@beta_tool read_file` — reads research.md and solution.md
  - `@beta_tool save_outline` — writes deck_outline.md
- **System prompt includes**: Common slide types menu, narrative arc guidance, headline writing rules
- **Slide count**: Model decides based on content strength (typically 8-14 slides)
- **Output**: `cases/{company}/deck_outline.md` with per-slide: headline, purpose, convey, content structure, recommended visuals

### 4. Deck Agent
- **Model**: `claude-sonnet-5`
- **Role**: Creates Canva slide deck from research + solution
- **Tools**:
  - `@beta_tool read_file` — reads research.md, solution.md, archetype template
  - `@beta_tool create_canva_design` — wrapper around Canva API to create a presentation
  - `@beta_tool add_slide` — adds a slide with content to the Canva design
  - `@beta_tool export_deck` — exports the design as PDF
- **Slide structure** (adapts per archetype):
  1. Title slide (company + case question)
  2. Problem statement / opportunity
  3. User segments & insights
  4. Solution overview (MVP scope)
  5. Feature prioritization (RICE scores)
  6. Success metrics & KPIs
  7. Go-to-market / rollout plan
  8. Risks & mitigations
  9. Appendix (market data, competitor matrix, sources)
- **Output**: Canva design URL + exported PDF in `cases/{company}/deck.pdf`

### 5. Evaluator Agent
- **Model**: `claude-opus-5` (needs strong reasoning for nuanced scoring)
- **Role**: Scores the solution against PM interview rubrics, identifies gaps
- **Tools**:
  - `@beta_tool read_file` — reads research.md and solution.md
  - `@beta_tool save_evaluation` — writes evaluation.md
  - `web_search_20250305` — to fact-check claims made in the solution
- **Scoring rubric** (each scored 1-5 with justification):
  - **Problem framing**: Clear scope? Right problem?
  - **User centricity**: Specific segments with real pain points?
  - **Solution creativity**: Non-obvious, defensible?
  - **Prioritization rigor**: Framework applied, tradeoffs justified?
  - **Metrics quality**: SMART, tied to business outcomes?
  - **Feasibility**: Technical + business viability?
  - **Communication clarity**: Narrative flow, data-backed?
- **Output**: `cases/{company}/evaluation.md`:
  ```
  # Evaluation: {Company}
  ## Overall Score: X/35
  ## Dimension Scores (1-5 each with justification)
  ## Strengths (what will impress the interviewer)
  ## Critical Gaps (must fix before presenting)
  ## Suggested Improvements
  ## Missing Data Points (go research these)
  ## Likely Interviewer Questions (prepare answers for these)
  ```

---

## PM Frameworks Baked Into Prompts

| Framework | Used By | Purpose |
|-----------|---------|---------|
| CIRCLES | Research Agent | Structured problem decomposition |
| TAM/SAM/SOM | Research Agent | Market sizing |
| RICE | Solution Agent | Feature prioritization |
| AARRR (Pirate Metrics) | Solution Agent | Metrics selection |
| Jobs-to-be-Done | Research Agent | User need identification |
| Porter's Five Forces | Research Agent (enter market archetype) | Competitive analysis |

---

## Data Flow

```
User inputs: company name + case question
         │
         ▼
    Classify archetype (single API call)
         │
         ▼
    Research Agent ──► cases/{company}/research.md
         │
         ▼
    *** USER CHECKPOINT ***
    (review research, approve direction)
         │
         ▼
    Solution Agent ──► cases/{company}/solution.md
         │
         ▼
    *** USER CHECKPOINT ***
    (review solution, approve/edit)
         │
         ▼
    Outline Agent ──► cases/{company}/deck_outline.md
         │
         ▼
    *** USER CHECKPOINT ***
    (review outline, approve/edit slide structure)
         │
    ┌────┴────┐
    ▼         ▼
  Deck     Evaluator
  Agent      Agent        ← parallel via asyncio.gather
    │         │
    ▼         ▼
  deck.pdf  evaluation.md
    │         │
    └────┬────┘
         ▼
    If critical gaps → targeted re-research → update solution → regenerate
         │
         ▼
    cases/{company}/final_summary.md
```

---

## Project Structure

```
AgentCAZ/
├── src/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point (click)
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── research.py     # Research agent: Tool Runner + web_search + custom tools
│   │   ├── solution.py     # Solution agent: reads research, outputs solution
│   │   ├── outline.py      # Outline agent: reads research + solution, outputs deck outline
│   │   ├── deck.py         # Deck agent: reads outline, calls Canva API
│   │   └── evaluator.py    # Evaluator agent: reads all outputs, scores and critiques
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── file_tools.py   # @beta_tool wrappers for read/write to cases/
│   │   └── canva_tools.py  # @beta_tool wrappers for Canva API
│   ├── prompts/
│   │   ├── classifier.md   # Archetype classification prompt
│   │   ├── researcher.md   # Research agent system prompt (includes CIRCLES, TAM/SAM/SOM)
│   │   ├── solver.md       # Solution agent system prompt (includes RICE, AARRR)
│   │   ├── outliner.md     # Outline agent system prompt (slide narrative design)
│   │   ├── deck_maker.md   # Deck agent system prompt
│   │   └── evaluator.md    # Evaluator system prompt (scoring rubric)
│   └── config.py           # Model choices, API keys, paths
├── templates/               # Slide structure templates per archetype
│   ├── improve_product.md
│   ├── build_new_product.md
│   ├── enter_market.md
│   ├── strategic_bet.md
│   ├── diagnose_problem.md
│   └── monetize_asset.md
├── cases/                   # Output directory (created at runtime)
├── .env                     # ANTHROPIC_API_KEY, CANVA_API_KEY
├── requirements.txt         # anthropic, click, python-dotenv, httpx
└── pyproject.toml
```

---

## CLI Interface

```bash
# Run a new case (full pipeline)
python -m src.cli run \
  --company "Spotify" \
  --question "Spotify's podcast discovery has low engagement. How would you improve it?"

# Run with auto mode (skip checkpoint)
python -m src.cli run --company "Spotify" --question "..." --auto

# Re-run just research
python3 run.py research -c "Spotify" -q "..."

# Re-run just solution (after editing research)
python3 run.py solution -c "Spotify" -q "..." -a improve_product

# Re-run just deck outline (after editing solution)
python3 run.py outline -c "Spotify" -q "..." -a improve_product

# List all cases
python3 run.py list
```

---

## Canva Integration

Use **Canva Connect API (REST)** via `httpx`:
- Create designs from templates, add pages with content, export as PDF
- Requires Canva API key (free tier available at canva.dev)
- Wrapped in `@beta_tool` functions so the Deck Agent calls them naturally
- Fallback: if Canva API setup is slow, generate slide content as structured markdown first, copy into Canva manually (still saves 80% of the work)

## Search Strategy

Using **Anthropic's built-in `web_search_20260209` server tool** for both Research and Evaluator agents. Single API key, no extra dependencies. Can swap in Perplexity later by replacing one `@beta_tool` function if deeper research quality is needed.

---

## Phased Build Plan

### Week 1: Research + Evaluation pipeline
1. **Project scaffolding** — directory structure, pyproject.toml, .env, config
2. **System prompts** — write all 5 prompts (classifier, researcher, solver, deck_maker, evaluator)
3. **File tools** — `@beta_tool` wrappers for reading/writing to `cases/`
4. **Research Agent** — Tool Runner + `web_search_20250305` → `research.md`
5. **Solution Agent** — reads research, applies RICE/AARRR → `solution.md`
6. **Evaluator Agent** — reads research + solution, scores → `evaluation.md`
7. **Orchestrator v1** — sequential pipeline with user checkpoint
8. **Test end-to-end** with a sample case

### Week 2: Deck + Polish
9. **Canva API integration** — auth, design creation, slide addition, export
10. **Deck Agent** — reads solution, creates Canva deck per archetype template
11. **Parallel execution** — `asyncio.gather(deck_agent, evaluator)`
12. **Refinement loop** — evaluator gaps trigger targeted re-research
13. **CLI polish** — progress bars, colored output, error handling
14. **Template library** — all 6 archetype slide structures

---

## Model Cost Estimates

| Agent | Model | ~Tokens/run | ~Cost/run |
|-------|-------|-------------|-----------|
| Classifier | Sonnet 5 | 2K | ~$0.02 |
| Research | Sonnet 5 | 50K (search-heavy) | ~$0.50 |
| Solution | Opus 5 | 10K | ~$0.45 |
| Outline | Opus 5 | 8K | ~$0.35 |
| Deck | Sonnet 5 | 15K | ~$0.15 |
| Evaluator | Opus 5 | 15K | ~$0.70 |
| **Total per case** | | | **~$2.15** |

*Costs are rough estimates based on current pricing. Web search tool has additional per-search costs.*

---

## Key Design Decisions

1. **Tool Runner over Managed Agents** — no beta access needed, standard API key works, same multi-agent behavior via Python orchestration
2. **Filesystem as the handoff protocol** — agents read/write markdown files in `cases/{company}/`, simple, inspectable, and manually editable between steps
3. **Human-in-the-loop checkpoints** — user reviews research, solution, and deck outline at each stage before proceeding (skippable with `--auto`)
4. **Archetype-specific templates** — deck structure adapts based on case type
5. **Evaluator + Deck in parallel** — no dependency between them, `asyncio.gather` saves time
6. **Opus for reasoning, Sonnet for volume** — evaluator and solution agent need strong reasoning; research and deck agents do more mechanical work

---

## Verification Plan
1. Run a test case end-to-end: "How would you improve Spotify's podcast discovery?"
2. Verify `research.md` contains real, sourced data (not hallucinated numbers)
3. Verify evaluator catches a planted gap (e.g., remove metrics section from solution, confirm evaluator flags it)
4. Verify Canva deck has correct number of slides matching the archetype template
5. Test the user checkpoint flow (pause, edit research.md, continue)
6. Test `--auto` mode (no pause)
7. Time the full pipeline — target under 5 minutes per case
8. Run 3 cases for different archetypes to verify template switching
