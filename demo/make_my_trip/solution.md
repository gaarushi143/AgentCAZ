# Solution: Make My Trip

## Case Archetype
improve_product

## Problem Statement
**MakeMyTrip's AI is solving the problem it has already won, and ignoring the one that is killing its brand.**

Myra 2.0 has genuinely fixed steps 1–5 of the journey (discovery → booking): 3M+ conversations/quarter, 8-language voice, ~10% higher conversion than the standard flow, 45%+ of usage from Tier-2/3 cities. But steps 6–7 — in-trip disruption and post-booking recovery — are unmanaged. MakeMyTrip carries a **1.2/5 Trustpilot rating (2,000+ reviews)** and **1.4/5 on PissedConsumer (17% would recommend, 1,016 reviews)**, and the complaint themes are almost entirely post-booking: hotels with "no record" of a confirmed, card-charged booking; cancellations resolved only as non-cash wallet credit; and an AI chatbot with no human escalation path during real emergencies (a 3:35am cab no-show before a flight; a same-day medical cancellation).

Meanwhile **Ixigo's TARA resolved 3.81M queries in Q3 FY26 (up from 2.11M in Q4 FY25) with 76% of voice calls fully AI-resolved end-to-end**, and is explicitly positioned on proactive disruption management, flight tracking, and automatic refunds. The #2 player is building its AI moat precisely where MakeMyTrip is weakest.

This matters commercially, not just reputationally. With **~50%+ of the addressable OTA market already captured** (FY25 gross bookings of $9.8B against conservative market estimates of $19–25B), further growth cannot come from share gains — it must come from (a) digitizing first-time Tier-2/3 travelers and (b) wallet share per traveler. Both require trust. And MakeMyTrip is currently buying growth instead: **FY25 sales & marketing spend rose 34.1% YoY to $165.3M, outpacing revenue growth (+27.4%)**, while Q1 FY26 profit fell to $9.1M from $25.8M. Leaky retention is being papered over with paid acquisition.

**Scoped problem:** Reduce post-booking trust failure for MakeMyTrip's ~35M annual transacting users — starting with the Tier-2/3 first-time digital traveler — by using AI to (1) verify supplier-side booking integrity *before* the traveler arrives, (2) predict and pre-empt disruption, and (3) adjudicate and refund to the original payment method automatically, so that AI reduces cost-to-serve *and* raises repeat rate simultaneously.

## Target Segment
**Primary: The Emerging Explorer — first-time and infrequent Tier-2/Tier-3 digital traveler (domestic hotel + flight/bus).**

Why this segment:

1. **It is already the AI-native segment.** 45%+ of Myra conversations come from Tier-2 and smaller cities, and voice usage there is ~50% higher than in metros. This segment has demonstrated it will adopt a conversational/voice AI interface — so a new AI capability faces no adoption barrier here. Any feature we ship lands on warm ground.

2. **It is the company's primary growth vector.** With ~50%+ of the addressable online OTA market already held, incremental gross bookings come disproportionately from expanding the pie via Tier-2/3 digitization (India has 900M+ wireless data users; domestic air traffic projected to double by 2030), not from taking share from players clustered at 7–9% each.

3. **It is the segment most damaged by the current failure mode, and least able to defend itself.** A first-time traveler with limited English fluency cannot parse a fare rule, cannot detect a phantom booking, and will not escalate a wallet-credit-instead-of-cash refund through a consumer forum. The research calls this a **monetizable trust asymmetry**: the segment MakeMyTrip most needs is the segment currently absorbing the most unresolved harm. One bad disruption permanently loses a lifetime traveler — and for a first-time online buyer, it also loses their household and referral network.

4. **It is the highest-leverage retention pool.** MakeMyTrip has 75M lifetime transacted users across MMT/Goibibo/redBus but is spending $165M/year to keep filling the top of the funnel. Converting a first-time Tier-2/3 booker into a repeat booker is far cheaper than acquiring a new one — and trust, not discount, is the binding constraint for this cohort.

**Deliberately deprioritized (for now):**
- *The Deal Optimizer (metro frequent traveler)* — high volume and vocal about mid-flow price drift, but already well served, price-elastic rather than trust-elastic, and will follow discounts regardless. They benefit from the solution as a spillover.
- *The Complex Itinerary Planner (international/bleisure/myBiz)* — highest *severity* per failure (missed international connection, denied check-in abroad, "unreachable phone lines from USA/UK") and strategically important (int'l = ~25% of FY25 revenue, int'l hotels +65% YoY). But international supplier integrations, multi-currency refunds, and 24×7 multi-timezone escalation make it the wrong place to start. **It is the Phase 3 monetization target**, where willingness-to-pay for protection is highest.

## Solution Proposals
**Feature 1 — "Myra Guardian" (Agentic Trip Protection: verify → predict → make whole)**

An always-on post-booking agent that owns the trip from confirmation to check-out, built on three loops:

- **Booking Assurance loop:** Within 60 minutes of booking, and again 24h before check-in/departure, Myra performs an automated supplier-side handshake — PMS/extranet API call where available, and an **agentic outbound voice/WhatsApp call to the hotel front desk in the local language** for the long tail of unbranded Tier-2/3 properties that have no API. If the supplier has no record, the traveler is auto-rebooked into an equal-or-better property *before* they travel, not after they are turned away at the desk. Output: a live "Booking Assured ✓" status in the app, replacing today's hollow "confirmed."
- **Disruption Prediction loop:** Monitors flight status, weather, airline schedule-change feeds, cab driver-accept latency, and historical supplier reliability to score each leg's disruption risk. When risk crosses a threshold, Myra acts *first* — pre-emptive cab reassignment, alternate flight options pre-loaded, hotel late-arrival notification — and messages the traveler in their language with one-tap choices rather than a link to a support queue.
- **Make-Whole loop:** An AI claims adjudicator that classifies the failure (supplier no-show, cancellation, service gap), applies fare/cancellation rules, and **auto-refunds to the original payment method within 24 hours below a defined value threshold — cash by default, wallet only if the user chooses it.** Critically, it also includes a **"Human in 60 Seconds" trigger**: an intent+sentiment classifier that detects in-trip emergencies (stranded, medical, same-day, abroad) and *skips the bot entirely*, routing to a live agent with the full trip context pre-loaded.

*Pain point:* The #1 complaint theme across Trustpilot (1.2/5), PissedConsumer (1.4/5), and ComplaintsBoard — phantom bookings, forced wallet refunds, and AI-only support that cannot escalate.
*Flywheel:* Directly attacks the flywheel's weak link. Post-booking intent data (which suppliers fail, which routes break, which travelers churn after disruption) feeds supply-side negotiation and ranking — MakeMyTrip can demote unreliable hotels and charge reliable ones for placement. Higher repeat rate lowers dependence on the $165M marketing line; higher AI resolution rate lowers cost-to-serve per booking. It is the only proposal that improves both revenue *and* the productivity metric Rajesh Magow explicitly named as AI's purpose.

---

**Feature 2 — "Bharosa Mode" (Vernacular Trust Layer for the pre-commit moment)**

A voice-first confidence layer that activates at the highest-anxiety point of the funnel — the seconds before payment. Three components: (a) **Fare Rules, Explained** — Myra reads back cancellation/change/baggage terms in plain spoken Hindi/Tamil/Telugu/Marathi/Bengali/Kannada/Malayalam ("if you cancel 3 days before, you get ₹4,200 of ₹6,000 back"), not legal text; (b) **Price Lock** — the quoted total is locked for 10 minutes from the moment of selection, with an AI check that flags and auto-honors the original fare if backend pricing drifts mid-flow; (c) **Pre-Pay Sanity Check** — an agent that catches the mistakes first-timers actually make (name/passport mismatch, wrong date, wrong airport code for same-named cities, non-refundable fare on a flexible-need trip) before the card is charged.

*Pain point:* Fare-rule illiteracy, distrust of online payment, and the repeated "price changed twice after I selected the flight" complaint.
*Flywheel:* Lifts conversion at the commit step for the exact cohort Myra over-indexes on, extending the ~10% Myra conversion lift. Cheap, fast, low-risk.

---

**Feature 3 — "Intent Bridge" (be the transaction layer of AI-led discovery)**

Turn the Feb 2026 OpenAI collaboration from an integration into a distribution channel. Expose MakeMyTrip's live inventory, pricing, and now *booking-integrity* signals as an agentic commerce endpoint so that a traveler who begins in ChatGPT/Gemini can complete a booking without leaving the conversation — plus a WhatsApp-native Myra so the assistant lives where Tier-2/3 India actually spends its time, and proactive pre-trip cross-sell (forex, insurance, intercity cabs — the fastest-growing "other" line, ~+30% YoY CC) fired at the 90-day-out engagement window where 35%+ of travelers already talk to Myra.

*Pain point:* Not a user pain point — a *company* pain point: the strategic risk that general assistants intercept travel intent before it reaches the app, disintermediating the OTA layer the way aggregators disintermediated hotels.
*Flywheel:* Defends the top of the funnel and could reduce paid-acquisition dependence over time. But it is a platform bet whose economics depend on a partner's roadmap, not MakeMyTrip's own execution.

## RICE Prioritization
Reach = unique users materially touched per year. Impact scale: 0.25 minimal / 0.5 low / 1 medium / 2 high / 3 massive. Effort in engineer-months. Baseline: ~35M annual transacting users across MMT/Goibibo/redBus (against 75M lifetime), ~65M annual transactions implied by $9.8B gross bookings.

---

**Feature 1 — Myra Guardian**
- **Reach: 35M/year.** Every booking gets the assurance handshake and risk monitoring, not just the ~8–12% of trips that actually break. Verification is a universal surface; recovery is the tail.
- **Impact: 2.5 (high→massive).** Uniquely hits three P&L lines at once: (i) retention — it repairs the single most-cited churn cause in 3,000+ public reviews; (ii) cost-to-serve — Ixigo's 76% AI-resolved voice benchmark proves 60–75% deflection of post-booking contacts is achievable; (iii) supply quality — reliability scoring improves ranking and negotiating leverage. No other feature compounds like this.
- **Confidence: 80%.** High on the AI/adjudication side (Ixigo has externally validated the pattern at 3.81M queries/quarter). The discount is supplier-integration coverage for long-tail Tier-2/3 properties and refund-float economics.
- **Effort: 24 engineer-months.** Heaviest of the three: supplier API/extranet handshakes, outbound agentic voice, disruption-risk models, refund rails to original payment method, escalation routing, fraud controls.
- **RICE = 35M × 2.5 × 0.8 / 24 = ~2.92M**

**Feature 2 — Bharosa Mode**
- **Reach: 15M/year.** ~12M Myra conversations/year (3M/quarter) plus adjacent commit-step traffic that can be routed through the layer.
- **Impact: 1.5 (medium→high).** A real conversion and trust lift at the commit moment — but it improves a step MakeMyTrip already leads (Myra already converts ~10% better), and it does nothing for the disruption complaints driving the 1.2/5 rating.
- **Confidence: 85%.** Highest of the three. Myra 2.0 already has 8-language voice and multimodal autofill; this is orchestration on proven rails. Price Lock is a product-policy decision more than an ML problem.
- **Effort: 8 engineer-months.**
- **RICE = 15M × 1.5 × 0.85 / 8 = ~2.39M**

**Feature 3 — Intent Bridge**
- **Reach: 6M/year.** Speculative. AI-led discovery traffic is real but early; the addressable slice that both starts in a general assistant *and* completes a transaction there is small today.
- **Impact: 1.0 (medium).** Strategically significant, but it defends existing demand rather than creating new booking value — and a booking captured via ChatGPT is a booking MakeMyTrip would largely have won anyway in the near term.
- **Confidence: 50%.** Lowest. Depends on OpenAI's agentic-commerce roadmap, third-party take-rate/economics that aren't yet defined, and consumer habit change that may take years.
- **Effort: 12 engineer-months.**
- **RICE = 6M × 1.0 × 0.5 / 12 = ~0.25M**

---

**Ranking: Guardian (2.92M) > Bharosa Mode (2.39M) > Intent Bridge (0.25M)**

**Honest read of the close call:** Guardian and Bharosa Mode are within ~20% — inside the noise of any RICE estimate. Two tie-breakers decide it in Guardian's favor:

1. **Defensibility.** Bharosa Mode is a feature any of the four 7–9%-share challengers can copy in a quarter. Guardian requires supplier-side integration depth across thousands of properties plus refund infrastructure — assets only the ~50%-share player with volume leverage over hotels and airlines can assemble. RICE measures value; it does not measure moat.
2. **Sequencing logic.** Bharosa Mode makes people *buy* more confidently; Guardian makes them *come back*. Adding conversion polish on top of a 1.2/5 trust base is pouring water into a leaking bucket — and MakeMyTrip is already paying for that leak at $165.3M/year in marketing (+34.1% YoY, outpacing revenue growth).

**Recommendation: build Myra Guardian first.** Bharosa Mode is small enough (8 eng-months) to run as a fast-follow in Phase 2 and is a natural companion — Guardian's disruption data tells Bharosa Mode which fare rules to warn about. Intent Bridge should continue as a lean partnership track, not a product investment, until agentic-commerce economics are proven.

## Proposed Solution
**Build Myra Guardian: turn Myra from a salesperson into a fiduciary.**

Today Myra's job ends at "payment successful." Guardian extends the same agent across the part of the journey where MakeMyTrip currently has no AI at all — verifying with the supplier that the booking is real, predicting the legs that will break, and making the traveler whole in cash, automatically, when they do.

**Why this wins**

*It is the highest-RICE option and the only one that compounds.* At ~2.92M it tops the list, but the more important point is that it is the only proposal that moves revenue and cost simultaneously. Retention lift is direct top-line: on ~65M annual transactions, a 3pp improvement in 12-month repeat rate is roughly 2M incremental transactions, or **~$25–30M of incremental annual revenue at MakeMyTrip's ~$15 revenue-per-transaction** — with zero incremental CAC. At the same time, deflecting 60–70% of post-booking contacts (against Ixigo's demonstrated 76% voice resolution) attacks cost-to-serve, which is exactly the "productivity" mandate leadership has publicly assigned to AI. Nothing else on the list pays twice.

*It attacks the real root cause, not the visible symptom.* The complaint data is unambiguous: users are not churning because search is hard. They are churning because a card-charged "confirmed" booking turned out not to exist, and the only recourse was a chatbot that offered wallet credit. Guardian's Booking Assurance handshake is a root-cause fix — it catches the supplier-system mismatch *before* the traveler is standing at a front desk in a strange city. Every other intervention (better chat, faster refunds) is downstream triage.

*It is the defensive move the competitive map demands.* Ixigo has told the market what its AI strategy is: TARA, proactive disruption management, 3.81M queries resolved in a quarter, 76% AI-resolved voice calls, a "Trip Mode" that tracks flights and files refunds. That is a direct assault on MakeMyTrip's weakest flank, from the fastest-growing challenger. If MakeMyTrip keeps shipping discovery polish while Ixigo owns "the app that takes care of you when things go wrong," the market leader's AI narrative becomes the *shallower* one — a dangerous position when your public rating is 1.2/5 and your challenger trades at ~119x P/E on exactly this story.

*It is the only option whose moat scales with MakeMyTrip's existing advantage.* Guardian's hard part is not the model — it is supplier-side integration across thousands of hotels, buses, and cab partners, plus the commercial leverage to make suppliers accept reliability scoring and SLA penalties. That leverage is precisely what ~50%+ market share and $9.8B in gross bookings buys, and precisely what a 7–9%-share competitor cannot replicate. Ixigo can build the assistant; it cannot build the handshake at MakeMyTrip's supply depth.

**Why the other two fall short**

*Bharosa Mode* scored a close second and is genuinely good — but it optimizes the step MakeMyTrip already wins. Myra already converts ~10% better than the standard flow; spending the flagship AI cycle to make a strong funnel slightly stronger, while the 1.2/5 trust problem goes unaddressed, is the classic PM error of improving the metric you can already move. It is also trivially copyable. Best outcome: ship it in Phase 2, where Guardian's disruption telemetry makes it smarter (Guardian learns which fare rules actually burn people; Bharosa Mode warns about those specific ones).

*Intent Bridge* is strategically the most interesting and operationally the weakest bet right now. At 50% confidence, it hinges on a partner's agentic-commerce roadmap and on consumer habits that haven't formed yet; and it defends demand MakeMyTrip would mostly capture anyway this year. Worse, it is *strengthened* by Guardian rather than competing with it: in a world where a general assistant can surface every OTA's price, price parity is table stakes and the differentiator becomes guarantee quality. "Book through MakeMyTrip — bookings are supplier-verified and refunds go back to your card in 24 hours" is a reason for an AI agent to prefer MakeMyTrip. **Guardian is the thing that makes Intent Bridge worth winning.** Run the partnership lean; build the guarantee.

**Flywheel fit**

MakeMyTrip's flywheel is: transactions → data → personalization → conversion and AOV → margin → reinvestment in marketing and supply → more transactions. Its disclosed vulnerability is that the spin is bought, not earned — marketing up 34.1% YoY to $165.3M, outpacing revenue growth. Guardian converts paid spin into organic spin at three points: it raises repeat rate (transactions without CAC), it generates a *new* proprietary data asset (supplier reliability and disruption telemetry, which no competitor at 7–9% share can accumulate) that improves ranking and supply negotiation, and it lowers support cost per booking, releasing margin back into the wheel. The AI-specific flywheel gets richer too — post-booking outcome data is the missing feedback loop that tells Myra which recommendations actually produced good trips, not just completed checkouts.

**Why it presents well**

It shows judgment over analysis: the obvious answer to "improve MakeMyTrip with AI" is more and better Myra discovery. The defensible answer is to notice that MakeMyTrip's AI spend and MakeMyTrip's customer pain are in different places, name the competitor already exploiting that gap, and reallocate. It also converts the ugliest fact about the company — a 1.2/5 rating — from a liability into the specific, measurable wedge for the recommendation.

## Success Metrics (AARRR)
**North Star: Trust-Adjusted Repeat Rate — % of transacting users who book again within 12 months, reported separately for the cohort that experienced a disruption.** The second number is the one that matters; today it is almost certainly far below the first, and closing that gap is Guardian's whole thesis.

**Acquisition**
- Tier-2/3 first-time-user booking conversion (app install → first completed booking) **+8% relative** within 6 months of "Booking Assured ✓" appearing in the flow and in creative.
- Blended CAC **down 5%** by 12 months, by reallocating ~10% of the $165.3M marketing budget from discount inducement to trust-guarantee messaging. *Guardrail: gross bookings growth must not fall below +18% CC.*
- Organic/direct share of new Tier-2/3 users **+5pp** by month 12.

**Activation** (of the Guardian capability itself)
- **≥90% of eligible bookings supplier-re-confirmed within 60 minutes**, and 100% re-verified at T-24h, by end of Phase 2.
- **Phantom-booking incidents (supplier has no record of a confirmed, charged booking) down 80%** within two quarters of full rollout — measured from the pre-launch complaint-tagged baseline.
- **≥70% of at-risk legs receive a proactive Myra intervention before the traveler contacts support** by month 9.

**Retention**
- Overall 12-month repeat booking rate **+3pp** by month 12 (≈2M incremental transactions on a ~65M base).
- Repeat rate for the disrupted cohort **+15pp** by month 12 — the single sharpest proof point.
- **Trustpilot 1.2 → 2.5 and PissedConsumer 1.4 → 2.8** within 12 months; "% likely to recommend" from 17% → 35%.
- App Store / Play Store rating **+0.5 stars**; share of reviews mentioning "refund," "wallet," or "no human" **down 50%**.

**Revenue**
- **Support cost-to-serve per booking down 30%** by month 12.
- **≥70% of post-booking queries fully AI-resolved end-to-end** by month 12 (benchmark: Ixigo TARA at 76% of voice calls); median in-trip human escalation time **under 60 seconds** for emergency-classified contacts.
- **Refunds issued to original payment method: ≥95%** of refund value (vs. wallet-credit default today) — a cost line we are deliberately accepting in exchange for retention.
- **Incremental revenue of ~$25–30M annualized** by month 18 from retention lift alone (~$15 revenue/transaction × ~2M incremental transactions).
- Phase 3 monetization: **"MMT Assure" premium protection attached to 12% of international bookings** at ~₹299 blended, plus travel-insurance attach rate **+25% relative** — feeding the "other" revenue line already growing ~30% YoY CC.

**Referral**
- **Post-disruption NPS from negative to +20** within 12 months (survey fired 72h after resolution).
- Referral-driven new users in Tier-2/3 **+10pp share** by month 18 — the strongest signal that the trust asymmetry has flipped from liability to advantage.
- **Supplier-side leading indicator:** ≥60% of Tier-2/3 room-night supply covered by a Guardian handshake (API or agentic voice) by month 12 — the input metric that gates everything above.

## Rollout Plan
**Phase 1 — Prove the handshake (Months 0–3): "Booking Assured" MVP**

*Scope:* The narrowest slice that tests the riskiest assumption — can we actually verify a booking supplier-side at scale? Ship two of the three loops only:
1. Post-booking supplier re-confirmation at T+60min and T-24h, via existing PMS/extranet API connections **only** (skip the long tail for now).
2. Auto-refund-to-original-payment-method with AI adjudication, capped at a low value threshold (e.g. ≤₹15,000) for a single clean failure class: **domestic hotel no-record / supplier-side cancellation.**
3. "Human in 60 Seconds" emergency classifier, shipped from day one — non-negotiable, because it is the reputational blast shield.

*Audience:* Domestic hotel bookings in the top 50 Tier-2/3 cities, 10% traffic A/B, Hindi + English. Deliberately excludes flights, cabs, international, and myBiz.

*Ship/kill gate:* ≥85% re-confirmation success on API-connected supply; auto-refund adjudication accuracy ≥95% vs. human audit; zero increase in fraudulent-claim rate; measurable drop in "no record of booking" contacts in the test cell. If re-confirmation coverage lands below ~60% of room nights, stop and re-scope to the agentic-voice path before scaling.

---

**Phase 2 — Close the coverage gap and go proactive (Months 3–9)**

*Iterate on Phase 1 learnings:*
- **Agentic outbound voice/WhatsApp to hotel front desks** in local languages — the unlock for the unbranded Tier-2/3 long tail with no API. This is the hardest and most defensible piece; sequence it second so Phase 1 data tells us exactly which supplier types need it.
- **Disruption Prediction loop goes live:** flight status and schedule-change feeds, weather, cab driver-accept latency, plus a **Supplier Reliability Score** built from Phase 1 telemetry. Pre-emptive cab reassignment and pre-loaded alternate flights with one-tap selection.
- Expand to **domestic flights, intercity cabs, and redBus/Goibibo** (redBus is the ideal second surface: high frequency, low ticket value, fast learning cycles).
- Raise the auto-refund ceiling as adjudication accuracy holds; expand to all 8 Myra voice languages.
- **Fast-follow Bharosa Mode (8 eng-months)** here, fed by Guardian data — warn travelers pre-purchase about the specific fare rules and suppliers that Guardian has learned actually cause trouble. Cheap, and it makes Guardian's value legible *before* the trip, not only after.
- Begin **supply-side commercial conversations**: reliability scoring in ranking, and SLA penalty/chargeback terms for suppliers who fail a verified booking. This is where MakeMyTrip's ~50% share becomes real leverage.

*Gate:* ≥50% AI resolution of post-booking queries; repeat rate in test cell measurably above control; supplier acceptance of SLA terms from at least the top 200 hotel chains/partners.

---

**Phase 3 — Full rollout, monetize, and export the guarantee (Months 9–18)**

- **100% rollout** across MakeMyTrip, Goibibo, and redBus, all categories, all 8 languages.
- **International outbound + myBiz** — the highest-severity, highest-willingness-to-pay segment (~25% of FY25 revenue; int'l hotels +65% YoY), and the one where "unreachable phone lines from USA/UK" is the loudest complaint. Requires 24×7 multi-timezone escalation and multi-currency refund rails, which is exactly why it comes last.
- **Monetization:** launch **"MMT Assure"** — baseline Guardian free for everyone (it is a trust utility, not a paywall), with paid premium tiers for international/complex itineraries (guaranteed rebooking, higher auto-refund ceilings, priority human access) and bundled free into MMT Black. Cross-sell into the fast-growing travel-insurance and forex ancillary lines.
- **Export the guarantee into Intent Bridge:** expose Guardian's verification and refund guarantee as a signal in the OpenAI/agentic-commerce integration, so that when a traveler asks a general assistant, MakeMyTrip is recommended not on price parity but on outcome certainty. This is how the low-RICE Feature 3 becomes valuable — Guardian gives it something to sell.
- **Marketing reallocation:** shift ~10% of the $165.3M budget from discount inducement to a trust campaign ("Verified before you arrive. Refunded to your card, not your wallet."). This is the moment the flywheel converts from bought spin to earned spin.
- **Publish the numbers.** Ixigo discloses TARA's resolution stats because it wins the narrative. MakeMyTrip should disclose re-confirmation rate, AI resolution rate, and refund-to-source percentage quarterly — it forces internal accountability and reclaims the AI story from the challenger.

## Risks & Mitigations
**1. Supplier coverage gap — the long tail of Tier-2/3 properties has no API to handshake with (highest risk; it is the entire thesis)**
If only branded/chain hotels can be verified, Guardian works precisely where the problem is smallest and fails where the Emerging Explorer actually books.
*Mitigation:* Sequence deliberately — Phase 1 tests API-connected supply only, with an explicit ≥60% room-night coverage gate before scaling. Phase 2 closes the gap with **agentic outbound voice/WhatsApp calls to front desks in local languages** (MakeMyTrip already runs 8-language voice for Myra; this reuses that stack in reverse). Where neither works, fall back to a **Supplier Reliability Score** and *demote or de-list* chronically unreliable properties — a lever only the ~50%-share player can credibly pull. Do not show "Assured ✓" on unverifiable inventory; show an honest "Verifying" state. Over-promising a badge would be worse than the status quo.

**2. Auto-refund abuse and refund-float economics — cash refunds cost real money and invite gaming**
Wallet credit exists because it retains float and suppresses payout. Switching to cash-by-default is a deliberate P&L hit, and an auto-approve engine is a fraud magnet.
*Mitigation:* Value-capped auto-approval (start ≤₹15,000, raise only as adjudication accuracy stays ≥95% against human audit); a claims-fraud model using booking, device, and repeat-claim history; mandatory human review above the cap. Recover cost on the supply side via **negotiated SLA penalties/chargebacks against suppliers who fail a verified booking** — the party that caused the loss pays for it. Frame internally as substituting refund cost for CAC: a ₹1,500 cash refund that retains a traveler is cheaper than re-acquiring one against a $165.3M marketing line. Track "refund cost per retained user" as the explicit trade-off metric.

**3. The AI makes it worse — over-automation on the exact surface users already hate**
The single loudest complaint is *AI-only support that cannot escalate*. Shipping more AI into that moment risks confirming the grievance and handing Ixigo a marketing gift.
*Mitigation:* **"Human in 60 Seconds" ships in Phase 1, not Phase 3** — an intent+sentiment classifier that detects stranded/medical/same-day/abroad contexts and bypasses the bot entirely, with full trip context pre-loaded for the agent. A visible, one-tap "talk to a person" affordance on every Guardian message — never buried. Publicly track median emergency escalation time (<60s) as a launch commitment. AI's job here is to *prevent* contacts and to *route* them correctly, not to trap users.

**4. Regulatory and compliance exposure — refunds, consumer protection, and data**
Automated adjudication and refund promises sit inside RBI payment/refund timelines, CCPA (India) guidelines on dark patterns and deficient service, and DPDP Act obligations — while the agentic outbound voice-calling of suppliers and consent for monitoring/notifications add their own surface.
*Mitigation:* Full audit trail for every automated adjudication decision (input signals, rule applied, outcome) to demonstrate non-arbitrary treatment; legal sign-off on "Assured" as a defined service commitment with published terms rather than an open-ended guarantee; explicit opt-in consent for proactive monitoring and messaging; DPDP-compliant data minimization on trip telemetry. Cash-by-default refunds actually *reduce* dark-pattern exposure versus forced wallet credit.

**5. Fast competitive response — Ixigo already has the capability and the narrative**
TARA is live, resolving 3.81M queries/quarter with 76% voice resolution. Ixigo can claim "we did it first."
*Mitigation:* Do not compete on assistant quality — compete on the layer Ixigo cannot reach. **Supplier-side verification and SLA enforcement require supply leverage that a 7–9%-share player does not have.** Ixigo's AI can tell you your flight is delayed; only MakeMyTrip can make thousands of hotels contractually accountable for honoring a verified booking. Move fast on the agentic-voice handshake (Phase 2) to build the coverage lead, and publish coverage/resolution metrics quarterly so the market scores the difference on substance, not on who announced first.
