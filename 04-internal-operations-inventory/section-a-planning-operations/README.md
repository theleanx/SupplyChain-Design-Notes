# Section A: Planning Operations

Planning operations translates aggregate supply-and-demand decisions into item-level production commitments, material requirements, and distribution replenishment signals.

This section follows fictional **Pinehaven Motion Systems**, a manufacturer of industrial servo drives. All examples, values, diagrams, datasets, and assessment questions are independently created for this repository.

## Learning outcomes

After completing Section A, you should be able to:

- place S&OP, master scheduling, MRP, production activity control, and their capacity checks in one planning architecture;
- build and interpret a master scheduling grid using forecast, customer orders, PAB, ATP, MPS, and time fences;
- distinguish independent and dependent demand and trace MRP from inputs to planned orders and exceptions;
- use BOM explosion, routing, lot sizing, lead-time offsetting, pegging, and firming correctly; and
- explain push, pull, and DRP logic across a multiechelon distribution network.

## Learning path

1. [Manufacturing Planning and Control Architecture](./01-manufacturing-planning-and-control-architecture.md)
2. [Master Scheduling and the Master Scheduling Grid](./02-master-scheduling-and-the-master-scheduling-grid.md)
3. [Planning Horizons, Time Fences, and Change Authority](./03-planning-horizons-time-fences-and-change-authority.md)
4. [Projected Available Balance and MPS Logic](./04-projected-available-balance-and-mps-logic.md)
5. [Allocation, Order Promising, and Available-to-Promise](./05-allocation-order-promising-and-available-to-promise.md)
6. [Disaggregation and Commitment Decision Points](./06-disaggregation-and-commitment-decision-points.md)
7. [MRP Logic, Inputs, and Demand Types](./07-mrp-logic-inputs-and-demand-types.md)
8. [Bills of Material and Explosion](./08-bills-of-material-and-explosion.md)
9. [Routing and Lot-Sizing for Dependent Demand](./09-routing-and-lot-sizing-for-dependent-demand.md)
10. [Lead Time, Offsetting, Planned Receipts, and Releases](./10-lead-time-offsetting-planned-receipts-and-releases.md)
11. [Managing MRP: Nervousness, Pegging, Firming, and Exceptions](./11-managing-mrp-nervousness-pegging-firming-and-exceptions.md)
12. [MRP Evolution: Closed-Loop MRP, MRP II, ERP, and DDMRP Context](./12-mrp-evolution-closed-loop-mrp-mrp-ii-erp-and-ddmrp-context.md)
13. [Push, Pull, and Distribution Requirements Planning](./13-push-pull-and-distribution-requirements-planning.md)
14. [Section A Review](./14-section-a-review.md)

## Working data and visuals

- [`master-schedule.csv`](../../assets/data/module-4/master-schedule.csv) — 13-week MPS, PAB, ATP, and time-fence scenario
- [`bom-structure.csv`](../../assets/data/module-4/bom-structure.csv) — multilevel PH-SD500 product structure
- [`mrp-planning.csv`](../../assets/data/module-4/mrp-planning.csv) — L4L/FOQ, projected on-hand, planned receipts/releases, and exceptions
- [`drp-network.csv`](../../assets/data/module-4/drp-network.csv) — two DCs, central supply, and plant replenishment logic
- [Internal Operations formula sheet](../../calculations/internal-operations/formula-sheet.md)

Each topic also includes a topic-specific original decision visual; process-oriented lessons include an operational flow where appropriate.

## How to study the section

Do not memorize the terms in isolation. Trace the same decision downstream: family plan → item master schedule → component requirement → timed release → distribution replenishment. Then trace exceptions backward using capacity checks, time fences, and pegging.

Every lesson contains an original decision visual, a fictional operating example, an applied artifact or calculation, trade-offs, common mistakes, and an original knowledge check.
