# 5. Warehouse Management Systems

## Learning objectives

After this topic, you should be able to:

- explain the role of a warehouse-management application;
- connect receiving, storage, replenishment, picking, packing, and shipping;
- identify core interfaces and master data; and
- distinguish inventory accuracy from warehouse productivity.

## Concept in plain English

A warehouse-management application converts orders and inventory policy into directed physical work. It tracks stock by location and status, sequences tasks, confirms movement, and produces execution events.

```mermaid
flowchart LR
    A[Receive] --> B[Inspect and identify]
    B --> C[Put away]
    C --> D[Replenish]
    D --> E[Pick]
    E --> F[Pack and stage]
    F --> G[Load and ship]
    G --> H[Confirm and reconcile]
```

## Core capabilities

- inbound appointment and receipt;
- license-plate, lot, serial, and status tracking;
- storage-location and putaway determination;
- cycle counting and inventory correction;
- wave, batch, zone, or discrete picking;
- replenishment and labor tasking;
- packing, labeling, staging, and loading;
- cross-docking and flow-through handling;
- returns and value-added services; and
- automation or equipment integration.

## Required interfaces

| Interface | Information exchanged |
|---|---|
| Transaction core | deliveries, inventory postings, orders, ownership, valuation reference |
| Planning | projected receipts, capacity, inventory availability |
| Transportation | load, package, weight, cube, dock appointment, departure |
| Automation | tasks, confirmations, device status, faults |
| Partners | advance shipment information, receipt and shipment events |

## AsterWorks example

The European postponement center handles common modules, finished cartridges, and customer returns. The location model must distinguish unrestricted, quality-hold, configuration, and return-evaluation stock. If the physical status is detailed but the core platform receives only an aggregate quantity, order promising may offer stock that is not usable.

## Performance measures

Use a balanced set:

- dock-to-stock time;
- inventory record accuracy;
- lines picked per labor hour;
- pick and pack accuracy;
- order release-to-ready time;
- on-time carrier handoff;
- space utilization; and
- safety or damage incidents.

Productivity without accuracy increases downstream rework. Accuracy without flow can still miss customer service.

## Why it matters

Warehouse execution affects inventory accuracy, order priority, labor, traceability, capacity, and the reliability of every downstream promise.

## Decision logic

Design receiving, putaway, inventory status, replenishment, picking, packing, staging, and exception rules around measurable service and control requirements. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain warehouse process map, location and item rules, status ownership, task priorities, capacity, scan evidence, exceptions, and performance. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **warehouse management systems decision record** with these fields:

- **Decision and boundary:** Design receiving, putaway, inventory status, replenishment, picking, packing, staging, and exception rules around measurable service and control requirements.
- **Required evidence:** warehouse process map, location and item rules, status ownership, task priorities, capacity, scan evidence, exceptions, and performance.
- **Expected result:** Warehouse execution affects inventory accuracy, order priority, labor, traceability, capacity, and the reliability of every downstream promise.
- **Balancing condition:** Detailed system-directed work improves consistency and traceability but requires accurate master data, devices, discipline, and recovery procedures.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Detailed system-directed work improves consistency and traceability but requires accurate master data, devices, discipline, and recovery procedures.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Design receiving, putaway, inventory status, replenishment, picking, packing, staging, and exception rules around measurable service and control requirements. Validate the result with warehouse process map, location and item rules, status ownership, task priorities, capacity, scan evidence, exceptions, and performance; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Automating a poor location and replenishment design.
- Using one unit of measure inconsistently across systems.
- Ignoring stock status during integration.
- Measuring picks per hour while encouraging order fragmentation.
- Treating interface reconciliation as an accounting-only task.

## Original knowledge check

The warehouse shows 100 units on hand, but 30 are on quality hold. What quantity should ordinary order promising consider before other reservations?

<details>
<summary>Answer and rationale</summary>

### Correct answer

At most 70 units. Stock status must be part of availability, not only the physical count.

### Why it is correct

Warehouse execution affects inventory accuracy, order priority, labor, traceability, capacity, and the reliability of every downstream promise. Design receiving, putaway, inventory status, replenishment, picking, packing, staging, and exception rules around measurable service and control requirements.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Automating a poor location and replenishment design.
- Using one unit of measure inconsistently across systems.
- Ignoring stock status during integration.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: Detailed system-directed work improves consistency and traceability but requires accurate master data, devices, discipline, and recovery procedures.

</details>

## Practitioner perspective

Use warehouse process map, location and item rules, status ownership, task priorities, capacity, scan evidence, exceptions, and performance as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts


- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/01-purchasing-flow-and-selection-routes.md)
Continue to [transportation management systems](06-transportation-management-systems.md).

---

[Previous: Event Management and Control Towers](04-event-management-and-control-towers.md) · [Next: Transportation Management Systems](06-transportation-management-systems.md)
