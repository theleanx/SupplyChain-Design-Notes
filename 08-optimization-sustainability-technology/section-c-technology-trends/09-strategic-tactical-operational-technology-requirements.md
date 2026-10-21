# 9. Strategic, Tactical, and Operational Technology Requirements

## Learning objectives

Translate this topic into an actionable supply-chain project decision with evidence, realistic feasibility limits and an accountable business owner.

## Concept in plain English

Technology needs should be expressed at several levels. **Strategic requirements** express how a system supports competitive positioning, structural integration and long-term decision capability. **Tactical requirements** define usable processes, automation and flexibility needed to operate the strategy. **Operational requirements** state the specific observable behavior, accuracy, timeliness, capacity and controls needed in real workflows.

For example, AlderGate's strategy may promise rapid visibility of engineered repair status. The tactical solution could offer role-based exception management across a supplier and two warehouses. A testable operational requirement might demand that 95% of relevant order-event changes become visible to authorized planners within ten minutes. The business must define who counts as a relevant order, what starts and stops the timer and how missing events are handled.

The manual encourages **SMART** objectives: specific, measurable, attainable, relevant and time-bound. A slogan such as "make planning digital" is not a specification or reliable vendor selection criterion. Every requirement should have a source owner, acceptance test, integration dependency and business rationale. Quality and cyber controls should not be hidden in a vendor presentation's performance score.

Tactical usefulness also depends on people and processes. A plant may gain sophisticated automated calculations yet need planners who can interpret exceptions and partner owners who can validate master data. A useful requirements workshop includes sales, sourcing, IT, Quality, logistics and finance where relevant. This prevents one group's UI preference from overriding fundamental customer constraints.

AlderGate documents how its promise connects to process workflow and data acceptance. Two pilots may show different strengths; the selection can only be made fairly when both are tested against the same population, timing and authorized action.

**Study-source mapping:** CSCP 2026 Module 8 pp. 249–253. All worked examples and artifacts below are independent, fictional and scoped to stated inputs.

## Why it matters

The decision changes AlderGate's ability to fulfill its intended customer promise, manage scarce resources and govern technology risks. Technical features matter only when the connected process can use them responsibly and support them after implementation.

## Decision model and workflow

![Original Strategic, Tactical, and Operational Technology Requirements model](../../assets/diagrams/module-8/section-c/strategic-tactical-operational-technology-requirements.svg)

### Evidence retained through the workflow

| Evidence domain | Required disposition |
| --- | --- |
| Strategic outcome | Retain source, owner, threshold and review date |
| Tactical flow | Retain source, owner, threshold and review date |
| Operational KPI | Retain source, owner, threshold and review date |
| Acceptance test | Retain source, owner, threshold and review date |

## Practical process flow

```mermaid
flowchart TD
    A[Document target operating result] --> B[Evaluate current capability and data]
    B --> C{All critical requirements feasible?}
    C -- No --> D[Remediate gap or reject proposal]
    D --> B
    C -- Yes --> E[Compare costs, benefits and dependencies]
    E --> F[Authorize owner-led implementation and review]
```

## Realistic example — AlderGate Motion Products

AlderGate translates 'real-time status' into measurable event age, access restrictions, and documented business ownership. The vendor must satisfy each critical acceptance threshold independently before a broader feature score is considered.

## Applied decision artifact or worked calculation

[Directly linked original training dataset](../../assets/data/module-8/section-c/requirement-results.csv)

Of **200** priority events, **192** appear within the defined target: **96%**, exceeding the fictional 95% requirement. Supplier confirmations pass only **82 of 100 = 82%**, missing a separate 90% requirement. The program must not declare all requirements met.

## Decision logic

- Establish the business goal and evidence denominator before describing technical success.
- Confirm the relevant people, suppliers, physical resources and data controls are ready.
- Exclude proposals with unresolved mandatory quality, legal, security or safety failures.
- Compare the remaining alternatives on consistent cost and service horizons.
- Link release, ongoing support and reassessment to the responsible business owner.

## Trade-offs

| Management tension | Consequence |
| --- | --- |
| Early delivery versus complete requirements | Unresolved dependencies can create repeated rework |
| Enterprise standards versus justified customization | A unique extension must demonstrate ongoing value and supportability |
| Project completion versus sustained benefit | Go-live should be followed by measured operating results |

## Commonly confused with

A project schedule is not a technology roadmap, a vendor feature demonstration is not an accepted requirement, and an audit closure ratio is not an authority to bypass a critical defect. Each record has its own specific decision use.

## Common mistakes

- Treating a better numerical average as a substitute for mandatory eligibility.
- Buying an application before evaluating process, people or data causes.
- Omitting the owners and acceptance conditions for project benefits.
- Assuming a technology project ends when software is installed.

## Original knowledge check

**Question.** Which is a properly testable operational technology requirement?

A. Become the most digital supplier

B. Buy the product with the most buttons

C. Provide modern user experiences whenever possible

D. Show verified priority exceptions to authorized planners within ten minutes for at least 95% of eligible events

<details>
<summary>Answer and rationale</summary>

### Correct answer

**D. Show verified priority exceptions to authorized planners within ten minutes for at least 95% of eligible events**

### Why it is correct

The requirement specifies a real event population, named behavior, time boundary and numeric acceptance criterion.

### Why the other answers are wrong

- **A.** The ambition lacks an acceptance test.
- **B.** Feature counts are not process requirements.
- **C.** An undefined experience promise cannot be objectively checked.

</details>

## Practitioner perspective

The solution team must preserve the relationship from requirement or finding to master data, processes, authorized user and acceptance test. Effective technology adoption requires post-go-live ownership.

## Related concepts

- [Previous topic](./08-technology-audits-risk-and-post-implementation-review.md)
- [Module 2 network and digital design](../../02-network-design-digital-connectivity-performance/README.md)
- [Module 7 contingency gates](../../07-supply-chain-risk/README.md)

---

[Section C overview](./README.md) · [Previous topic](./08-technology-audits-risk-and-post-implementation-review.md)
