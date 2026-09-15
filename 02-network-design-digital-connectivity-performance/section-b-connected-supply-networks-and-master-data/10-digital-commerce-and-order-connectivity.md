# 10. Digital Commerce and Order Connectivity

## Learning objectives

After this topic, you should be able to:

- distinguish customer experience from order execution;
- trace digital order flow from discovery through settlement;
- identify content, promise, payment, fulfillment, and return dependencies; and
- evaluate channel economics beyond sales volume.

## Concept in plain English

Digital commerce connects product discovery, configuration, price, availability, order capture, payment, fulfillment, service, and return. A polished front end creates value only when the downstream network can keep the promise it presents.

```mermaid
flowchart LR
    A[Discover and configure] --> B[Price and promise]
    B --> C[Order and payment]
    C --> D[Allocate and fulfill]
    D --> E[Deliver and notify]
    E --> F[Return or service]
```

## Key design elements

| Element | Required control |
|---|---|
| Product content | approved descriptions, attributes, compatibility, and media |
| Price | customer, currency, tax, validity, and approval rules |
| Availability | time-phased supply, reservation, and allocation policy |
| Promise | cutoffs, calendars, lead times, capacity, and delivery service |
| Order | identity, duplicate prevention, change, cancellation, and status |
| Payment and credit | authorization, fraud, exposure, and settlement |
| Fulfillment | node selection, split rules, packaging, transport, and documentation |
| Returns | eligibility, label, disposition, refund, and recovery value |

## AsterWorks example

A customer portal shows every cartridge as “available” because it reads total global inventory. Some stock is reserved, under inspection, or too distant to meet the delivery promise. The corrected design requests a segment-specific promise using usable inventory, capacity, calendars, and transportation service.

## Channel economics

Evaluate:

- acquisition and platform fees;
- fulfillment and last-mile cost;
- packaging and returns;
- payment and fraud loss;
- customer-service contacts;
- inventory duplication;
- incremental margin; and
- effect on existing channels and partners.

High digital sales can destroy value if returns, expedites, and fragmented fulfillment are ignored.

## Why it matters

A digital channel can increase demand while creating invalid promises, fragmented orders, returns, fraud, and service inconsistency.

## Decision logic

Connect offer, price, availability, promise, order, fulfillment, payment, status, cancellation, and return through shared identifiers and controls. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain channel promise, product and customer data, price and availability source, order status events, payment control, returns, and service owner. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **digital commerce and order connectivity decision record** with these fields:

- **Decision and boundary:** Connect offer, price, availability, promise, order, fulfillment, payment, status, cancellation, and return through shared identifiers and controls.
- **Required evidence:** channel promise, product and customer data, price and availability source, order status events, payment control, returns, and service owner.
- **Expected result:** A digital channel can increase demand while creating invalid promises, fragmented orders, returns, fraud, and service inconsistency.
- **Balancing condition:** Faster self-service improves reach and convenience but increases real-time data, availability, cybersecurity, and exception demands.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Faster self-service improves reach and convenience but increases real-time data, availability, cybersecurity, and exception demands.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Connect offer, price, availability, promise, order, fulfillment, payment, status, cancellation, and return through shared identifiers and controls. Validate the result with channel promise, product and customer data, price and availability source, order status events, payment control, returns, and service owner; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Treating the website as separate from supply-chain design.
- Showing stock rather than a reliable promise.
- Capturing duplicate customer and product records by channel.
- Measuring conversion without delivered margin and return cost.
- Designing outbound fulfillment before the returns process.

## Original knowledge check

Why might “12 units in stock” be insufficient for a customer-facing promise?

<details>
<summary>Answer and rationale</summary>

### Correct answer

The units may be reserved, blocked, at the wrong location, or unable to reach the customer within the requested time.

### Why it is correct

A digital channel can increase demand while creating invalid promises, fragmented orders, returns, fraud, and service inconsistency. Connect offer, price, availability, promise, order, fulfillment, payment, status, cancellation, and return through shared identifiers and controls.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Treating the website as separate from supply-chain design.
- Showing stock rather than a reliable promise.
- Capturing duplicate customer and product records by channel.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: Faster self-service improves reach and convenience but increases real-time data, availability, cybersecurity, and exception demands.

</details>

## Practitioner perspective

Use channel promise, product and customer data, price and availability source, order status events, payment control, returns, and service owner as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts


- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/01-purchasing-flow-and-selection-routes.md)
Continue to [partner visibility and data sharing](11-partner-visibility-and-data-sharing.md).

---

[Previous: Integration Patterns, APIs, Middleware, and Events](09-integration-patterns-apis-middleware-events.md) · [Next: Partner Visibility and Data Sharing](11-partner-visibility-and-data-sharing.md)
