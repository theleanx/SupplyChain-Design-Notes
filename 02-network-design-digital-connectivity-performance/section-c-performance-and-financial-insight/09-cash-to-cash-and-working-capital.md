# 9. Cash-to-Cash and Working Capital

## Learning objectives

After this topic, you should be able to:

- explain inventory, receivables, and payables days;
- calculate cash-to-cash cycle time;
- connect operational changes to working capital; and
- avoid interpreting a lower number without understanding its cause.

## Core formula

$$
\text{Cash-to-cash days}=\text{inventory days}+\text{receivable days}-\text{payable days}
$$

Common approximations are:

$$
\text{Inventory days}=\frac{\text{average inventory}}{\text{annual cost of goods sold}}\times365
$$

$$
\text{Receivable days}=\frac{\text{average trade receivables}}{\text{annual credit revenue}}\times365
$$

$$
\text{Payable days}=\frac{\text{average trade payables}}{\text{annual purchases}}\times365
$$

When purchases are unavailable, some organizations use cost of goods sold as an approximation. State the convention and use it consistently.

## Worked example

From [`working-capital.csv`](../../assets/data/module-2/section-c/working-capital.csv), assume:

- inventory days = 64;
- receivable days = 42; and
- payable days = 38.

Then:

$$
64+42-38=68\text{ days}
$$

![Cash-to-cash operating cycle](../../assets/diagrams/module-2/section-c/cash-to-cash.svg)

## Operating connection

```mermaid
flowchart LR
    A[Buy and pay] --> B[Hold and transform inventory]
    B --> C[Sell and deliver]
    C --> D[Invoice and collect]
    D --> E[Cash recovered]
```

## AsterWorks example

Regional stock shortens customer delivery but initially adds twelve inventory days. The design also improves invoicing accuracy and reduces receivable days by five. The working-capital effect must include both changes rather than treating inventory in isolation.

## Interpretation cautions

A lower cash-to-cash cycle may result from:

- better flow and inventory design;
- faster, more accurate invoicing and collection;
- extended supplier terms;
- delayed purchases or unpaid obligations; or
- business-mix changes.

The number improves financially only when the mechanism is sustainable and does not transfer unacceptable risk to suppliers or customers.

## Why it matters

Inventory, receivables, and payables connect operational design to cash and can shift financing pressure across the network.

## Decision logic

Calculate all three day measures using consistent annual flows, compare scenarios, and explain the operating mechanism behind every change. Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner.

## Evidence retained through the workflow

Retain average balances, annual revenue, COGS and purchases, day conventions, scenario assumptions, service effect, partner effect, and owner. Record the decision date and the event or threshold that requires reassessment.

## Applied decision artifact

Use a one-page **cash-to-cash and working capital decision record** with these fields:

- **Decision and boundary:** Calculate all three day measures using consistent annual flows, compare scenarios, and explain the operating mechanism behind every change.
- **Required evidence:** average balances, annual revenue, COGS and purchases, day conventions, scenario assumptions, service effect, partner effect, and owner.
- **Expected result:** Inventory, receivables, and payables connect operational design to cash and can shift financing pressure across the network.
- **Balancing condition:** Lower inventory releases cash but can reduce service or resilience; longer payables improve buyer cash while increasing supplier strain.
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory.

## Trade-offs

Lower inventory releases cash but can reduce service or resilience; longer payables improve buyer cash while increasing supplier strain.

## Commonly confused with

Do not confuse a preferred decision method with a guaranteed outcome. Calculate all three day measures using consistent annual flows, compare scenarios, and explain the operating mechanism behind every change. Validate the result with average balances, annual revenue, COGS and purchases, day conventions, scenario assumptions, service effect, partner effect, and owner; the evidence, not the method's label, determines whether the choice worked.

## Common mistakes

- Mixing end-of-period balance with average-balance formulas.
- Using revenue in inventory days when cost is required.
- Treating all inventory reduction as service-neutral.
- Extending supplier payment without assessing continuity and relationship impact.
- Comparing companies with inconsistent classifications.

## Original knowledge check

Inventory days are 50, receivable days 35, and payable days 40. What is cash-to-cash time?

<details>
<summary>Answer and rationale</summary>

### Correct answer

`50 + 35 - 40 = 45 days`.

### Why it is correct

Inventory, receivables, and payables connect operational design to cash and can shift financing pressure across the network. Calculate all three day measures using consistent annual flows, compare scenarios, and explain the operating mechanism behind every change.

### Why the other answers are wrong

Alternative responses reproduce failure modes already discussed:

- Mixing end-of-period balance with average-balance formulas.
- Using revenue in inventory days when cost is required.
- Treating all inventory reduction as service-neutral.

They do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: Lower inventory releases cash but can reduce service or resilience; longer payables improve buyer cash while increasing supplier strain.

</details>

## Practitioner perspective

Use average balances, annual revenue, COGS and purchases, day conventions, scenario assumptions, service effect, partner effect, and owner as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision.

## Related concepts



- [Network and performance formula sheet](../../calculations/network-performance/formula-sheet.md)
- [Section overview](./README.md)
- [Module 3 continuation](../../03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)
Continue to [asset efficiency and inventory turnover](10-asset-efficiency-and-inventory-turnover.md).

---

[Previous: Cost, Profit, and Productivity](08-cost-profit-and-productivity.md) · [Next: Asset Efficiency and Inventory Turnover](10-asset-efficiency-and-inventory-turnover.md)
