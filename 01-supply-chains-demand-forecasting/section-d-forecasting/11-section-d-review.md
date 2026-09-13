# 11. Section D Review and Original Practice

These original questions reinforce forecasting concepts through practical scenarios and calculations.

## Rapid review

You should be able to explain these relationships without notes:

```text
Demand history
   ↓ visualize
Pattern identified
   ↓
Seasonal? → deseasonalize
   ↓
Choose method
   ├─ qualitative
   ├─ time-series
   └─ associative
   ↓
Back-test
   ↓
Forecast
   ↓
Reseasonalize if needed
   ↓
Measure error
   ├─ MAD
   ├─ tracking signal
   ├─ standard deviation
   ├─ MSE
   └─ MAPE
   ↓
Improve model / assumptions
```

## Original practice questions

### 1. Orders vs. demand

A distributor orders 600 additional pumps because it expects a supplier shortage, even though customer consumption has not changed. Which quantity should a demand forecaster be most careful about using as the demand signal?

A. Customer consumption  
B. Distributor replenishment order  
C. Product-family forecast  
D. Installed-base data

<details><summary>Answer</summary>

**B. Distributor replenishment order.** The order contains inventory-positioning behavior that is not the same as end demand.
</details>

### 2. Aggregation

A company can forecast total monthly demand for all safety gloves more accurately than demand for one color and size combination. Which principle best explains this?

A. Causation  
B. Risk pooling / aggregation  
C. Exponential smoothing  
D. Tracking signal

<details><summary>Answer</summary>

**B.** Item-level errors can partially offset when demand is pooled.
</details>

### 3. Forecast horizon

Which forecast would generally be expected to have less error, all else equal?

A. SKU-level demand 18 months from now  
B. Product-family demand next month  
C. New-product configuration mix in two years  
D. Individual-customer demand in five years

<details><summary>Answer</summary>

**B.** Near-term and aggregated forecasts are generally more accurate.
</details>

### 4. New product

A company is launching a new industrial sensor with no usable sales history. What is the strongest starting approach?

A. Six-month moving average of zero demand  
B. Structured expert judgment supported by market evidence  
C. Tracking signal  
D. MSE

<details><summary>Answer</summary>

**B.** Qualitative methods are especially important when historical demand does not exist.
</details>

### 5. Moving-average periods

A planner increases a moving average from 3 periods to 8 periods. What is the most likely effect?

A. Less smoothing and faster response  
B. More smoothing and more lag  
C. Automatic removal of seasonality  
D. Elimination of forecast error

<details><summary>Answer</summary>

**B.** More periods damp random fluctuations but normally react more slowly to trend change.
</details>

### 6. Exponential smoothing

Last period's actual demand is 250, last period's forecast is 230, and α = 0.25. What is the new forecast?

A. 235  
B. 240  
C. 245  
D. 250

<details><summary>Answer</summary>

**A. 235.** `0.25×250 + 0.75×230 = 235`.
</details>

### 7. Seasonal index

A month has an average demand of 150 units while the overall average month is 120 units. What is its seasonal index?

A. 0.80  
B. 1.20  
C. 1.25  
D. 1.50

<details><summary>Answer</summary>

**C. 1.25.** `150 / 120 = 1.25`.
</details>

### 8. Reseasonalizing

A deseasonalized forecast is 200 units and the future month's seasonal index is 0.80. What is the planning forecast?

A. 160  
B. 200  
C. 240  
D. 250

<details><summary>Answer</summary>

**A. 160.** `200 × 0.80 = 160`.
</details>

### 9. Service forecasting

A contact center experiences two daily peaks. What is the most direct use of an hourly demand forecast?

A. Set annual depreciation  
B. Plan staffing and service capacity by time interval  
C. Calculate product life cycle  
D. Determine vertical integration

<details><summary>Answer</summary>

**B.** Service capacity often must be matched closely to demand by hour.
</details>

### 10. Associative forecasting

A replacement-parts company forecasts compressor-kit demand from the installed population of compressors. What type of approach is this?

A. Associative forecasting  
B. Naive forecasting  
C. Random variation  
D. Delphi

<details><summary>Answer</summary>

**A.** An external or causal predictor is used to estimate demand.
</details>

### 11. Correlation

A model shows `r = 0.90`. What can be concluded safely?

A. The predictor causes demand  
B. The variables have a strong positive linear relationship in the data  
C. Forecast accuracy is 90%  
D. MAPE is 10%

<details><summary>Answer</summary>

**B.** Correlation describes relationship strength; it does not by itself prove causation or forecast accuracy.
</details>

### 12. Bias

Actual-minus-forecast error is negative month after month. What pattern does this suggest?

A. Persistent over-forecasting  
B. Persistent under-forecasting  
C. No bias  
D. Perfect accuracy

<details><summary>Answer</summary>

**A.** Under the sign convention used here, negative error means forecast exceeds actual demand.
</details>

### 13. MAD

Absolute forecast errors over four months are 3, 5, 2, and 6. What is MAD?

A. 4  
B. 8  
C. 16  
D. 64

<details><summary>Answer</summary>

**A.** `(3+5+2+6)/4 = 4`.
</details>

### 14. Tracking signal

Cumulative signed forecast error is −12 and MAD is 3. What is the tracking signal?

A. −4  
B. −3  
C. +3  
D. +4

<details><summary>Answer</summary>

**A. −4.** `−12 / 3 = −4`.
</details>

### 15. Standard deviation and service level

If a planner increases the safety factor while the variability estimate stays the same, what generally happens?

A. Safety stock decreases  
B. Safety stock increases  
C. MAPE becomes zero  
D. Seasonality disappears

<details><summary>Answer</summary>

**B.** Greater service protection normally requires a larger buffer.
</details>

### 16. MSE

Forecast errors are +2 and −4. What is the MSE?

A. 3  
B. 6  
C. 10  
D. 20

<details><summary>Answer</summary>

**C. 10.** `(2² + (−4)²) / 2 = (4+16)/2 = 10`.
</details>

### 17. MAPE

Why can MAPE be useful when comparing two product families of very different volume?

A. It measures only bias  
B. It expresses error on a percentage scale  
C. It removes seasonality  
D. It guarantees causal validity

<details><summary>Answer</summary>

**B.** Percentage error provides a common relative scale.
</details>

### 18. Commercial override

A statistical forecast is consistently improved by a sales override. What should the company do?

A. Remove all judgment immediately  
B. Keep measuring baseline and adjusted forecast separately  
C. Stop measuring error  
D. Convert the model to naive forecasting

<details><summary>Answer</summary>

**B.** Separate measurement shows whether judgment adds repeatable value and guards against hidden bias.
</details>

## Final checklist

- [ ] I can explain the major forecasting principles.
- [ ] I can choose between qualitative, time-series, and associative approaches.
- [ ] I can calculate seasonal indices and reseasonalize a forecast.
- [ ] I can calculate moving averages and exponential smoothing.
- [ ] I understand service-sector intraday forecasting.
- [ ] I can explain leading vs. lagging indicators.
- [ ] I understand regression, correlation, and causation.
- [ ] I can calculate forecast error, MAD, tracking signal, MSE, and MAPE.
- [ ] I can explain the role of standard deviation and safety factors.

## Related concepts

Module 1 → Section D → all major forecasting topics. Questions, distractors, examples, and explanations are original.
