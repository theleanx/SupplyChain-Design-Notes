# 8. Forecast Error, Accuracy, Bias, and Random Variation

## Learning objectives

You should be able to:

- calculate forecast error;
- calculate absolute percentage error and forecast accuracy;
- distinguish bias from random variation;
- explain why monetary impact can matter more than unit error alone.

## Forecast error

Use a consistent sign convention. In this repository:

`Forecast Error = Actual Demand − Forecast Demand`

Example:

- actual = 98;
- forecast = 100.

`Error = 98 − 100 = −2`

A negative error means the forecast was higher than actual demand.

The **absolute error** is:

`|Actual − Forecast|`

so the absolute error is 2 units.

## Percentage error

Absolute percentage error (APE):

`APE = |Actual − Forecast| / Actual × 100%`

For actual demand of 98 and forecast of 100:

`APE = 2 / 98 × 100% ≈ 2.04%`

A simple forecast-accuracy expression is:

`Forecast Accuracy = 100% − APE`

so accuracy for that period is about **97.96%**.

## Unit error vs. business impact

A 100-unit miss on a $2 consumable is not financially equivalent to a 100-unit miss on a $20,000 component.

Forecast governance should therefore consider:

- error in units;
- error as a percentage;
- financial exposure;
- customer-service consequence;
- operational consequence.

## Bias vs. random variation

![Bias versus random variation](../../assets/diagrams/module-1/section-d/bias-vs-random-variation.svg)

### Bias

Bias exists when errors consistently lean in the same direction.

Examples:

- persistent over-forecasting;
- persistent under-forecasting;
- sales overrides that are consistently optimistic;
- seasonal peaks occurring earlier than the model expects.

### Random variation

Random variation produces positive and negative errors that can largely cancel over time.

Zero cumulative error does **not** mean the forecast is perfect. Large positive and negative misses could still be operationally painful.

## Original eight-period example

Original data:

[`forecast-error-example.csv`](../../assets/data/module-1/section-d/forecast-error-example.csv)

Errors are:

`−2, +3, −3, +3, +3, −2, +4, −1`

Cumulative algebraic error:

`+5 units`

The positive total suggests some net under-forecasting over the review window, although it is not extreme by itself.

## Practical diagnostic questions

If error increases, ask:

1. Is the problem directional bias or random noise?
2. Has seasonality shifted?
3. Did a promotion or one-time order distort demand?
4. Did a commercial override introduce bias?
5. Has the product life cycle changed?
6. Is the forecasting method still appropriate?

## Why it matters

Error magnitude and error direction drive different decisions: variability affects buffers, while persistent bias requires a model or process correction.

## Decision logic

Freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **forecast error, accuracy, bias, and random variation decision record** with these fields:

- **Decision and boundary:** Freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes.
- **Required evidence:** actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action.
- **Expected result:** Error magnitude and error direction drive different decisions: variability affects buffers, while persistent bias requires a model or process correction.
- **Balancing condition:** Aggregated accuracy simplifies reporting but can hide offsetting bias, high-value misses, and service-critical failures.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Aggregated accuracy simplifies reporting but can hide offsetting bias, high-value misses, and service-critical failures.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes. Validate the result with actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes
MAD uses absolute errors, so positive and negative signs disappear. Bias and tracking signal use signed error because direction matters.

## Original knowledge check

**Question.** NorthStar is deciding how to apply forecast error, accuracy, bias, and random variation. Which proposal is most defensible?

A. Use forecast error, accuracy, bias, and random variation as a label for the preferred option before defining the decision outcome, constraints, or owner.
B. Freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes.
C. Choose the apparent upside without evaluating this balancing condition: Aggregated accuracy simplifies reporting but can hide offsetting bias, high-value misses, and service-critical failures.
D. Approve the choice without retaining actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action; omit the reassessment trigger as well.

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes.**

### Why it is correct

Error magnitude and error direction drive different decisions: variability affects buffers, while persistent bias requires a model or process correction. The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes.
- **C** optimizes one visible result and omits the balancing effects: aggregated accuracy simplifies reporting but can hide offsetting bias, high-value misses, and service-critical failures.
- **D** leaves the approval unauditable. A reviewer would be missing actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: aggregated accuracy simplifies reporting but can hide offsetting bias, high-value misses, and service-critical failures.

</details>

## Practitioner perspective

A review should be able to reconstruct the choice from actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action. If those records cannot explain what changed, who decided, and when the decision will be revisited, the process is not yet controlled.

## Related concepts



- [Forecasting formula sheet](../../calculations/forecasting/formula-sheet.md)
- [Section overview](./README.md)
- [Module 2 continuation](../../02-network-design-digital-connectivity-performance/section-c-performance-and-financial-insight/01-measurement-system-design.md)
Module 1 → Section D → Forecast Error and Accuracy / Bias and Random Variation. Numerical example and visual are original.

---

[Previous: Leading Indicators, Regression, Correlation, and Causation](07-leading-indicators-regression-correlation.md) · [Next: MAD, Tracking Signal, Standard Deviation, and Safety Stock](09-mad-tracking-signal-standard-deviation.md)
