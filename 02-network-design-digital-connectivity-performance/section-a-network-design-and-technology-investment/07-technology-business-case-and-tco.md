# 7. Technology Business Case and Total Cost

## Learning objectives

After this topic, you should be able to:

- distinguish benefits, costs, risks, and enabling assumptions;
- calculate benefit-cost ratio, ROI, and simple payback;
- build a total-cost view across implementation and operation; and
- test whether benefits are owned and measurable.

## Concept in plain English

A technology business case explains how a changed capability produces an operational outcome and how that outcome creates economic value. The application is an enabler, not the benefit itself.

```mermaid
flowchart LR
    A[Technology capability] --> B[Process change]
    B --> C[Operational outcome]
    C --> D[Financial effect]
    D --> E[Measured realization]
```

Example: event integration → earlier delay detection → more recovery time → fewer expedites and service failures → lower cost and retained revenue.

![Technology investment value chain](../../assets/diagrams/module-2/section-a/technology-value-chain.svg)

## Cost categories

Include the full lifecycle:

- subscription, license, infrastructure, or device cost;
- implementation, configuration, integration, migration, and testing;
- data cleansing and governance;
- process redesign, training, and change support;
- internal subject-matter and backfill time;
- security, privacy, assurance, and partner onboarding;
- support, monitoring, upgrades, and continuous improvement;
- transition, parallel operation, and retirement of old services; and
- contingency for defined risks.

The analysis dataset is [`technology-business-case.csv`](../../assets/data/module-2/section-a/technology-business-case.csv).

## Benefit categories

Benefits may be:

- **cost removed:** freight, labor, write-offs, downtime, or fees;
- **cash released:** lower inventory or faster collection;
- **capacity created:** more throughput without equivalent capital;
- **revenue protected or enabled:** better availability or service;
- **risk reduced:** lower probability or consequence of a defined event; or
- **decision quality improved:** faster, more consistent, or more explainable choices.

Keep cash, accounting profit, capacity, and risk benefits separate. They are not interchangeable.

## Core calculations

Assume three-year quantified benefits of $690,000 and total costs of $510,000.

### Benefit-cost ratio

$$
\text{Benefit-cost ratio}=\frac{690{,}000}{510{,}000}=1.35
$$

A value above 1.0 means quantified benefits exceed quantified costs under the stated assumptions.

### Return on investment

$$
\text{ROI}=\frac{690{,}000-510{,}000}{510{,}000}=35.3\%
$$

### Simple payback

If initial implementation is $330,000 and steady annual net cash benefit is $150,000:

$$
\text{Payback}=\frac{330{,}000}{150{,}000}=2.2\text{ years}
$$

Simple payback ignores the timing of cash flows after recovery. For large or long-duration investments, discounted cash-flow analysis is more informative.

## Benefit ownership table

| Benefit | Baseline | Target | Owner | Evidence |
|---|---:|---:|---|---|
| Expedite cost | $420k/year | $270k/year | transportation lead | freight invoices |
| Inventory write-off | $180k/year | $120k/year | planning lead | disposal postings |
| Planner rework | 2,400 h/year | 1,200 h/year | planning manager | activity sample |

If no operational owner accepts the target or no baseline exists, the benefit is not ready for approval.

## Sensitivity analysis

Test at least:

- slower adoption;
- lower transaction volume;
- implementation delay;
- cost overrun;
- partial partner participation; and
- benefits beginning later than planned.

Do not use false precision. Present a base case, downside case, and key break-even assumption.

## Why it matters

Technology value depends on adoption, process change, data quality, and benefit ownership—not licensed functionality alone.

## Decision logic

Build a time-phased total-cost and benefit model, separate cash from capacity and risk, calculate ROI and payback, and test volume, adoption, and timing sensitivity. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain cost and benefit rows by year, baseline, measurement basis, owner, adoption assumption, dependencies, sensitivity, and realization evidence. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **technology business case and total cost decision record** with these fields:

- **Decision and boundary:** Build a time-phased total-cost and benefit model, separate cash from capacity and risk, calculate ROI and payback, and test volume, adoption, and timing sensitivity.
- **Required evidence:** cost and benefit rows by year, baseline, measurement basis, owner, adoption assumption, dependencies, sensitivity, and realization evidence.
- **Expected result:** Technology value depends on adoption, process change, data quality, and benefit ownership—not licensed functionality alone.
- **Balancing condition:** A broader first release may promise more value but increases integration, change, schedule, and benefit-realization risk.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

A broader first release may promise more value but increases integration, change, schedule, and benefit-realization risk.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Build a time-phased total-cost and benefit model, separate cash from capacity and risk, calculate ROI and payback, and test volume, adoption, and timing sensitivity. Validate the result with cost and benefit rows by year, baseline, measurement basis, owner, adoption assumption, dependencies, sensitivity, and realization evidence; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Counting every saved minute as headcount reduction.
- Including revenue opportunity without probability or capacity constraints.
- Omitting internal time and ongoing data cost.
- Treating sunk cost as a reason to continue a weak investment.
- Approving benefits without an accountable operational owner.

## Original knowledge check

A project claims 10,000 hours of capacity benefit but has no plan to reduce overtime, avoid hiring, increase output, or redeploy the time. Is the amount a realized cash benefit?

<details>
<summary>Answer and rationale</summary>

### Correct answer

**Not yet.** It is potential capacity. The business case must state how the released time changes cash, cost, throughput, or another measured outcome.

### Why it is correct

Technology value depends on adoption, process change, data quality, and benefit ownership—not licensed functionality alone. Build a time-phased total-cost and benefit model, separate cash from capacity and risk, calculate ROI and payback, and test volume, adoption, and timing sensitivity.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Counting every saved minute as headcount reduction.
- Including revenue opportunity without probability or capacity constraints.
- Omitting internal time and ongoing data cost.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: A broader first release may promise more value but increases integration, change, schedule, and benefit-realization risk.

</details>

## Practitioner perspective

Use cost and benefit rows by year, baseline, measurement basis, owner, adoption assumption, dependencies, sensitivity, and realization evidence as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts



- [Network and performance formula sheet](../../calculations/network-performance/formula-sheet.md)
- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-a-sourcing-alignment-and-total-cost/01-strategic-sourcing-from-demand.md)
Continue to [capability maturity and transformation roadmap](08-capability-maturity-and-transformation-roadmap.md).

---

[Previous: Digital Requirements and Information Latency](06-digital-requirements-and-information-latency.md) · [Next: Capability Maturity and Transformation Roadmap](08-capability-maturity-and-transformation-roadmap.md)
