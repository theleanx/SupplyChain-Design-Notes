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

## Common mistakes

- Encoding descriptive data without a governed unique identifier.
- Assuming every RFID read means a confirmed business movement.
- Capturing time without time zone.
- Failing to link item, case, pallet, and shipment hierarchy.
- Measuring scan volume instead of event accuracy and process outcome.

## Original knowledge check

A reader detects the same passive tag eight times as a pallet passes a doorway. How many business departure events should normally be created?

<details><summary>Answer</summary>

One validated departure event. Device reads must be filtered and interpreted in process context.
</details>

## Related concepts

Continue to [data quality, cleansing, and stewardship](17-data-quality-cleansing-and-stewardship.md).
