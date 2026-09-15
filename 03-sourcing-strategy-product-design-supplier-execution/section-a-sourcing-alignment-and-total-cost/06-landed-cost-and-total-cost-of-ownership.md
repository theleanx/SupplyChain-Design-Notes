# 6. Landed Cost and Total Cost of Ownership

## Learning objectives

After this topic, you should be able to:

- distinguish price, landed cost, and total cost;
- select differentiating costs for an analysis;
- avoid false precision;

## Concept in plain English

Purchase price is the quoted item amount. Landed cost adds the cost to place the item where it is needed. Total cost of ownership adds transition, quality, inventory, administration, risk, use, service, and end-of-life consequences over the decision horizon.

## Why it matters

A distant source may win on price and lose after freight, duty, longer pipeline inventory, defects, engineering support, and disruption exposure are included.

## Decision model and workflow

![Landed Cost and Total Cost of Ownership decision workflow](../../assets/diagrams/module-3/section-a/06-landed-cost-and-total-cost-of-ownership-workflow.svg)

### Evidence retained through the workflow

| Stage | Required evidence or output |
|---|---|
| **1. Fix the decision horizon and volume** | Common volume, horizon, location, service level, and scenario assumptions |
| **2. Identify costs that differ by option** | Cost boundary showing purchase, landed, ownership, risk, and end-of-life elements |
| **3. Normalize currency, timing, and units** | Normalized cost model with currency date, payment timing, units, and tax treatment |
| **4. Quantify uncertainty with scenarios** | Base, favorable, and adverse scenarios with named drivers and confidence ranges |
| **5. Compare cost with service and risk** | Decision view separating expected cost, cash flow, service consequence, and residual risk |

## Practical process flow

```mermaid
flowchart TD
    A["Fix volume, horizon, destination, and service"] --> B["Normalize quotes and currency"]
    B --> C["Add freight, duty, and pipeline inventory"]
    C --> D["Add quality, control, and continuity costs"]
    D --> E["Test favorable and adverse scenarios"]
    E --> F["Compare cost, service, cash, and residual risk"]
```

## Realistic example — Rivermark Climate Systems

A Rivermark control board costs $74 locally and $61 from a distant supplier. After freight, duty, pipeline inventory, expected defect cost, relationship management, and continuity controls, the modeled per-unit total is $79.20 locally versus $82.60 distantly.

**Decision insight.** The distant source's $13 quote advantage becomes a $3.40 total-cost disadvantage after the options are compared at the same destination, service level, quality expectation, and continuity design.

All names and values in this example are fictional and independently selected for learning purposes.

## Worked decision — quote-to-total-cost bridge

The [total-cost dataset](../../assets/data/module-3/section-a/total-cost-options.csv) is denominated in USD per unit. The local-source total is:

`$74.00 + $1.20 + $0.00 + $0.55 + $1.35 + $1.10 + $1.00 = $79.20 per unit`

The distant-source total is:

`$61.00 + $4.80 + $3.10 + $3.40 + $4.20 + $3.00 + $3.10 = $82.60 per unit`

The distant quote is **$13.00 lower**, yet its modeled total cost is **$3.40 higher per unit**. At 24,000 units, that total-cost disadvantage is `$3.40 × 24,000 = $81,600 per year`. Keep uncertain quality and continuity estimates visible as scenarios; do not disguise them as audited cash costs.

## Decision logic

- Exclude costs identical across alternatives.
- Show expected, optimistic, and adverse cases.
- Keep hard cost, estimated exposure, and qualitative risk visibly separate.

## Trade-offs

| Choice tension | Decision implication |
|---|---|
| Broader scope improves completeness but increases uncertainty | Add a cost element only when it differs among options and can be estimated without double counting; show uncertain items as ranges. |
| Monetizing risk supports comparison but can imply unjustified precision | Report expected loss and non-financial exposure separately when monetization would suggest more certainty than the evidence supports. |

## Commonly confused with

Landed cost ends when usable supply arrives at the required location. Total cost continues through ownership, support, performance, and disposition.

## Common mistakes

- Adding only freight to purchase price.
- Double-counting risk in both expected cost and a score.
- Using one-year cost for a multi-year decision.

## Original knowledge check

**Question.** Which item belongs in total cost but not normally in landed cost?

A. Import duty

B. Inbound freight

C. Expected field-failure and warranty cost

D. Customs brokerage

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. Expected field-failure and warranty cost**

### Why it is correct

Field-failure cost occurs during ownership and use, after the item has landed.

### Why the other answers are wrong

A, B, and D are costs of bringing the item to the required location.

</details>

## Practitioner perspective

Show the cost bridge from quote to landed to total. Executives can challenge assumptions more effectively when additions are visible.

## Related concepts

- [Module 3 overview](../README.md)
- [Section overview](./README.md)
- [Total-cost dataset](../../assets/data/module-3/section-a/total-cost-options.csv)
- [Should-Cost and the Sourcing Business Case](./07-should-cost-and-business-case.md)
- [Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)

---

[Previous: Sourcing Requirements and Timing](./05-sourcing-requirements-and-timing.md) · [Next: Should-Cost and the Sourcing Business Case](./07-should-cost-and-business-case.md)
