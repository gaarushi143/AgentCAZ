# Research: RazorpayX

## Case Archetype
improve_product

## Company Context
**RazorpayX** is the business-banking / neobanking arm of Razorpay, India's largest payment gateway (founded 2014, Bengaluru, by Harshil Mathur & Shashank Kumar). Razorpay overall processes ~$180B in annualised Total Payment Volume (TPV) across 8M+ merchants, holds ~55% of India's online PG market, and posted FY25 consolidated revenue of ₹3,783 crore (+65% YoY), though it reported a ₹1,209 crore loss in FY25 due to tax/restructuring costs from its reverse-flip to India ahead of a planned IPO. Payments still contribute ~75% of group revenue (down from 90% two years ago), with RazorpayX and adjacent products making up the rest.

Launched in 2018 (earlier as "Opfin"), RazorpayX is the company's fastest-growing segment: $30B in annualised transaction volume (85% YoY growth), 50,000+ businesses, and ~5% of all digital money transfers in India. It operates via partner banks (RBL, YES Bank, IDFC First, Axis) offering a traditional Current Account, or "RazorpayX Lite" (instant-KYC digital account on an existing bank account) for lighter use cases.

**Product suite relevant to this case:**
- **Current Account** (partner-bank-backed, cheque book, debit card) or **Lite** (quick KYC digital account)
- **Payouts** (API/dashboard, NEFT/RTGS/IMPS/UPI, ₹2-5/payout after 250 free/month)
- **Payout Links** (send a link via SMS/email; beneficiary enters bank/UPI details — no fund-account setup needed)
- **Vendor Payments / AP Automation / Source to Pay**: OCR invoice capture, 3-way PO-GRN-invoice matching, multi-layer approval workflows (team- and amount-based), TDS auto-calculation, vendor self-serve KYC portal, one-click payouts, accounting integrations (Tally, Zoho Books, QuickBooks)
- **Corporate Cards** (with YES Bank/RBL): up to ₹2 Cr unsecured credit, FD-backed secured option, unlimited add-on cards with per-card/category/MCC limits, default roles = Owner/Admin, Finance, Cardholder, Viewer
- **Payroll**, **Tax Payments**, accounting integrations

RazorpayX's own case studies and testimonials are overwhelmingly from startups, SaaS companies, and digital-native marketplaces (Kissht, MPL, Supermoney, Astrotalk, Bangalore Brewing Company) — not owner-run manufacturing/retail SMEs. The product language throughout ("dashboard," "approval workflow," "bulk import," "finance teams") assumes a desk-based finance function, consistent with the case brief's framing.

**Strategic context**: Razorpay is preparing for an India IPO (confidential DRHP filed, targeting ₹5,000-6,000 crore raise), and leadership has flagged RazorpayX's AI-driven "CFO co-pilot" ambitions and continued neobanking expansion as a growth vector beyond the now-EBITDA-profitable core payments business.

## Business Model / Flywheel
**Core flywheel (Payments → Banking → Lending cross-sell):**
1. Razorpay acquires a business as a payment-gateway customer (collections) — low-friction API/dashboard onboarding, KYC, developer-first docs drive fast activation.
2. Collections generate transaction data and a trusted financial relationship → Razorpay cross-sells RazorpayX (current account, payouts) to capture the *outflow* side of the same business's money movement, turning a one-sided gateway relationship into a full banking relationship.
3. More businesses on RazorpayX → more transaction/cash-flow data → enables Razorpay Capital (working-capital loans) underwritten on transaction history with low default rates — a high-margin, sticky product.
4. Each additional product (Payroll, Tax Payments, Corporate Cards, Vendor Payments) increases switching costs and "share of financial wallet," reinforcing retention and defensibility — described internally as RazorpayX growing 85% YoY off this cross-sell motion.
5. Scale (8M+ merchants, $180B TPV) gives Razorpay negotiating leverage with banks/networks, funding further product bundling.

**For this case, the flywheel implication is critical**: RazorpayX's primary growth loop today depends on businesses *already* having digital, bank-routed collections (i.e., they are Razorpay payment-gateway customers first). Owner-run SMEs (retail shops, small factories) largely are *not* Razorpay gateway customers for collections — they collect via personal/business UPI QR on PhonePe/GPay/Paytm rails directly, bypassing Razorpay's PG entirely. This means the natural cross-sell entry point (PG customer → RazorpayX) doesn't exist for this segment; RazorpayX must win them cold on the payments/vendor-management side alone, which is a structurally harder, lower-trust entry motion.

**Secondary flywheel opportunity (this case's thesis)**: If RazorpayX becomes the system of record for *staff-initiated* vendor payments + digital khata at these SMEs, it could create a new loop — more staff transactions → richer per-vendor and per-person transaction data → better credit underwriting for both the SME (working capital) and potentially its vendors (supply-chain finance) → deeper lock-in. This would effectively open a *new* acquisition funnel into RazorpayX (via the outflow/vendor side) rather than relying on the existing PG-led funnel — directly growing TAM for Razorpay Capital.

## Market Analysis
**TAM/SAM/SOM (owner-run SME vendor-payment & reconciliation tooling in India):**

- **Total MSME base**: India has an estimated 63.4 million MSMEs (630.5 lakh micro, 3.3 lakh small, ~5,000 medium); 4.72 crore are formally Udyam-registered as of mid-2026. MSMEs employ ~111 million people and contribute ~27-31% of GDP and ~45-48% of exports.
- **Target segment (5-20 employees, owner-run, no finance team)**: No official census bucket matches exactly, but this sits within the "micro-to-small" band. Using a conservative estimate that a meaningful fraction of the ~3.3 lakh registered "small" enterprises plus the upper tail of "micro" enterprises (those with paid staff beyond the owner, i.e., employing 5-20 people) fall in-segment, a reasonable estimate is **several million businesses** nationally (this is an inference, not an official figure — no primary source precisely sizes "5-20 employee, owner-run, no finance team" businesses).
- **TAM proxy — digital payments flowing through this segment**: UPI P2M (person-to-merchant) transactions reached 67.01 billion in H1 2025 alone (37% YoY growth), with 86% of P2M transactions under ₹500 — i.e., small-ticket, high-frequency, exactly the profile of vendor/staff payments described in the case. UPI overall processed ₹314 lakh crore annually (FY25-26).
- **Market growth driver**: UPI QR codes grew 91.5% YoY to 658 million in FY25, with ~70 million QR-enabled merchants — most of them exactly the kirana/small-factory/food-business vendors this case describes paying into. This is sometimes called the "Kirana Effect."
- **SAM — RazorpayX's current footprint**: 50,000+ businesses on RazorpayX processing $30B annualised — but these skew toward digitally-native startups/SaaS/marketplaces per RazorpayX's own case studies, not owner-run manufacturing/retail SMEs. This suggests the owner-run SME segment is a largely *untapped* SAM for RazorpayX specifically, even though it's a massive, already-digitized (UPI-first) payments market overall.
- **SOM**: Realistically, a v1 product targeting owner-run SMEs would start with a few thousand pilot businesses in dense SME clusters (e.g., textile/chemical/packaging manufacturing belts in Gujarat, Tamil Nadu, Delhi-NCR) before scaling.

**Key behavioral market trend**: A government-backed survey (10,378 respondents, 2,199 merchants, 15 states) found UPI is now preferred by 57% vs cash at 38%, and 94% of small merchants accept UPI, with 72% satisfied and 57% reporting a sales increase from digital payments. This confirms collection-side digitization is largely solved; the gap (per the case brief) is on the *payment-out* / record-keeping side.

**Adjacent market — digital khata apps**: OkCredit alone claims 5M+ installs (other sources cite 30M+ MSME users) across 50+ business categories and 2,800+ cities, indicating massive unmet demand for simple, mobile-first credit/ledger tracking among exactly this SME profile — but these apps run *parallel to*, not *integrated with*, actual bank-rail payments, which is the core gap RazorpayX could close.

**Sources**: IBEF MSME sector overview; datarankindia.com Udyam statistics (2026); Mordor Intelligence/IMARC UPI market reports; PIB/NPCI UPI decade report (2025); RBI Annual Report FY25 (via Medianama); OkCredit.in; AngelOne/Worldline H1 2025 report.

## Competitor Landscape
**India — direct/adjacent competitors**

| Player | Who initiates payment | Spend controls | Receipt/bill capture | Vendor balance tracking | Pricing | Segment fit |
|---|---|---|---|---|---|---|
| **RazorpayX Vendor Payments** | Owner/finance via dashboard | Amount/team-based approval workflows | OCR invoice upload (desk-based) | Yes, via invoice/bill module | Subscription + ₹2-7/payout | Startups/SaaS with a finance person |
| **Open Money** | Owner/finance; VISA debit cards issued to employees with set limits | Per-card limits via dashboard | Manual invoice/bill entry | Auto-reconciliation of AP/AR (paid tiers) | Free–₹6,999/mo tiers | SMEs/startups, broader reach than RazorpayX into SME banking |
| **EnKash** | Admin issues prepaid/virtual cards instantly (<60 sec) to employees/vendors | MCC-locked, reloadable limits per card | OCR + petty cash/UPI-based expense controls | Ledger via expense management suite | Platform fee + card fees | Mid-size businesses, branch/petty-cash use cases — closest analogue to "staff card" model |
| **Happay** | Admin issues prepaid cards; employees spend | Daily/weekly/channel limits, lock/unblock | Multi-source auto-capture (OCR, WhatsApp, email, SMS) via "Xpendite" | Branch Petty Cash Management module | Enterprise-priced (contact for pricing) | Mid-to-large enterprises; has a "Branch Petty Cash" product conceptually adjacent to factory-manager float |
| **Fyle** | Employee via card swipe | Policy enforced in real time | Real-time credit card network API capture (no manual receipt) | Accounting sync (QuickBooks/Xero/NetSuite) | $6.99+/user/mo | Mid-market/MNC subsidiaries in India |
| **Vyapar** | Owner/staff records *after the fact*; no payment initiation | N/A — it's a billing/ledger tool, not a payment rail | Manual entry | Core strength: GST billing + supplier/customer ledger, multi-user access | Low-cost subscription | 1.5 Cr+ Indian SMEs — massive install base but **no payment execution**, pure record-keeping |
| **OkCredit / Khatabook / Bahi Khata apps** | N/A — ledger only, often used for *customer* credit (receivables), some use for supplier/payable tracking | None | Manual entry, photo of old registers | This IS the product — udhar/khata ledger with reminders | Free/freemium | Kirana/micro-retail; proves massive demand for "khata," but disconnected from actual bank rails |
| **Zoho Books + BillPay** | Finance team via dashboard | Approval workflows, vendor portal | OCR auto-scan | Vendor bills tracked; purchase orders | ₹ per org/month tiers, free tier <₹25L turnover | SMEs comfortable with accounting software — assumes bookkeeping discipline |
| **NPCI UPI Circle** | Secondary user (staff/family) initiates directly from their own phone via linked UPI ID | Full Delegation: ₹5,000/transaction, ₹15,000/month cap, no PIN needed; Partial: primary approves every transaction with PIN | None — just a payment rail | None — no bill/vendor ledger layer | Free (UPI has zero MDR) | Any UPI user; **most relevant regulatory analogue** for staff-initiated payment delegation, but has no bill-before-pay, no vendor balance, hard ₹15K/month ceiling (too low for a trusted factory manager's ₹10-15k single-purchase limit per the case) |

**Global analogues (for benchmarking model choices, not India rails):**

| Player | Model | Relevant lesson |
|---|---|---|
| **Pleo** (Europe, SMEs 5-200 employees) | Employee gets a smart card with a pre-set limit; photographs receipt instantly in-app; no expense reports ever filed | Validates "card + instant receipt capture + no reimbursement" as the winning UX for decentralizing spend in small teams |
| **Ramp** | Blocks out-of-policy spend *before* transaction completes (hard decline at point of sale) | Pre-transaction control > post-hoc policy enforcement — relevant to the "approve vs notify" trade-off in H3 |
| **Brex** | Sets thresholds that trigger alerts/review *after* the transaction | Shows the "notify" model is viable at scale but requires trust in the employee base |
| **Mercury, Payhawk, Spendesk, Expensify** | Various combinations of corporate cards + receipt OCR + accounting sync | Converging pattern: card-centric decentralization + automatic reconciliation is now table stakes globally; India's gap is adapting this to **UPI-first, no-card, cash-adjacent** behavior rather than a card-first model |

**Key competitive insight**: No Indian competitor currently combines (a) staff-initiated payment execution, (b) bill-before-pay proof capture, (c) running per-vendor supplier credit/khata balances, and (d) owner real-time ledger — in one integrated, bank-rail-connected flow. Khata apps (OkCredit/Vyapar) own the *record-keeping* habit at massive scale but don't move money. Card-based platforms (EnKash/Happay/Open) own *spend control* but are card-centric, which doesn't match UPI-dominant, no-card vendor payment behavior in this segment. RazorpayX has the payment rails and vendor/invoice infrastructure but not the mobile-first, staff-initiated, khata-aware layer.

## User Segments
**Segment 1: Owner (Proprietor/Founder) — e.g., retail shop owner, small factory owner**
- *JTBD*: "When I can't be everywhere at once, help me delegate payment authority to people I trust without losing visibility or control, so I can grow the business instead of being the only person who can pay anyone."
- Pain points: Routes most vendor payments through personal UPI because it's instant and frictionless; has informally extended trust-based limits to a factory manager (₹10-15k) with no system backing it; three weeks later, can't recall what a payment was for; reconciliation is a monthly fire-drill handed to an accountant who charges for hours spent matching bills to bank statements.
- What they *don't* want: to approve every single ₹500-5,000 payment (too much friction, erodes the point of delegating); a system that feels like policing family members or long-tenured staff.

**Segment 2: Staff / Manager / Family member (on-the-ground payer)**
- *JTBD*: "When I'm at the vendor with goods to collect, let me pay instantly without using my own money or waiting for approval, and give me proof I did it right so I'm never blamed later."
- Pain points: Pays from personal UPI and waits (sometimes weeks) to get reimbursed or "adjusted"; carries the burden of remembering/justifying every payment; has no formal record protecting them if a dispute arises later ("did you really pay that vendor ₹8,000, or did you pocket it?").
- This segment will resist anything that feels like surveillance (per H5) — the system must *protect* them (proof of correct payment, no out-of-pocket float) as much as it controls them.

**Segment 3: Accountant / Bookkeeper (part-time or visiting, not in-house finance team)**
- *JTBD*: "When it's month-end, give me data in a format I already use (Tally/Excel) so I don't have to manually match UPI screenshots, WhatsApp images, and handwritten slips to GST bills for hours."
- Pain points: Receives a mix of paper, screenshots, and verbal explanations; must reconstruct "who paid whom, for what, against which bill" after the fact with degraded memory/context; GST input credit claims are at risk when bills aren't properly matched to payments.
- What they want: structured exports (Tally-compatible), vendor-wise statements that already reconcile to GST invoices, minimal manual data entry.

**Cross-cutting tension**: All three segments are already fluent in UPI (collectively, India's small merchants show 94% UPI acceptance and owners/staff use UPI daily) — the barrier isn't digital literacy, it's that **UPI itself has no memory**: it moves money but captures no purpose, no linkage to a bill, and today's delegation feature (UPI Circle) caps at ₹15,000/month, well below what a trusted factory manager might need in a single day for raw-material purchases.

## User Journey
**Primary segment: Staff/Manager making an on-the-spot vendor payment (current state, inferred from case brief + competitive/behavioral research — not yet primary-validated)**

1. **Trigger**: Manager/staff is physically at a vendor (supplier of raw material, packaging, ingredients) to collect goods. Vendor expects payment now, by whichever means is fastest — usually a UPI QR scan.
2. **Payment decision**: Staff has no company-linked payment instrument. They either (a) pay from their *personal* UPI account and plan to get reimbursed/"adjusted" later, or (b) call/message the owner to send money directly to the vendor, or (c) use petty cash if available.
   - *Friction*: No real-time way to pay "as the business" without being the owner. UPI Circle exists but caps delegated spend at ₹15,000/month total — too low for someone regularly handling ₹10-15k single purchases, and it requires both parties to proactively set it up on a specific UPI app, which neither party has reason to discover.
3. **Partial payment / credit (khata)**: For regular suppliers, payment is often partial against a running balance — the vendor's own notebook or WhatsApp thread is the "source of truth" for outstanding dues, and it frequently diverges from what the business believes it owes.
   - *Friction*: No single, structured place tracks the running per-vendor balance; it lives in the vendor's head, a notebook, Excel, or WhatsApp — reconciled only sporadically and often incorrectly.
4. **Proof capture**: A GST bill, handwritten slip, or nothing at all is collected. If the staff member remembers, they photograph it and send it via WhatsApp to the owner or accountant — but this is manual, easy to forget, and context (why, for what PO/order) is lost quickly.
   - *Friction/drop-off*: In the gap between "payment happened" and "proof reaches someone who records it," context decays. By month-end, "nobody remembers what a payment was for."
5. **Reimbursement/adjustment**: If paid from personal UPI, the staff/family member must separately claim reimbursement from the owner — another manual, trust-based, undocumented step, creating float and potential friction/resentment (the staff fronted their own cash).
6. **Month-end reconciliation**: The accountant (often external/part-time) receives a mix of UPI screenshots, GST bills, WhatsApp texts, and verbal recollections, and must manually match each to a vendor and a bank-statement line, often across multiple personal and business accounts. This is described as taking "hours," with owners and staff unable to recall transaction purposes three weeks later.
   - *Friction/outcome*: Reconciliation is slow, error-prone, and disconnects GST input-credit claims from the invoices that justify them — a compliance risk, not just a time cost.
7. **Owner's visibility throughout**: Near-zero in real time. The owner typically learns about a payment only when asked for reimbursement or when the accountant flags a discrepancy weeks later — meaning the "delegation" that already exists informally (e.g., trusting a factory manager with ₹10-15k) is a leap of faith with no real-time checkpoint and no systemic memory of purpose or proof.

**Moments of relative delight (what already works and shouldn't be broken)**: UPI itself is fast, familiar, and nearly universally accepted by vendors (94% of small merchants accept UPI) — any solution must preserve this "scan and pay in seconds" feel rather than replacing it with a slower, more bureaucratic flow (this underlies H4's <30-second constraint).

**Unmet needs surfaced**: (a) a company-linked way for staff to pay without personal float; (b) bill-before/at-pay capture that doesn't require a separate manual step; (c) an automatically updating per-vendor running balance (digital khata) that both sides trust; (d) real-time, per-person visibility for the owner without requiring pre-approval of every transaction; (e) accountant-ready, structured output at month-end.

## Key Insights
1. **RazorpayX's core growth flywheel structurally excludes this segment.** RazorpayX's cross-sell motion depends on a business already being a Razorpay payment-gateway (collections) customer — but owner-run SMEs typically collect via PhonePe/GPay/Paytm UPI QR directly, never touching Razorpay's rails. This means RazorpayX can't rely on its usual "already in our funnel" advantage here; it must win this segment cold, on the payments/vendor side alone, which is a fundamentally different (harder, lower-trust, lower-urgency) sale than its existing PLG motion with digital-native businesses.

2. **UPI Circle looks like the "obvious" regulatory answer but is capped too low to matter for this segment.** NPCI's delegated-payments feature (launched Aug 2024) allows full delegation only up to ₹5,000/transaction and ₹15,000/month — but the case's own example of a trusted factory manager handling ₹10-15k in *single* purchases shows the real-world need exceeds UPI Circle's ceiling in the very first transaction. This is a non-obvious but important finding: **the generic NPCI rail is not sufficient by itself**; RazorpayX would need its own business-account-based delegation layer (built on its existing Payouts/Vendor Payments infrastructure, which has no per-transaction value ceiling) rather than waiting for or relying on UPI Circle to solve this.

3. **The real unmet need is "memory," not "money movement."** UPI has already solved payment execution for this segment (94% merchant acceptance, P2M growing 37% YoY) — the gap is that UPI transactions carry no structured purpose, no link to a bill, and no running balance. This reframes RazorpayX's opportunity away from "build a better payment rail" (which doesn't matter — UPI is already fast and free) toward "build the memory layer that sits on top of payments" — directly validating H2 (the core pain is recording/reconciliation, not theft) and suggesting RazorpayX's moat should be the bill-to-ledger linkage, not the payment execution itself.

4. **Existing digital-khata apps (OkCredit, Vyapar) prove massive latent demand for exactly this record-keeping behavior, but at a structural disadvantage: they are disconnected from actual money movement.** OkCredit has 5M+ installs; Vyapar claims 1.5 Cr+ users — yet neither initiates real payments, so the ledger and the bank statement always need manual reconciliation. RazorpayX is uniquely positioned to be the first player to unify "the khata" and "the actual payment rail" into one object (a single digital record where paying *is* updating the ledger), which neither the khata apps nor the card-based expense players (EnKash, Happay) can currently offer, because the former don't move money and the latter are card-centric in a UPI-first market.

5. **The employee-protection framing (H5) may be a bigger adoption lever than fraud prevention.** Global analogues (Pleo) succeed specifically by selling the *employee* benefit ("never front your own money, never get blamed") as much as the *employer* control benefit. In the Indian context, where family members and long-tenured staff already enjoy informal trust, a system perceived as "surveillance" risks rejection even if monetary leakage is minimal (₹1-5k/month per the case's own signal) — suggesting the product's primary value narrative to staff must lead with "proof you paid correctly" and "no more waiting for reimbursement," not "the owner can now watch you."

## Data Points
1. RazorpayX processes $30B in annualised transaction volume (85% YoY growth), used by 50,000+ businesses, ~5% of all digital money transfers in India. Source: https://digitalinasia.com/razorpay-explained/
2. Razorpay FY25 consolidated revenue: ₹3,783 crore (+65% YoY from ₹2,296 crore in FY24); FY25 net loss ₹1,209 crore due to tax/reverse-flip costs. Source: https://www.business-standard.com/industry/news/razorpay-fy25-results-revenue-up-65-percent-loss-due-to-tax-costs-125101601178_1.html
3. Razorpay overall: $180B annualised TPV, 8M+ merchants, ~55% share of India's online PG market, $9.2B valuation (June 2025). Source: https://digitalinasia.com/razorpay-explained/
4. RazorpayX Payouts pricing: free current account, 250 free payouts/month, then ₹1.5-7 per payout depending on amount tier/rail. Source: https://productgrowth.in/tools/payments/razorpay-x/
5. RazorpayX Corporate Card default roles: Owner/Admin, Finance, Cardholder, Viewer — no staff-initiated-payment-with-bill-upload role exists today. Source: https://razorpay.com/docs/x/capital/corporate-cards/?preferred-country=IN
6. RazorpayX Vendor Payments workflow: OCR invoice capture, 3-way PO-GRN-invoice matching, multi-layer approval workflows, one-click dashboard payouts — a desk-based, invoice-first flow. Source: https://razorpay.com/x/vendor-payments/
7. UPI Circle (NPCI, launched Aug 13, 2024): max 5 secondary users per primary; Full Delegation capped at ₹5,000/transaction and ₹15,000/month without per-transaction approval; Partial Delegation requires primary's UPI PIN each time. Source: https://fintechchronicler.substack.com/p/npci-s-upi-circle-what-you-need-to
8. UPI FY2025-26: 24,162 crore annual transactions, ₹314 lakh crore annual value, UPI ~85% of India's digital payments, ~49% of world's real-time payment volume. Source: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2257087&reg=3&lang=1
9. UPI P2M = 63% of UPI volume but only ~28-29% of value; 86% of P2M transactions under ₹500. Source: https://coinlaw.io/upi-statistics/
10. UPI QR codes grew 91.5% to 658 million in FY25; PoS terminals grew 24.7% to 1.1 crore; ~70 million QR-enabled merchants nationwide. Source: https://www.medianama.com/2025/05/223-upi-84-india-fy25-retail-payment-volume-rbi/
11. UPI handled 84% of India's retail payment volume in FY25 (RBI Annual Report); 185.9 billion transactions in FY25 vs 131.1 billion in FY24 (+41.7%). Source: https://www.medianama.com/2025/05/223-upi-84-india-fy25-retail-payment-volume-rbi/
12. India has ~63.4 million MSMEs (630.5 lakh micro, 3.3 lakh small, ~5,000 medium); MSMEs employ ~111 million people, contribute ~27-31% of GDP, ~45-48% of exports. Source: https://www.ibef.org/blogs/india-s-msme-sector
13. 4.72 crore MSMEs registered on Udyam portal as of mid-2026; 98.9% micro, ~4.9 lakh small, 37,042 medium. Source: https://datarankindia.com/india-msme-statistics/
14. Government-backed survey (10,378 respondents, 2,199 merchants, 15 states): UPI preferred by 57% vs cash 38%; 94% of small merchants accept UPI; 72% satisfied; 57% reported sales increase. Source: https://openthemagazine.com/business/upi-overtakes-cash-as-indias-most-preferred-payment-mode-survey
15. OkCredit (digital khata app): 5,000,000+ Play Store installs, used across 50+ business categories in 2,800+ Indian cities. Source: https://okcredit.in/en/
16. Open Money pricing: Free / ₹1,199-1,499 / ₹5,599-6,999 per month tiers; offers VISA debit cards to employees with set limits. Source: https://open.money/pricing
17. EnKash issues prepaid corporate cards (up to ₹2,00,000, MCC-locked) in under 60 seconds via its own RBI-authorised PPI license; backed by $23M funding, 5,000+ businesses. Source: https://www.enkash.com/products/corporate-cards
18. Pleo (European SME analogue): individual pre-set card limits, instant in-app receipt capture, no expense reports; serves SMEs of ~5-200 employees; pricing €0-€79/month. Source: https://www.pleo.io/en/howitworks
19. Ramp blocks out-of-policy spend before transaction completion (hard decline); Brex allows transaction then triggers alert/review — illustrating the "approve vs notify" design trade-off. Source: https://relayfi.com/blog/brex-vs-ramp/
20. RazorpayX with Current Account base charge: $1.5/employee/month subscription; 250 free payouts/month; 6 months free Payroll bundled. Source: https://happay.com/blog/razorpayx-reviews-pricing/

**Notable gaps requiring primary research** (not found in secondary sources): precise count of "5-20 employee, owner-run, no finance team" businesses in India (no official census bucket matches this exactly — estimate only); a direct, recent (last 12 months) survey quantifying the specific UPI/cash/credit split *for vendor payments* (as opposed to general consumer/merchant UPI stats) among owner-run SMEs in this size band; direct evidence on how much monetary leakage vs. time-cost dominates in this segment (the case brief notes this is an "early, unvalidated signal"); and RazorpayX's own internal data on SME segment usage/churn, which is not publicly disclosed.
