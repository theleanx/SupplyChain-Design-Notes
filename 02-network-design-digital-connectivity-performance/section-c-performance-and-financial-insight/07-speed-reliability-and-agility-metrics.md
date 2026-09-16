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

## Why it matters

Average speed can improve while variability and recovery remain poor, leaving customers unable to rely on the promise.

## Decision logic

Measure cycle-time distribution, promise reliability, and response to a defined disruption or demand change, then connect each to customer consequence. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain start and end events, time distribution, promise basis, on-time tolerance, disruption scenario, recovery measure, segment, and action. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **speed, reliability, and agility metrics decision record** with these fields:

- **Decision and boundary:** Measure cycle-time distribution, promise reliability, and response to a defined disruption or demand change, then connect each to customer consequence.
- **Required evidence:** start and end events, time distribution, promise basis, on-time tolerance, disruption scenario, recovery measure, segment, and action.
- **Expected result:** Average speed can improve while variability and recovery remain poor, leaving customers unable to rely on the promise.
- **Balancing condition:** Buffers improve reliability and agility but add inventory, capacity, time, or cost; removing them can expose variability.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Buffers improve reliability and agility but add inventory, capacity, time, or cost; removing them can expose variability.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Measure cycle-time distribution, promise reliability, and response to a defined disruption or demand change, then connect each to customer consequence. Validate the result with start and end events, time distribution, promise basis, on-time tolerance, disruption scenario, recovery measure, segment, and action; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Reporting cycle time without event boundaries.
- Using only averages for skewed distributions.
- Measuring recovery without an acceptable-performance threshold.
- Calling unused theoretical capacity “upside capability.”
- Improving speed by changing the promise rather than the process.

## Original knowledge check

Two lanes average six days. Lane A ranges from five to seven; Lane B ranges from two to eighteen. Are they operationally equivalent?

<details>
<summary>Answer and rationale</summary>

### Correct answer

No. Lane B is much less reliable and requires different promise, buffer, and exception treatment.

### Why it is correct

Average speed can improve while variability and recovery remain poor, leaving customers unable to rely on the promise. Measure cycle-time distribution, promise reliability, and response to a defined disruption or demand change, then connect each to customer consequence.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Reporting cycle time without event boundaries.
- Using only averages for skewed distributions.
- Measuring recovery without an acceptable-performance threshold.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: Buffers improve reliability and agility but add inventory, capacity, time, or cost; removing them can expose variability.

</details>

## Practitioner perspective

Use start and end events, time distribution, promise basis, on-time tolerance, disruption scenario, recovery measure, segment, and action as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts


- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)
Continue to [cost, profit, and productivity](08-cost-profit-and-productivity.md).

---

[Previous: Perfect Order and Customer Service](06-perfect-order-and-customer-service.md) · [Next: Cost, Profit, and Productivity](08-cost-profit-and-productivity.md)
