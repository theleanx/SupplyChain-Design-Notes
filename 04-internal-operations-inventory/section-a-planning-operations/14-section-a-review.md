# 14. Section A Review

Use these independently authored questions to test planning logic, calculations, and decision judgment. Choose an answer before opening the rationale.

## Question 1

**Question.** A dependent component has a gross requirement of 620 units, 170 units projected on hand, and a valid scheduled receipt of 100 units. Before lot sizing, what is the net requirement?

A. 350

B. 450

C. 550

D. 890

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. 350**

### Why it is correct

620 − 170 − 100 = 350 units.

### Why the other answers are wrong

- **B.** This subtracts only one available-supply element.

- **C.** This does not net both on-hand and scheduled receipt correctly.

- **D.** This adds available supply instead of subtracting it.

</details>

## Question 2

**Question.** Which record tells a planner which components and quantities are required to build PH-SD500?

A. Routing

B. Bill of material

C. Master schedule

D. Capacity plan

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Bill of material**

### Why it is correct

The BOM is the controlled quantitative product structure used for component explosion.

### Why the other answers are wrong

- **A.** Routing defines the operation path and sequence.

- **C.** The master schedule states item-level production commitments.

- **D.** Capacity planning tests resource feasibility.

</details>

## Question 3

**Question.** Which planning check is paired most directly with the master schedule?

A. Resource planning

B. Rough-cut capacity planning

C. Cycle counting

D. Input/output control only

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Rough-cut capacity planning**

### Why it is correct

RCCP tests whether critical resources can support the MPS before it drives detailed material planning.

### Why the other answers are wrong

- **A.** Resource planning is the longer-range check paired with aggregate production planning.

- **C.** Cycle counting checks inventory records.

- **D.** Input/output control is an execution-level capacity-control activity.

</details>

## Question 4

**Question.** Pinehaven has 80 units beginning inventory, an MPS receipt of 300, and 250 customer orders before the next MPS receipt. What is first-bucket discrete ATP?

A. 50

B. 80

C. 130

D. 380

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. 130**

### Why it is correct

First ATP = 80 + 300 − 250 = 130 units.

### Why the other answers are wrong

- **A.** This subtracts the values incorrectly.

- **B.** Beginning inventory alone is not ATP when an MPS receipt is also available.

- **D.** This ignores committed customer orders.

</details>

## Question 5

**Question.** Which item is a direct input to MRP for dependent-demand planning?

A. The master production schedule

B. A component sales forecast only

C. The annual financial statement

D. A cycle-count tolerance

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. The master production schedule**

### Why it is correct

MRP uses the parent/item plan in the MPS together with BOM, inventory status, and planning factors.

### Why the other answers are wrong

- **B.** Dependent requirements are calculated from parent demand rather than forecasted as the only direct driver.

- **C.** Financial statements are not a direct MRP material input.

- **D.** Cycle-count tolerances govern inventory control, not material explosion.

</details>

## Question 6

**Question.** Where should the operation sequence and work-center path for a component be maintained?

A. BOM

B. Routing

C. ATP bucket

D. Demand time fence

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Routing**

### Why it is correct

The routing describes the operation sequence, work centers, and associated processing path.

### Why the other answers are wrong

- **A.** The BOM defines components and quantities.

- **C.** ATP supports order promising.

- **D.** The DTF is a schedule-governance boundary.

</details>

## Question 7

**Question.** A part must be available in week 10 and has a two-week lead time. What is the basic offset release week?

A. Week 8

B. Week 10

C. Week 12

D. Week 20

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. Week 8**

### Why it is correct

Offsetting moves the release two weeks earlier than the required receipt date.

### Why the other answers are wrong

- **B.** This starts the order at the need date.

- **C.** This offsets in the wrong direction.

- **D.** Lead time is not multiplied by the need week.

</details>

## Question 8

**Question.** A single component reschedule message appears. Which action best limits unnecessary MRP churn?

A. Regenerate and change every order

B. Trace the exception with pegging and use targeted/net-change replanning when appropriate

C. Delete all firm planned orders

D. Increase the forecast

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Trace the exception with pegging and use targeted/net-change replanning when appropriate**

### Why it is correct

The planner should understand the parent impact and change only what the valid exception requires.

### Why the other answers are wrong

- **A.** Broad regeneration may amplify change without evidence.

- **C.** Firming controls should be reviewed, not universally removed.

- **D.** A forecast change is unrelated unless real independent demand changed.

</details>

## Question 9

**Question.** What does pegging tell the planner?

A. The source or parent requirement creating a component's demand

B. The current inventory valuation method

C. The work-center efficiency percentage

D. The customer credit limit

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. The source or parent requirement creating a component's demand**

### Why it is correct

Pegging links a component requirement to the parent demand/allocation that generated it.

### Why the other answers are wrong

- **B.** Inventory valuation is a financial/accounting topic.

- **C.** Capacity efficiency is a work-center measure.

- **D.** Credit limits do not establish MRP requirement origin.

</details>

## Question 10

**Question.** A proposed schedule change affects week 2 inside Pinehaven's frozen zone. Who should decide using the site's defined policy?

A. Any salesperson

B. The higher authority designated for frozen-zone changes

C. The MRP program without human review

D. The warehouse picker

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. The higher authority designated for frozen-zone changes**

### Why it is correct

Frozen-zone commitments require stronger approval because materials and capacity are already committed.

### Why the other answers are wrong

- **A.** Sales input may be important but does not override change governance.

- **C.** Automatic replanning is exactly what the protected zone restricts.

- **D.** Warehouse execution does not own the master-schedule decision.

</details>

## Question 11

**Question.** After the DTF, prior PAB is 140, MPS is 300, forecast is 220, and orders are 180. What is PAB under the method used in this section?

A. 220

B. 260

C. 300

D. 440

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. 220**

### Why it is correct

Use the greater demand signal, 220: 140 + 300 − 220 = 220.

### Why the other answers are wrong

- **B.** This subtracts 180 booked orders instead of the higher forecast.

- **C.** This ignores part of the demand.

- **D.** This adds supply but subtracts no demand.

</details>

## Question 12

**Question.** Which statement about MRP demand is most accurate?

A. Every component should be forecast independently

B. Dependent demand is derived from the parent structure, although the same item can also have independent demand

C. Independent demand is always internal

D. MRP removes the need for inventory records

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Dependent demand is derived from the parent structure, although the same item can also have independent demand**

### Why it is correct

An item can be both a component and an independently sold spare, so demand classification depends on the requirement source.

### Why the other answers are wrong

- **A.** Forecasting every dependent component ignores the BOM relationship.

- **C.** Independent demand is defined by independence from another item, not organization boundary.

- **D.** MRP depends on inventory status for netting.

</details>

## Question 13

**Question.** What was a key limitation of basic material-only MRP that closed-loop planning addresses?

A. It could assume capacity would be available for the material plan

B. It could not store any BOM

C. It prohibited lead times

D. It required every product to be make-to-stock

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. It could assume capacity would be available for the material plan**

### Why it is correct

Closed-loop planning adds capacity/execution feedback so infeasible schedules can be corrected.

### Why the other answers are wrong

- **B.** BOM automation is central to MRP.

- **C.** Lead times are required for timing.

- **D.** MRP logic is not limited to one manufacturing environment.

</details>

## Question 14

**Question.** Which statement best distinguishes MRP from DRP?

A. MRP follows the product structure; DRP follows the distribution-network structure

B. DRP forecasts all components while MRP counts warehouses

C. MRP is only financial and DRP is only physical

D. There is no difference

<details>
<summary>Answer and rationale</summary>

### Correct answer

**A. MRP follows the product structure; DRP follows the distribution-network structure**

### Why it is correct

Both can use time-phased netting and offsetting, but the structure being traversed is different.

### Why the other answers are wrong

- **B.** Component requirements in MRP are derived, not simply forecasted.

- **C.** Both are operational planning methods.

- **D.** Their planning structures and outputs differ.

</details>

## Question 15

**Question.** A 70-unit net requirement is governed by an FOQ of 500 units. What should the planned receipt be under the fixed-quantity rule?

A. 70

B. 430

C. 500

D. 570

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. 500**

### Why it is correct

FOQ creates the controlled fixed quantity when replenishment is triggered.

### Why the other answers are wrong

- **A.** 70 would be the L4L amount.

- **B.** 430 could resemble remaining excess after consumption, not the receipt.

- **D.** The shortage is not added to the fixed order quantity.

</details>

## Question 16

**Question.** What is the strongest reason to define commitment decision points with suppliers?

A. To ensure every forecast is legally binding

B. To clarify when planning visibility becomes volume or dated purchase commitment

C. To eliminate long-range forecasts

D. To make all suppliers carry unlimited buffer

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. To clarify when planning visibility becomes volume or dated purchase commitment**

### Why it is correct

Decision points align expectations about what each demand signal means and when the parties may act on it as a commitment.

### Why the other answers are wrong

- **A.** Long-range visibility can be nonbinding.

- **C.** Forecast visibility can still be valuable for capacity planning.

- **D.** Buffer responsibility should be deliberately agreed, not unlimited.

</details>

## Section completion check

You are ready to continue when you can:

- explain the full planning hierarchy without treating forecast, MPS, MRP, and execution as one plan;
- reproduce the PAB, ATP, net-requirement, BOM-explosion, and offsetting logic with new numbers;
- use time fences, pegging, firming, and exceptions to control—not suppress—change; and
- trace a downstream DRP release upstream to central supply and factory planning.

[Return to Section A](./README.md) · [Return to first lesson](./01-manufacturing-planning-and-control-architecture.md)
