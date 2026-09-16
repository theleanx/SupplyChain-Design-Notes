# Capstone Solution Guide

This guide demonstrates one defensible approach to the NorthStar planning decision. A different recommendation can be equally strong when its assumptions, calculations, trade-offs, and triggers are explicit.

## Executive recommendation

Approve the 4,100-unit Q1 demand plan conditionally and use the capacity-plus-controlled-demand-movement response. The plan combines 1,150 units of normal monthly output, 100 monthly overtime units, no more than 200 units of external finishing, and an agreed movement of 80 flexible March units to April. It maintains the 150-unit finished-goods floor at an incremental cost of **$29,600**, which is $4,000 below the feasible no-movement response.

Approval depends on verified framework-agreement timing, weekly electronic-control-kit confirmation, customer consent for moved demand, protected April capacity, and qualified external-finishing performance. Commercial owns agreement conversion and customer consent; procurement owns kit confirmation and recovery; operations owns output, inventory, and external quality. Any failed condition reopens the plan rather than becoming an informal expedite.

## 1. Supply-network diagnosis

The primary vulnerability is the single-source electronic control kit. The monthly allocation supports the proposed plan, but February demand consumes the full available quantity and March retains only 20 units of theoretical headroom. A late shipment, quality hold, or yield loss would therefore affect customer service quickly.

The most important synchronized flows are:

- **Material:** kits and castings must arrive in time for assembly and final configuration.
- **Information:** commercial agreements, regional priorities, supplier allocations, capacity, inventory, and quality status must use the same planning dates and product-family definitions.
- **Funds:** premium supply decisions must be compared with contribution, service exposure, and the cost of moving demand.

Platform design and final configuration can be centrally governed, while regional teams can propose prioritization within approved service rules. Supplier allocation, aggregate capacity, and the quarterly demand plan should remain cross-functional decisions.

## 2. Demand-pattern interpretation

Actual demand increases from 820 units in January to 1,320 units in December. The pattern contains a clear upward trend, with additional event effects in July, November, and December. The market index also rises, so it may be a useful directional signal, but the dataset does not establish causation.

Actual demand exceeds the baseline forecast in each of the final four months. That pattern suggests systematic underforecasting rather than a single isolated miss. Before accepting the commercial plan, NorthStar should confirm agreement start dates, customer order flexibility, probability-weighted volumes, cancellation terms, regional mix, and the availability of the constrained control kit.

## 3. Forecast evaluation

### Three-month moving average

Using October–December actual demand:

`(1,130 + 1,200 + 1,320) / 3 = 1,216.7 units`

The rounded statistical starting point is **1,217 units** for January.

### Four-month error analysis

| Month | Actual | Baseline forecast | Error: actual − forecast | Absolute error | Absolute percentage error |
|---|---:|---:|---:|---:|---:|
| September | 1,090 | 1,060 | 30 | 30 | 2.75% |
| October | 1,130 | 1,100 | 30 | 30 | 2.65% |
| November | 1,200 | 1,150 | 50 | 50 | 4.17% |
| December | 1,320 | 1,230 | 90 | 90 | 6.82% |

`MAD = (30 + 30 + 50 + 90) / 4 = 50 units`

`MAPE = (2.75% + 2.65% + 4.17% + 6.82%) / 4 = 4.10%`

`Cumulative error = 30 + 30 + 50 + 90 = 200 units`

`Tracking signal = 200 / 50 = +4.0`

MAPE is relatively small, but it should not be considered alone. Every recent error is positive, and the tracking signal indicates sustained underforecasting under the stated error convention. NorthStar should investigate model lag, event treatment, and missing commercial information.

## 4. Demand recommendation

The three-month moving average is materially below the commercial proposal because a moving average lags a rising series. The commercial plan also includes new agreements not fully represented in shipment history. A reasonable recommendation is therefore to **accept the 4,100-unit quarterly plan with conditions** rather than mechanically adopting either the statistical value or the commercial proposal.

Conditions should include:

- named owners for agreement validation and electronic-kit allocation;
- a weekly view of firm orders, cancellations, and supplier confirmation;
- a downside scenario if an agreement starts late;
- an upside scenario for accelerated customer adoption; and
- replanning if confirmed demand or component supply changes by more than an agreed threshold.

## 5. Supply response

### Response A — Capacity-led hybrid plan

| Month | Beginning inventory | Normal output | Overtime | External finishing | Demand | Ending inventory |
|---|---:|---:|---:|---:|---:|---:|
| January | 220 | 1,150 | 100 | 0 | 1,320 | 150 |
| February | 150 | 1,150 | 100 | 110 | 1,360 | 150 |
| March | 150 | 1,150 | 100 | 170 | 1,420 | 150 |

Incremental cost:

- Overtime: `300 × $42 = $12,600`
- External finishing: `280 × $75 = $21,000`
- **Total: $33,600**

This plan protects the 150-unit inventory floor and fulfills the quarterly plan, but it depends on near-perfect electronic-kit supply and external-partner execution.

### Response B — Capacity plus controlled demand movement

Assume 80 flexible March units can move to April using a $25-per-unit commercial service credit. External finishing falls from 280 to 200 units.

- Overtime: `300 × $42 = $12,600`
- External finishing: `200 × $75 = $15,000`
- Service credits: `80 × $25 = $2,000`
- **Total: $29,600**

The second response saves **$4,000** versus Response A and creates more March supply headroom. It is preferable only if the affected customers agree and April capacity is reserved rather than allowing the problem to move into the next cycle.

## 6. Example executive decision note

> Approve the 4,100-unit Q1 demand plan subject to weekly validation of the two new customer agreements and supplier confirmation of electronic control kits. Use normal output plus 100 overtime units per month. Authorize up to 200 units of external finishing and move 80 flexible March units to April only with customer agreement and protected April capacity. The expected incremental planning cost is $29,600 while maintaining the 150-unit inventory floor. The principal risks are control-kit disruption (owner: procurement), delayed agreement conversion (owner: commercial), and external-partner quality or delivery failure (owner: operations). Track supplier-confirmed kits as the leading indicator and customer fill rate as the lagging indicator. Leadership must approve the external-spend ceiling and the rule for selecting flexible orders.

## Practitioner takeaway

The statistical forecast, commercial plan, and supply plan answer different questions. Strong planning does not force them to match silently; it makes the differences visible, assigns assumptions, evaluates feasible responses, and records the executive decision.

## Sensitivity and failure cases

The preferred response changes under several plausible conditions:

- **Customer movement is rejected.** Restore the 80 March units and use Response A. Incremental cost rises from $29,600 to **$33,600**, so the economic advantage disappears even though the plan remains arithmetically feasible.
- **The electronic-kit source loses effective capacity.** February already uses the full stated 1,360-unit allocation and March has only 20 units of nominal headroom. A delay, hold, or yield loss therefore triggers allocation, approved inventory use, or plan reduction; it cannot be hidden inside the forecast.
- **Commercial evidence weakens.** If agreement start dates or probability-weighted volumes no longer support 4,100 units, return to the statistical baseline and rebuild the monthly mix rather than preserving an unsupported override.
- **April cannot absorb the shifted units.** The movement is not a solution unless April capacity, component supply, and customer dates are protected. Otherwise use the no-movement response or reopen the quarterly demand decision.

The planning record should state these triggers before approval so that a later change is governed replanning, not a silent exception.

## Implementation roadmap

| Timing | Required action and evidence | Accountable owner | Gate or trigger |
|---|---|---|---|
| Before Q1 release | validate agreement start dates, customer flexibility, component allocations, external-finisher capacity, and the 150-unit inventory rule | commercial, procurement, operations, finance | release only when assumptions have dated evidence and owners |
| Weekly during Q1 | reconcile firm demand, cancellations, supplier-confirmed kits, output, external quality, and projected ending inventory | demand manager and supply-planning lead | reopen when a material assumption breaches its approved tolerance |
| Month end | compare baseline forecast, approved plan, actual demand, incremental cost, fill rate, and moved-order performance | S&OP owner and finance | continue, correct, or escalate with a documented cause and action |
| Q1 close | measure bias, service, inventory, supplier reliability, and realized response cost; update the next-cycle assumptions | executive S&OP team | retain the policy only when outcomes support it |

## Evaluation rubric

| Level | Evidence of completion |
|---|---|
| Incomplete | reports a forecast or preferred plan without reproducing the error measures, monthly inventory balance, cost, assumptions, or owners |
| Competent | reproduces the calculations, selects a feasible response, states the main trade-offs, and assigns the critical assumptions and risks |
| Excellent | also tests a decision-changing case, preserves forecast-versus-plan lineage, completes an executable decision record, and defines the evidence that authorizes continuation, correction, or escalation |

Return to the [capstone](README.md), the [Module 1 overview](../README.md), or the [forecasting formula sheet](../../calculations/forecasting/formula-sheet.md). Continue into [Module 2: Network Design, Digital Connectivity, and Performance](../../02-network-design-digital-connectivity-performance/README.md) to convert the approved demand and supply requirements into network, technology, data, and performance decisions.
