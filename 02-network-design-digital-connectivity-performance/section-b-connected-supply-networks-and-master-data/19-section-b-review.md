# 19. Section B Review and Original Practice

These questions test application boundaries, integration, visibility, master data, controls, and decision intelligence.

## Original knowledge checks

### 1. Digital thread

What makes a digital thread more than a collection of interfaces?

<details><summary>Answer</summary>

Connected identifiers, definitions, decisions, transactions, events, ownership, and traceable outcomes across the lifecycle.
</details>

### 2. Application authority

Can two applications display the same inventory while only one remains authoritative?

<details><summary>Answer</summary>

Yes. Copies are acceptable when update authority, synchronization, and reconciliation are explicit.
</details>

### 3. Capability placement

When does a specialized application create the strongest case?

<details><summary>Answer</summary>

When it provides material decision or execution value that the core cannot meet adequately and its data, integration, cost, security, and exit risks are controlled.
</details>

### 4. Configuration

Why is supported configuration generally easier to sustain than deep customization?

<details><summary>Answer</summary>

It usually preserves standard interfaces and upgrade paths and creates a smaller regression and support burden.
</details>

### 5. Planning feasibility

A model assumes seven-day production, but the plant works five days. What type of defect is this?

<details><summary>Answer</summary>

A calendar and capacity-model defect that can produce infeasible promises or plans.
</details>

### 6. Optimization

Does “optimal” mean best for every stakeholder and objective?

<details><summary>Answer</summary>

No. It means best within the model's objective, constraints, data, and assumptions.
</details>

### 7. Event management

What converts an alert into a managed case?

<details><summary>Answer</summary>

Business impact, ownership, evidence, decision options, action, escalation, and closure outcome.
</details>

### 8. Control-tower value

Which is more meaningful: number of alerts displayed or percentage of exceptions resolved before customer impact?

<details><summary>Answer</summary>

Percentage resolved before impact, because it measures decision and outcome value.
</details>

### 9. Warehouse status

Why must quality-hold stock be distinguished from unrestricted stock?

<details><summary>Answer</summary>

Physical existence does not make inventory available for ordinary fulfillment.
</details>

### 10. Transportation utilization

A vehicle carries 12,000 kg against 15,000 kg usable capacity. What is weight utilization?

<details><summary>Answer</summary>

`12,000 / 15,000 = 80%`.
</details>

### 11. Delivered economics

Why can the lowest freight rate create higher network cost?

<details><summary>Answer</summary>

It may add transit inventory, handling, damage, variability, service failures, or later expedites.
</details>

### 12. Data meaning

Why should requested, promised, and planned delivery dates be separate?

<details><summary>Answer</summary>

They answer different questions and are required to diagnose customer commitment and execution performance.
</details>

### 13. Cloud responsibility

Does a hosted service transfer accountability for business continuity to the provider?

<details><summary>Answer</summary>

No. Responsibilities are shared, and the customer retains accountability for its process, data, reconciliation, and customer obligations.
</details>

### 14. Safe retry

What property prevents a retried booking request from creating duplicate pickups?

<details><summary>Answer</summary>

Idempotency using a stable business request identifier.
</details>

### 15. Commerce promise

Why is global inventory balance insufficient for a customer promise?

<details><summary>Answer</summary>

Status, reservation, location, capacity, calendar, and transport feasibility determine usable availability.
</details>

### 16. Data sharing

What should come before selecting fields to share with a partner?

<details><summary>Answer</summary>

The shared business decision and permitted purpose.
</details>

### 17. Consignment

Which event often triggers financial ownership or payment in a consigned arrangement?

<details><summary>Answer</summary>

Contractually defined consumption or withdrawal, not merely physical delivery.
</details>

### 18. Privacy

What does data minimization require?

<details><summary>Answer</summary>

Collect and share only data necessary and proportionate for the defined lawful purpose.
</details>

### 19. Cyber recovery

What must follow technical service restoration?

<details><summary>Answer</summary>

Reconciliation of missing, duplicated, delayed, altered, or out-of-sequence business transactions and events.
</details>

### 20. Master-data lifecycle

Why use effective dates for a future calendar or rate change?

<details><summary>Answer</summary>

To preserve current execution, future planning, and historical meaning without overwriting all periods.
</details>

### 21. Identification

Does every RFID read represent a business movement?

<details><summary>Answer</summary>

No. Device reads must be filtered and interpreted using location, direction, timing, and process context.
</details>

### 22. Data quality

Why can 99% overall completeness still be unacceptable?

<details><summary>Answer</summary>

The missing 1% may contain fields critical to safety, compliance, planning, or delivery.
</details>

### 23. Model validation

What is data leakage?

<details><summary>Answer</summary>

Using information in training or evaluation that would not be available at the actual decision time, causing overstated performance.
</details>

### 24. Automation

Name three conditions required before automating a supply-chain decision.

<details><summary>Answer</summary>

Examples include explicit objective, trusted inputs, encoded guardrails, detectable failure, override, escalation, reversibility, and outcome monitoring.
</details>

## Section B completion check

Sketch AsterWorks’ target application landscape and trace one delayed shipment from physical event through case, decision, execution, and outcome learning.

Continue to [Section C — Performance Measurement and Financial Insight](../section-c-performance-and-financial-insight/).
