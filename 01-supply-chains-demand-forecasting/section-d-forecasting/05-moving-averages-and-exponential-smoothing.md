# 5. Moving Averages and Exponential Smoothing

## Learning objectives

You should be able to:

- calculate a simple moving average;
- calculate a weighted moving average;
- calculate exponential smoothing;
- explain how weights and alpha affect responsiveness;
- compare smoothing methods conceptually.

## Simple moving average

A simple moving average gives equal weight to a fixed number of recent periods.

For a 3-period moving average:

`Forecast = (A1 + A2 + A3) / 3`

Example using deseasonalized demand of 104, 108, and 111:

`(104 + 108 + 111) / 3 = 107.67`

### Trade-off

- more periods → more smoothing;
- more periods → more lag when the trend changes.

## Weighted moving average

A weighted moving average can give more importance to recent demand.

Example weights:

- oldest period = 1;
- middle period = 2;
- newest period = 3.

`Forecast = (1×104 + 2×108 + 3×111) / (1+2+3)`

`= 108.83`

The weights should be tested against historical results rather than selected only because they “feel right.”

## Exponential smoothing

Exponential smoothing uses:

- last period's actual demand;
- last period's forecast;
- smoothing constant **α**.

Formula:

`New Forecast = α(Last Actual) + (1−α)(Last Forecast)`

Example:

- α = 0.30;
- last actual = 111;
- last forecast = 106.

`0.30×111 + 0.70×106 = 107.5`

## What alpha means

| Alpha | Behavior |
|---|---|
| Low α | More weight on prior forecast; smoother; slower reaction |
| High α | More weight on recent actual; faster reaction; less smoothing |
| α = 1.0 | Becomes equivalent to a naive forecast |

A larger alpha is not automatically better. It should be selected by testing forecast error against history.

## Original comparison

![Forecast method comparison](../../assets/diagrams/module-1/section-d/forecast-method-comparison.svg)

Source data:

[`forecast-method-comparison.csv`](../../assets/data/module-1/section-d/forecast-method-comparison.csv)

## Why all three methods can lag

All three methods are mainly backward-looking. When demand changes structurally, each method needs actual observations before it can respond.

A forecast can therefore be mathematically consistent and still be strategically wrong.

## Quick comparison

| Method | Main strength | Main weakness |
|---|---|---|
| Naive | Very simple and cheap | Carries one-time spikes forward |
| Simple moving average | Smooths noise | Lags real trend changes |
| Weighted moving average | More responsive than equal weights | Requires judgment/testing of weights |
| Exponential smoothing | Efficient, tunable, low data storage | Still lags structural change |

## Why it matters

The smoothing choice determines how quickly a plan reacts to real change and how much random variation enters operations.

## Decision logic

Compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **moving averages and exponential smoothing decision record** with these fields:

- **Decision and boundary:** Compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs.
- **Required evidence:** actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change.
- **Expected result:** The smoothing choice determines how quickly a plan reacts to real change and how much random variation enters operations.
- **Balancing condition:** Greater smoothing stabilizes production and inventory but increases lag; higher responsiveness detects change faster but can amplify noise.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Greater smoothing stabilizes production and inventory but increases lag; higher responsiveness detects change faster but can amplify noise.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs. Validate the result with actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Increasing the number of moving-average periods usually increases smoothing **and** lag.
- Increasing alpha makes exponential smoothing **more responsive**, not more stable.
- Exponential smoothing does not eliminate lag.

## Original knowledge check

**Question.** NorthStar is deciding how to apply moving averages and exponential smoothing. Which proposal is most defensible?

A. Use moving averages and exponential smoothing as a label for the preferred option before defining the decision outcome, constraints, or owner.
B. Compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs.
C. Choose the apparent upside without evaluating this balancing condition: Greater smoothing stabilizes production and inventory but increases lag; higher responsiveness detects change faster but can amplify noise.
D. Approve the choice without retaining actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change; omit the reassessment trigger as well.

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs.**

### Why it is correct

The smoothing choice determines how quickly a plan reacts to real change and how much random variation enters operations. The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs.
- **C** optimizes one visible result and omits the balancing effects: greater smoothing stabilizes production and inventory but increases lag; higher responsiveness detects change faster but can amplify noise.
- **D** leaves the approval unauditable. A reviewer would be missing actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: greater smoothing stabilizes production and inventory but increases lag; higher responsiveness detects change faster but can amplify noise.

</details>

## Practitioner perspective

A review should be able to reconstruct the choice from actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change. If those records cannot explain what changed, who decided, and when the decision will be revisited, the process is not yet controlled.

## Related concepts



- [Forecasting formula sheet](../../calculations/forecasting/formula-sheet.md)
- [Section overview](./README.md)
- [Module 2 continuation](../../02-network-design-digital-connectivity-performance/section-c-performance-and-financial-insight/01-measurement-system-design.md)
Module 1 → Section D → Simple and Weighted Moving Averages, Exponential Smoothing. Numerical examples and visuals are original.

---

[Previous: Seasonality, Deseasonalizing, and Reseasonalizing](04-seasonality-deseasonalizing-reseasonalizing.md) · [Next: Service-Sector and Associative Forecasting](06-service-sector-and-associative-forecasting.md)
