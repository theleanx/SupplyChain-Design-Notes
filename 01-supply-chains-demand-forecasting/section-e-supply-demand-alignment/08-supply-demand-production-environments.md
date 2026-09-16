# 8. Supply-Demand Production Environments: MTS, MTO, ETO, ATO, and PTO

## Learning objectives

You should be able to:

- distinguish the main production environments by the point at which the customer order enters;
- explain the inventory and lead-time trade-off of each environment;
- identify the likely master-scheduling focus.

![Supply-demand production environments](../../assets/diagrams/module-1/section-e/supply-demand-strategies.svg)

## The central question

> **How much work is completed before the customer order arrives?**

That customer-order decoupling point drives inventory, customization, delivery speed, and planning logic.

## Comparison

| Environment | Before customer order | After customer order | Typical characteristics | Planning focus |
|---|---|---|---|---|
| Make-to-stock (MTS) | Finished goods | Pick / ship | Higher volume, lower variety, fast response | Finished goods |
| Assemble-to-order (ATO) | Common modules/components | Final assembly/configuration | Many end-item combinations from limited modules | Modules/components |
| Make-to-order (MTO) | Possibly raw materials/common parts | Manufacture product | Lower volume, higher variety | Raw materials / capacity |
| Engineer-to-order (ETO) | Little product-specific design | Engineer + procure + manufacture | Unique design / high customization | Project, engineering, long-lead items |
| Package-to-order (PTO) | Common physical product | Customer-specific packaging | Same item, delayed pack/label | Common item + packaging requirements |

## MTS example

NorthStar stocks a standard replacement pump that has stable service demand. Finished units are produced before specific customer orders arrive.

**Risk:** excess inventory and obsolescence if demand changes.

## ATO example

ATO needs enough final-assembly capability near the customer-order point. If assembly is pushed into a distribution center or fulfillment location, the organization may need additional skills, training, equipment, quality controls, and space.

NorthStar holds standard pump modules—motor sizes, seal kits, controllers, and housings—and performs final assembly after the customer selects the configuration.

This supports many end-item combinations without stocking every finished variant.

## MTO example

A specialty process pump is manufactured only after the customer order is accepted. The customer tolerates a longer lead time in exchange for customization.

## ETO example

A refinery requests a pump skid with unique process calculations, piping design, instrumentation, and purchased components. Engineering work is part of the order itself.

## PTO example

A common spare-parts kit is manufactured in advance but packed after the customer order to support different languages, quantities, regulatory labels, or branded cartons.

## Why it matters

The customer-order decoupling point determines what may be forecast, stocked, configured, engineered, and promised before actual demand arrives.

## Decision logic

Choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain decoupling point, forecast level, inventory position, configuration or engineering lead time, capacity reservation, and promise rule. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **supply-demand production environments: MTS, MTO, ETO, ATO, and PTO decision record** with these fields:

- **Decision and boundary:** Choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content.
- **Required evidence:** decoupling point, forecast level, inventory position, configuration or engineering lead time, capacity reservation, and promise rule.
- **Expected result:** The customer-order decoupling point determines what may be forecast, stocked, configured, engineered, and promised before actual demand arrives.
- **Balancing condition:** Earlier commitment shortens response but increases forecast and inventory exposure; later commitment reduces exposure but lengthens customer lead time.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Earlier commitment shortens response but increases forecast and inventory exposure; later commitment reduces exposure but lengthens customer lead time.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content. Validate the result with decoupling point, forecast level, inventory position, configuration or engineering lead time, capacity reservation, and promise rule; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- ATO master scheduling normally focuses on common modules/components rather than every possible finished combination.
- ETO involves unique engineering, not merely selecting standard options.
- PTO delays packaging, not necessarily manufacturing of the common physical item.
- MTS provides fast customer response but shifts risk toward finished-goods inventory.

## Original knowledge check

**Question.** NorthStar is deciding how to apply supply-demand production environments: MTS, MTO, ETO, ATO, and PTO. Which proposal is most defensible?

A. Use supply-demand production environments: MTS, MTO, ETO, ATO, and PTO as a label for the preferred option before defining the decision outcome, constraints, or owner.
B. Choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content.
C. Choose the apparent upside without evaluating this balancing condition: Earlier commitment shortens response but increases forecast and inventory exposure; later commitment reduces exposure but lengthens customer lead time.
D. Approve the choice without retaining decoupling point, forecast level, inventory position, configuration or engineering lead time, capacity reservation, and promise rule; omit the reassessment trigger as well.

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content.**

### Why it is correct

The customer-order decoupling point determines what may be forecast, stocked, configured, engineered, and promised before actual demand arrives. The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content.
- **C** optimizes one visible result and omits the balancing effects: earlier commitment shortens response but increases forecast and inventory exposure; later commitment reduces exposure but lengthens customer lead time.
- **D** leaves the approval unauditable. A reviewer would be missing decoupling point, forecast level, inventory position, configuration or engineering lead time, capacity reservation, and promise rule, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: earlier commitment shortens response but increases forecast and inventory exposure; later commitment reduces exposure but lengthens customer lead time.

</details>

## Practitioner perspective

The correct production environment is not just a manufacturing choice. It influences forecast granularity, inventory location, product design, order promising, BOM structure, capacity planning, and customer lead time.

## Related concepts


- [Section overview](./README.md)
- [Module 2 continuation](../../02-network-design-digital-connectivity-performance/section-a-network-design-and-technology-investment/03-network-configuration-and-flow-design.md)
Module 1 → Section E → Supply-Demand Strategies. Definitions are independently summarized; examples and matrix are original.

---

[Previous: Level, Chase, and Hybrid Operations Strategies](07-level-chase-hybrid-strategies.md) · [Next: Financial Reconciliation and Executive S&OP](09-reconciliation-and-executive-sop.md)
