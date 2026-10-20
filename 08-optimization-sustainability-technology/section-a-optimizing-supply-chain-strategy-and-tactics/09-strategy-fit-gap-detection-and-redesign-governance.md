# 9. Strategy Fit, Gap Detection, and Redesign Governance

## Learning objectives

Understand the decision techniques in strategy fit, gap detection, and redesign governance, use explicit evidence and practical trade-offs, and test their physical and regulatory feasibility before choosing a solution.

## Concept in plain English

The strategic fit of a supply chain changes when the business, market or capabilities change. Misalignment can result from a new corporate direction, business combination, changing product life cycle, new channel, unforeseen demand behavior, disruptive technology or a supplier/transport shock. These triggers differ in origin. A redesign team should identify the cause before prescribing more inventory, another warehouse or a new planning platform.

A **gap** is a measurable difference between the required outcome or capability and what the current network delivers. The difference may concern customer lead time, available capacity, skill, data quality, financing, environmental performance or partner behavior. A gap statement requires a population, time horizon, verified baseline and a target. “Improve flexibility” is not enough to justify a costly initiative. “Protect five-day response for emergency customers when actual validated service is eight days” defines a testable gap.

A useful assessment examines the organization, processes, technology, people, metrics and partner commitments together. If sales changes the offer but supply contracts still assume twelve-week lead times, the company should not interpret every late order as a warehouse failure. Root-cause techniques may be borrowed from Module 4; supply disruption analysis from Module 7; supplier relationship controls from Module 6. Module 8 owns deciding whether the combined operating design still serves the strategy.

Redesign governance should not chase every short-term fluctuation. Changing the network frequently incurs transition cost and can destabilize planning. Leaders need a clear trigger: sustained measured gap, unacceptable compliance finding, loss of a critical supplier, a new market position or failure of the current design under tested conditions. Then they can decide whether to adjust a policy, invest in capability, change a partner arrangement or restructure the physical network. The least disruptive viable option deserves serious evaluation.

Complexity must be priced. Adding product variants, specialized fulfillment classes or redundant nodes can improve customer value, yet each adds master data, inventory, coordination and maintenance demands. A design improvement can therefore involve simplifying unnecessary variety rather than adding infrastructure. AlderGate's expansion plan includes product variants with very low observed demand; the team tests whether delayed differentiation and common subassemblies serve customers better than storing every finished variant.

## Why it matters

This capability matters when a proposed local change creates consequences outside its sponsoring function. The chosen customer promise, common planning horizon, implementation owner and evidence quality must remain visible to management. An analytically attractive idea may still be premature when the affected network cannot execute it safely or economically.

## Decision model and workflow

The gap register should show what changed in the customer's promise, which operating assumptions are now invalid, whether the deviation is sustained and which functions can fix it. The review team should also retain one rejected alternative and the reason it was rejected.

### Evidence retained through the workflow

| Decision record | Purpose |
| --- | --- |
| Baseline and target | State the population, units, horizon and accountable owner |
| Operating constraints | Preserve capacity, customer, safety, partner and legal conditions |
| Candidate economics | Compare consistent cost, benefit and resource assumptions |
| Alternatives and sensitivity | Retain why each option passed or failed and when to review |

## Practical process flow

```mermaid
flowchart TD
    A[Identify the customer outcome and scope]
    B[Retain quantified capabilities and assumptions]
    C[Screen mandatory gates and feasibility]
    D[Evaluate eligible alternatives and sensitivity]
    E[Approve owners and monitor results]
    A --> B
    B --> C
    C --> D
    D --> E
```

## Realistic example — AlderGate Motion Products

AlderGate is an independent fictional industrial manufacturer with standard couplings and an engineered repair line. The operations team must reconcile production and service requirements, while Quality confirms process qualification and Finance checks resource economics. The case below uses deliberately selected training figures; no values imply a universal industry benchmark.

## Applied decision artifact or worked calculation

An illustrative customer-service target is **95%** complete-on-time delivery over a defined month, while actual performance is **88%**. The gap is **7 percentage points**, not a 7% relative change. Suppose 350 of 4,000 orders fail the stated completeness/timing requirement: attainment is 3,650/4,000 = **91.25%** for that separate sample, with a 3.75-point gap to 95%. These populations must not be combined without reconciling definitions and time windows. Record root cause, owner, target, measured counterfactual and reassessment date.

## Decision logic

- Frame one clear decision, with measurable output and the same time units for all options.
- Verify required regulatory, safety, quality, security, continuity and capacity conditions before ranking.
- Compare the remaining feasible alternatives against an explicit enterprise objective.
- Preserve uncertainty and implement an owner-led review trigger for changing assumptions.

## Trade-offs

| Choice | Decision consequence |
| --- | --- |
| Greater analytical detail | Can better reflect reality but also increases maintenance and error risks |
| Greater flexibility | Can improve service but requires resource and governance costs |
| Narrow local optimization | Can improve one metric while worsening total enterprise value |

## Commonly confused with

A business objective does not automatically become a valid mathematical objective function. A method's numerical output must be interpreted against the operating model it represents. Feasibility, efficiency and strategic effectiveness answer distinct questions.

## Common mistakes

- Optimizing a metric that does not reflect the target customer or economic objective.
- Mixing monthly and weekly capacities or inconsistent financial scopes.
- Assigning a weighted penalty to an alternative that actually fails a mandatory condition.
- Claiming that a model result eliminates the need for implementation and sensitivity testing.

## Original knowledge check

**Question.** What is the strongest starting point for correcting a strategy-to-supply mismatch?

A. Buy a new system because technology changes faster than the market

B. Create a measurable gap statement, verify cause, then test least-disruptive feasible alternatives

C. Open a regional warehouse whenever there is a single missed order

D. Ignore stakeholder changes until every operating metric fails

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Create a measurable gap statement, verify cause, then test least-disruptive feasible alternatives**

### Why it is correct

A defined measured gap and credible diagnosis prevent expensive remedies for the wrong underlying cause.

### Why the other answers are wrong

- **A.** Technology without an operating cause may automate the failure.
- **C.** A single event does not necessarily justify fixed asset expansion.
- **D.** Changes to the competitive promise can require proactive assessment.

</details>

## Practitioner perspective

The cross-functional team should document whether the gap is a policy mismatch, a technology/data issue, a partner problem or a true physical capacity shortage. That classification determines the change owner and avoids treating every symptom as justification for a capital project.

## Related concepts

- [Previous topic](./customer-service-resource-and-partner-competencies.md)
- [Module 2 — Network Performance](../../02-network-design-digital-connectivity-performance/README.md)
- [Module 7 — Risk Analysis](../../07-supply-chain-risk/README.md)

---

[Previous topic](./customer-service-resource-and-partner-competencies.md) · [Section overview](./README.md)
