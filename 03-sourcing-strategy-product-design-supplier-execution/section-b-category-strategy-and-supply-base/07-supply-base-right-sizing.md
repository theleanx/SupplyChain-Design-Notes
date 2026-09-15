# 7. Supply-Base Right-Sizing

## Learning objectives

After this topic, you should be able to:

- determine an appropriate supplier count;
- balance efficiency with continuity and competition;
- sequence consolidation responsibly;

## Concept in plain English

Right-sizing seeks the supplier base that best supports cost, capacity, innovation, resilience, and governance. It may consolidate fragmented spend, add alternate sources, or replace weak sources.

## Why it matters

Fewer suppliers can reduce transaction cost and increase leverage, but excessive consolidation creates capacity, bargaining, geographic, and recovery risk.

## Decision model and workflow

![Supply-Base Right-Sizing decision workflow](../../assets/diagrams/module-3/section-b/07-supply-base-right-sizing-workflow.svg)

### Evidence retained through the workflow

| Stage | Required evidence or output |
|---|---|
| **1. Define category objectives** | Category objectives for cost, innovation, capacity, service, resilience, and administration |
| **2. Map suppliers, sites, capabilities, and dependencies** | Supplier-site network including ownership, common subtiers, tooling, technology, and geography |
| **3. Model target concentration and capacity** | Target award shares tested against capacity, dependency, qualification, and failure scenarios |
| **4. Sequence awards and exits** | Sequenced award, development, qualification, transition, and exit plan |
| **5. Monitor savings and residual risk** | Benefits and risk dashboard covering concentration, utilization, switching readiness, and health |

## Practical process flow

```mermaid
flowchart TD
    A["Map demand, capacity, qualification, and parent exposure"] --> B["Calculate concentration and switching constraints"]
    B --> C{"Aggregation benefit exceeds resilience loss?"}
    C -->|Yes| D["Consolidate with continuity controls"]
    C -->|No| E["Diversify or qualify alternate"]
    D --> F["Set allocation and trigger limits"]
    E --> F
    F --> G["Monitor performance and concentration"]
```

## Realistic example — Rivermark Climate Systems

Rivermark reduces fabricated-enclosure suppliers from nine to five but keeps two qualified geographic regions and no supplier above 45% of category volume. For the single-source sensor, right-sizing means adding—not removing—a second qualified source.

**Decision insight.** The five-supplier design reduces administrative load while the regional and share caps prevent savings from creating a single failure point.

All names and values in this example are fictional and independently selected for learning purposes.

## Worked decision — parent-level concentration

Use the [supplier-share dataset](../../assets/data/module-3/section-b/supplier-shares.csv), which reconciles suppliers to parent groups. Compressor-assembly shares are 52%, 28%, and 20%, producing:

`HHI = 52² + 28² + 20² = 3,888`

Refrigerant sensors have one qualified parent at 100%, so `HHI = 100² = 10,000`. The calculation exposes concentration but does not prescribe an arbitrary supplier count. Compare the benefit of consolidation with capacity headroom, recovery time, tooling portability, qualification expense, geographic correlation, and supplier investment. Set allocation limits and a trigger—for example, a capacity or financial event—that causes the sourcing team to activate an alternate path.

## Decision logic

- Set target counts by category rather than enterprise slogan.
- Measure concentration at parent, site, material, and tooling levels.
- Retain competition and recovery capacity where consequences justify it.

## Trade-offs

| Choice tension | Decision implication |
|---|---|
| Consolidation lowers administrative cost but increases exposure | Consolidate only after modeling the loss of a supplier, site, region, or shared subtier at the proposed award shares. |
| Dual sourcing improves continuity but divides learning and volume | Use dual sourcing when independent qualified capacity justifies its cost; otherwise maintain a credible alternate process or recovery plan. |

## Commonly confused with

Rationalization does not always mean reduction. The correct size may be larger when resilience is inadequate.

## Common mistakes

- Applying an arbitrary percentage-reduction target.
- Dropping small suppliers without capability review.
- Claiming savings before transition cost and volume commitments are secured.

## Original knowledge check

**Question.** When can adding a supplier be a right-sizing action?

A. When the current sourcing team has unused administrative capacity

B. When one qualified source creates unacceptable continuity risk

C. When additional competition may lower price, without testing qualification cost or capacity need

D. When the incumbent's award share falls below an arbitrary percentage

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. When one qualified source creates unacceptable continuity risk**

### Why it is correct

Right-sizing optimizes the supply base; it is not synonymous with shrinking it.

### Why the other answers are wrong

A, C, and D use workload, price pressure, or an arbitrary threshold without proving a resilience need.

</details>

## Practitioner perspective

Track residual risk after consolidation. Savings are incomplete if the organization quietly accepts a recovery exposure it cannot tolerate.

## Related concepts

- [Module 3 overview](../README.md)
- [Section overview](./README.md)
- [Supplier-share dataset](../../assets/data/module-3/section-b/supplier-shares.csv)
- [Category Portfolio Analysis](./03-portfolio-analysis.md)
- [Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)

---

[Previous: Spend Analysis and Supply-Market Intelligence](./06-spend-analysis-and-market-intelligence.md) · [Section review](./08-section-b-review.md)
