# 8. Short- and Medium-Term Demand Patterns

## Learning objectives

You should be able to:

- explain the operating logic behind short- and medium-term demand patterns;
- apply the lesson to a realistic planning or supply-chain decision; and
- identify the evidence, trade-off, and trigger needed for responsible use.

## The pattern-decomposition idea

Historical demand is rarely one clean signal. A useful mental model is:

**observed demand = base level + trend + seasonality + cycles/external drivers + promotions/internal drivers + random variation**

![Original demand-pattern decomposition](../../assets/diagrams/module-1/section-b/demand-pattern-decomposition.svg)

The purpose of analysis is not to force every data point into a story. It is to explain the repeatable structure well enough that forecasting can treat predictable effects differently from noise.

## Trend

A **trend** is a persistent direction over time — upward, flat, or downward. It can be linear or accelerate/decelerate.

Example: NorthStar's smart-pump family has grown about 7–10% annually for four years as customers adopt condition monitoring.

## Cycle

A **cycle** is a wave-like movement that lasts longer than a normal seasonal calendar pattern. Economic expansion and recession are classic examples. The timing is not reliably fixed to a month or quarter.

Example: demand for heavy construction equipment may rise and fall with multi-year investment cycles. External drivers can sometimes be tracked through **leading indicators** (early signal) or **lagging indicators** (confirmation after the change).

## Seasonality

**Seasonality** is a recurring calendar-linked pattern within a year. It can occur by month, week, day, or even hour.

Examples:

- cold-drink demand rises in summer;
- parcel volume rises around year-end holidays;
- restaurant demand peaks at meal times;
- a B2B company sees order spikes at fiscal-quarter end.

If seasonality is material, forecasting often separates the underlying level/trend from the seasonal effect and then reapplies the seasonal pattern.

## Promotions and other internal drivers

Discounts, advertising, special placement, and commercial campaigns can intentionally change demand. If a promotion caused a spike, treating that spike as ordinary base demand can create a bad forecast.

### Example

Normal weekly demand for a home air purifier is about **2,400 units**. A two-week retail promotion creates sales of **5,800** and **6,200 units**. If the planner simply averages those weeks into the baseline, the future forecast may be inflated unless the promotion effect is identified separately.

## Random variation

Random variation is the residual fluctuation that remains after identifiable patterns and causes have been accounted for. It is the part we cannot reliably explain or predict.

A statistical-process-control analogy can help: identifiable effects such as a promotion or seasonal event behave like **special/assignable causes**, while the many small unexplained influences resemble **common-cause variation**. The analogy is useful because it encourages the planner to remove explainable structure before labeling the remainder as noise.

After identifiable structure has been removed, the remaining residual should behave more like noise than a repeatable pattern. If the residual still shows a strong shape, the analyst may have missed an explanatory driver. The goal is not to explain every point, but also not to label a repeatable cause as random.

A useful test is:

> If trend, seasonality, promotions, events, and other known drivers have already been addressed, what remains may be random variation rather than another pattern that needs a story.

## Compare the four major patterns

| Pattern | Calendar-fixed? | Typical horizon | Predictability |
|---|---:|---|---|
| Trend | No | Long | Direction may persist but can change |
| Seasonality | Yes | Within a year | Relatively predictable if history is stable |
| Cycle | No | Multi-year / irregular | Harder to time precisely |
| Random variation | No | Any | Unpredictable by definition |

## Why it matters

Trend, seasonality, cycles, promotions, and random variation require different forecasts and different operational responses.

## Decision logic

Decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain time series, event calendar, decomposition choice, horizon, parameters, residual error, owner, and recalibration trigger. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **short- and medium-term demand patterns decision record** with these fields:

- **Decision and boundary:** Decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions.
- **Required evidence:** time series, event calendar, decomposition choice, horizon, parameters, residual error, owner, and recalibration trigger.
- **Expected result:** Trend, seasonality, cycles, promotions, and random variation require different forecasts and different operational responses.
- **Balancing condition:** A responsive method detects change sooner but may overreact to noise; a stable method reduces noise but can lag a genuine shift.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

A responsive method detects change sooner but may overreact to noise; a stable method reduces noise but can lag a genuine shift.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions. Validate the result with time series, event calendar, decomposition choice, horizon, parameters, residual error, owner, and recalibration trigger; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes
Do not confuse **seasonality** with a **cycle**. A December holiday spike that repeats each year is seasonal. A multi-year construction boom and slowdown is cyclical.

## Original knowledge check

**Question.** NorthStar is deciding how to apply short- and medium-term demand patterns. Which proposal is most defensible?

A. Use short- and medium-term demand patterns as a label for the preferred option before defining the decision outcome, constraints, or owner.
B. Decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions.
C. Choose the apparent upside without evaluating this balancing condition: A responsive method detects change sooner but may overreact to noise; a stable method reduces noise but can lag a genuine shift.
D. Approve the choice without retaining time series, event calendar, decomposition choice, horizon, parameters, residual error, owner, and recalibration trigger; omit the reassessment trigger as well.

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions.**

### Why it is correct

Trend, seasonality, cycles, promotions, and random variation require different forecasts and different operational responses. The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions.
- **C** optimizes one visible result and omits the balancing effects: A responsive method detects change sooner but may overreact to noise; a stable method reduces noise but can lag a genuine shift.
- **D** leaves the approval unauditable. A reviewer would be missing time series, event calendar, decomposition choice, horizon, parameters, residual error, owner, and recalibration trigger, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: A responsive method detects change sooner but may overreact to noise; a stable method reduces noise but can lag a genuine shift.

</details>

## Practitioner perspective

Forecasting systems can decompose history mathematically, but human review still matters. Promotions, product transitions, stockouts, one-time projects, and data errors can all create apparent patterns that should not be extrapolated automatically.

## Related concepts


- [Section overview](./README.md)
- [Module 2 continuation](../../02-network-design-digital-connectivity-performance/section-a-network-design-and-technology-investment/02-market-segmentation-and-service-choices.md)
Module 1 → Section B → Short- to Medium-Term Demand Patterns, Trends, Cycles, Seasonality, Promotions, Random Variation. Graphic, table, examples, and wording are original.

---

[Previous: Microeconomics, Price Elasticity, and Marginal Analysis](07-microeconomics-price-elasticity-marginal-analysis.md) · [Section review](09-section-b-review.md)
