# 8. Capability Maturity and Transformation Roadmap

## Learning objectives

After this topic, you should be able to:

- assess capability maturity without using it as a vanity score;
- sequence foundation, integration, decision, and optimization capabilities;
- distinguish technology installation from operational adoption; and
- build a roadmap around dependencies and value releases.

## Concept in plain English

Capability maturity describes how reliably an organization can perform and improve a business capability. It includes process, people, data, technology, governance, and partner behavior—not software age alone.

## Five practical stages

| Stage | Operating characteristics | Next priority |
|---|---|---|
| 1. Fragmented | local records, manual handoffs, unclear ownership | define process and authoritative data |
| 2. Repeatable | common procedures in selected areas | standardize measures and controls |
| 3. Connected | integrated transactions and shared identifiers | manage end-to-end exceptions |
| 4. Coordinated | cross-functional planning and partner workflows | improve scenario decisions |
| 5. Adaptive | rapid learning and controlled automation | continuously test value and risk |

Maturity is capability-specific. A company may have adaptive transportation visibility and fragmented supplier capacity data.

## Dependency logic

```mermaid
flowchart TD
    A[Process and ownership] --> B[Trusted master data]
    B --> C[Connected transactions and events]
    C --> D[Managed exceptions]
    D --> E[Scenario decisions]
    E --> F[Controlled automation]
```

Skipping layers creates fragile progress. Predictive models cannot compensate for undefined timestamps, inconsistent identifiers, or unowned exceptions.

## Maturity assessment questions

Evaluate each capability across six dimensions:

1. Is the process defined end to end?
2. Are decision rights and exception owners clear?
3. Are critical data defined, timely, and governed?
4. Do applications and interfaces support the process reliably?
5. Are partners included where the process crosses boundaries?
6. Are outcomes measured and used for improvement?

Use evidence—cycle times, defect rates, adoption, interface reliability, and decision records—rather than opinion alone.

## AsterWorks roadmap

AsterWorks initially wants predictive shipment-risk alerts. Its assessment finds that carriers use inconsistent shipment identifiers and departure events are missing on 18% of priority loads.

A sensible sequence is:

- define canonical shipment and order identifiers;
- improve milestone completeness;
- assign exception ownership;
- implement deterministic late-event rules;
- establish response history; and
- train a predictive model only when the label and action data are credible.

## Roadmap design

Organize the roadmap into value releases, not technology components:

| Release | Business outcome | Required foundation |
|---|---|---|
| Reliable promise | consistent available date and allocation | item, location, capacity, and lead-time data |
| Managed delivery | early exception detection and ownership | shipment events and customer impact link |
| Scenario response | comparable recovery options | cost, capacity, and policy data |
| Controlled automation | low-risk actions executed within guardrails | proven rules, monitoring, and override |

## Why it matters

A roadmap fails when later capabilities depend on data, process, skills, or governance that earlier releases did not establish.

## Decision logic

Assess current capability with evidence, define the target decision behavior, map dependencies, and gate each release on measurable readiness and benefit. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain current and target maturity, dependency map, release outcomes, entry and exit criteria, owners, adoption, benefit, and stop decision. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **capability maturity and transformation roadmap decision record** with these fields:

- **Decision and boundary:** Assess current capability with evidence, define the target decision behavior, map dependencies, and gate each release on measurable readiness and benefit.
- **Required evidence:** current and target maturity, dependency map, release outcomes, entry and exit criteria, owners, adoption, benefit, and stop decision.
- **Expected result:** A roadmap fails when later capabilities depend on data, process, skills, or governance that earlier releases did not establish.
- **Balancing condition:** Rapid scope can demonstrate ambition but creates fragile dependencies; staged delivery reduces risk but delays some benefits.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Rapid scope can demonstrate ambition but creates fragile dependencies; staged delivery reduces risk but delays some benefits.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Assess current capability with evidence, define the target decision behavior, map dependencies, and gate each release on measurable readiness and benefit. Validate the result with current and target maturity, dependency map, release outcomes, entry and exit criteria, owners, adoption, benefit, and stop decision; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Assigning one maturity score to the entire enterprise.
- Assuming technology deployment proves adoption.
- Automating an unstable process.
- Building a roadmap by vendor product rather than business outcome.
- Advancing analytics while foundational data remain unreliable.

## Original knowledge check

A company has a sophisticated optimization engine, but planners export results to spreadsheets because capacity and lead-time data are unreliable. Which capability should be addressed first?

<details>
<summary>Answer and rationale</summary>

### Correct answer

**Trusted planning data and ownership.** More advanced optimization will not create reliable decisions until the foundational inputs are controlled.

### Why it is correct

A roadmap fails when later capabilities depend on data, process, skills, or governance that earlier releases did not establish. Assess current capability with evidence, define the target decision behavior, map dependencies, and gate each release on measurable readiness and benefit.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Assigning one maturity score to the entire enterprise.
- Assuming technology deployment proves adoption.
- Automating an unstable process.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: Rapid scope can demonstrate ambition but creates fragile dependencies; staged delivery reduces risk but delays some benefits.

</details>

## Practitioner perspective

The purpose of maturity assessment is sequencing. A lower score is not a failure if it reveals the dependency that prevents value. The dangerous result is a high score unsupported by operating evidence.

## Related concepts


- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-a-sourcing-alignment-and-total-cost/01-strategic-sourcing-from-demand.md)
Continue to [governance, change, and network orchestration](09-governance-change-and-network-orchestration.md).

---

[Previous: Technology Business Case and Total Cost](07-technology-business-case-and-tco.md) · [Next: Governance, Change, and Network Orchestration](09-governance-change-and-network-orchestration.md)
