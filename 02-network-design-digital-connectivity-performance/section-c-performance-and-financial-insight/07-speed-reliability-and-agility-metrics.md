# 7. Speed, Reliability, and Agility Metrics

## Learning objectives

After this topic, you should be able to:

- distinguish speed, reliability, and agility;
- define cycle-time boundaries and percentiles;
- measure recovery and upside response; and
- avoid using averages that hide operational risk.

## Three performance questions

- **Speed:** How long does the process take?
- **Reliability:** How consistently does it meet the defined promise or plan?
- **Agility:** How effectively can it respond to a material change?

A fast process can be unreliable. A reliable normal process may lack agility during disruption.

## Cycle time

$$
\text{Cycle time}=\text{end timestamp}-\text{start timestamp}
$$

State the events. “Order cycle time” could mean customer submission to delivery, acceptance to delivery, release to shipment, or another interval.

Report median and a high percentile when variability matters. An average of five days can hide a group of orders taking twenty days.

## Reliability

Reliability measures include:

- on-time-to-request and on-time-to-promise;
- schedule attainment within a tolerance;
- lead-time variability;
- commit stability; and
- repeatable quality or yield.

## Agility measures

| Measure | Definition concept |
|---|---|
| Upside response time | time required to achieve a defined sustained increase |
| Upside capacity | increase achievable within a defined period and constraints |
| Time to detect | disruption occurrence to validated recognition |
| Time to decide | recognition to approved response |
| Time to recover | disruption occurrence to restored acceptable performance |
| Value at risk | estimated consequence under a defined scenario |

```mermaid
flowchart LR
    A[Disruption occurs] --> B[Detect]
    B --> C[Assess impact]
    C --> D[Decide]
    D --> E[Execute recovery]
    E --> F[Restore and learn]
```

## AsterWorks example

AsterWorks’ average European delivery time is nine days. The median is seven, but the 90th percentile is nineteen because customs exceptions form a long tail. The average alone would understate reliability risk.

## Common mistakes

- Reporting cycle time without event boundaries.
- Using only averages for skewed distributions.
- Measuring recovery without an acceptable-performance threshold.
- Calling unused theoretical capacity “upside capability.”
- Improving speed by changing the promise rather than the process.

## Original knowledge check

Two lanes average six days. Lane A ranges from five to seven; Lane B ranges from two to eighteen. Are they operationally equivalent?

<details><summary>Answer</summary>

No. Lane B is much less reliable and requires different promise, buffer, and exception treatment.
</details>

## Related concepts

Continue to [cost, profit, and productivity](08-cost-profit-and-productivity.md).
