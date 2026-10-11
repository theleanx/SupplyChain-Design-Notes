# 15. Section C Review

These independently authored questions test the Section C decision logic. They do not reproduce private question-bank wording or answer choices. Choose an answer before opening the rationale.

## Question 1

**Question.** Pinehaven stocks a repair module that moves irregularly and only a few times per month. Forecast demand is lumpy by future week. Which ordering logic is the strongest candidate for evaluation?

A. Time-phased order point logic
B. A fixed daily reorder regardless of future needs
C. Maximum safety stock at every site
D. No planning because volume is low

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Time-phased order point logic**

### Why it is correct

Time-phased logic is useful for low-volume or irregular independent-demand items because it can see dated future requirements instead of relying only on an average trigger.

### Why the other answers are wrong

B ignores the lumpy pattern, C adds stock without solving timing, and D abandons control.

</details>

## Question 2

**Question.** Finished Pinehaven drives are loaded on a truck from the plant to a regional DC. What inventory category best describes them while they are moving between the two locations?

A. MRO
B. Work in process
C. In-transit inventory
D. Raw material

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. In-transit inventory**

### Why it is correct

The units are physically moving between supply-chain locations, so they are in transit.

### Why the other answers are wrong

A supports operations, B is not yet accepted finished output, and D has not entered production.

</details>

## Question 3

**Question.** A controller has completed assembly but is waiting for required final inspection and acceptance. Which category best fits?

A. Work in process
B. Finished goods
C. MRO
D. Hedge inventory

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Work in process**

### Why it is correct

The defined production/acceptance process is not complete, so the controller remains WIP.

### Why the other answers are wrong

B is premature; C and D describe different physical/policy concepts.

</details>

## Question 4

**Question.** A network has a supplier level, a manufacturing level, a distribution-center level, and a retailer level. It contains 31 individual sites. How many echelons are represented?

A. 4
B. 31
C. 35
D. One for every warehouse only

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. 4**

### Why it is correct

Echelons are structural levels rather than the number of individual sites.

### Why the other answers are wrong

B, C, and D count nodes or only one node type instead of the network levels.

</details>

## Question 5

**Question.** A spare part moves slowly, quantity demand is stable, but inbound transit time varies widely. What deserves evaluation before increasing a permanent quantity buffer?

A. Safety lead time
B. A larger selling price
C. More product variety
D. Elimination of the item master

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Safety lead time**

### Why it is correct

The dominant uncertainty is timing, so a time buffer may protect the need date without creating a large slow-moving quantity buffer.

### Why the other answers are wrong

B and C do not directly control replenishment timing, and D removes planning rather than improving it.

</details>

## Question 6

**Question.** Which environment is closest to the assumptions of the basic EOQ model taught in this section?

A. Known stable demand and lead time, all-at-once receipts, no modeled quantity discounts
B. Highly seasonal demand with unpredictable lead time and staged receipts
C. A one-time engineered project with no repeat demand
D. An item whose only constraint is a regulatory safety hold

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Known stable demand and lead time, all-at-once receipts, no modeled quantity discounts**

### Why it is correct

Those conditions are among the simplifying assumptions supporting the basic EOQ model.

### Why the other answers are wrong

B violates several assumptions, C is not a repeating replenishment environment, and D is a disposition/control issue.

</details>

## Question 7

**Question.** Pinehaven buys cleaning solvent used to maintain equipment; it does not become part of the product. In the Module 4 framing, how is it treated?

A. Finished-goods inventory asset
B. Work-in-process inventory
C. MRO support supply treated as a period expense in this learning context
D. Customer allocation

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. MRO support supply treated as a period expense in this learning context**

### Why it is correct

MRO supports operations rather than becoming saleable product inventory, and this section distinguishes its financial treatment from raw material, WIP, and finished goods.

### Why the other answers are wrong

A and B are saleable-production categories, and D is unrelated.

</details>

## Question 8

**Question.** Demand is 25 units/day, the review interval is 6 days, lead time is 4 days, safety stock is 75 units, and 145 units are on hand. What is the periodic-review order quantity?

A. 105 units
B. 180 units
C. 325 units
D. 395 units

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. 180 units**

### Why it is correct

Maximum level = `25 × (6 + 4) + 75 = 325`. Order quantity = `325 − 145 = 180`.

### Why the other answers are wrong

A omits part of the protection interval, C is the maximum target, and D adds terms incorrectly.

</details>

## Question 9

**Question.** Pinehaven wants to reduce counting effort without weakening control. Which policy is strongest?

A. Count all SKUs at exactly the same frequency forever
B. Count higher-value/critical or historically inaccurate items more frequently and use lower frequency where risk allows
C. Never count C items
D. Count only items that already have zero variance

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Count higher-value/critical or historically inaccurate items more frequently and use lower frequency where risk allows**

### Why it is correct

Cycle counting can direct effort based on value, criticality, movement, and error history.

### Why the other answers are wrong

A wastes effort, C removes necessary control, and D avoids the items that need investigation.

</details>

## Question 10

**Question.** An item has a minimum of 450 units, maximum of 1,500 units, and 420 units on hand at review. Under a simple min-max rule, what action follows?

A. No order because stock is above zero
B. Order 30 units to reach the minimum
C. Order 1,080 units to replenish toward the maximum
D. Order the EOQ automatically regardless of the min-max rule

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. Order 1,080 units to replenish toward the maximum**

### Why it is correct

The position is below the minimum, so the simple rule replenishes toward the maximum: `1,500 − 420 = 1,080`.

### Why the other answers are wrong

A ignores the trigger, B reaches only the minimum, and D substitutes another model.

</details>

## Question 11

**Question.** Pinehaven stops selling an older controller this year but has committed to field support for several more years. Which planning implication is correct?

A. Support costs and service-parts exposure can continue after the final sale
B. All obligations end when marketing stops selling the product
C. Every remaining spare should be scrapped on the end-of-sales date
D. Supplier contracts no longer matter after end of sales

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Support costs and service-parts exposure can continue after the final sale**

### Why it is correct

End of sales and end of service are separate milestones; installed products may require support long afterward.

### Why the other answers are wrong

B, C, and D ignore ongoing service, warranty, and supply commitments.

</details>

## Question 12

**Question.** Demand for an old product is falling, and a component supplier raises its minimum order quantity. What should Pinehaven evaluate?

A. Remaining demand, excess/obsolescence exposure, service need, and the economics of the new MOQ
B. Only the new unit price
C. Only warehouse square footage
D. Only the replacement-product advertising budget

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Remaining demand, excess/obsolescence exposure, service need, and the economics of the new MOQ**

### Why it is correct

A larger MOQ can force excess purchasing just as the product is declining, so it must be evaluated with remaining sales and service demand.

### Why the other answers are wrong

B, C, and D each omit essential end-of-life supply consequences.

</details>

## Question 13

**Question.** A replacement drive will be released in four months. Which information most directly helps decide how many units of the old drive to build before production stops?

A. Remaining lifetime sales quantity and timing
B. The oldest employee's service date
C. Last year's highest warehouse temperature
D. The EOQ of an unrelated MRO item

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Remaining lifetime sales quantity and timing**

### Why it is correct

The phase-out plan needs an estimate of remaining old-product demand so operations can choose the stop-production point and coordinate the replacement.

### Why the other answers are wrong

B, C, and D do not determine remaining customer demand for the old product.

</details>

## Question 14

**Question.** Annual volume is unchanged, but Pinehaven doubles the number of replenishment orders. Which inventory-cost category most directly increases if cost per order is unchanged?

A. Ordering cost
B. Unit acquisition cost
C. Finished-goods revenue
D. Standard selling price

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Ordering cost**

### Why it is correct

Ordering cost is driven by the number of order/setup events, so more events increase the annual total when cost per event is unchanged.

### Why the other answers are wrong

B depends on units and unit price, while C and D are commercial measures rather than event-driven inventory costs.

</details>

## Question 15

**Question.** Average demand is 60 units/day, lead time is 9 days, and safety stock is 140 units. What is the basic order point?

A. 400 units
B. 540 units
C. 680 units
D. 1,260 units

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. 680 units**

### Why it is correct

Lead-time demand is `60 × 9 = 540`; adding 140 safety stock gives an order point of 680 units.

### Why the other answers are wrong

A and B omit part of the requirement, while D multiplies rather than adds the safety buffer.

</details>

## Question 16

**Question.** Which risk becomes more significant when Pinehaven repeatedly orders well above forecasted need for a technology component with frequent revisions?

A. Obsolescence exposure
B. Lower average inventory by definition
C. Elimination of carrying cost
D. Guaranteed higher customer demand

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Obsolescence exposure**

### Why it is correct

Excess stock is more likely to remain when the item changes or demand falls, increasing write-down/write-off exposure.

### Why the other answers are wrong

B and C move in the opposite direction, and D is not caused by buying extra stock.

</details>

## Question 17

**Question.** Which inventory-related consequence is often important in a safety-stock decision even though it is harder to quantify than unit price or storage rent?

A. Lost-sale or lost-customer cost
B. The printed purchase price
C. A known invoice-processing fee
D. Contracted warehouse rent

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Lost-sale or lost-customer cost**

### Why it is correct

Service failure can create meaningful economic loss, but its value is usually more uncertain than direct transaction or facility costs.

### Why the other answers are wrong

B, C, and D are generally more directly observable.

</details>

## Question 18

**Question.** What is the strongest aggregate inventory-management objective?

A. Minimize inventory dollars regardless of service
B. Balance customer service, operating efficiency, and inventory investment in support of strategy and financial goals
C. Maximize every SKU's individual turns
D. Put the same number of units in every DC

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Balance customer service, operating efficiency, and inventory investment in support of strategy and financial goals**

### Why it is correct

Aggregate inventory management balances competing enterprise objectives instead of optimizing one measure in isolation.

### Why the other answers are wrong

A, C, and D can create service failures or unnecessary stock.

</details>

## Question 19

**Question.** Which finance concept can be used as evidence for the opportunity cost of capital tied up in inventory?

A. An approved weighted average cost of capital (WACC) basis
B. The product's color code
C. The warehouse aisle number
D. The customer service phone queue

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. An approved weighted average cost of capital (WACC) basis**

### Why it is correct

Capital tied up in inventory has an opportunity cost; finance may use an approved WACC or related capital basis as part of the carrying-rate policy.

### Why the other answers are wrong

B, C, and D do not measure the cost of capital.

</details>

## Question 20

**Question.** Why should the old product's phase-out plan be coordinated with replacement-product readiness?

A. To reduce the risk that the old product is unavailable before the replacement can satisfy customer demand
B. To guarantee the new product never needs inventory
C. To eliminate all service obligations immediately
D. To make supplier lead times irrelevant

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. To reduce the risk that the old product is unavailable before the replacement can satisfy customer demand**

### Why it is correct

End-of-life management should protect the customer transition while avoiding both premature stockout and excessive residual inventory.

### Why the other answers are wrong

B, C, and D overstate what a phase-out plan can accomplish.

</details>

## Section completion check

You are ready to continue when you can explain the trade-offs behind the answers, reproduce the section calculations from the locked datasets, and apply the inventory logic to a different business without reusing Pinehaven's assumptions.

[Return to Section C](./README.md)
