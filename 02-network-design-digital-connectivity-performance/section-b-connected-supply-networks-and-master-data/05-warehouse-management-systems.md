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

## Common mistakes

- Automating a poor location and replenishment design.
- Using one unit of measure inconsistently across systems.
- Ignoring stock status during integration.
- Measuring picks per hour while encouraging order fragmentation.
- Treating interface reconciliation as an accounting-only task.

## Original knowledge check

The warehouse shows 100 units on hand, but 30 are on quality hold. What quantity should ordinary order promising consider before other reservations?

<details><summary>Answer</summary>

At most 70 units. Stock status must be part of availability, not only the physical count.
</details>

## Related concepts

Continue to [transportation management systems](06-transportation-management-systems.md).
