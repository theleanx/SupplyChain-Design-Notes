# 16. Automatic Identification and Traceability

## Learning objectives

After this topic, you should be able to:

- separate identity, data carrier, reader, event, and business context;
- compare common barcode and radio-frequency approaches;
- design traceability events using what, where, when, why, and custody; and
- evaluate read quality and exception handling.

## Concept in plain English

Automatic identification reduces manual capture by linking a physical object to a digital identifier. The identifier is useful only when it is unique at the required level and connected to a trusted business record.

## Identification chain

```mermaid
flowchart LR
    A[Physical object] --> B[Identifier]
    B --> C[Data carrier]
    C --> D[Reader or sensor]
    D --> E[Capture event]
    E --> F[Business transaction and trace history]
```

## Technology comparison

| Method | Strength | Limitation | Suitable examples |
|---|---|---|---|
| Linear barcode | inexpensive and mature | line-of-sight and limited data | item or case scan |
| Two-dimensional barcode | more data in compact area | still requires optical readability | serial, lot, link, service data |
| Passive RFID | fast non-line-of-sight group reads | environment and reader design affect performance | cases, pallets, reusable assets |
| Active device | longer range and sensor capability | higher cost, battery, and lifecycle management | high-value asset or condition monitoring |

[GS1 barcode](https://www.gs1.org/standards/barcodes), [RFID](https://www.gs1.org/standards/rfid), and [traceability](https://www.gs1.org/standards/traceability) resources provide public standards for interoperable identification, capture, and sharing.

## Traceability event

A useful event records:

- **what:** item, lot, serial, logistics unit, or asset;
- **where:** physical and business location;
- **when:** event time with time zone;
- **why:** receiving, packing, shipping, transforming, consuming, returning;
- **custody or ownership:** who possessed or controlled it; and
- **source:** device, application, partner, and confidence.

## AsterWorks example

AsterWorks scans a pallet identifier at departure, but individual serialized controllers are not linked to that pallet. The carrier event proves pallet movement but cannot identify which customer units are affected by a recall. Packing must establish parent-child relationships before shipment.

Use-case design should test label placement, print quality, read zone, metal or liquid interference, duplicate reads, missed reads, damaged labels, offline operation, and manual exception correction.

## Why it matters

Traceability fails when identifiers, events, locations, quantities, and transformations cannot be connected across organizations and systems.

## Decision logic

Choose identification and capture technology for the required granularity, record trusted events, link parent-child transformations, and test recall questions. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain identifier standard, label and reader rule, commissioning, event and location, aggregation, transformation, exception, and trace test. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **automatic identification and traceability decision record** with these fields:

- **Decision and boundary:** Choose identification and capture technology for the required granularity, record trusted events, link parent-child transformations, and test recall questions.
- **Required evidence:** identifier standard, label and reader rule, commissioning, event and location, aggregation, transformation, exception, and trace test.
- **Expected result:** Traceability fails when identifiers, events, locations, quantities, and transformations cannot be connected across organizations and systems.
- **Balancing condition:** Finer serialization improves traceability but raises label, scanning, data-volume, exception, and partner-adoption cost.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Finer serialization improves traceability but raises label, scanning, data-volume, exception, and partner-adoption cost.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Choose identification and capture technology for the required granularity, record trusted events, link parent-child transformations, and test recall questions. Validate the result with identifier standard, label and reader rule, commissioning, event and location, aggregation, transformation, exception, and trace test; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Encoding descriptive data without a governed unique identifier.
- Assuming every RFID read means a confirmed business movement.
- Capturing time without time zone.
- Failing to link item, case, pallet, and shipment hierarchy.
- Measuring scan volume instead of event accuracy and process outcome.

## Original knowledge check

A reader detects the same passive tag eight times as a pallet passes a doorway. How many business departure events should normally be created?

<details>
<summary>Answer and rationale</summary>

### Correct answer

One validated departure event. Device reads must be filtered and interpreted in process context.

### Why it is correct

Traceability fails when identifiers, events, locations, quantities, and transformations cannot be connected across organizations and systems. Choose identification and capture technology for the required granularity, record trusted events, link parent-child transformations, and test recall questions.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Encoding descriptive data without a governed unique identifier.
- Assuming every RFID read means a confirmed business movement.
- Capturing time without time zone.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: Finer serialization improves traceability but raises label, scanning, data-volume, exception, and partner-adoption cost.

</details>

## Practitioner perspective

Use identifier standard, label and reader rule, commissioning, event and location, aggregation, transformation, exception, and trace test as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts


- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/01-purchasing-flow-and-selection-routes.md)
Continue to [data quality, cleansing, and stewardship](17-data-quality-cleansing-and-stewardship.md).

---

[Previous: Master-Data Domains and Lifecycle](15-master-data-domains-and-lifecycle.md) · [Next: Data Quality, Cleansing, and Stewardship](17-data-quality-cleansing-and-stewardship.md)
