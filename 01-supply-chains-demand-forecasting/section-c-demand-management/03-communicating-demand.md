# 3. Communicating Demand

## Learning objectives

You should be able to:

- explain why demand communication reduces supply-chain surprises;
- apply the three communication principles: **soon, structured, focused**;
- describe basic order processing in a demand-management context;
- explain why transactional data alone is not enough;
- connect communication quality to the bullwhip effect.

## Concept in plain English

Even a strong demand plan fails if the people who must act on it learn about changes too late.

Communicating demand means moving relevant demand information to the right internal teams and supply-chain partners in time for them to respond.

At a basic level, this includes processing customer orders and routing the requirements to inventory or production. At a more collaborative level, it includes sharing forecasts, promotions, risks, assumptions, and actual demand signals across organizations.

## The three principles

```mermaid
flowchart LR
    A[Communicate soon<br/>Minimize surprises] --> G[Good demand communication]
    B[Structure communication<br/>Make it repeatable] --> G
    C[Focus communication<br/>Fit the audience] --> G
```

### 1. Communicate soon

Early information is useful even when it is imperfect.

A marketing team that waits for "perfect" promotion-volume estimates can cause more damage than a team that says early:

> "Promotion is confirmed. We currently estimate +15% to +30%. We will update the range next week."

The uncertainty can be planned around. Silence cannot.

This is especially important for bad news. A weak pipeline, canceled order, competitor action, or delayed launch should be shared while the organization still has options.

### 2. Structure communications

Critical communication should not depend on someone remembering to send an email.

Recurring demand planning needs scheduled, repeatable interactions.

```mermaid
flowchart TD
    I[Demand-plan inputs<br/>forecast + assumptions + commercial actions] --> R[Consensus demand review]
    R --> V[Challenge / validate assumptions]
    V --> D[Consensus demand plan]
    D --> S[S&OP reconciliation<br/>with supply + finance]
    S --> M[Master scheduling / supply planning]
    M --> P[Performance monitoring]
    P --> F[Feedback and exceptions]
    F --> I
```

Systems can move transactional data, but people are still needed to explain nuance, challenge assumptions, resolve conflict, and build commitment.

### 3. Focus communications

Different audiences need different forms of the same information.

- Operations may need **units**.
- Finance may need **dollars and margin**.
- Sales may need **customer and product availability**.
- Executives may need **exceptions, risks, and scenario impact**.

Too little information creates guesswork. Too much detail hides the decision.

## Order processing

Demand communication also includes the administrative processing of a customer order so it can be fulfilled.

Depending on the supply model, the order may trigger:

- a shipment from inventory;
- a production requirement;
- an allocation decision;
- a customer confirmation;
- updates to planning systems.

## Collaborative communication

A company can share demand information beyond its own walls. The objective is to reduce latency between a real market change and the supply-chain response.

That can reduce overreaction and help dampen the **bullwhip effect**, because upstream partners are not relying only on delayed replenishment orders as a proxy for final demand.

## Realistic example — promotion uncertainty

A retailer plans a six-week promotion for NorthStar's residential water-pressure product.

Early estimate: **+20% to +45%** volume.

The marketing team should not wait until the estimate narrows to +32%.

A stronger approach is:

1. communicate the promotion date immediately;
2. share the current range and assumptions;
3. identify the most constrained components;
4. agree on a weekly estimate update;
5. monitor actual sell-through once the campaign starts;
6. update supply plans quickly.

## Why it matters

The same demand signal can produce conflicting actions when functions receive different versions, units, timing, or confidence.

## Decision logic

Define the audience, decision, aggregation, timing, uncertainty, and feedback route before selecting the dashboard or message. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain audience-decision matrix, approved version, units, horizon, assumptions, exception thresholds, acknowledgement, and feedback. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **communicating demand decision record** with these fields:

- **Decision and boundary:** Define the audience, decision, aggregation, timing, uncertainty, and feedback route before selecting the dashboard or message.
- **Required evidence:** audience-decision matrix, approved version, units, horizon, assumptions, exception thresholds, acknowledgement, and feedback.
- **Expected result:** The same demand signal can produce conflicting actions when functions receive different versions, units, timing, or confidence.
- **Balancing condition:** More detail supports diagnosis but can obscure the decision; greater aggregation improves alignment but can hide mix and local risk.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

More detail supports diagnosis but can obscure the decision; greater aggregation improves alignment but can hide mix and local risk.

## Commonly confused with
**Data transfer vs. communication:** sending a number through a system is not the same as reaching shared understanding. Demand communication includes assumptions, uncertainty, priorities, and feedback.

## Common mistakes
When the main problem is "other parties did not know about a change soon enough," the best answer will often involve earlier, structured communication rather than simply more inventory.

## Original knowledge check

**Question.** NorthStar is deciding how to apply communicating demand. Which proposal is most defensible?

A. Use communicating demand as a label for the preferred option before defining the decision outcome, constraints, or owner.
B. Define the audience, decision, aggregation, timing, uncertainty, and feedback route before selecting the dashboard or message.
C. Choose the apparent upside without evaluating this balancing condition: More detail supports diagnosis but can obscure the decision; greater aggregation improves alignment but can hide mix and local risk.
D. Approve the choice without retaining audience-decision matrix, approved version, units, horizon, assumptions, exception thresholds, acknowledgement, and feedback; omit the reassessment trigger as well.

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Define the audience, decision, aggregation, timing, uncertainty, and feedback route before selecting the dashboard or message.**

### Why it is correct

The same demand signal can produce conflicting actions when functions receive different versions, units, timing, or confidence. The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: define the audience, decision, aggregation, timing, uncertainty, and feedback route before selecting the dashboard or message.
- **C** optimizes one visible result and omits the balancing effects: more detail supports diagnosis but can obscure the decision; greater aggregation improves alignment but can hide mix and local risk.
- **D** leaves the approval unauditable. A reviewer would be missing audience-decision matrix, approved version, units, horizon, assumptions, exception thresholds, acknowledgement, and feedback, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: more detail supports diagnosis but can obscure the decision; greater aggregation improves alignment but can hide mix and local risk.

</details>

## Practitioner perspective

A review should be able to reconstruct the choice from audience-decision matrix, approved version, units, horizon, assumptions, exception thresholds, acknowledgement, and feedback. If those records cannot explain what changed, who decided, and when the decision will be revisited, the process is not yet controlled.

## Related concepts

- [Section overview](./README.md)
- [Module 2 continuation](../../02-network-design-digital-connectivity-performance/section-b-connected-supply-networks-and-master-data/03-advanced-planning-and-constraint-management.md)
- [Demand manager and dashboard](04-demand-manager-and-dashboard.md)
- [Demand shaping and the Four Ps](06-demand-shaping-and-four-ps.md)
Module 1 → Section C → Communicating Demand; Communicate Soon; Structure Communications; Focus Communications.

---

[Previous: Planning Demand and the Demand Plan](02-planning-demand-and-demand-plan.md) · [Next: Demand Manager and Demand-Review Dashboards](04-demand-manager-and-dashboard.md)
