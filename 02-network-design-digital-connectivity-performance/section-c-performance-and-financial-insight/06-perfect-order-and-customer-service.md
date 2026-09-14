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

## Common mistakes

- Counting a partially filled order as perfect.
- Moving the promised date after acceptance without preserving history.
- Mixing orders, lines, units, and value denominators.
- Excluding difficult orders without transparent eligibility rules.
- Multiplying aggregate component rates instead of testing each order.

## Original knowledge check

An order is on time and complete but has incorrect compliance documentation. Is it perfect?

<details><summary>Answer</summary>

**No**, if correct documentation is a required condition. Perfect order is all-or-nothing at the defined evaluation level.
</details>

## Related concepts

Continue to [speed, reliability, and agility metrics](07-speed-reliability-and-agility-metrics.md).
