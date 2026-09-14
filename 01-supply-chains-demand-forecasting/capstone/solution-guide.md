# Capstone Solution Guide

This guide demonstrates one defensible approach to the NorthStar planning decision. A different recommendation can be equally strong when its assumptions, calculations, trade-offs, and triggers are explicit.

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

Return to the [capstone](README.md), the [Module 1 overview](../README.md), or the [forecasting formula sheet](../../calculations/forecasting/formula-sheet.md).
