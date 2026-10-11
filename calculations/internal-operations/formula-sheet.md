# Internal Operations and Inventory Formula Sheet

These formulas support the fictional Pinehaven Motion Systems examples in Module 4. Use the units and time horizon stated in each dataset.

## Master scheduling

### Projected available balance before the demand time fence

```text
PAB_t = PAB_(t-1) + MPS_t - Customer Orders_t
```

Inside the demand time fence, booked customer orders are the demand signal used in the worked example.

### Projected available balance after the demand time fence

```text
PAB_t = PAB_(t-1) + MPS_t - max(Forecast_t, Customer Orders_t)
```

Beyond the demand time fence, the example protects against using demand lower than either the forecast or the orders already booked.

### First-period available-to-promise

```text
ATP_1 = Beginning Inventory + MPS_1 - Customer Orders until the next MPS receipt
```

### Later-period available-to-promise

```text
ATP_t = MPS_t - Customer Orders until the next MPS receipt
```

Use this form only in periods with an MPS receipt. The repository examples use discrete, noncumulative ATP.

## Material requirements planning

### Net requirements

```text
Net Requirements = max(0, Gross Requirements - Projected Available Before Receipt - Scheduled Receipts)
```

The floor at zero prevents negative net requirements.

### Lead-time offsetting

```text
Planned Order Release Period = Planned Order Receipt Period - Lead Time
```

Offsetting changes timing, not the required quantity. Lot-sizing rules can change the planned receipt quantity.

## Capacity

### Available time

```text
Available Time = Hours of Operation × Number of Workers or Machines
```

State whether the result is worker-hours, machine-hours, or another capacity unit.

### Utilization

```text
Utilization = Hours Actually Worked / Available Hours × 100%
```

### Efficiency

```text
Efficiency = Standard Hours of Output / Hours Actually Worked × 100%
```

### Rated capacity

```text
Rated Capacity = Available Time × Utilization × Efficiency
```

Use utilization and efficiency as decimals in the multiplication.

### Demonstrated capacity

```text
Demonstrated Capacity = Sum of Actual Output over n periods / n
```

Demonstrated capacity is a historical practical result, so it may differ from rated capacity.

## Inventory and finance

### Average inventory estimate

```text
Average Inventory = (Beginning Inventory + Ending Inventory) / 2
```

This is a quick estimate only when the two endpoints reasonably represent the period.

### Annual monetary volume for ABC analysis

```text
Annual Monetary Volume = Unit Value × Annual Usage
```

Sort the values from highest to lowest before building cumulative percentages. Criticality or policy may justify an override of the value-only class.

### Accounting equation

```text
Assets = Liabilities + Owners' Equity
```

Inventory is an asset; this relationship is used only to show its financial-statement context.

### Inventory turns

```text
Inventory Turns = Annual Cost of Goods Sold / Average Inventory
```

Use inventory valued on a basis consistent with cost of goods sold.

## Replenishment

### Economic order quantity

```text
EOQ = sqrt((2 × Annual Demand × Ordering Cost) / (Annual Carrying Rate × Unit Cost))
```

The classical model assumes relatively stable demand and replenishment, no material stockout behavior, and a meaningful trade-off between ordering/setup cost and carrying cost.

### Order point

```text
Order Point = Demand During Lead Time + Safety Stock
```

If using a demand rate:

```text
Demand During Lead Time = Demand Rate × Lead Time
```

Keep the demand-rate and lead-time units consistent.

### Periodic-review maximum level

```text
Maximum Level = Demand Rate × (Review Interval + Lead Time) + Safety Stock
```

### Periodic-review order quantity

```text
Order Quantity = Maximum Level - Inventory On Hand
```

If a lesson introduces on-order inventory or backorders, the inventory-position definition must be stated explicitly before changing this calculation.

### Safety-stock control

Module 4 uses several safety-stock approaches conceptually rather than prescribing one universal numeric formula. The public lessons will identify the method used and will not invent a single mandatory formula.

## Lean / JIT

### Takt time

```text
Takt Time = Available Production Time / Customer Demand
```

Takt is the pace required to match customer demand. It is not the same as actual cycle time.

## Interpretation rule

A calculation is not a decision by itself. Each Module 4 lesson must state the assumptions, unit, horizon, operational consequence, and action or control supported by the result.
