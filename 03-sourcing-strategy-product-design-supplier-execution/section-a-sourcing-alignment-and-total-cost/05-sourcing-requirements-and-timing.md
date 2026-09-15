# 5. Sourcing Requirements and Timing

## Learning objectives

After this topic, you should be able to:

- build measurable sourcing requirements;
- connect time horizons to supplier readiness;
- prioritize requirements by category;

## Concept in plain English

A sourcing requirement states what the supply solution must achieve and by when. It covers volume, mix, quality, capacity, lead time, flexibility, design support, compliance, sustainability, data, and continuity.

## Why it matters

Vague requirements create incomparable proposals and late disputes. Timing must include qualification, tooling, integration, ramp-up, logistics, and approval—not just the supplier's quoted production lead time.

## Decision model and workflow

![Sourcing Requirements and Timing decision workflow](../../assets/diagrams/module-3/section-a/05-sourcing-requirements-and-timing-workflow.svg)

### Evidence retained through the workflow

| Stage | Required evidence or output |
|---|---|
| **1. Segment demand and service needs** | Demand and service segments with baseline, upside, downside, and emergency scenarios |
| **2. Define measurable requirements** | Requirements written with unit, measurement method, tolerance, and evidence source |
| **3. Separate mandatory from weighted criteria** | Pass/fail gates separated from scored preferences and negotiation variables |
| **4. Build the readiness timeline** | Backward plan for design freeze, qualification, tooling, ramp, and first usable supply |
| **5. Approve assumptions and tolerances** | Cross-functional approval of assumptions, ownership, exceptions, and change control |

## Practical process flow

```mermaid
flowchart TD
    A["Confirm business need"] --> B["Translate need into measurable specification"]
    B --> C["Separate mandatory gates from preferences"]
    C --> D["Validate demand and award timing"]
    D --> E["Choose event and evaluation plan"]
    E --> F{"Cross-functional approval?"}
    F -->|No| B
    F -->|Yes| G["Release sourcing brief"]
```

## Realistic example — Rivermark Climate Systems

For a refrigerant sensor, Rivermark specifies annual volume of 48,000 units, a peak month of 5,600, 12-week initial qualification, 98% delivery reliability, traceable calibration records, and a four-week surge response for a 20% increase.

**Decision insight.** The requirement set is bid-ready because suppliers can tell exactly how delivery reliability, surge response, and calibration evidence will be measured.

All names and values in this example are fictional and independently selected for learning purposes.

## Applied decision artifact — requirement quality test

Challenge every requirement with four questions: Is it measurable? Is its business reason documented? Does it discriminate among viable solutions? Can compliance be verified before award? Put non-negotiable legal, safety, cyber, and technical conditions in a gate table; put value-creating preferences in the weighted scorecard.

Back-plan the event from the required operational date through contract approval, supplier qualification, tooling, validation, and transition buffer. If the calendar cannot support those activities, escalate the timing conflict instead of compressing supplier due diligence invisibly. Freeze a numbered requirement baseline for bids and log every later clarification so all suppliers compete against the same scope.

## Decision logic

- Use ranges and scenarios for uncertain demand.
- Give pass/fail status only to genuine constraints.
- Define the measurement method, data source, and acceptable tolerance.

## Trade-offs

| Choice tension | Decision implication |
|---|---|
| Tighter requirements reduce risk but may reduce competition | Make a requirement mandatory only when failure creates an unacceptable safety, regulatory, quality, or service consequence. |
| Earlier commitment protects capacity but increases forecast exposure | Secure flexible capacity in bands or options when forecast uncertainty makes a firm volume commitment unnecessarily expensive. |

## Commonly confused with

A specification defines the item or service. A sourcing requirement includes the broader operating and commercial conditions needed to supply it.

## Common mistakes

- Publishing target volumes without peak or variability.
- Calling every preference mandatory.
- Omitting the time needed for validation and systems integration.

## Original knowledge check

**Question.** Which requirement is most decision-ready?

A. Supplier must be flexible

B. Supplier should provide good quality

C. Supplier must support 5,600 units in the peak month with 98% on-time delivery

D. Supplier should have sufficient capacity

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. Supplier must support 5,600 units in the peak month with 98% on-time delivery**

### Why it is correct

It defines quantity, period, and measured performance.

### Why the other answers are wrong

A, B, and D are directionally useful but cannot be tested consistently.

</details>

## Practitioner perspective

A requirement is complete only when two evaluators would reach the same conclusion using the same evidence.

## Related concepts

- [Module 3 overview](../README.md)
- [Section overview](./README.md)
- [Strategic Sourcing from Demand](./01-strategic-sourcing-from-demand.md)
- [Supplier Criteria and Weighted Evaluation](../section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)

---

[Previous: Transition Risk and Knowledge Retention](./04-transition-risk-and-knowledge-retention.md) · [Next: Landed Cost and Total Cost of Ownership](./06-landed-cost-and-total-cost-of-ownership.md)
