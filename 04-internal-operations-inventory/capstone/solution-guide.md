# Pinehaven Q3 Operations Stabilization — Worked Solution Guide

There is no single mandatory management answer. A strong submission is internally consistent, reproducible from the fictional evidence, explicit about uncertainty, and governed by owners and triggers. This guide demonstrates the expected depth rather than providing a script to copy.

## Executive recommendation

Pinehaven should keep the current Q3 master schedule as the planning baseline only after separating three different questions: **inventory feasibility, customer promiseability, and execution capacity**. The 13-week PAB remains nonnegative, but Week 4 has only 50 units of ATP, so a new 60-unit request cannot be silently promised in full. Commit the 50 currently available-to-promise units and route the remaining 10 through an explicit schedule, allocation, or later-date decision.

The Week-27 execution plan is not yet feasible at all work centers. Final Assembly, Burn-in Test, and CNC Enclosure exceed both rated or demonstrated capacity, while Pack & Label has spare hours that cannot be assumed transferable. The immediate operating package should protect Burn-in as the system constraint, subordinate release to it, execute the validated false-failure/DMAIC improvement, use controlled short-term capacity or load actions for Assembly and CNC, and prevent new upstream release from simply creating WIP.

Inventory policy should remain differentiated. PH-PWR220 requires tight Class-A control and its EOQ/order-point assumptions should be monitored; PH-CNK500 can use its periodic-review policy; PH-FUSE7 remains Class C by monetary value but receives a Class-A policy override because its service consequence and long lead time are material. Traceability and count discrepancies must be reconciled before replenishment relies on them, and return R-1002 stays quarantined until the safety gate is closed.

The performance evidence indicates a system-wide stabilization problem rather than one isolated KPI miss. Burn-in queue, first-pass yield, setup time, incoming defects, schedule attainment, inventory accuracy, lead time, perfect-order contribution, inventory turns, and cost of poor quality all cross their stated action triggers. Pinehaven should use TOC to govern the constraint and release pace, DMAIC to reduce burn-in false failures and other measurable variation, lean/JIT to remove waste only after process reliability is protected, and local capacity actions where the Week-27 gap remains after those improvements.

## 1. Master-schedule validation and the Week-4 promise

The master-schedule dataset already provides the required demand logic. Recalculation gives the following end-of-week PAB values:

| Week | Demand used | MPS receipt | PAB |
|---:|---:|---:|---:|
| 1 | 160 | 400 | 590 |
| 2 | 175 | 0 | 415 |
| 3 | 190 | 0 | 225 |
| 4 | 200 | 400 | 425 |
| 5 | 210 | 0 | 215 |
| 6 | 220 | 400 | 395 |
| 7 | 225 | 0 | 170 |
| 8 | 230 | 450 | 390 |
| 9 | 235 | 0 | 155 |
| 10 | 240 | 450 | 365 |
| 11 | 245 | 0 | 120 |
| 12 | 250 | 450 | 320 |
| 13 | 255 | 0 | 65 |

No PAB bucket is negative. That shows the baseline schedule is inventory-feasible under the stated demand rule; it does **not** prove that every new order is immediately promiseable or that shop-floor capacity can execute the plan.

The discrete ATP buckets are:

- Week 1: **225**
- Week 4: **50**
- Week 6: **120**
- Week 8: **215**
- Week 10: **275**
- Week 12: **330**

For the additional Week-4 request of 60 units, Pinehaven can promise **50 units from the current Week-4 ATP**. The remaining **10 units** require a governed decision: reallocate from another commitment if policy permits, change the MPS, negotiate a later requested date, or add feasible supply after checking capacity and material consequences. The company should not silently consume a later ATP bucket because that would change the availability promised to future demand without recording the trade-off.

### Decision record

| Field | Recommendation |
|---|---|
| Decision | Promise 50 units from Week-4 ATP; hold the remaining 10 for approved schedule/allocation review |
| Owner | Master scheduler with customer-service/sales approval per commitment policy |
| Evidence | `master-schedule.csv`; PAB and ATP recalculation |
| Trigger | Any revised MPS, cancellation, new high-priority order, or capacity/material exception affecting the promise |
| Control | Preserve the ATP bucket and the authorization trail for any reallocation |

## 2. MRP timing and BOM stress calculation

### PH-PWR220 — L4L

With a two-week lead time, the planned receipt is offset two weeks earlier for release. The time-phased requirements in the locked file produce:

- Week 5: net requirement **250**, receipt **250**, release **Week 3**
- Week 7: net requirement **450**, receipt **450**, release **Week 5**
- Week 9: net requirement **450**, receipt **450**, release **Week 7**
- Week 11: net requirement **450**, receipt **450**, release **Week 9**

L4L prevents intentional lot-size excess: receipt quantity follows the net requirement.

### PH-CNK500 — FOQ

The one-week lead time and 500-unit fixed order quantity produce:

- Week 3: need 50 net, receipt **500**, release **Week 2**
- Week 6: need 50 net, receipt **500**, release **Week 5**
- Week 10: need 250 net, receipt **500**, release **Week 9**

The fixed lot creates planned residual inventory. That is not an MRP error; it is the consequence of the selected lot-sizing rule.

### 100-unit PH-SD500 BOM stress case

This is a **stress calculation**, not a change to the approved MPS. Using the locked BOM quantities:

| Component | Quantity per SD-500 | Gross quantity for 100 SD-500 |
|---|---:|---:|
| PH-CTRL210 | 1 | 100 |
| PH-PWR220 | 1 | 100 |
| PH-ENC500 | 1 | 100 |
| PH-FAN120 | 2 | 200 |
| PH-CNK500 | 1 | 100 |
| PH-PCB210 via CTRL210 | 1 | 100 |
| PH-MCU88 via CTRL210 | 1 | 100 |
| PH-HARN210 via CTRL210 | 2 | 200 |
| PH-SHEET14 via ENC500 | 1.8 | 180 |

The stress case shows the quantity relationships only. Timing still requires lead-time offsetting, inventory status, scheduled receipts, and the applicable lot-sizing rule before a release recommendation is made.

## 3. Week-27 capacity feasibility

| Work center | Rated capacity | Demonstrated capacity | Required load | Gap vs rated | Gap vs demonstrated |
|---|---:|---:|---:|---:|---:|
| Final Assembly | 378.00 | 376.00 | 410 | **−32.00** | **−34.00** |
| Burn-in Test | 144.40 | 144.00 | 150 | **−5.60** | **−6.00** |
| CNC Enclosure | 175.75 | 176.67 | 190 | **−14.25** | **−13.33** |
| Pack & Label | 220.50 | 220.67 | 200 | **+20.50** | **+20.67** |

Three resources are overloaded. Pack & Label's spare capacity does not prove those shortages are solved because a standard hour at Pack & Label may not have the skill, machine, tooling, routing, or timing capability needed at Assembly, Burn-in, or CNC.

### Immediate response package

1. **Protect Burn-in Test as the near-term system constraint.** Use the existing queue/buffer status and subordinate upstream releases rather than feeding more WIP to the constraint.
2. **Execute the validated TOC/DBR improvement.** The locked improvement case raises Burn-in capability from 144 to **154 standard hours/week**, enough for the current 150-hour base load with only 4 hours of headroom.
3. **Execute the burn-in false-failure DMAIC control.** The separate case reduces false failures from **4.8% to 1.6%**, helping protect useful constraint time from avoidable retest/rework.
4. **Close Final Assembly's 32-standard-hour gap through an approved short-term capacity/load action.** If overtime is allowed and 105% efficiency is sustained, 32 standard hours corresponds to about `32 / 1.05 = 30.48` additional actual work hours. Across 10 resources and five days, that is about **0.61 hour per resource per day**. This is an illustrative feasibility calculation; labor rules, skill coverage, fatigue, quality, and cost must be checked before approval.
5. **Close CNC's 14.25-standard-hour rated-capacity gap** using approved overtime, schedule movement, alternate routing, or subcontracting only after quality/tooling/economic feasibility is verified.
6. **Do not count Pack & Label spare hours as a solution** unless an alternate routing/cross-skill plan proves they can do the required constrained work.

## 4. Inventory and replenishment controls

### PH-PWR220

- ABC value class: **A**
- Policy class: **A**
- Lead time: 8 weeks in the item master; the separate replenishment model uses a 15-day scenario for its calculation example. These are different illustrative decision contexts and should not be merged silently.
- EOQ model: annual demand 12,000; unit cost $168; order cost $145; annual carrying rate 22%.

`EOQ = sqrt((2 × 12,000 × 145) / (0.22 × 168)) ≈ 306.85 units`

Order point in the replenishment scenario:

`48 units/day × 15 days + 380 safety stock = 1,100 units`

Use the EOQ only while its stability assumptions remain a reasonable approximation; long lead time, disruption risk, quantity breaks, or changing demand can require a different policy.

### PH-CNK500

- ABC value class: **C**
- Policy class: **C**
- Periodic-review scenario: demand 72/day, lead time 8 days, review interval 10 days, safety stock 210, on hand 620.

`Maximum = 72 × (10 + 8) + 210 = 1,506 units`

`Order quantity = 1,506 − 620 = 886 units`

The periodic-review method is appropriate only if the review cadence, inventory-position definition, service policy, and common replenishment source remain valid.

### PH-FUSE7

- Value class: **C**
- Policy class: **A** because of the documented criticality override
- Min level: 700
- Max level: 2,200
- Current on hand: 650

Because inventory is below the minimum, the selected min-max action is:

`2,200 − 650 = 1,550 units`

The **4,700-unit** field elsewhere in the same row is a periodic-review comparison and must not be mislabeled as the min-max order. This is a useful governance example: the model being applied must be identified before using a number.

## 5. Traceability, inventory accuracy, and return disposition

The trace file shows PWR220 lot **PWR220-L2704** through the following events for serial **SD500-SN-27031**:

1. receipt verified;
2. component issued to the serial at Final Assembly;
3. Burn-in Test passed; and
4. finished good released to stock.

That event chain provides component-to-serial genealogy for investigation or targeted containment.

### Cycle-count differences

| SKU | Book | Actual | Difference | Required control response |
|---|---:|---:|---:|---|
| PH-PWR220 | 482 | 480 | −2 | Validate the stated issue-posting lag, correct the transaction/record under authorization, and confirm no unposted movement remains |
| PH-MCU88 | 316 | 316 | 0 | No quantity adjustment; retain count evidence |
| PH-CNK500 | 740 | 735 | −5 | Resolve the five units in the unposted quality hold, then reconcile the system/location status |
| PH-PKG500 | 1,900 | 1,910 | +10 | Correct the case-pack conversion/master-data or transaction cause before final adjustment |

Only one of the four records is an exact match. That **does not mean formal inventory accuracy is 25%**, because the dataset does not specify the organization's allowable tolerance rule. Pinehaven should not invent a tolerance after seeing results.

### Return R-1002

R-1002 has a modeled recoverable value of $250 and processing cost of $180, so a simple economic view shows +$70. However, its status is **electrical failure under investigation** with a **regulatory or safety hold = yes**. The item remains quarantined. Economics are considered only after the mandatory safety/failure-analysis gate determines which disposition options are eligible.

## 6. Performance and quality diagnosis

Every KPI row in the locked operations dataset crosses its stated action trigger:

- schedule attainment 94.5% — below 96% trigger;
- first-pass yield 97.8% — below 98.5%;
- inventory accuracy 96.8% — below 98%;
- burn-in queue 124 units — above 100;
- order lead time 6.4 days — above 6;
- supplier incoming defect rate 1.1% — above 0.8%;
- inventory turns 4.36 — below 4.5;
- setup time 37 minutes — above 30;
- perfect-order contribution 96.2% — below 97.5%; and
- cost of poor quality 3.4% of sales — above 3%.

The response should not be “launch ten unrelated projects.” The evidence points to a connected stabilization chain: supplier/input quality, setups and release practices feed WIP and burn-in queue; false failures consume constraint time; poor flow lengthens lead time and schedule attainment; inventory-record weakness undermines planning and replenishment.

### Quality-tool evidence

The Pareto dataset totals **66 defects**. The first three categories—Loose connector 24, Burn-in failure 18, Label mismatch 11—represent `53 / 66 = 80.30%` of the recorded defects. That makes them rational investigation priorities, subject to any safety/severity override.

The control-chart sample has a mean of approximately **5.0242 mm** and sample standard deviation of approximately **0.04776 mm**. These figures describe the illustrative sample; they do not establish product capability without approved control/specification limits and an appropriate control-chart design.

The humidity/defect scatter data have a very strong positive sample correlation (about **0.9979**). Treat humidity as a high-priority hypothesis, not as a proven cause. Confirm with process knowledge, controlled comparison, stratification, or another valid causal test before changing specifications or controls.

The lean-flow file shows Burn-in Test at **4.1 min/unit** versus a takt requirement of **3.5 min/unit**. The process is slower than the required customer pace, consistent with the queue and constraint evidence.

## 7. Improvement portfolio and failure case

The methods solve different problems and should be combined deliberately:

| Method | Pinehaven use | Control |
|---|---|---|
| TOC / DBR | Protect Burn-in as the current constraint, control upstream release, preserve the buffer, and focus throughput improvement | Constraint capacity, buffer status, accepted throughput, WIP |
| DMAIC | Reduce measurable false-failure variation and rework at Burn-in; separately attack other stable data-driven defect processes | False-failure rate, control chart, validated root cause |
| Lean / JIT | Reduce waiting, setup, excess WIP, travel, and release waste after reliability is protected | Takt vs cycle time, setup time, queue/WIP, pull signal |
| Local capacity/load action | Close the remaining dated Assembly/CNC gap through overtime, alternate route, schedule movement, or qualified outside capacity | Standard-hour gap, cost, quality, due-date consequence |

The improvement dataset shows TOC/DBR raising Burn-in capability from **144 to 154 standard hours/week**. For the current 150-hour load, the improvement gives **4 hours of headroom**.

### Failure / sensitivity case

If Week-27 Burn-in load rises to **165 standard hours**:

`165 − 154 = 11 standard hours remaining overload`

The improvement is still valuable, but it no longer makes the schedule feasible. Pinehaven must activate another decision: add qualified capacity, move load, change the schedule, or renegotiate demand. The DBR release control remains necessary so upstream output does not simply create a larger queue.

This is the key capstone lesson: an improvement result is not automatically a release decision. It must be compared against the demand/load it is expected to support.

## 8. Financial and operating consequence

The financial scenario provides an additional reason to stabilize flow rather than solve every issue with inventory.

| Scenario | Average inventory | Annual COGS | Inventory turns | Cash released vs current |
|---|---:|---:|---:|---:|
| Current | $4.50m | $19.60m | 4.356 | $0 |
| Improvement | $4.35m | $20.80m | 4.782 | $0.90m |

Both balance-sheet scenarios satisfy `Assets = Liabilities + Owners' Equity`. The improvement case illustrates higher inventory velocity and cash release, but it should only be pursued with customer-service and reliability controls. Cutting inventory while capacity, quality, or record accuracy remain unstable could simply convert working capital into stockouts and expedites.

## 30/60/90-day stabilization plan

| Timing | Decision/evidence gate | Accountable roles | Trigger or measure |
|---|---|---|---|
| Days 1–30 | Freeze uncontrolled schedule changes; validate PAB/ATP; reconcile high-impact count errors; protect Burn-in buffer; approve temporary Assembly/CNC response | Master Scheduling, Production Control, Inventory Control, Operations | ATP exceptions, standard-hour gaps, queue >100, count discrepancy unresolved |
| Days 31–60 | Complete burn-in DMAIC action; implement DBR release rule; attack top Pareto defects; verify supplier incoming-quality corrective action; reduce setup time with controlled trials | Quality, Manufacturing Engineering, Supplier Quality, Operations | false-failure rate, FPY, incoming defects, setup >30 min, buffer status |
| Days 61–90 | Confirm sustained constraint capacity, schedule attainment, lead time, inventory accuracy, and turns; decide whether to remove temporary capacity, extend validation, or replan Q4 | Operations Planning, Finance, Quality, Supply Chain leadership | 154-hour constraint capacity sustained, schedule/FPY/accuracy triggers cleared, stress-case headroom adequate |

The day-90 gate is not “project complete.” It is a decision point: **release the stabilized operating model, continue controlled improvement, activate contingency capacity, or revise the supply/demand plan**.

## Replan triggers

Reopen the affected decision when any of the following occurs:

- a new order consumes more ATP than the authorized bucket can support;
- PAB turns negative under the approved demand logic;
- a component release would require violating the frozen/firming rule without approval;
- Assembly, Burn-in, or CNC load exceeds approved capacity after the selected response;
- Burn-in load exceeds the improved 154-standard-hour capability without contingency capacity;
- a critical-item inventory policy can no longer protect the required service level within the lead time;
- inventory accuracy remains below its action threshold or traceability evidence is incomplete;
- a safety/regulatory hold remains unresolved;
- first-pass yield, incoming defects, setup time, or cost of poor quality fail their control thresholds after the improvement period; or
- the customer-demand pace changes enough to make the current takt/capacity basis invalid.

## Evaluation rubric

| Level | Evidence of completion |
|---|---|
| Incomplete | Uses PAB as ATP, treats plant capacity as fungible, ranks returns before safety gates, or chooses improvement tools without reproducible evidence |
| Competent | Reproduces the key calculations, separates planning/material/capacity/inventory decisions, applies gates, and states owners and action thresholds |
| Excellent | Also tests a decision-changing failure case, preserves an executable contingency, links operating improvements to customer/financial outcomes, and states exactly what evidence would force a replan |
