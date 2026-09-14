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

## Common mistakes

- Treating the website as separate from supply-chain design.
- Showing stock rather than a reliable promise.
- Capturing duplicate customer and product records by channel.
- Measuring conversion without delivered margin and return cost.
- Designing outbound fulfillment before the returns process.

## Original knowledge check

Why might “12 units in stock” be insufficient for a customer-facing promise?

<details><summary>Answer</summary>

The units may be reserved, blocked, at the wrong location, or unable to reach the customer within the requested time.
</details>

## Related concepts

Continue to [partner visibility and data sharing](11-partner-visibility-and-data-sharing.md).
