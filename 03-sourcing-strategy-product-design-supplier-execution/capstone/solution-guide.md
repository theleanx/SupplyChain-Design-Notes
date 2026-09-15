# Rivermark Capstone Worked Solution Guide

There is no single mandatory answer. A strong submission is internally consistent, reproducible from the fictional evidence, explicit about uncertainty, and executable. This guide demonstrates the expected depth; it is not a script to copy.

## Executive recommendation

Rivermark should retain control algorithms, firmware release, test design, interface ownership, and final product release. It should use qualified external board assembly with an internal or second-path recovery capability until transition evidence proves stability. Nearshore assembly leads the stated three-year cost model, but a hybrid path remains a defensible continuity choice if leadership values knowledge control and faster recovery above the modeled cost premium.

The distant control-board quote should not be awarded on purchase price. Its $13.00 quote advantage becomes a $3.40 per-unit total-cost disadvantage in the base case. Compressor assemblies require strategic capacity and continuity governance; refrigerant sensors require urgent alternate qualification or redesign. The modular product platform should advance through technical and operational validation, not immediate release. NorthPeak is the leading eligible supplier; VectorTherm is ineligible until its gate failure is resolved.

The commercial package should combine a transparent indexed price for established output with controlled development milestones, capacity commitments, service levels, change control, and obligation ownership. The first 90 days should close evidence gaps, qualify critical paths, configure controls, and prove the design and transaction process before irreversible cutover.

## 1. Capability boundary and transition

| Capability | Boundary | Reason | Retained control |
|---|---|---|---|
| Control algorithm and firmware | Make | Differentiating field performance and hard-to-rebuild learning | Source code, release authority, cyber controls, and test vectors |
| Board assembly | Buy with hybrid recovery | Capable external scale; process is important but not itself differentiating | Process specification, tooling rights, traceability, test data, and alternate route |
| Test design | Make | Controls product acceptance and preserves failure learning | Test limits, measurement system, golden samples, and change approval |
| Final product release | Make | Rivermark remains accountable to customers and regulators | Quality release, deviation authority, and field feedback |

### Three-year cost comparison

Use `three-year cost = 3 × (24,000 × unit conversion cost + annual fixed cost) + transition cost`.

| Option | Three-year cost | Readiness | Knowledge control | Continuity risk |
|---|---:|---:|---:|---:|
| Internal cell | $8,232,000 | 9 months | 5/5 | 2/5 |
| Domestic partner | $7,862,000 | 6 months | 4/5 | 2/5 |
| Nearshore partner | **$6,546,000** | 11 months | 3/5 | 3/5 |
| Hybrid internal/partner | $8,176,000 | 8 months | 5/5 | 1/5 |

Nearshore is $1,630,000 below hybrid over the modeled horizon. That difference is a decision input, not a command. A robust decision would test volume, utilization, transition duration, disruption probability, recovery cost, and a nonzero discount rate. The hybrid premium may be justified during launch and removed only after evidence-based exit gates.

### Transition gates

1. Process documentation, control plan, tooling ownership, and data access approved.
2. Receiving team trained and measurement systems correlated.
3. First articles and three representative lots conform.
4. Sustained-rate run demonstrates capacity, yield, traceability, and recovery.
5. Parallel supply protects customer service through stabilization.
6. Legacy capacity is retired only after the new route meets release criteria and an executable fallback remains.

## 2. Total-cost and should-cost conclusions

### Control-board bridge

| Cost element | Local | Distant | Distant minus local |
|---|---:|---:|---:|
| Purchase price | $74.00 | $61.00 | −$13.00 |
| Inbound freight | $1.20 | $4.80 | +$3.60 |
| Duty and brokerage | $0.00 | $3.10 | +$3.10 |
| Pipeline inventory | $0.55 | $3.40 | +$2.85 |
| Expected quality cost | $1.35 | $4.20 | +$2.85 |
| Relationship and control | $1.10 | $3.00 | +$1.90 |
| Continuity controls | $1.00 | $3.10 | +$2.10 |
| **Total per unit** | **$79.20** | **$82.60** | **+$3.40** |

At 24,000 units, the base-case distant disadvantage is `$3.40 × 24,000 = $81,600 per year`. The conclusion could reverse if the distant purchase price falls by more than $3.40 without offsetting changes, if quality and continuity exposure is overestimated, if logistics design materially lowers freight or pipeline time, or if the local source cannot meet required capacity or service. The model owner should show favorable, base, and adverse cases rather than reporting one number as certain.

### Should-cost fact base

The enclosure model totals `$54.60 + $12.80 + $7.00 + $4.00 + $10.00 = $88.40`. The $96.00 quotation therefore has a $7.60 modeled gap. Rivermark should validate material yield, changeover, lot size, utilization, and capital before treating any portion as addressable. A negotiated reduction is different from an engineering benefit that still requires investment and implementation.

## 3. Category and supply-base strategy

| Category | Portfolio view | Relationship and supply-base action |
|---|---|---|
| Compressor assemblies | Strategic: impact 5, risk 5 | Joint capacity and continuity plan, executive governance, sub-tier visibility, controlled allocation |
| Electronic controls | Strategic: impact 5, risk 4 | Platform governance, parent/site mapping, cyber and continuity qualification |
| Fabricated enclosures | Leverage: impact 4, risk 2 | Common specification, qualified regional panel, competitive total-cost event |
| Refrigerant sensors | Bottleneck: impact 2, risk 5 | Alternate qualification or redesign, controlled buffer, failure and recovery trigger |
| Fasteners | Routine: impact 1, risk 1 | Catalog automation, part standardization, exception-based management |
| Packaging | Routine: impact 2, risk 2 | Standardize specifications, compete qualified sources, manage sustainability evidence |

Parent-level compressor HHI is `52² + 28² + 20² = 3,888`. Sensor HHI is `100² = 10,000`. HHI indicates concentration, but the action also depends on independent capacity, common subtiers, qualification lead time, tooling portability, switching cost, and service consequence. Rivermark should not chase a generic supplier count.

## 4. Product-design decision

| Alternative | Parts | Assembly | Service | Units/pallet | Packaging/year | Failures/1,000 | Conversion cost | Validation risk |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Current integral | 184 | 46 min | 18 min | 6 | $310,000 | 14 | $0 | 1/5 |
| Simplified integral | 151 | 38 min | 12 min | 7 | $268,000 | 10 | $240,000 | 2/5 |
| Modular platform | **139** | **34 min** | **7 min** | **8** | **$224,000** | **8** | $650,000 | 4/5 |

Relative to current, the modular platform forecasts 24.5% fewer unique parts, 26.1% less assembly time, 61.1% less service time, 33.3% more units per pallet, 27.7% lower annual packaging cost, and 42.9% fewer estimated failures. It also requires the highest irreversible investment and carries the highest validation risk.

Advance it through gated validation covering safety, system performance, interfaces, tolerance stack, software and cyber behavior, pallet stability, handling, transport damage, assembly capability, field repair, supplier capacity, and customer acceptance. The release case should calculate payback using all recurring benefits—not packaging alone—and show downside scenarios. The simplified integral option is the fallback if modular-interface evidence does not clear the gate.

## 5. Supplier evaluation and award

The formula is `Σ(raw score ÷ 5 × criterion weight)`. Recalculation produces approximately 83 for NorthPeak, 78 for BlueHarbor, and 78 for VectorTherm. Apply gates before ranking:

| Supplier | Recalculated total | Gate | Award status |
|---|---:|---|---|
| NorthPeak | 83 | Pass | Preferred negotiation path |
| BlueHarbor | 78 | Pass | Credible BATNA and continuity option |
| VectorTherm | 78 | Fail | Ineligible pending resolved and reapproved evidence |

A sensitivity test might increase total-cost weight from 20 to 30 and reduce technical weight from 25 to 15. Recalculate from raw scores and document whether the eligible ranking reverses. Even if BlueHarbor moves ahead under that scenario, leadership must decide whether the new weights reflect the approved business need rather than adjusting weights to reach a preferred winner.

## 6. Negotiation and contract package

Rivermark's interests are assured capacity, field quality, transparent cost movement, technical support, recovery, and controlled change. NorthPeak may value forecast stability, capacity utilization, investment recovery, efficient governance, and growth. BlueHarbor is the principal BATNA, but its qualification status, available capacity, switching time, and implementation cost must be confirmed before negotiation.

Tradable packages can exchange a longer demand commitment for reserved capacity, forecast discipline for flexibility bands, shared productivity investment for verified cost reduction, and faster payment for economic value. Walk-away boundaries should cover total cost, minimum capacity, mandatory technical/legal conditions, liability, data access, and recovery rights.

Use defined unit pricing with a transparent index formula for uncontrollable input movements. Use milestone or target-cost controls for uncertain joint development. Include specification and change control, forecast and commitment rules, capacity, quality, delivery, warranty, tooling and intellectual property, cyber and compliance, audit, business continuity, liability, termination, and transition assistance. Place each risk with the party able to control it and price any retained exposure visibly.

## 7. Contract deployment and procure-to-pay controls

Convert each obligation into owner, evidence, frequency, threshold, and response. The provided register already covers price/index, forecast exchange, delivery reliability, incoming quality, cyber controls, and rebate. Add effective date, system control, escalation time, cure path, and retention requirement. Test the first forecast, PO, receipt, invoice, quality report, and rebate calculation before declaring deployment complete.

For PO 4500810, the PO authorizes 100 units at $50, the receipt is 98, and the invoice is 100. Release no more than `98 × $50 = $4,900` absent an approved tolerance or contract rule; hold the $100 difference and determine whether the cause is short shipment, receipt timing, or receiving error. For PO 4500812, the invoice is $129 against an authorized $125 for 40 units. Hold the `$4 × 40 = $160` price difference and validate the contract or approved PO change. Preserve the original records and resolution trail.

## 8. Exception priority

| Priority | Exception | Evidence-led response |
|---:|---|---|
| 1 | Refrigerant sensor | Twelve days late, two days cover, final-test stoppage. Confirm supplier overtime/courier, validate $3,900 authority, protect displaced demand, and activate continuity escalation. |
| 2 | Compressor 10 kW | Nine days late, three days cover, two priority units affected. Evaluate partial air freight at $6,800 against customer consequence and allocation alternatives. |
| 3 | Control board V4 | Two days late, nine days cover, service-stock risk. Reallocate uncommitted stock only after checking the demand it would displace. |
| 4 | Filter kit | On time, 26 days cover, no customer impact. Monitor without expediting. |

Every expedite should record decision authority, incremental cost, supplier commitment, next check, displaced consequence, root cause, and prevention owner. Premium freight is a recovery action, not a substitute for corrective action.

## 9. Ninety-day implementation

| Timing | Decision and evidence gate | Accountable roles |
|---|---|---|
| Days 1–15 | Approve capability boundary, assumptions, requirements, gates, and exception priorities | Executive sponsor, engineering, sourcing, planning |
| Days 16–30 | Validate TCO and should-cost drivers; confirm supplier parent/site map; start sensor alternate qualification | Finance, category lead, quality |
| Days 31–45 | Complete design prototypes and transport/service tests; recalculate supplier scores and sensitivity | Engineering, logistics, quality, sourcing |
| Days 46–60 | Approve architecture gate; negotiate commercial packages and confirm BATNA; select eligible award | Design authority, legal, finance, steering team |
| Days 61–75 | Sign and deploy obligations, master data, catalog/PO controls, receipt and invoice tolerances | Procurement operations, IT, AP, logistics |
| Days 76–90 | Run production and transaction pilots; test recovery escalation; approve controlled release or fallback | Operations, quality, planning, executive sponsor |

The day-90 decision is not “project complete.” It is an evidence gate: release, extend validation, use the fallback, or stop. The ongoing review should track total cost, delivery, incoming quality, capacity, expedite cost, design benefits, match exceptions, obligation compliance, and the triggers that would change the sourcing boundary.

## Final quality test

The recommendation is ready only when another reviewer can reproduce every major number, trace each decision to a dataset or stated assumption, see why the strongest alternative was rejected, identify the residual risk and contingency, and name the system, evidence owner, threshold, and date that will show whether the decision works.
