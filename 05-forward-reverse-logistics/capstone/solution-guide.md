# HarborPeak Capstone — Worked Solution Guide

This solution uses only the fictional Module 5 datasets and the controlled assumptions in the assignment. It is one defensible decision package, not the only possible design. A different recommendation is acceptable if it applies the same mandatory gates, reproduces the numbers, and explains the trade-offs.

## Executive recommendation

HarborPeak should use the **Northstar 4PL orchestrated** model as the base logistics-provider structure, operate the **3-DC hybrid** warehouse pattern for the modeled service requirement, use **Regional pooled inventory** as the core B2B + e-commerce fulfillment pattern, and contract the focal multi-region lane to **Summit Contract Carriage** after the stated structural gates.

The physical design should size to the locked warehouse-capacity horizon rather than simply extending the current footprint. For the new carton cell, **Conveyor + sortation** is the least-capital option that passes safety/capability and clears the 500-unit/hour threshold. The Supplier Bay-Cedar lane requires an immediate **15-unit/week capacity correction** before it can be called ready.

Cross-border release must remain gate-driven. **TC-007 is a hard hold** until its restricted-product and marking review closes. In the training Incoterms case IC-01, FCA at the HarborPeak Dallas dock is the stated rule/place; in the synthetic border-cost case BC-01, modeled duty is **$2,870** and modeled landed cost is **$90,250**.

Reverse flow should be managed as a separate operating system. RC-01 is the only reverse-cost line with a positive modeled result; RC-02, RC-03, and RC-04 require redesign or policy action. Product-level e-waste/battery flags must be closed before disposition economics are ranked. The waste program should push material as high in the hierarchy as practical while preserving documented custody.

## 1. Forward-logistics operating structure

### Provider gate and economic comparison

From `logistics-strategy.csv`:

| Alternative | Modeled total logistics cost | Capability gate | Base-case disposition |
|---|---:|---|---|
| HarborPeak internal network | $8,970,000 | PASS | Feasible, higher cost |
| BlueHarbor 3PL regional | $8,390,000 | PASS | Feasible |
| Northstar 4PL orchestrated | **$8,070,000** | PASS | **Select** |
| BudgetFreight 3PL basic | $7,900,000 | **FAIL** | Exclude until gate is resolved |

Northstar is the **lowest-cost feasible** option. It is $320,000/year below BlueHarbor and $900,000/year below the internal model. BudgetFreight appears $170,000/year cheaper than Northstar, but that saving is not actionable because the capability gate fails.

The decision is not “pick the cheapest row.” It is “remove non-feasible alternatives, then rank the feasible set.”

### Warehouse-network aggregation

For each network, sum annual transport, inventory, and overhead costs across its rows. Weight response time and service score by the service-coverage percentage.

**2-DC owned**

- transport = $3,180,000 + $1,250,000 = **$4,430,000**
- inventory = $1,390,000 + $580,000 = **$1,970,000**
- overhead = $1,260,000 + $690,000 = **$1,950,000**
- total = **$8,350,000/year**
- coverage = 72% + 28% = **100%**
- weighted response = `(72×2.3 + 28×2.8) / 100 = 2.44 days`
- weighted service score = `(72×4 + 28×3) / 100 = 3.72`

The cost is attractive, but the 2.44-day weighted response fails the capstone's 2.0-day requirement.

**3-DC hybrid**

- transport = $1,900,000 + $1,030,000 + $840,000 = **$3,770,000**
- inventory = $1,060,000 + $620,000 + $490,000 = **$2,170,000**
- overhead = $1,260,000 + $690,000 + $780,000 = **$2,730,000**
- total = **$8,670,000/year**
- coverage = 48% + 27% + 25% = **100%**
- weighted response = `(48×1.7 + 27×1.9 + 25×1.2) / 100 = 1.629 days`
- weighted service score = `(48×4 + 27×3 + 25×5) / 100 = 3.98`

All included rows have PASS labor and regulatory flags. The network therefore meets the mandatory service gate.

The 3-DC hybrid costs **$320,000/year more** than the 2-DC owned design, but improves service-weighted response by approximately **0.811 day**. Under the stated service requirement, this is not an optional premium: it is the cost of moving from a failed service design to a feasible one.

The 4-DC dataset row is not a complete 100%-coverage design and has a WATCH labor flag, so it cannot be treated as a feasible network simply because its visible site is fast.

## 2. Space, handling, and lane capacity

### 2030 warehouse requirement

The 2030 dataset gives:

- forecast inventory cube = 10,100 m³
- pallet cube = `1.2 × 1.0 × 1.35 = 1.62 m³`
- base bays = `10,100 / 1.62 = 6,234.57`
- adjusted bays = `6,234.57 × 1.12 = 6,982.72`
- raw footprint = `6,982.72 × 1.2 = 8,379.26 m²`
- handling-adjusted footprint = `8,379.26 × 2.95 = 24,718.81 m²`
- vertical-adjusted area = `24,718.81 / 4 = 6,179.70 m²`
- utilization-adjusted core area = `6,179.70 / 0.81 = 7,629.26 m²`
- plus 610 m² bulk allowance = **8,239.26 m² total required area**

That result reproduces the locked dataset.

The base 2031 dataset shows higher inventory cube but five usable vertical levels. The extra vertical level reduces the floor-area requirement enough that the recorded total becomes 7,587.78 m². The lesson is that cube growth and floor-area growth are not the same thing when the storage geometry changes.

### Material handling

The new carton cell requires at least 500 units/hour and PASS safety/capability gates.

- Counterbalance forklift: 34 units/hour — fails throughput requirement.
- Reach truck + selective rack: 42 units/hour — fails throughput requirement.
- Conveyor + sortation: **560 units/hour**, PASS/PASS, $980,000 capex — feasible.
- AS/RS shuttle: 820 units/hour, PASS/PASS, $1,850,000 capex — feasible but higher capital.
- Low-cost manual carts: safety FAIL and capability FAIL — not rankable.

The base recommendation is therefore **Conveyor + sortation**. It satisfies the stated throughput requirement at $870,000 less capex than AS/RS. If future demand requires more than 560 units/hour, the decision should be reopened rather than pretending the lower-capital option still has sufficient capacity.

### Lane capacity

Every lane except one has nonnegative capacity gap. Supplier Bay-Cedar requires 705 units/week with only 690 reserved:

`capacity gap = 690 − 705 = −15 units/week`

HarborPeak must close **15 units/week** before calling the lane ready. The immediate owner should secure additional contracted capacity, reduce the promotion-driven requirement with an approved demand decision, or create a documented alternate lane. Spare capacity on an unrelated lane is not automatically transferable.

## 3. Fulfillment, distribution, modes, and carrier

### Core fulfillment strategy

The capstone requires B2B + e-commerce, service score 5, and average lead time ≤2.0 days.

- Integrated national DC: B2B + e-commerce, but service score 4 and 3.2-day lead — fails.
- Dedicated e-commerce DC: strong service, but channel is e-commerce only — does not cover the core mixed-channel requirement.
- **Regional pooled inventory:** B2B + e-commerce, service score 5, 1.7-day lead, flexibility 5 — **passes and is selected**.
- Ship from store/service depot: e-commerce only.
- Supplier drop ship: service gate FAIL.

This does not mean dedicated e-commerce or ship-from-store designs are universally inferior. They can remain channel-specific patterns, while the pooled network carries the capstone's core mixed-channel requirement.

### Warehouse execution

`warehouse-operations.csv` shows why all outbound units should not be forced through the same path. The normal receipt path has receiving plus put-away; order fulfillment has picking plus packing. XDK-1190 is explicitly a **cross-dock** transaction: 310 units, only 0.2 hour storage time, 46 minutes touch time, and $68 handling cost. Its purpose is to bypass ordinary storage when timing and destination alignment support it.

POS-3031 and KIT-4420 illustrate postponement/value-added paths. Final labeling and kitting add handling work deliberately because differentiation is being delayed until demand is clearer. The execution control is therefore to route only qualifying units to cross-dock or postponement rather than treating these services as generic warehouse steps.

### Mode decisions

Apply the PASS service gate, then choose the lower-cost PASS option per shipment:

| Shipment | PASS alternatives | Selected base option | Modeled line-haul cost |
|---|---|---|---:|
| SHP-501 Smart controller | Air | **Air** | $5,400 |
| SHP-502 Cordless drill kits | Motor; Rail+Motor | **Rail+Motor** | $2,150 |
| SHP-503 Steel tool stands | Motor | **Motor** | $1,850 |
| SHP-504 Replacement batteries | Air; Motor | **Motor** | $2,760 |

For SHP-502, Rail+Motor saves **$1,150** versus the other PASS option. For SHP-504, Motor saves **$3,440** versus Air in the fictional data. The battery shipment still requires any applicable dangerous-goods/safety checks before physical release; the dataset's service PASS is not a legal authorization.

### Carrier choice

AgriLocal Exempt is removed because its structural gate is FAIL. The focal lane requires multi-region reach and equipment-fit score 5. **Summit Contract Carriage** satisfies both, has a PASS structural gate, and has the lowest rate among the feasible focal-lane candidates at **$1,710/shipment**.

A simple average of its five qualitative scores is `(4+4+5+4+4)/5 = 4.2`, higher than the 4.0 averages of Atlas and HarborPeak Private Fleet. That score supports the choice, but the structural/geographic/equipment gates are what make Summit eligible in the first place.

## 4. Cross-border release decision

### Hard hold

TC-007 is the clearest release gate in the register:

- restricted-goods screen = REVIEW
- document-pack status = Incomplete markings
- compliance risk = Critical
- required action = **Do not load until restricted-product and marking review closes**

The control record should show the rule/source consulted, the product facts used in the restriction determination, approved markings/labels, reviewer/owner, closure date, and released document set. Changing carrier or Incoterms® does not resolve the product/marking problem.

### Incoterms training decision

IC-01 states **FCA — HarborPeak Dallas dock** for a containerized/multimodal servo-controller shipment. In this fictional case, HarborPeak clears export and hands the goods over at the named place; the buyer wants main-carriage control and has import capability.

The named place and edition must be recorded with the term. The rule allocates delivery/risk/cost/clearance responsibilities; it should not be used as a shortcut for title transfer, payment conditions, sanctions compliance, or tax treatment.

### BC-01 border-cost calculation

The synthetic training values are:

- customs-assessment value = $82,000
- modeled duty rate = 3.5%
- international freight = $4,100
- broker/entry fees = $1,280
- modeled import-tax rate = 0% in this case

Duty:

`$82,000 × 0.035 = $2,870`

Modeled landed cost:

`$82,000 + $2,870 + $0 + $4,100 + $1,280 = $90,250`

The arithmetic is reproducible; the classification and rate are explicitly synthetic. A live entry would require the current importing-country tariff schedule, valuation rules, origin facts, special-program eligibility, and other transaction-specific controls.

## 5. Reverse-flow economics

### Return rates

Return rate = returned units / shipped units.

| Case | Returned / shipped | Return rate | Regulatory training flag |
|---|---:|---:|---|
| RF-01 HX-400 controller | 900 / 18,000 | **5.0%** | none |
| RF-02 PX-9 sensor kit | 1,440 / 12,000 | **12.0%** | electronics review |
| RF-03 RT-60 tote | 340 / 8,500 | **4.0%** | none |
| RF-04 LB-22 battery module | 504 / 4,200 | **12.0%** | battery and e-waste review |
| RF-05 MX-12 drive assembly | 1,560 / 26,000 | **6.0%** | none |

The two 12% cases deserve immediate diagnostic attention, but RF-04 additionally needs the regulatory/product-integrity gate before disposition ranking.

### Reverse-cost results

For each row, modeled revenue/benefit is the sum of resale/liquidation, repair fees, recycling, restocking fees, incentive value, and estimated warranty sales uplift. Modeled cost is the sum of return credits, reverse transportation, processing/handling, repair parts, reverse warehousing, and disposal/compliance.

| Case | Modeled revenue/benefit | Modeled cost | Economic result | Result per return |
|---|---:|---:|---:|---:|
| RC-01 controllers | $223,000 | $200,000 | **+$23,000** | **+$25.56** |
| RC-02 sensor kits | $232,200 | $284,500 | **−$52,300** | **−$36.32** |
| RC-03 battery modules | $124,200 | $155,900 | **−$31,700** | **−$62.90** |
| RC-04 drive assemblies | $434,500 | $438,600 | **−$4,100** | **−$2.63** |

Across the four modeled lines, the net is **−$65,100**. RC-01 demonstrates that reverse flow can create a positive result under the stated assumptions. RC-02 and RC-03 deserve the highest redesign attention because the loss per return is material; RC-04 is close to breakeven and may respond to transportation, processing, credit-policy, repair-yield, or recovery changes.

The service/warranty uplift is modeled evidence, not guaranteed revenue. Management should therefore maintain a version of this analysis with and without less-certain benefit categories when making financial commitments.

## 6. Waste hierarchy and custody

The highest practical route stated in each row is:

| Waste case | Highest stated route before lower hierarchy options | Gate/control |
|---|---|---|
| WD-01 polymer transit tote | **Wash and reuse** | Track cycles/damage |
| WD-02 aluminum housing | **Remanufacture/component reuse** | Quality/economic gate |
| WD-03 printed circuit board | **Selective component reuse** if qualified; otherwise authorized electronics recycling | E-waste review |
| WD-04 spent cleaning solvent | **Closed-loop recovery if feasible** | Hazard characterization and permitted route |
| WD-05 oily absorbent media | Limited reuse; then permitted material/energy recovery | Hazard characterization |
| WD-06 corrugated cardboard | **Reuse for internal moves**, then fiber recycling | Segregation quality |
| WD-07 retired lithium battery module | **Second life only after engineering gate**, otherwise specialized material recovery | Battery/e-waste and cross-border legal review |

WD-04 and WD-07 are intentionally strong examples of **gate before economics**. For WD-04, HarborPeak must determine the legal waste/hazard status and permitted handling route. For WD-07, engineering fitness, battery/e-waste requirements, qualified recovery, and any transboundary controls must be resolved before a high recovery value could justify movement.

Minimum custody evidence should include the material/product identifier, quantity, hazard/waste determination basis, origin and destination, approved handler/carrier/facility, shipment/manifest or equivalent record where required, handoff dates, receiving confirmation, final treatment/disposition evidence, exception record, and retention owner.

## Sensitivity and failure cases

### 2031 fifth-level delay

Base 2031 values include:

- handling-adjusted footprint = 27,751.11 m²
- usable storage levels = 5
- target utilization = 0.80
- separate bulk allowance = 650 m²

Base result:

`27,751.11 / 5 = 5,550.222 m²`

`5,550.222 / 0.80 = 6,937.7775 m²`

`6,937.7775 + 650 = 7,587.78 m²`

Now hold every other 2031 input constant but delay the fifth level, leaving only four usable levels:

`27,751.11 / 4 = 6,937.7775 m²`

`6,937.7775 / 0.80 = 8,672.221875 m²`

`8,672.221875 + 650 = 9,322.22 m²`

The sensitivity requires **1,734.44 m² more** than the base 2031 design and exceeds the 2030 requirement of 8,239.26 m² by **1,082.96 m²**. That is decision-changing. HarborPeak should not commit to a smaller 2031 floor-area plan unless the fifth storage level is funded, technically feasible, safe, and scheduled with adequate confidence. The implementation gate should therefore tie facility commitment to evidence that the vertical-capacity assumption will actually exist when needed.

### Other failure triggers

The strategy should also be reopened if any of these occur:

- the 3-DC hybrid weighted response rises above 2.0 days;
- the selected provider loses its capability gate or exit/subcontract governance becomes unacceptable;
- outbound carton demand exceeds the conveyor's 560-unit/hour modeled throughput;
- Supplier Bay-Cedar remains below required capacity after the procurement lead time;
- a selected transport mode drops below the required service gate;
- a shipment develops an unresolved restriction, documentation, origin, classification, or security exception;
- a reverse flow changes waste/hazard status or loses an approved recovery partner; or
- return rates/costs materially exceed the modeled assumptions.

## Implementation roadmap

| Horizon | Owner | Action | Measure / gate | Trigger and response |
|---|---|---|---|---|
| 0–30 days | VP Supply Chain + Logistics Procurement | Confirm Northstar 4PL due diligence, scope, metrics, subcontracting visibility, remedies, and exit controls | Capability gate remains PASS; commercial scope reconciled | Any unresolved control/exit weakness pauses award |
| 0–30 days | Network Design Lead | Validate 3-DC hybrid service model and each site's labor/regulatory readiness | 100% coverage; weighted response ≤2.0 days | Reoptimize if service or site gate fails |
| 0–30 days | Transportation Manager | Close Supplier Bay-Cedar shortfall | Reserved capacity ≥705 units/week | Add contracted reserve/alternate plan before release |
| 0–30 days | Trade Compliance Lead | Hold and remediate TC-007 | Restriction/marking/document evidence complete | No load while critical exception remains open |
| 31–60 days | DC Engineering | Confirm conveyor cell and 2030 space plan | ≥500 units/hour; safety/capability PASS; 8,239.26 m² plan supported | Escalate to AS/RS evaluation if required throughput >560/hour |
| 31–60 days | Fulfillment Lead | Pilot regional pooled inventory for mixed channel | Service score/lead-time targets maintained | Rebalance nodes if lead time exceeds 2.0 days |
| 31–60 days | Reverse Logistics Manager | Launch triage and cost-reduction actions on RC-02/03/04 | Loss/return and cycle time trend downward | Escalate product/policy/network redesign if no improvement |
| 31–60 days | EHS/Compliance + Engineering | Establish WD-04/WD-07 route controls | Approved status, handler, custody and disposition evidence | Block movement to unapproved route |
| 61–90 days | Finance + Supply Chain Analytics | Reconcile total-cost and reverse-economics assumptions | Actual-vs-modeled variance with source data | Refresh business case if variance breaches agreed tolerance |
| 61–90 days | Facilities + DC Engineering | Gate 2031 footprint on vertical-level readiness | Fifth level approved, safe, funded, and scheduled | Use 9,322.22 m² sensitivity requirement if fifth level is not credible |

The plan is deliberately evidence-driven. “Complete project” is not a control; a control states the threshold, owner, evidence, and response when the threshold is missed.

## Completed executive decision record

| Decision | Mandatory gate | Evidence | Strongest rejected alternative | Trigger |
|---|---|---|---|---|
| Northstar 4PL | Capability PASS | `logistics-strategy.csv`; $8.07M feasible cost | BudgetFreight is cheaper but FAIL | Capability, control, subcontract, or exit weakness |
| 3-DC hybrid | 100% coverage; site gates PASS; response ≤2.0 days | $8.67M; 1.629-day weighted response | 2-DC owned costs $8.35M but response is 2.44 days | Response >2.0 or site readiness changes |
| Conveyor + sortation | Safety/capability PASS; ≥500 units/hour | 560 units/hour; $980k capex | AS/RS is faster but $870k more capex | Requirement >560 units/hour |
| Regional pooled fulfillment | B2B+e-commerce; service 5; lead ≤2.0 days | 1.7 days, service/flexibility 5 | Integrated national DC misses service/lead gate | Lead time >2.0 or channel mix changes |
| Summit Contract Carriage | Structural PASS; multi-region; equipment fit 5 | $1,710/shipment; 4.2 avg score | Atlas lacks equipment-fit 5; private fleet regional | Geographic/equipment requirement changes |
| Hold TC-007 | Compliance/document gates | Critical risk; review + incomplete markings | Any load-before-close option | Release only on documented closure |
| Reverse redesign on RC-02/03/04 | Regulatory/integrity first | −$52.3k; −$31.7k; −$4.1k | Passive acceptance | Loss/return rate persists after countermeasure |
| Gate WD-04/07 routes | Hazard/e-waste/custody | Dataset flags and qualified partner requirement | Pure price/recovery ranking | Classification, destination, partner, or law changes |

## Evaluation rubric

A strong capstone response should demonstrate all of the following:

- **Gate discipline:** failed capability, service, safety, trade, or waste gates are never averaged away by a lower cost.
- **Reproducibility:** calculations match the linked datasets, including the 3-DC weighted response, 2030 space requirement, BC-01 landed cost, reverse-cost results, and 2031 four-level sensitivity.
- **Scope discipline:** provider-model costs, warehouse-network costs, fulfillment capital, shipment line-haul costs, and reverse-flow economics are not incorrectly added together when they represent different decision scopes.
- **Operational judgment:** recommendations explain what changes in physical flow, customer response, capacity, or control—not just which number is smallest.
- **Trade discipline:** training Incoterms and border-cost arithmetic are clearly separated from current legal/tariff verification.
- **Reverse-flow discipline:** regulatory and chain-of-custody gates precede recovery economics.
- **Implementation quality:** every major recommendation has an accountable owner, threshold, evidence source, review timing, and an explicit response when assumptions fail.

[Return to the capstone assignment](./README.md) · [Return to Module 5](../README.md)