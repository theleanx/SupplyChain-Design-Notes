# 3. Category Portfolio Analysis

## Learning objectives

After this topic, you should be able to:

- classify categories by business impact and supply risk;
- select differentiated category actions;
- avoid static quadrant thinking;

## Concept in plain English

Portfolio analysis positions a category using two dimensions: consequence to the business and difficulty of securing supply. The result guides attention, competition, collaboration, continuity, and investment.

## Why it matters

Treating every category alike wastes scarce management capacity. Routine spend should be efficient; constrained and strategically important supply needs deliberate protection.

## Decision model and workflow

![Category Portfolio Analysis decision workflow](../../assets/diagrams/module-3/section-b/03-portfolio-analysis-workflow.svg)

### Evidence retained through the workflow

| Stage | Required evidence or output |
|---|---|
| **1. Define impact measures** | Business-impact measures covering margin, revenue, operations, quality, and customer consequence |
| **2. Define supply-risk measures** | Supply-risk measures covering scarcity, switching time, concentration, technology, and location |
| **3. Score with evidence** | Evidence-based scoring with sources, confidence, and cross-functional challenge |
| **4. Place the category** | Portfolio placement with boundary cases and uncertainty made visible |
| **5. Select and review the strategy** | Category action plan matched to the quadrant and reviewed after material changes |

## Practical process flow

```mermaid
flowchart TD
    A["Define business-impact scale"] --> B["Define supply-risk scale"]
    B --> C["Score categories with evidence"]
    C --> D["Place category in portfolio"]
    D --> E["Select quadrant-specific action"]
    E --> F["Set triggers and review cadence"]
    F --> C
```

## Realistic example — Rivermark Climate Systems

Rivermark classifies fasteners as routine, sheet metal as leverage, refrigerant sensors as bottleneck, and compressor assemblies as strategic. The actions differ: automate fasteners, compete sheet metal, secure sensors, and co-plan compressors.

**Decision insight.** The result prevents low spend from hiding the sensor constraint and prevents high spend alone from turning competitive sheet metal into a strategic partnership.

All names and values in this example are fictional and independently selected for learning purposes.

## Worked decision — portfolio classification

Apply one documented scale to the [category-portfolio dataset](../../assets/data/module-3/section-b/category-portfolio.csv). Compressor assemblies score 5 for business impact and 5 for supply risk, so they are strategic; fasteners score 1 and 1, so they are routine. The label is a starting hypothesis, not the analysis itself.

For each placement, attach evidence and a response: strategic categories need joint capacity and continuity; bottlenecks need qualification or redesign; leverage categories need competitive and specification actions; routine categories need standardization and automation. Set an event trigger—such as capacity loss, regulation, sole-source status, or spend change—because a portfolio position can move before the annual refresh.

## Decision logic

- Use multiple evidence points rather than one opinion.
- Document why a category sits near a boundary.
- Reassess after design, market, or demand changes.

## Trade-offs

| Choice tension | Decision implication |
|---|---|
| A simple matrix improves focus but compresses nuance | Use the matrix to allocate attention, then add category-specific evidence for decisions the two axes cannot represent. |
| Scoring improves consistency but can conceal weak evidence | Keep the underlying facts beside every score so reviewers can distinguish measured exposure from judgment. |

## Commonly confused with

High spend does not automatically mean strategic. A low-cost component can be a bottleneck if its absence stops shipment.

## Common mistakes

- Using purchase price as the only impact measure.
- Assuming many suppliers means low risk without qualification checks.
- Keeping the classification unchanged after redesign.

## Original knowledge check

**Question.** A low-cost sensor has one qualified source and stops final shipment when unavailable. How should it be treated?

A. Routine

B. Leverage

C. Bottleneck

D. Routine, because low spend should override supply risk

<details>
<summary>Answer and rationale</summary>

### Correct answer

**C. Bottleneck**

### Why it is correct

Its financial spend is low, but supply difficulty and operational consequence demand continuity attention.

### Why the other answers are wrong

A and B understate scarcity; D incorrectly lets low spend override supply difficulty and operational consequence.

</details>

## Practitioner perspective

The debate behind the placement is often more valuable than the quadrant label. Record the evidence and uncertainty.

## Related concepts

- [Module 3 overview](../README.md)
- [Section overview](./README.md)
- [Category-portfolio dataset](../../assets/data/module-3/section-b/category-portfolio.csv)
- [Supply-Base Right-Sizing](./07-supply-base-right-sizing.md)

---

[Previous: Category Architecture and Strategy](./02-category-architecture.md) · [Next: Supplier Attractiveness and Segmentation](./04-supplier-attractiveness-and-segmentation.md)
