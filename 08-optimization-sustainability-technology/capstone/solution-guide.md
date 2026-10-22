# AlderGate Transformation Investment — Fully Worked Module 8 Capstone Solution

> **Instructor/self-check guide, not an approved corporate business case.** Every company, vendor, financial amount, threshold and program control is fictional. The calculations below use the locked existing Section A/B/C inputs and new capstone input CSVs. The exercise models **five complete operating years only after gate closure and acceptance**; it does not imply current production cutover is permitted. Do not quote fictional environmental factors as verified emissions or time savings as cash until independently evidenced.

## 1. Executive recommendation: conditional investment, not production release

**Recommendation:** Select the **regional network** as the least-cost base-volume **eligible design** and **vendor B** as the only proposal that simultaneously meets the stated technology gates and recurring expense cap. The **75% realization scenario** produces modeled five-year NPV **+$35,813** on **$185,000 time-zero investment**, with **$108,000/year** certain new service/support expenses; it passes the fictional **$200,000 t0** and **$110,000/year** caps.

**Authorize only planning, design, data reconciliation and a controlled non-releasing pilot subject to normal procurement and security permissions. Do not authorize a full automated cutover or assert realized savings at this time.** Two critical Quality/release tests are unresolved; active process use is **67%**, below the fictional **75%** gate; Finance has not verified that released hours create avoidable cash expense; public recycling proof has two outstanding records; and the network/emission assumptions remain modeled rather than live-verified. Document actual safety/permit and customer requirements separately. The model's attractiveness is a rationale to investigate, not proof that the enterprise is ready.

At 1,200 units/week demand stress, the preferred regional design is **100 units/week short**. The central candidate has exactly 1,200 units/week nominal capacity, subject to requalification. The base annual $50,000 regional savings, its 109-tonne footprint and the financial scenario **must be re-estimated**, not carried forward as guaranteed under stress.

![Gated investment and release sequence](../../assets/diagrams/module-8/capstone/aldergate-gated-program-decision.svg)

## 2. Locked decision and evidence ledger

| Required fact / training assumption | Value and precise interpretation | Direct evidence |
| --- | --- | --- |
| Customer population | One regional market, **1,000 units/week**, 52 assumed weeks, **52,000 units/year** | [Policy](../../assets/data/module-8/capstone/executive-policy.csv) |
| Stress demand | **1,200 units/week** independently, *not* new base scenario | [Policy](../../assets/data/module-8/capstone/executive-policy.csv) |
| Evaluation | Five *complete operating years after acceptance*, 10% annual discount; end-year cash, t0 investment | [Policy](../../assets/data/module-8/capstone/executive-policy.csv) |
| Capital and recurring caps | **$200,000 t0** and **$110,000/year incremental technology fee plus support** — separate limits | [Policy](../../assets/data/module-8/capstone/executive-policy.csv) |
| Section A network cost | Facility + transport + inventory + **existing network service-failure cost**, excluding separate manual-event and invoice activities | [Section A existing input](../../assets/data/module-8/section-a/location-design-alternatives.csv) |
| New technology offer | Vendor B: **$84,000/year**, conditional technical qualification | [Section C vendor input](../../assets/data/module-8/section-c/technology-selection.csv) |
| New program cost | **$185,000 t0**, plus **$24,000/year** support separate from vendor B | [Program cost input](../../assets/data/module-8/capstone/program-costs.csv) |
| Labor savings | Potential **$155,000/year**, fully assumed cash-avoidable, but **Finance confirmation pending** | [Separate benefit populations](../../assets/data/module-8/capstone/manual-work-benefits.csv) |
| Baseline evidence | Training 90%; actual active use 67%; two critical cutover failures | [Change pilot](../../assets/data/module-8/section-c/change-coalition.csv); [test results](../../assets/data/module-8/section-c/cutover-acceptance.csv) |
| Environmental comparison | Warehouse energy + outbound transport **only**; invented tonne estimates, **120-tonne voluntary aspiration** | [Footprint and worker gates](../../assets/data/module-8/capstone/network-sustainability.csv) |

The existing Section A study, the Section B two-plant waste case, and Section C vendor/pilot lessons were separate examples. The **capstone policy** explicitly joins their scopes for educational purposes. Do not add their other sample totals, percentages or event populations to this case without a corresponding mapping.

## 3. Strategy, base demand and network screening (Section A)

AlderGate competes on dependable service for one regional engineered-components market. A feasible network must cover the **1,000 units/week** qualified commitment and documented worker/destination gates. Demand = 1,000 × 52 = **52,000 units/year** under a stable-week assumption. This does not introduce another product family or simulate seasonality.

Compute for each option:

`annual network cost = facility + transport + inventory + modeled network service-failure cost`.

| Option | Cost arithmetic (USD/year) | Total/year | Capacity units/week | Slack vs 1,000 | Worker/destination gates | Rank status |
| --- | --- | ---: | ---: | ---: | --- | --- |
| Central | 280,000 + 220,000 + 85,000 + 40,000 | **625,000** | 1,200 | **+200** | yes / yes | Eligible |
| Regional | 365,000 + 130,000 + 65,000 + 15,000 | **575,000** | 1,100 | **+100** | yes / yes | **Eligible and preferred** |
| Low-cost | 315,000 + 120,000 + 75,000 + 10,000 | **520,000** | 850 | **−150** | **no** / yes | **Blocked** |

The apparently cheapest $520,000 alternative cannot fulfill the committed volume and fails the fictional worker-safety gate. The least-cost **eligible** network is **regional**; it saves **$625,000 − $575,000 = $50,000 per modeled year** versus central, provided operational capacity is independently qualified. This is a network-only difference already inclusive of the cost line labeled `service_failure_cost_usd`; it is not proof of incremental manual-processing benefit.

**Trade-off:** Regional reduces modeled cost but leaves 100 rather than 200 units/week nominal headroom. Operations must validate staffing, warehouse throughput and alternate contingency options rather than relying only on quoted capacity.

![Network feasibility and environmental footprint](../../assets/diagrams/module-8/capstone/aldergate-network-capacity-and-footprint.svg)

## 4. Economic, environmental and social outcomes (Section B)

[Capstone network sustainability input](../../assets/data/module-8/capstone/network-sustainability.csv) contains illustrative **tonnes CO₂e/year** from *two sources only*.

| Option | Warehouse-energy t CO₂e/year | Outbound t CO₂e/year | Combined modeled tonnes/year | Meets **voluntary** 120-t aspiration? |
| --- | ---: | ---: | ---: | --- |
| Central | 61 | 78 | **139** | No |
| Regional | 48 | 61 | **109** | Yes |
| Low-cost | 42 | 59 | **101** | Numerically yes, **not eligible** due to other gates |

Moving the modeled base flow from central to regional reduces combined scoped footprint by **139 − 109 = 30 tonnes CO₂e/year**, or **30/139 × 100 = 21.58%** of central. The regional option meets a management aspiration; the central option's missed aspiration is not a statutory prohibition. Neither result is externally verified. The decision requires actual energy invoices/meters, route distances, factors, carrier utilization and a comparable period, plus legal approvals. Do not claim a full corporate lifecycle footprint or a measured reduction.

The [existing Section B waste file](../../assets/data/module-8/section-b/recycling-lineage.csv) relates to two operating sites in the defined reporting population, **not** to the three network's alternative emissions figures. Reconstruct the *mass-weighted* recycling rate:

- Plant A: **8,400 / 12,000 = 70%** verified recyclable mass by reported quantity.
- Plant B: **4,800 / 8,000 = 60%**, with **two open source exceptions**.
- Combined: **(8,400 + 4,800) / (12,000 + 8,000) = 13,200/20,000 = 66%**.

A simple mean of 70% and 60% gives 65% but would use equal site weights despite different eligible masses. The two Plant B exceptions are an **evidence and public-claim hold**; a calculation can be arithmetically correct while disclosure is not supportable.

**Mandatory versus voluntary:** The low-cost option fails worker-safety readiness and should not be restored by a favorable 101-tonne footprint. UNGC principles, GRI impacts and ISO certification terms can inform governance, but they do not replace site-specific worker, waste, customs or product permission. Suppliers' responsible-material and statutory filing duties also depend on actual legal/product scope, not a general score.

## 5. Secure vendor selection and avoidable-process benefit (Section C)

The [Section C vendor file](../../assets/data/module-8/section-c/technology-selection.csv) is a fictional supplier qualification table.

| Vendor | Annual fee | Access gate | Response gate | Illustrative score | Cap with $24k support | Result |
| --- | ---: | --- | --- | ---: | ---: | --- |
| A | $92,000 | Pass | Pass | 78 | **$116,000/year** — above $110k cap | Technically qualified, **budget-ineligible** without exception |
| B | $84,000 | Pass | Pass | 86 | **$108,000/year** — within cap | **Preferred eligible** |
| C | $65,000 | **Fail** | Pass | 94 | $89,000/year | **Security-ineligible** despite the score |

The high weighted rating of C cannot compensate for missing required data access protection. B's service fee is not part of Section A network expense; adding it is legitimate under the explicit case boundary. An implementation owner must still validate contracts, service response, data export and restoration.

[Potential manual benefit sources](../../assets/data/module-8/capstone/manual-work-benefits.csv):

| Non-overlapping activity | Annual cases | Avoidable hours per case | Assumed avoidable cash USD/hour | Maximum potential/year |
| --- | ---: | ---: | ---: | ---: |
| Order-event reconciliation | 15,000 | 0.35 | $20 | **$105,000** |
| Invoice-dispute processing | 5,000 | 0.50 | $20 | **$50,000** |
| **Maximum modeled potential** | Separate activity populations | | | **$155,000/year** |

Hours saved are **not automatically cash savings**: the plant might pay employees the same wages and simply redeploy them to more valuable work. The input records currently mark `confirmed_cash_avoidability = pending_finance_verification`. Finance must corroborate workload baseline, staff contracts, avoided overtime or agency spend, explicit savings account, retained customer service and possible overlap. Without that evidence, NPV is a **scenario only**.

## 6. Funding and full five-year financial bridge

[Program costs](../../assets/data/module-8/capstone/program-costs.csv) are separate from vendor fee and network expense:

- **t0 integration/security:** $110,000.
- **t0 partner training and change:** $45,000.
- **t0 master-data clean-up:** $30,000.
- **Total certain up-front:** **$185,000**, versus **$200,000 maximum** → $15,000 remaining.
- **Annual vendor B + continuing support:** $84,000 + $24,000 = **$108,000/year**, versus **$110,000 maximum** → $2,000 remaining.

**Both caps pass but financial authority is not yet granted.** Apply the caps to their *respective* expense types; neither substitutes for security, safety or service authorization.

Annual operating ledgers at full baseline activity:

`Existing central network + separate manual work = $625,000 + $155,000 = $780,000/year.`

Proposed regional + B + support + unreduced manual work at fraction `f` of achieved cash avoidance:

`$575,000 + $84,000 + $24,000 + $155,000 × (1−f) = $683,000 + $155,000 × (1−f).`

Therefore the **annual incremental net cash saving** (before financing, inflation and taxes) is:

`$780,000 − [$683,000 + $155,000 × (1−f)] = −$58,000 + $155,000 × f.`

Equivalent bridge: **$50,000 network saving + $155,000 × f realized process saving − $108,000 new annual expense.** Do **not** add the $50,000 again to an already netted proposed cost, treat the $185,000 as annually recurring, or claim the manual $155,000 is separate from the residual manual expense.

For the **conditional 75% realization model**: process savings = 0.75×$155,000 = **$116,250/year**. Manual remainder = **$38,750/year**. Proposed expense = $683,000 + $38,750 = **$721,750/year**. Difference versus baseline $780,000 = **$58,250/year**.

Let `PVA(10%,5) = Σ [1/(1.10)^t], t=1…5 = 3.79078677`. The five-year NPV at acceptance is:

`NPV(f) = −$185,000 + (−$58,000 + $155,000×f) × 3.79078677.`

At **f=0.75**, this is **−$185,000 + $58,250 × 3.79078677 = +$35,813.33**. The **simple undiscounted payback** at a level annual benefit is **$185,000/$58,250 = 3.176 operating years**. This payback is not discounted payback, and the five annual savings are a modeled assumption **after release gates close**, not cash realized today.

### Sensitivity and financial viability

![Five-year value is sensitive to realized benefits](../../assets/diagrams/module-8/capstone/aldergate-npv-adoption-sensitivity.svg)

| Assumed realizable cash benefit fraction `f` | Annual net saving | Five-year NPV at 10% | Interpretation |
| --- | ---: | ---: | --- |
| **60% downside** | **$35,000** | **−$52,322** | Negative; no economic sign-off on this assumption |
| **67% pilot-use proxy** | **$45,850** | **−$11,192** | Negative; user adoption is not even proof of equivalent cash realization |
| **75% approval scenario** | **$58,250** | **+$35,813** | Conditional, *not* met in current adoption/test evidence |
| **100% modeled potential** | **$97,000** | **+$182,706** | Optimistic ceiling, not a verified business result |

Break-even at nonnegative five-year NPV requires

`f_break_even = [($185,000 / 3.79078677) + $58,000] / $155,000 ≈ 0.68905 = 68.90%.`

**Do not confuse two thresholds:** ~68.90% is the narrow fictional **financial crossover** under verified cash saving assumptions, whereas 75% is the separately adopted **operational gate**; that gate remains in force even if a scenario shows positive NPV at a lower percentage. Nor is active user fraction a validated one-to-one benefit realization curve.

## 7. Operational cutover and organizational-change gate dashboard

The current [change pilot](../../assets/data/module-8/section-c/change-coalition.csv) lists 120 warehouse staff and 80 partner staff, **200 affected workers**:

- Trained: 108 + 72 = 180 → **180/200 = 90%**, meeting the fictional minimum training gate.
- Active users of the new governed process: 90 + 44 = 134 → **134/200 = 67%**, **below the 75% gate**.
- Required active users at the same population = 0.75×200 = **150**. The team needs **at least 16 additional active users**, *and evidence of correct transaction outcomes*, before a retest could pass.

The [cutover suite](../../assets/data/module-8/section-c/cutover-acceptance.csv) passes critical 38/40 and noncritical 152/160, giving **190/200 = 95%** overall. There are **two critical blocking failures**. The policy tolerates **zero** critical blocked-release defects, so the affected **automated production cutover is blocked** regardless of overall test pass percentage.

**Permitted preparation:** Design workshops, data-quality work, supplier role agreement, and separately permissioned **read-only** or simulated pilot activity that cannot allocate restricted inventory, dispatch ineligible orders or trigger external release. Any pilot must itself pass its relevant access and safety requirements; "read-only" is not a universal exemption.

**Not yet permitted:** Full automated order release, retiring safe legacy fallback before validated replay/rollback, claiming avoided labor cost as realized cash, or publishing a fully verified recycling percentage while the Plant B evidence gaps persist. Approvals are distinct: Quality owns product release, CISO owns information access, Operations owns cutover and customer service, Finance owns cash benefits, Sustainability owns reporting evidence.

## 8. Risk, demand stress, and robustness

Use [governance actions](../../assets/data/module-8/capstone/governance-actions.csv) as the controlled owner/trigger ledger. The proposed base region retains **100 units/week slack**. A separate demand stress of **1,200 units/week** produces:

| Network | Rated weekly capacity | Stress required | Stress slack | Base strategy consequence |
| --- | ---: | ---: | ---: | --- |
| Central | 1,200 | 1,200 | **0** | Nominally covers stress; operational qualification required |
| Regional | 1,100 | 1,200 | **−100** | **Cannot** promise 1,200/week without additional qualified supply |
| Low-cost | 850 | 1,200 | **−350** | Remains infeasible |

**Do not** retain $575,000 regional annual cost or its 109-tonne figure as if they describe an accepted 1,200-unit configuration. Re-estimate handling labor, shifts, freight, inventory, actual customer service and environmental factor/loads for any revised site/route design. Operations must qualify a 100-unit/week addition or evaluate the 1,200-unit central capacity and its contingency; the existing central quote also needs capacity assurance at zero slack.

A deliberately **partial financial stress**, which removes the $50,000 network saving while holding vendor/support fee and the modeled 75% manual benefit unchanged, has annual net `$116,250 − $108,000 = $8,250`. Five-year NPV under *these limited held-constant inputs* is **−$153,726**. This demonstrates reliance on the network savings; it is **not** a full economic model of 1,200 units/week and cannot authorize the stressed plan.

Additional failure cases: a partner may withdraw event authorization, a vendor may miss restoration targets, emission-source records may prove unreliable, and process benefits may become only reallocated staff hours rather than avoidable spending. Any such finding reopens selection and funding rather than silently preserving the positive NPV.

## 9. Owned decision matrix and 30/60/90-day implementation

| Topic | Decision/status today | Decision owner | Exit evidence / escalation |
| --- | --- | --- | --- |
| Regional network 1,000/week | **Preferred design, conditionally** | VP Network Operations | Qualified site throughput, labor and destination release proof; regional slack and contingency |
| Vendor B | **Preferred eligible model, conditionally** | CISO + Procurement | Access tests, data export/recovery, contract service terms; vendor C stays blocked |
| Investment package | **Scenario passes spend caps, not approved cash ROI** | CFO/Finance Controller | Evidence that 15k and 5k case populations are exclusive and labor costs genuinely avoidable |
| Automated cutover | **BLOCKED** | IT Delivery + Quality + Operations | Two critical release tests corrected, 0 blocking failures, replay/rollback proven |
| Worker/partner adoption | **BLOCKED for full rollout** | Change Lead + partner owners | ≥90% trained and ≥75% active with correct outcomes, independently sampled |
| Public sustainability disclosure | **HOLD** | Sustainability and Compliance | Plant B's two missing records and footprint source/method verified |
| Stress demand 1,200/week | **REGIONAL PLAN INFEASIBLE** | Planning + Network Operations | Qualified additional 100 units/week or revised, recosted alternative |
| Security/safety incident recovery | **NOT YET DEMONSTRATED** | IT Operations + HSE/Quality | Signed restore, incident escalation and permitted restart drills |

The review cadence begins **Day 0 = 2 November 2026**, while **investment time zero is separately defined as the point *after* business acceptance**. This keeps the 30/60/90 preactivation work distinct from modeled five complete operating years.

**Days 0–30 (through 2 December 2026):** Network Operations verifies 1,100 qualified weekly throughput for the base and explores stress capacity; Procurement/CISO test vendor B's identities and response requirements; Quality and IT correct and independently retest the two critical release controls; Finance reconciles labor process populations and expense accounts. Executive gate: no production cutover or irreversible committed capital without required procurement and funding approval.

**Days 31–60 (through 1 January 2027):** Change leads and partner managers remove adoption barriers, conduct scenario-based training and verify at least 150 genuinely active users in the same 200-worker population; Sustainability resolves the two Plant B evidence records and validates emissions boundaries; Finance updates the benefit scenario based on avoidable costs; Operations completes acceptance and owner training.

**Days 61–90 (through 31 January 2027):** IT/Logistics exercise restore and replay after a failed connection, confirm rollback and customer-notice responsibilities, and run one integrated order-to-customer exception drill. Recalculate network/technology cost and NPV using verified evidence, seek formal charter and funding authority, then consider a staged go-live only if mandatory gates are closed. If any hard gate fails, hold the affected release, maintain authorized fallback, and publish the decision in the risk/action register.

**Ongoing:** Sponsor owns investment performance; Operations owns customer fulfillment; IT Operations maintains interfaces, service recovery and access; Procurement governs vendor obligations; Environment/Sustainability owns the reporting method; Finance tracks confirmed cost savings; the Change Lead validates adoption. KPIs include qualified capacity utilization, customer exceptions resolved within target, blocked-order violations (target zero), verified maintenance and incident recovery, active adoption, true avoidable cost, and environmental reporting exceptions.

## 10. Final decision rule and cross-module handoffs

**Conditional go for governed design/pilot; no full production go-live now.** A modeled positive financial value at 75% realization does not prove eligible capacity under stress, safety, verified sustainability reporting, secure vendor integration, cash avoidability, working adoption or critical cutover readiness. The policy's economic crossover and funding caps are necessary **but not sufficient** conditions.

This capstone integrates [Module 8 Section A](../section-a-optimizing-supply-chain-strategy-and-tactics/README.md) strategic/network economics, [Section B](../section-b-sustainability/README.md) triple-bottom-line/evidence boundaries, and [Section C](../section-c-technology-trends/README.md) technology selection, change and support. The gates derive from the risk/continuity method taught in [Module 7](../../07-supply-chain-risk/README.md). The demand, architecture, supplier, execution, logistics and partner handoffs belong to [Modules 1–6](../../LEARNING-PATHS.md).

The entire solution is recalculated by [the independent capstone replay](../../calculations/module8-capstone/replay.py) from the linked original and existing CSV data. It remains a **training model** until business and financial owners verify the underlying assumptions and evidence.

[Assignment and direct input list](./README.md) · [Module 8 overview](../README.md)
