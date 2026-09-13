# 6. Service-Sector and Associative Forecasting

## Learning objectives

You should be able to:

- explain why service demand may require hourly or even shorter forecasting buckets;
- connect service forecasts to capacity decisions;
- distinguish time-series forecasting from associative forecasting;
- explain independent and dependent variables in a forecasting context.

## Service-sector forecasting

A factory may plan demand by week or month. A service operation may need to plan by **hour** because unused service capacity often cannot be stored for later.

Examples:

- call center agents;
- restaurant staff;
- hospital intake capacity;
- airport security lanes;
- field-service technicians;
- checkout counters.

![Service-sector hourly demand](../../assets/diagrams/module-1/section-d/service-hourly-demand.svg)

Original data:

[`service-hourly-demand.csv`](../../assets/data/module-1/section-d/service-hourly-demand.csv)

### Planning implications

An hourly demand forecast can influence:

- shift schedules;
- break timing;
- number of service stations;
- queue capacity;
- replenishment timing;
- perishable inventory;
- temporary labor.

The forecast may also need a **service mix** forecast. A restaurant needs more than total customer count; it also needs expected demand by menu item.

## Associative forecasting

Associative forecasting predicts demand using one or more variables thought to have a meaningful relationship with demand.

Terminology:

- **independent variable (x):** predictor;
- **dependent variable (y):** value being forecast.

Examples:

| Predictor | Possible demand being forecast |
|---|---|
| Building permits | Construction materials |
| Installed machine population | Spare-parts demand |
| Airline passenger bookings | Airport catering volume |
| Weather severity index | Emergency repair demand |
| Advertising spend | Consumer-product sales |

## Intrinsic vs. extrinsic idea

Time-series forecasting is often considered **intrinsic** because it uses the item's own history.

Associative forecasting is often considered **extrinsic** because it uses information outside the demand series itself.

## When associative forecasting is useful

Use it when:

- a meaningful driver of demand can be measured;
- the historic time series alone does not explain changing demand;
- a longer-term or aggregate forecast is needed;
- the relationship is plausible and can be tested.

## Correlation is not enough

A predictor should make business sense. A variable can correlate statistically by coincidence or because both variables are affected by a third factor.

The forecasting team should be able to explain **why** the relationship is useful, not merely show a high correlation number.

## Common mistake

Forecasting kitchen-appliance demand from new-housing activity is an **associative** approach because an external predictor is being used to forecast demand.

## Related concepts

Module 1 → Section D → Service-Sector Forecasting / Quantitative Methods: Associative Forecasting. Wording, examples, and visual are original.
