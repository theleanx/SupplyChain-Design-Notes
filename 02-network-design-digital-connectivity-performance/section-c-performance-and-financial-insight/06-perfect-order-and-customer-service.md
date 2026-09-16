# 6. Perfect Order and Customer Service

## Learning objectives

After this topic, you should be able to:

- define perfect order at order level;
- distinguish requested, promised, and actual performance;
- calculate fill, on-time, and perfect-order measures; and
- avoid partial-credit and denominator ambiguity.

## Perfect-order definition

An order is perfect when it meets every required condition, commonly including:

- correct product and quantity;
- delivered by the defined date and time;
- damage-free and usable condition; and
- complete and accurate documentation.

Organizations may add segment-specific conditions. The definition should remain stable and auditable.

## Calculation

$$
\text{Perfect-order rate}=\frac{\text{orders meeting every required condition}}{\text{eligible orders}}\times100\%
$$

If 930 of 1,000 eligible orders meet all conditions:

$$
930/1{,}000=93.0\%
$$

Use [`customer-service-metrics.csv`](../../assets/data/module-2/section-c/customer-service-metrics.csv) for the worked data.

## Related service measures

| Measure | Example definition |
|---|---|
| Order fill | orders shipped complete on the first committed shipment / eligible orders |
| Line fill | lines supplied in full / eligible lines |
| Unit fill | units supplied / units requested |
| On-time to request | deliveries meeting customer-requested date / eligible deliveries |
| On-time to promise | deliveries meeting accepted promised date / eligible deliveries |

These measures can produce different results. State the denominator and date basis.

## Decision flow

```mermaid
flowchart LR
    A[Customer request] --> B[Accepted promise]
    B --> C[Allocation and execution]
    C --> D[Actual delivery]
    D --> E[Condition and documentation]
    E --> F[Order-level result and cause]
```

## AsterWorks example

AsterWorks improves on-time-to-promise by extending promised lead times. The metric rises, but customer-request performance and cancellations worsen. The scorecard therefore shows request-to-promise gap alongside promise reliability.

## Why it matters

Separate service averages can look strong while few orders satisfy every customer requirement at the same time.

## Decision logic

Define eligible orders and all required conditions, calculate the intersection as perfect order, and diagnose failures by reason and segment. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain eligible population, requested and promised dates, completeness, damage and documentation rules, order-level evidence, failure reason, and owner. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **perfect order and customer service decision record** with these fields:

- **Decision and boundary:** Define eligible orders and all required conditions, calculate the intersection as perfect order, and diagnose failures by reason and segment.
- **Required evidence:** eligible population, requested and promised dates, completeness, damage and documentation rules, order-level evidence, failure reason, and owner.
- **Expected result:** Separate service averages can look strong while few orders satisfy every customer requirement at the same time.
- **Balancing condition:** A strict composite metric reflects customer experience but can hide which component caused failure without supporting diagnostics.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

A strict composite metric reflects customer experience but can hide which component caused failure without supporting diagnostics.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Define eligible orders and all required conditions, calculate the intersection as perfect order, and diagnose failures by reason and segment. Validate the result with eligible population, requested and promised dates, completeness, damage and documentation rules, order-level evidence, failure reason, and owner; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Counting a partially filled order as perfect.
- Moving the promised date after acceptance without preserving history.
- Mixing orders, lines, units, and value denominators.
- Excluding difficult orders without transparent eligibility rules.
- Multiplying aggregate component rates instead of testing each order.

## Original knowledge check

An order is on time and complete but has incorrect compliance documentation. Is it perfect?

<details>
<summary>Answer and rationale</summary>

### Correct answer

**No**, if correct documentation is a required condition. Perfect order is all-or-nothing at the defined evaluation level.

### Why it is correct

Separate service averages can look strong while few orders satisfy every customer requirement at the same time. Define eligible orders and all required conditions, calculate the intersection as perfect order, and diagnose failures by reason and segment.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Counting a partially filled order as perfect.
- Moving the promised date after acceptance without preserving history.
- Mixing orders, lines, units, and value denominators.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: A strict composite metric reflects customer experience but can hide which component caused failure without supporting diagnostics.

</details>

## Practitioner perspective

Use eligible population, requested and promised dates, completeness, damage and documentation rules, order-level evidence, failure reason, and owner as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts



- [Network and performance formula sheet](../../calculations/network-performance/formula-sheet.md)
- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)
Continue to [speed, reliability, and agility metrics](07-speed-reliability-and-agility-metrics.md).

---

[Previous: Benchmarking and Gap Analysis](05-benchmarking-and-gap-analysis.md) · [Next: Speed, Reliability, and Agility Metrics](07-speed-reliability-and-agility-metrics.md)
