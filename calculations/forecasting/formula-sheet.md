# Forecasting Formula Quick Sheet

## Three-point qualitative estimate

Simple:

`(P + M + O) / 3`

Weighted most-likely estimate:

`(P + 4M + O) / 6`

## Seasonal index

`Seasonal Index = Period Average / Overall Average Period`

## Deseasonalize

`Deseasonalized Demand = Raw Demand / Seasonal Index`

## Reseasonalize

`Final Forecast = Deseasonalized Forecast × Seasonal Index`

## Simple moving average

`SMA = Sum of Selected Recent Actuals / Number of Periods`

## Weighted moving average

`WMA = Σ(Weight × Actual) / ΣWeights`

## Exponential smoothing

`F(t) = αA(t−1) + (1−α)F(t−1)`

## Simple regression

`y = a + bx`

## Coefficient of determination

For simple correlation/regression interpretation:

`r² = r × r`

## Forecast error

Sign convention used in this repository:

`Error = Actual − Forecast`

## Absolute percentage error

`APE = |Actual − Forecast| / Actual × 100%`

## Forecast accuracy for one period

`Accuracy = 100% − APE`

## Mean absolute deviation

`MAD = Σ|Actual − Forecast| / n`

## Tracking signal

`Tracking Signal = Cumulative Signed Forecast Error / MAD`

## Sample standard deviation

`SD = √[Σ(x − x̄)² / (n−1)]`

## Mean squared error

`MSE = Σ(Actual − Forecast)² / n`

## Mean absolute percentage error

`MAPE = [Σ(|Actual − Forecast| / Actual) / n] × 100%`

## Safety-stock concept

`Safety Stock = Variability Measure × Service Factor`

Use the organization's approved variability basis and make sure the time interval of the variability measure matches the replenishment-risk interval.
