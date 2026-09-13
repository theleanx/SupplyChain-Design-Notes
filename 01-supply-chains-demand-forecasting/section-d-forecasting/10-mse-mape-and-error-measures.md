# 10. MSE, MAPE, and Choosing an Error Measure

## Learning objectives

You should be able to:

- calculate mean squared error (MSE);
- calculate mean absolute percentage error (MAPE);
- explain why MSE emphasizes large misses;
- explain why percentage error supports comparison across products of different scale;
- select an error metric that matches the management question.

## Mean squared error (MSE)

MSE squares each forecast error before averaging.

`MSE = Σ(Actual − Forecast)² / n`

Using the original eight-period example:

Squared errors:

`4, 9, 9, 9, 9, 4, 16, 1`

Total = `61`

`MSE = 61 / 8 = 7.625`

### Why squaring matters

![MAD vs MSE penalty](../../assets/diagrams/module-1/section-d/mad-vs-mse-penalty.svg)

A miss of 6 units contributes:

- 6 to an absolute-error total;
- 36 to a squared-error total.

MSE therefore reacts strongly to large misses.

## Mean absolute percentage error (MAPE)

MAPE expresses the average absolute error relative to actual demand.

`MAPE = [Σ(|Actual − Forecast| / Actual) / n] × 100%`

For the original eight-period example:

`MAPE ≈ 2.40%`

This makes error easy to compare between products with very different demand volumes.

## Strengths and limits

| Metric | Strength | Limitation |
|---|---|---|
| MAD | Easy to understand in units | Hard to compare across very different volume scales |
| MSE | Strong penalty for large misses | Result is in squared units and less intuitive |
| MAPE | Scale-free percentage | Becomes problematic when actual demand is zero or very small |
| Tracking signal | Detects directional bias | Not a general magnitude measure |
| Standard deviation | Useful variability measure | Not the same as forecast error unless method is defined accordingly |

## Which measure should management use?

Use the metric that matches the decision.

### Question: “How many units are we typically wrong by?”

Use **MAD**.

### Question: “Are we systematically high or low?”

Use **tracking signal / cumulative signed error**.

### Question: “Are large misses especially unacceptable?”

MSE may be useful.

### Question: “Which product family has worse relative error?”

MAPE may help because it is percentage-based.

### Question: “How variable is demand around its mean?”

Use **standard deviation**.

## Worked comparison

Original eight-period example:

| Metric | Result |
|---|---:|
| MAD | 2.625 units |
| MSE | 7.625 squared units |
| MAPE | 2.40% |
| Cumulative signed error | +5 units |
| Tracking signal | +1.90 |

The metrics answer different questions. There is no single “best” error measure for every use.

## Common mistakes

- MSE magnifies larger errors because of squaring.
- MAPE is a percentage, not a unit quantity.
- A low cumulative signed error can hide large random positive and negative misses.

## Related concepts

Module 1 → Section D → Mean Squared Error / Mean Absolute Percentage Error / Error Measurement. Numerical example and visual are original.
