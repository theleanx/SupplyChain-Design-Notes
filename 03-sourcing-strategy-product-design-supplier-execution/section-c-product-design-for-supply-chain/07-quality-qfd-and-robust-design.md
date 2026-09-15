# 7. Quality, Customer Translation, and Robust Design

## Learning objectives

After this topic, you should be able to:

- distinguish design quality from conformance;
- translate customer needs into technical measures;
- manage conflicting characteristics;

## Concept in plain English

Design quality chooses the characteristics customers need; conformance quality delivers the approved design consistently. Structured customer translation links customer language to measurable engineering and operating requirements.

## Why it matters

A defect-free product can still disappoint if the design solves the wrong problem. Conversely, a valuable design fails when production cannot reproduce it.

## Decision model and workflow

![Quality, Customer Translation, and Robust Design decision workflow](../../assets/diagrams/module-3/section-c/07-quality-qfd-and-robust-design-workflow.svg)

### Evidence retained through the workflow

| Stage | Required evidence or output |
|---|---|
| **1. Capture segmented customer needs** | Segmented customer evidence with context, frequency, importance, and unmet need |
| **2. Prioritize needs and competitive gaps** | Prioritized needs and competitor gaps separated from proposed solutions |
| **3. Translate into measurable characteristics** | Traceable technical characteristics with units, targets, direction, and test methods |
| **4. Analyze interactions and conflicts** | Interaction analysis showing positive support, conflict, technical difficulty, and risk |
| **5. Set targets and verify capability** | Capability evidence proving the design remains acceptable across expected variation |

## Practical process flow

```mermaid
flowchart TD
    A["Capture customer needs in measurable language"] --> B["Prioritize needs and failure consequences"]
    B --> C["Translate needs into technical responses"]
    C --> D["Resolve response conflicts and set targets"]
    D --> E["Test variation and noise conditions"]
    E --> F{"Capability and robustness demonstrated?"}
    F -->|No| C
    F -->|Yes| G["Release control plan"]
```

## Realistic example — Rivermark Climate Systems

Customers say the rooftop unit must be 'quiet and easy to service.' Rivermark translates this into sound-power limits, panel-removal time, tool count, filter-access clearance, and diagnostic-code accuracy.

**Decision insight.** The vague words “quiet” and “easy” become measurable targets that engineering, suppliers, production, and service teams can verify consistently.

All names and values in this example are fictional and independently selected for learning purposes.

## Applied decision artifact — requirement-to-control trace

Create a trace from each high-priority customer need to a measurable technical response, design target, validation method, process control, and accountable owner. For “quiet operation,” for example, define the sound metric, operating condition, limit, measurement method, and relevant variation sources rather than repeating the customer phrase.

Use QFD to expose weak or conflicting technical coverage, then test robustness against realistic noise: material lots, operators, voltage, temperature, transport, wear, and supplier processes. A passing nominal prototype is not enough. Release the requirement only when the measurement system, capability evidence, reaction plan, and post-launch signal are defined.

## Decision logic

- Keep the customer need visible beside each technical target.
- Separate target importance from technical difficulty.
- Verify that production and suppliers can hold critical characteristics.

## Trade-offs

| Choice tension | Decision implication |
|---|---|
| Higher targets can increase cost or reduce another characteristic | Resolve target conflicts through explicit customer priorities and sensitivity testing rather than maximizing every characteristic. |
| Extensive matrices improve traceability but require disciplined maintenance | Maintain the translation matrix as a living decision record tied to requirements, tests, changes, and capability evidence. |

## Commonly confused with

Voice of the customer is evidence about needs. The translation method converts that evidence into design and process requirements.

## Common mistakes

- Treating the loudest customer as the whole market.
- Writing subjective needs without measurable tests.
- Ignoring negative interactions among targets.

## Original knowledge check

**Question.** Which statement is a technical requirement rather than a customer need?

A. Easy to service

B. Quiet during operation

C. Filter replacement in under eight minutes using one standard tool

D. Reliable

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. Filter replacement in under eight minutes using one standard tool**

### Why it is correct

It is measurable and testable while preserving the intent of service ease.

### Why the other answers are wrong

A, B, and D express needs but require translation.

</details>

## Practitioner perspective

Trace every critical specification back to a customer, regulatory, safety, or lifecycle need; delete orphan requirements.

## Related concepts

- [Module 3 overview](../README.md)
- [Section overview](./README.md)
- [Collaborative Design and Early Involvement](./02-collaborative-design-and-early-involvement.md)
- [Supplier Criteria and Weighted Evaluation](../section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)

---

[Previous: Simplification, DFMA, and Serviceability](./06-simplification-dfma-and-serviceability.md) · [Next: Postponement, Mass Customization, and Localization](./08-postponement-mass-customization-and-localization.md)
