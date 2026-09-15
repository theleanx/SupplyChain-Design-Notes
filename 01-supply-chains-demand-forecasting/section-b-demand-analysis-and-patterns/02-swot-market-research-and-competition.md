# 2. SWOT, Market Research, and Competitive Intelligence

## Learning objectives

You should be able to:

- explain the operating logic behind swot, market research, and competitive intelligence;
- apply the lesson to a realistic planning or supply-chain decision; and
- identify the evidence, trade-off, and trigger needed for responsible use.

## Concept in plain English

Strategic demand analysis needs both an **inside view** and an **outside view**. SWOT provides the frame; market research and competitive intelligence provide much of the evidence.

### SWOT in one picture

| | Positive | Negative |
|---|---|---|
| **Internal** | **Strengths** — capabilities that help us compete | **Weaknesses** — internal gaps that hold us back |
| **External** | **Opportunities** — conditions we could exploit | **Threats** — external conditions that could hurt results |

A good SWOT is evidence-based. A vague statement such as “strong brand” is less useful than “repeat-purchase rate is 18 percentage points above the category average in our largest segment.”

## Original visualization — from business plan to market plan

```mermaid
flowchart TD
    BP[Business plan] --> F[Finance]
    BP --> E[Engineering / product]
    BP --> M[Marketing]
    BP --> O[Operations / supply chain]
    M --> MP[Market plan]
    MP --> P1[Current market position]
    MP --> P2[Opportunities and issues]
    MP --> P3[Objectives and strategies]
    MP --> P4[Actions, programs, projects]
    MP --> P5[Forecast financial outcome]
    MP --> P6[Management controls]
    O -. feasibility and service capability .-> MP
    E -. product capability .-> MP
    F -. financial boundaries .-> MP
```

## Original visualization — market-analysis landscape

```mermaid
flowchart LR
    GE[Global / regional economy] --> MA[Market analysis]
    IE[Industry conditions] --> MA
    GR[Government / regulation] --> MA
    EV[Major events / disruptions] --> MA
    CP[Competitors / substitutes] --> MA
    CU[Customer needs / behavior] --> MA
    MA --> MS[Market size and location]
    MA --> SG[Segmentation opportunities]
    MA --> SH[Share / competitive position]
    MA --> FO[Forward-looking assumptions]
```


> **Terminology:** These notes use **market research** as a concise label for systematically gathering and analyzing market, sales, and customer information to support decisions.

## Three useful forms of market research

- **Market analysis:** how large the market is, where it is, how it behaves, and what segments exist.
- **Sales analysis:** how sales and market share are changing by product, customer, geography, or channel.
- **Consumer/customer research:** what buyers value, reject, prefer, complain about, and may be willing to pay for.

## Original process — what market research is trying to accomplish

```mermaid
flowchart LR
    A[Find potential demand
Is there a meaningful need?] --> B[Analyze the market
Who? where? when? why? how many?]
    B --> C[Refine the offer
features, service, price, support]
    C --> D[Test supply-chain feasibility
capacity, cost, channel, service]
```

## Handoff risk — research is not the same as a neutral forecast

Commercial teams naturally want growth, and optimistic assumptions can unintentionally enter the demand plan. If supply planners respond by creating their own conservative version, the organization ends up with competing plans instead of one shared set of assumptions. Cross-functional review is therefore important: assumptions, uncertainty, promotions, and known market events should be visible to everyone using the forecast. In collaborative supply relationships, forecast information may also need to be shared across company boundaries.

Market research should also inform the **service and reverse-flow design** of the offer: documentation, languages, support channels, return policy, repair expectations, disposal/recycling concerns, and other post-sale requirements can all change total demand and total cost.

## Realistic example — smart pump launch

NorthStar is considering a predictive-maintenance version of its pump. Interviews show that large chemical plants value remote condition monitoring, but smaller municipal customers care more about purchase price and ease of repair.

The research result should **not** automatically produce two highly customized products. The team should ask whether the additional variants create enough incremental margin to justify engineering, inventory, service, documentation, and forecasting complexity.

## Competitive scan

A useful competitor scan asks:

- What does the competitor offer?
- At what effective price and service level?
- Where is it stronger or weaker by region?
- Which customer need is still unsatisfied?
- Is the advantage based on cost, availability, quality, innovation, service, or channel access?
- How mature is the competitor's supply-chain capability?

```mermaid
flowchart TD
    C[Competitor / substitute scan] --> G[Identify customer gap]
    G --> V[Define a credible value advantage]
    V --> S[Check supply-chain capability]
    S --> T[Test in target segment]
    T --> L[Learn and scale]
```

## Why it matters

Strategy deteriorates when internal opinions, customer evidence, and competitor signals are blended without source or confidence.

## Decision logic

Use SWOT as a synthesis after research, document evidence separately, and show how each material finding changes demand, positioning, or capacity decisions. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain research question, source, sample or method, finding, confidence, competitive implication, assumption, and decision affected. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **SWOT, market research, and competitive intelligence decision record** with these fields:

- **Decision and boundary:** Use SWOT as a synthesis after research, document evidence separately, and show how each material finding changes demand, positioning, or capacity decisions.
- **Required evidence:** research question, source, sample or method, finding, confidence, competitive implication, assumption, and decision affected.
- **Expected result:** Strategy deteriorates when internal opinions, customer evidence, and competitor signals are blended without source or confidence.
- **Balancing condition:** More research reduces uncertainty but consumes time; stop when additional evidence is unlikely to change the decision or range.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

More research reduces uncertainty but consumes time; stop when additional evidence is unlikely to change the decision or range.

## Commonly confused with
**Market share** is the portion of current market demand captured by the company or product. It is not the same as revenue growth. A company can grow revenue while losing share if the total market grows faster.

## Common mistakes
A customer survey alone does not tell you whether the market contains an unmet need. You also need to understand competing and substitute offerings.

## Original knowledge check

**Question.** NorthStar is deciding how to apply SWOT, market research, and competitive intelligence. Which proposal is most defensible?

A. Use SWOT, market research, and competitive intelligence as a label for the preferred option before defining the decision outcome, constraints, or owner.
B. Use SWOT as a synthesis after research, document evidence separately, and show how each material finding changes demand, positioning, or capacity decisions.
C. Choose the apparent upside without evaluating this balancing condition: More research reduces uncertainty but consumes time; stop when additional evidence is unlikely to change the decision or range.
D. Approve the choice without retaining research question, source, sample or method, finding, confidence, competitive implication, assumption, and decision affected; omit the reassessment trigger as well.

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Use SWOT as a synthesis after research, document evidence separately, and show how each material finding changes demand, positioning, or capacity decisions.**

### Why it is correct

Strategy deteriorates when internal opinions, customer evidence, and competitor signals are blended without source or confidence. The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: use SWOT as a synthesis after research, document evidence separately, and show how each material finding changes demand, positioning, or capacity decisions.
- **C** optimizes one visible result and omits the balancing effects: more research reduces uncertainty but consumes time; stop when additional evidence is unlikely to change the decision or range.
- **D** leaves the approval unauditable. A reviewer would be missing research question, source, sample or method, finding, confidence, competitive implication, assumption, and decision affected, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: more research reduces uncertainty but consumes time; stop when additional evidence is unlikely to change the decision or range.

</details>

## Practitioner perspective

Market research becomes operationally valuable when it changes a decision: product design, service level, forecast, customer segment, distribution channel, sourcing model, or inventory strategy. Research that never affects a decision is merely information collection.

## Related concepts


- [Section overview](./README.md)
- [Module 2 continuation](../../02-network-design-digital-connectivity-performance/section-a-network-design-and-technology-investment/02-market-segmentation-and-service-choices.md)
Module 1 → Section B → SWOT Analysis, Market Research, Competition, Market Plan. Public wording and diagrams are original.

---

[Previous: Demand Analysis and Environmental Scanning](01-demand-analysis-and-environmental-scan.md) · [Next: Global Perspectives and Market Volatility](03-global-perspectives.md)
