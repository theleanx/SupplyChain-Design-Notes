# 10. Receiving and Three-Way Match

## Learning objectives

After this topic, you should be able to:

- trace receipt and invoice control;
- manage quantity, price, and acceptance differences;
- design risk-based inspection;

## Concept in plain English

Three-way match compares the authorized order, evidence of receipt or service acceptance, and supplier invoice before payment. Receiving verifies identity, quantity, condition, and required quality evidence.

## Why it matters

The control prevents unauthorized, duplicate, incorrect, or premature payment while creating reliable inventory and financial records.

## Decision model and workflow

![Receiving and Three-Way Match decision workflow](../../assets/diagrams/module-3/section-d/10-receiving-and-three-way-match-workflow.svg)

### Evidence retained through the workflow

| Stage | Required evidence or output |
|---|---|
| **1. Record physical receipt or service acceptance** | Timestamped receipt or service acceptance linked to order, shipment, lot, serial, and location |
| **2. Inspect according to risk and supplier status** | Risk-based inspection status, sample, result, nonconformance, disposition, and release authority |
| **3. Compare order, receipt, and invoice** | Comparison of order, accepted receipt, and invoice for item, quantity, price, tax, freight, and terms |
| **4. Resolve tolerances and discrepancies** | Owned discrepancy workflow with tolerances, evidence, debit or credit, and escalation |
| **5. Approve payment and close records** | Payment approval and auditable closure of receipt, quality, invoice, and commitment records |

## Practical process flow

```mermaid
flowchart TD
    A["Approve purchase order"] --> B["Record physical or service receipt"]
    B --> C["Capture supplier invoice"]
    C --> D{"PO, receipt, invoice agree within tolerance?"}
    D -->|Yes| E["Release approved amount for payment"]
    D -->|No| F["Hold exception and assign cause"]
    F --> G["Correct receipt, price, quantity, or invoice"]
    G --> D
```

## Realistic example — Rivermark Climate Systems

Rivermark receives 996 boards against an order for 1,000. Four were damaged in transit. The receipt records 996 accepted, the discrepancy is assigned, and the invoice is blocked until quantity and freight responsibility are resolved.

**Decision insight.** Recording only the 996 accepted boards keeps inventory, supplier performance, liability, and payment aligned while the four damaged units are resolved.

All names and values in this example are fictional and independently selected for learning purposes.

## Worked decision — three-way-match exception

In the [three-way-match dataset](../../assets/data/module-3/section-d/three-way-match.csv), PO 4500810 authorizes 100 units at $50, only 98 are received, and 100 are invoiced. The authorized received value is:

`98 × $50 = $4,900`

The remaining `$5,000 − $4,900 = $100` is a quantity exception and should be held unless approved tolerance or contract terms support another treatment. PO 4500812 has a price exception: `$129 − $125 = $4` per unit, or `$160` across 40 units.

Route each mismatch to the party that can correct the evidence. Do not alter receipt or PO data merely to make the invoice pass; preserve the audit trail and root cause.

## Decision logic

- Define tolerances by category and risk.
- Separate receipt from technical acceptance when testing takes time.
- Use certified-supplier status only with monitoring and revocation rules.

## Trade-offs

| Choice tension | Decision implication |
|---|---|
| Full inspection reduces escape risk but adds delay and cost | Shift inspection intensity using supplier performance, process capability, item criticality, and change status—not convenience alone. |
| Automatic match improves efficiency but depends on clean master and transaction data | Automate clean matches but route exceptions by cause and value so efficiency does not approve unsupported payment. |

## Commonly confused with

A packing slip is supplier shipment information. A receiving record is the buyer's evidence of what was actually accepted.

## Common mistakes

- Paying from the invoice alone.
- Correcting discrepancies outside the system.
- Reducing inspection without performance evidence.

## Original knowledge check

**Question.** Which documents form the classic three-way match?

A. Forecast, contract, and scorecard

B. Purchase order, receiving record, and invoice

C. Bid, email, and bank statement

D. Bill of material, routing, and forecast

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Purchase order, receiving record, and invoice**

### Why it is correct

The match links authorization, receipt, and requested payment.

### Why the other answers are wrong

A, C, and D do not establish all three control points.

</details>

## Practitioner perspective

Design exception queues, not only happy paths. The value of matching is in disciplined resolution of differences.

## Related concepts

- [Module 3 overview](../README.md)
- [Section overview](./README.md)
- [Three-way-match dataset](../../assets/data/module-3/section-d/three-way-match.csv)
- [Purchase Orders and Blanket Arrangements](./09-purchase-orders-and-blanket-orders.md)

---

[Previous: Purchase Orders and Blanket Arrangements](./09-purchase-orders-and-blanket-orders.md) · [Next: Order Tracking, Exceptions, and Expediting](./11-order-tracking-exceptions-and-expediting.md)
