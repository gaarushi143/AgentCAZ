# Deck Outline: Spotify — Improving Podcast Discovery

**Narrative arc:** Spotify won podcast *supply* and lost podcast *discovery* (tension) → the failure is a mechanism mismatch, not a content or demand gap (diagnosis) → target the one segment with proven intent and proven product failure (focus) → three features that change the discovery *input* (payoff) → sequenced, gated, and measured against cannibalization (proof of rigor).

**Reading just the headlines tells the whole story.** 14 slides, data on every slide.

---

## Slide 1: Title

- **Headline**: Spotify Has 7M Podcasts and 6% Podcast Engagement — Fixing the Bridge, Not the Catalog
- **Purpose**: Frame the case question and plant the thesis in the first 10 seconds so the interviewer knows where the deck is going.
- **Convey**: This is a discovery-routing problem, and I already know which side of it I'm arguing.
- **Content**: Case question ("How would you improve Spotify's podcast discovery?"), one-line thesis, presenter name/date. Three small stat chips along the bottom: **7M titles · 6% podcast MAU · 21% share (down from #1)**.
- **Visuals**: Clean title slide, Spotify green accent. Three stat chips as a horizontal strip — no chart.

---

## Slide 2: Problem

- **Headline**: 42M of 713M Users Listen to Podcasts — and Podcasts Are Just 2.8% of Listening Time
- **Purpose**: Establish the problem with the sharpest possible numbers before any solutioning. This is the tension-builder.
- **Convey**: The engagement chasm is enormous, it's on Spotify's own platform with Spotify's own users, and it's getting worse.
- **Content**: Two-column layout. Left = "The chasm": podcast MAU 42.4M vs. total MAU 713M (~6%); podcast listening 1,042 min/yr vs. music 37,229 min/yr (2.8%). Right = "And share is moving the wrong way": YouTube ~39% vs. Spotify ~21% of weekly US podcast consumers; YouTube "used most often" up 31% → 37% in two years, overtaking Spotify. Bottom callout bar: *"Same users. Same app. Same home screen. The gap is product, not audience."*
- **Visuals**: Two-panel visual. Left: a single dramatic proportional area/waffle chart — 713M block with the 42.4M sliver highlighted in green. Right: a slope chart showing YouTube 31%→37% rising and Spotify falling from #1 to 21%, two lines crossing.

---

## Slide 3: Market Context & Stakes

- **Headline**: A $28–48B Market Growing ~25% a Year — and Spotify's $1B Podcast Target Needs This Fixed
- **Purpose**: Prove the prize is worth chasing and tie the product problem to an explicit company commitment. Answers "why does this matter to the business?"
- **Convey**: Demand is booming and Spotify has already spent the money — the only missing piece is the discovery layer.
- **Content**: Three stacked bands. (1) **Market**: TAM $28.2–47.8B in 2025, 23.7–30% CAGR; North America = 38.5% of revenue; US monthly podcast listeners 135M → 158M in one year. (2) **Spotify's investment already sunk**: 7M titles, 500K video podcasts, $100M+ paid to creators in Q1 2025 alone, Partner Program launched. (3) **The commitment**: $1B podcast revenue by 2026. Closing line: *"Supply is bought and paid for. Demand is growing 25% a year. The bottleneck is in between."*
- **Visuals**: Funnel-style diagram: wide "Market demand: 158M US listeners" → wide "Spotify supply: 7M titles" → a visibly pinched middle labeled **"DISCOVERY"** → narrow output "42.4M podcast MAU." Small inset bar showing US listener growth 135M → 158M.

---

## Slide 4: Key Insight

- **Headline**: Spotify Exposes ~50 of Its 7 Million Shows — Because 61% of Discovery Already Happened on YouTube
- **Purpose**: The intellectual centerpiece. Reframes the case from "improve the algorithm" to "change the discovery mechanism." Everything downstream is justified here.
- **Convey**: Three compounding failures explain the chasm — and none of them are fixed by better collaborative filtering.
- **Content**: Three numbered insight cards, each with evidence and the "so what."
  1. **Top-of-funnel disintermediation** — 40% of listeners found their favorite show on YouTube; YouTube + social = 61% of all favorite-show discovery. *So what: in-app recommendations compete for a minority of discovery moments.*
  2. **The long-tail collapse** — recommenders are "optimised for retention at the platform level, not useful discovery at the individual level"; objectives diverge past the top ~50 shows. Spotify pays "tens of millions" to a handful of shows, concentrating surface area. *So what: 7M titles, ~50 exposed.*
  3. **The physics mismatch** — a music engine (3-min items, high repeat, 30-sec skip cost) grafted onto podcasts (45–60 min items, low repeat, severe cold start). *So what: the same tile UI asks for a 55-minute bet.*
  - Bottom banner: **"All three change the INPUT to discovery. None are solved by asking the same objective function for different output."**
- **Visuals**: Side-by-side comparison table "Music physics vs. Podcast physics" (item length, repeat-listen rate, skip/abandon cost, cold-start difficulty, discovery unit) — makes the mismatch undeniable in five rows. Plus a small donut for the 61% off-platform discovery stat.

---

## Slide 5: Segmentation & Target

- **Headline**: I'm Betting on the 50–70M Who Already Tried Podcasts and Bounced — Bigger Than the Entire Habituated Base
- **Purpose**: Show segmentation rigor and make a defensible, non-obvious choice (not the biggest segment).
- **Convey**: The Podcast-Curious Explorer combines proven intent with a failure entirely inside Spotify's control — zero acquisition cost.
- **Content**: Three-column segment comparison table: **Music-First Listener** (~670M / never expressed intent / changing a category preference, not fixing a bug / spillover only) | **Podcast-Curious Explorer** ← highlighted (~50–70M/yr / played ≥1 episode, no habit / cold-start trap + commitment risk / **PRIMARY**) | **Cross-Platform Fan** (subset of 42.4M / discovery job already done by YouTube / grows minutes, not users / Phase 3). Rows: size, JTBD, why they fail today, verdict. Below the table, the explorer's JTBD verbatim: *"Find a show that reliably fits MY niche — not the mainstream top 50 — without hunting."* Supporting evidence strip: 50% looked for a new podcast last month; 45% started a new show in 3 months; 75% of limited-series listeners seek a replacement.
- **Visuals**: Segment comparison table with the middle column visually elevated (green border/shading). Small horizontal bar showing relative segment sizes (670M / 50–70M / ~20M) so the "I chose the middle one on purpose" decision is visible.

---

## Slide 6: Goal & Solution Overview

- **Headline**: Three Features, One Design Principle: Lower the Cost of a Wrong Guess, Make the Right Guess Reachable
- **Purpose**: The pivot from diagnosis to payoff. Maps each feature to a specific root cause so nothing looks like a feature wish-list.
- **Convey**: Each feature attacks a named failure mode, and together they change the input to discovery.
- **Content**: Top band = the goal, stated as numbers: podcast activation (3+ episodes across 2+ shows in 14 days) **12% → 25%**; podcast MAU **42.4M → 70M+ (10% of MAU)**; share of listening time **2.8% → 5%**. Scope guardrails in small type: in-product mobile changes, 4 quarters; out of scope = content deals, pricing, standalone app, paid acquisition. Below: three feature cards, each showing *Root cause → Feature → Mechanism*:
  - Commitment risk + cold start → **Clip Radio** → 45-second sampling replaces a 45-minute bet
  - Long-tail routing failure → **Niche Finder** → stated intent + transcript retrieval + editorial curation
  - Habit-loop breakage → **The Handoff + Podcast Mix** → fire at the highest-intent moment
  - Footer: *Considered and cut for Phase 3 — "Shazam for podcast clips" (serves habituated users, depends on external platforms).*
- **Visuals**: Three-column mapping diagram with arrows from a left "Root Cause" column (from Slide 4) into a right "Feature" column — visually proving 1:1 traceability between diagnosis and solution.

---

## Slide 7: Feature Deep-Dive — Clip Radio

- **Headline**: Clip Radio: Collapse the Cost of a Wrong Guess from 45 Minutes to 45 Seconds
- **Purpose**: The flagship bet deserves its own slide — this is the feature that changes the discovery *mechanism* and directly answers YouTube.
- **Convey**: A swipeable clip feed solves commitment risk and cold-start in a single session, using assets Spotify already owns.
- **Content**: Left half = the experience: full-screen vertical feed of 30–60s auto-extracted podcast moments (video where available, audiogram + live captions where not); three one-tap actions — **▶ Play full episode from here / + Add to Queue / ♡ Follow show**; seeded from the user's *music* taste graph, re-ranked live on swipe behavior. Right half = why it works: 20 swipes generate more preference signal than 20 homepage impressions (forced per-item judgment); the mechanic is exactly what's winning the market (61% of discovery via clips on YouTube/social); Spotify's own proof — management confirmed off-platform video exposure "resulted in net incremental usage on Spotify"; assets in place — 500K video podcasts, 390M users have already streamed one (+54% YoY), 80%+ of US top 50 publish video. Bottom callout — **the critical design decision**: *the ranker is rewarded on episode minutes listened within 48h, NOT clip watch-time.*
- **Visuals**: Annotated mobile mockup (phone frame) of the vertical clip feed with the three tap-targets called out, sized to show "Play full episode" and "Add to Queue" as the largest targets. Beside it, a small flywheel diagram: clips → long-form minutes → Free-tier ad inventory → Partner Program payouts → more creator clips → more discovery.

---

## Slide 8: Feature Deep-Dive — Niche Finder

- **Headline**: Niche Finder: Search 7M Shows by Intent, With Popularity Bias Deliberately Penalized
- **Purpose**: Show the long-tail fix and demonstrate willingness to make an opinionated ranking tradeoff (with a guardrail) — plus the editorial hedge.
- **Convey**: Let users *state* the niche need, match at the episode level, and structurally force exposure below the top 500.
- **Content**: Left = the query experience with three real example prompts: *"a calm history podcast under 30 minutes about the Roman navy," "true crime set in the Pacific Northwest," "something about B2B pricing strategy."* Middle = the two deliberate design decisions: (1) retrieval over **episode-level transcript embeddings**, not show metadata — because long-tail relevance lives at the episode-topic level; (2) **popularity-penalty term** in the ranker — a minimum share of results outside the top 500 by plays, behind a tunable dial with a satisfaction guardrail. Right = **the editorial hedge**: ~200 curator-built "Niche Collections" per market (Regional True Crime, Solo-Founder Podcasts, Under 20 Minutes) — deliberately borrowing Apple's proven strength, which no collaborative filtering produces. Target metric callout: **long-tail play share 15% → 30%**. Constraint note: constrained retrieval only, matching transcript passage shown as evidence, no LLM-authored descriptions.
- **Visuals**: Two-part visual. (1) Search-result mockup showing a natural-language query with results tagged "Top 500" vs. "Long tail," plus the visible "why this matched" transcript snippet. (2) A stacked bar showing today's play distribution (85% top-500 / 15% long tail) versus target (70/30).

---

## Slide 9: Feature Deep-Dive — The Handoff

- **Headline**: The Handoff: 75% of Series-Finishers Want a Replacement — Today We Answer With a Generic Row
- **Purpose**: Showcase the highest-confidence, lowest-effort feature and set up the sequencing argument on the next slide.
- **Convey**: The single highest-intent, lowest-cold-start moment in podcasting is currently wasted — and capturing it ships in six weeks.
- **Content**: Two linked mechanics. (1) **The Handoff** — on finishing a limited series' final episode or catching up on a followed show, fire a full-screen card with **3 curated successors + a one-line "why this"** ("Same narrative producer as *Serial*"; "Also 8 episodes, also unsolved-case format") and a "Start Episode 1" button that auto-queues. (2) **Podcast Mix** — a weekly *episode-level* personalized queue (the Discover Weekly of podcasts): 1 episode from a followed show, 2 adjacent, 2 long-tail explorations, each with a stated runtime. Evidence strip: 75% of limited-series listeners seek a replacement; 50% hunted for a new show last month. Targets: Handoff acceptance **≥18%** (vs. ~2–4% for today's generic row); Podcast Mix weekly return **40%**. Strategic note: *also the cheapest data-generating feature — completion and successor-acceptance events materially improve Clip Radio's cold-start seeding.*
- **Visuals**: A user-journey timeline: "Final episode ends" → **[Handoff card mockup with 3 successors]** → "Episode 1 auto-queued" → "Podcast Mix arrives Monday" → "Weekly habit." Small side-by-side bar: today's generic row ~2–4% acceptance vs. target 18%.

---

## Slide 10: Prioritization

- **Headline**: Clip Radio Wins on RICE — But The Handoff Ships First at One-Fifth the Effort
- **Purpose**: Demonstrate prioritization rigor and, more importantly, a sequencing judgment that goes beyond just sorting a table.
- **Convey**: Ship the fast, high-confidence win to fund, instrument, and *seed* the flagship bet — there's a real dependency, not a convenient story.
- **Content**: RICE table with reasoning column:
  | Feature | Reach/Q | Impact | Conf. | Effort (eng-mo) | RICE |
  |---|---|---|---|---|---|
  | Clip Radio | 100M | 2.0 | 70% | 30 | **4.7M** |
  | The Handoff + Podcast Mix | 25M | 1.2 | 85% | 6 | **4.3M** |
  | Niche Finder | 35M | 1.5 | 80% | 18 | **2.3M** |
  Below, the sequencing recommendation: **Handoff (Q1, 6 weeks) ∥ Clip Radio alpha (Q1) → Clip Radio flagship (Q1–Q3) → Niche Finder (Q2–Q4, editorial starts Q2)**. Three reasons Handoff goes first: (a) fast defensible activation win, (b) builds the instrumented discovery funnel and clean baseline, (c) generates completion/successor data that seeds Clip Radio. Niche Finder is third because it's a *pull* surface — its ceiling is capped until Clip Radio manufactures podcast intent. Pre-empt box: **"Why not just fix the algorithm?" — it isn't broken; it's optimized for platform retention and will re-collapse to popularity under any retention-based loss function. All three features change the input.**
- **Visuals**: RICE table plus a Gantt-style 4-quarter sequencing bar chart showing the three features' overlapping timelines, with a dependency arrow from Handoff's data output into Clip Radio's ranker.

---

## Slide 11: Rollout Plan

- **Headline**: Four Phases, Each With a Kill Criterion: Flat Net Podcast Minutes Means We Stop
- **Purpose**: Show operational credibility and — critically — that I'll shut down my own flagship if the data says so.
- **Convey**: This is a de-risked, gated rollout with a permanent hold-out, not a big-bang launch.
- **Content**: Four-column phase table. **Phase 0 (Wks 0–4) Instrument**: build the Podcast Discovery Funnel (impression→tap→30s→5min→completion→follow→2nd show→W4) cut by segment; ship long-tail share metric; stand up a permanent **1% global hold-out**; extend Partner Program T&Cs for clip consent; negotiate top-20 publishers. **Phase 1 (Q1) Prove intent capture**: Handoff to 5%→25% of podcast MAU (US/UK/CA), *gate: acceptance ≥12%, no completion-rate decline*; Clip Radio closed alpha at 2% (US/UK/Sweden), Wizard-of-Oz — editorially picked clips from ~5,000 opted-in shows, video-only, *gate: clip→episode-start ≥5%, net minutes ≥+5% vs. hold-out, D7 feed return ≥30%*. **Phase 2 (Q2–Q3) Scale the mechanic**: Clip Radio to 20% MAU incl. music-only users, swap in automated extraction + creator clip-picker/veto tool, add audiograms, low-load clip ads; Handoff global + Podcast Mix ships; Niche Finder beta + first 100 Niche Collections. *Gate: share of listening ≥4.0%, long-tail ≥22%, music minutes flat-or-up.* **Phase 3 (Q4+) Flywheel close**: Clip Radio 100%, Niche Finder GA multi-language, TikTok/IG/YouTube deep-linking to exact timestamp, clips wired into Partner Program payouts, launch alongside **Wrapped** — *"your podcast taste, discovered in 60 seconds."*
- **Visuals**: Horizontal phase roadmap (swimlane per feature across Q0–Q4) with diamond-shaped gate markers at each phase boundary, each labeled with its numeric threshold. Red "STOP" marker on the Phase 1 net-minutes gate.

---

## Slide 12: Success Metrics

- **Headline**: North Star: Weekly Habituated Podcast Listeners — +65% in 12 Months
- **Purpose**: Prove measurement rigor across the funnel and show I'm tracking the metrics that could indict the work, not just flatter it.
- **Convey**: Habit formation is the goal, activation is the primary metric, and net incremental minutes is the guardrail that decides the flagship's fate.
- **Content**: North Star at top with definition (≥2 podcast sessions/week across ≥1 followed show) and rationale (measures habit, which is exactly what the explorer lacks). Then a compact AARRR table — 2–3 headline metrics per stage:
  - **Acquisition**: podcast penetration 6% → **10% (≈71M)**; Clip Radio trial 0 → **25%** of exposed MAU; Edison US weekly share 21% → **≥25%**
  - **Activation (primary)**: activation rate ~12% → **25%**; clip→episode-start **≥8%**; clip→qualified listen (>5 min) **≥3%**; Handoff acceptance **≥18%**; time-to-first-follow 9 days → **<2 days**
  - **Retention**: W4 retention of new activations 20% → **35%**; share of listening time 2.8% → **5.0%**; long-tail play share 15% → **30%**
  - **Revenue**: Free-tier podcast ad impressions **+40%**; **$100–150M** annualized incremental run-rate; podcast-active Premium churn **≥15% lower**
  - **Referral**: **1 in 20** clip views shared off-platform; inbound clip-link→episode start **≥35%**; **20,000+** sub-top-500 shows gain net-new followers
  - Distinct bottom band — **⚠️ Guardrails & counter-metrics**: net podcast minutes vs. 1% hold-out **≥+5%, never negative**; episode completion rate within **−5%**; **music minutes must not decline**; creator clip opt-out rate. Note: (est.) baselines confirmed in Phase 0.
- **Visuals**: AARRR funnel graphic on the left with the five stages, metric table on the right. The guardrail band styled distinctly (amber/red border) at the bottom so it reads as a separate commitment.

---

## Slide 13: Risks & Competitive Advantage

- **Headline**: The Real Risk Isn't That Clips Flop — It's That They Succeed and Cannibalize Long-Form
- **Purpose**: Show intellectual honesty on the biggest threat to my own proposal, then close on the durable moat. Combines risk and "why we win."
- **Convey**: The failure modes are named, mitigated, and gated — and Spotify's moat is audio continuity, not a video-feed arms race.
- **Content**: Left two-thirds = risk table (Risk | Why it's real | Mitigation):
  1. **Cannibalization (highest)** — short-form is engineered to satisfy in isolation; clips could snack away the long-form ad inventory that funds the $1B goal → optimize the ranker on **downstream episode minutes**, not clip watch-time; net-minutes-vs-hold-out as a hard phase gate; friction asymmetry (largest tap targets are "Play full episode" / "Add to Queue"); soft session caps + "out of clips" terminal state; keep clip ad load low.
  2. **Creator & rights backlash** — most of 7M titles arrive via third-party RSS; NYT/NPR/iHeart could refuse or object publicly → **opt-in only**, launch on owned + Partner Program catalog; creator clip-picker + veto tool ships *before* scaling automation; verbatim transcript-anchored excerpts only, full attribution; pitch clips as free back-catalog promotion, evidenced by Spotify's own net-incremental-usage finding.
  3. **Long-tail hurts satisfaction** — popularity bias exists because popular shows retain better → tunable dial with completion/save guardrails (within 5%); constrained retrieval with evidence passages, no free generation; editorial Niche Collections as the hedge; DSA-ready "not based on profiling" toggle + "why you're seeing this."
  4. **YouTube retaliates** — ~39% share, 1B+ monthly podcast viewers, best recommender on earth → see right panel.
  Right third = **"We don't fight on their axis"** panel: Spotify's moat is **audio continuity** — eyes-off playback, queue, offline, car/Bluetooth/wearable handoff, and a unified **music + podcast taste graph** YouTube structurally lacks. *A YouTube clip converts into a 45-minute watch you can't take driving. A Clip Radio clip converts into a 45-minute commute listen with one tap.* Plus: treat YouTube as a funnel (Phase 3 deep-linking), and compete in the mid-tail where 7M titles + editorial + Partner Program economics is a **supply** advantage, not a UI advantage — and therefore durable.
- **Visuals**: Risk table with severity coding (highest risk row emphasized). Right panel: a simple two-column "YouTube strength vs. Spotify moat" comparison with icons for the audio-continuity surfaces (car, headphones, offline, queue).

---

## Slide 14: Appendix

- **Headline**: Appendix: Sources, Sizing Logic, and RICE Assumptions
- **Purpose**: Backstop for Q&A — lets me defend any number on demand without cluttering the main deck.
- **Convey**: Every figure in this deck is sourced or transparently estimated.
- **Content**: Four blocks. (1) **Key data points with sources** — MAU 713M (Q3'25); podcast MAU 42.4M; 7M titles / 500K video; 390M video-podcast viewers (+54% YoY); platform share YouTube ~39% / Spotify ~21% / Apple ~8%; 61% discovery via YouTube+social; 2.8% time-spent ratio (MIDiA 1,042 vs. 37,229 min); TAM $28.2–47.8B at 23.7–30% CAGR; 158M US monthly listeners; $1B revenue target; $100M+ Q1'25 creator payouts; Apple catalog 2.82M. (2) **Segment sizing logic** — how 50–70M/yr "tried-and-lapsed" is derived from 42.4M podcast MAU vs. 713M MAU and adjacent-format trial-to-habit funnels. (3) **RICE assumption detail** — Reach derivations (e.g., Clip Radio's 100M = ~15% of 713M MAU tapping a new short-form surface in a quarter, benchmarked against Shorts/Reels adoption and the 390M video-podcast precedent); effort conventions (1 squad-quarter ≈ 30 eng-months). (4) **Estimated baselines flagged for Phase 0 confirmation** — ~12% activation, ~20% W4 retention, ~15% long-tail share, ~9-day time-to-first-follow, 2–4% generic-row acceptance.
- **Visuals**: Dense but organized two-column reference table; no chart. Numbered footnotes matching in-deck citations.
