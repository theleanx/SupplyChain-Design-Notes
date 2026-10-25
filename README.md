# Supply Chain Design Notes

Independent, practitioner-oriented learning notes for designing supply networks, planning demand, sourcing and operating supply, moving goods, managing customer and supplier relationships, and measuring performance.

> **Current release: v8.0.1 — all eight supply-chain learning modules are published on `main`.** Module 8 was merged through [PR #17](https://github.com/theleanx/SupplyChain-Design-Notes/pull/17) and separately authorized for [v8.0.0 publication](https://github.com/theleanx/SupplyChain-Design-Notes/releases/tag/v8.0.0) and the [v8.0.1 documentation patch](https://github.com/theleanx/SupplyChain-Design-Notes/releases/tag/v8.0.1). All content uses original explanations, fictional examples and independently authored practice checks.

## Start here

| Module | Focus | Open |
|---|---|---|
| 1 | Supply-chain foundations, demand analysis, forecasting, and supply-demand alignment | [Supply Chains, Demand, and Forecasting](./01-supply-chains-demand-forecasting/) |
| 2 | Network design, digital connectivity, master data, performance, and financial insight | [Network Design, Digital Connectivity, and Performance](./02-network-design-digital-connectivity-performance/) |
| 3 | Sourcing strategy, category management, product design, supplier selection, contracting, and procurement | [Sourcing Strategy, Product Design, and Supplier Execution](./03-sourcing-strategy-product-design-supplier-execution/) |
| 4 | Internal operations, master scheduling, MRP, capacity, inventory, quality, and continuous improvement | [Internal Operations and Inventory](./04-internal-operations-inventory/) |
| 5 | Logistics, warehousing, fulfillment, transportation, international trade, returns, reverse logistics, and waste | [Forward and Reverse Logistics](./05-forward-reverse-logistics/) |
| 6 | Customer relationships, CRM, supplier relationships, SRM, alliances, performance, certification, collaboration, and communication | [Supply Chain Relationships](./06-supply-chain-relationships/) |
| 7 | Risk governance, qualitative/quantitative assessment, response economics, disruption recovery and business continuity | [Supply Chain Risk](./07-supply-chain-risk/) |
| 8 | Strategic optimization, sustainability, technology adoption and lifecycle decisions | [Module 8 — Optimization, Sustainability, and Technology](./08-optimization-sustainability-technology/README.md) |

Choose a route using the [role-based learning paths](./LEARNING-PATHS.md), look up a term in the [repository glossary](./GLOSSARY.md), or move directly to a quantitative reference:

- [Forecasting formula sheet](./calculations/forecasting/formula-sheet.md)
- [Network and performance formula sheet](./calculations/network-performance/formula-sheet.md)
- [Sourcing and procurement formula sheet](./calculations/sourcing-procurement/formula-sheet.md)
- [Internal operations and inventory formula sheet](./calculations/internal-operations/formula-sheet.md)
- [Logistics, trade, and reverse-flow formula sheet](./calculations/logistics-trade-reverse/formula-sheet.md)
- [Relationship performance formula & control sheet](./calculations/relationship-performance/formula-sheet.md)
- [Risk analysis and response formula sheet](./calculations/risk-response/formula-sheet.md)

Each module ends with an integrated fictional case:

- [NorthStar planning capstone](./01-supply-chains-demand-forecasting/capstone/README.md)
- [AsterWorks network-transformation capstone](./02-network-design-digital-connectivity-performance/capstone/README.md)
- [Rivermark sourcing-and-design capstone](./03-sourcing-strategy-product-design-supplier-execution/capstone/README.md)
- [Pinehaven operations-stabilization capstone](./04-internal-operations-inventory/capstone/README.md)
- [HarborPeak network, trade, and reverse-flow stabilization capstone](./05-forward-reverse-logistics/capstone/README.md)
- [ClearSpan customer-supplier relationship stabilization capstone](./06-supply-chain-relationships/capstone/README.md)
- [Stonebridge risk and resilience capstone](./07-supply-chain-risk/capstone/README.md)
- [AlderGate integrated optimization, sustainability and technology capstone](./08-optimization-sustainability-technology/capstone/README.md)

## What makes this repository useful

Each major topic follows a consistent learning pattern:

1. concept and plain-English explanation;
2. business relevance and decision logic;
3. an original diagram, table, or process flow;
4. a realistic, independently created example;
5. a worked calculation when applicable;
6. trade-offs, common confusion, and common mistakes;
7. an original knowledge check and practitioner perspective; and
8. related concepts and further exploration.

The examples use fictional organizations and independently selected values. Diagrams are maintained as repository-native Mermaid or SVG assets, while calculation inputs are provided as CSV files where useful.

## Repository map

```text
01-supply-chains-demand-forecasting/                  Module 1 learning content
02-network-design-digital-connectivity-performance/  Module 2 learning content
03-sourcing-strategy-product-design-supplier-execution/ Module 3 learning content
04-internal-operations-inventory/                    Module 4 learning content
05-forward-reverse-logistics/                        Module 5 learning content
06-supply-chain-relationships/                        Module 6 learning content
07-supply-chain-risk/                                 Module 7 learning content
08-optimization-sustainability-technology/             Module 8 learning content
assets/diagrams/module-1/                            Module 1 SVG diagrams
assets/diagrams/module-2/                            Module 2 SVG diagrams
assets/diagrams/module-3/                            Module 3 SVG diagrams
assets/diagrams/module-4/                            Module 4 SVG diagrams
assets/diagrams/module-5/                            Module 5 SVG diagrams
assets/diagrams/module-6/                            Module 6 SVG diagrams
assets/diagrams/module-7/                            Module 7 SVG diagrams
assets/diagrams/module-8/                            Module 8 SVG diagrams
assets/data/module-1/                                Module 1 example datasets
assets/data/module-2/                                Module 2 example datasets
assets/data/module-3/                                Module 3 example datasets
assets/data/module-4/                                Module 4 example datasets
assets/data/module-5/                                Module 5 example datasets
assets/data/module-6/                                Module 6 example datasets
assets/data/module-7/                                Module 7 example datasets
assets/data/module-8/                                Module 8 example datasets
calculations/forecasting/                            Forecasting references
calculations/network-performance/                    Network and performance references
calculations/sourcing-procurement/                   Sourcing and procurement references
calculations/internal-operations/                    Internal operations and inventory references
calculations/logistics-trade-reverse/                Logistics, trade, and reverse-flow references
calculations/relationship-performance/                 Relationship-management performance and control references
calculations/risk-response/                           Risk-response calculations and decision-control references
calculations/module8-capstone/                        Module 8 integrated decision models and replay
GLOSSARY.md                                           Cross-module terminology index
LEARNING-PATHS.md                                     Role- and time-based reading routes
_templates/                                           Reusable authoring templates
scripts/                                              Automated repository validation
QUALITY.md                                            Quality and originality standards
```

## Module 8 published inventory — v8.0.0

Module 8 contains **54 module learning/reference Markdown pages**, including **42 original lessons** across three sections, three section reviews, and the worked AlderGate integrated capstone; **45 original Module 8 SVG diagrams** and **47 fictional Module 8 CSV datasets**. It has **89 answered checks**: 42 lesson questions, 42 section-review scenarios and five capstone questions. The owner reviewed the visuals/editorial content and waived external independent review. [PR #17](https://github.com/theleanx/SupplyChain-Design-Notes/pull/17) was merged into `main` on October 25, 2026, and [v8.0.0](https://github.com/theleanx/SupplyChain-Design-Notes/releases/tag/v8.0.0) records the released baseline.

- [Module 8 learning path](./08-optimization-sustainability-technology/README.md)
- [Capstone student assignment](./08-optimization-sustainability-technology/capstone/README.md) and [worked solution](./08-optimization-sustainability-technology/capstone/solution-guide.md)
- [Module 8 synthetic data catalog](./assets/data/module-8/README.md)
- [Module 8 calculations and gated replay](./calculations/module8-capstone/README.md)

## Quality status

The repository currently includes:

- 423 structured Markdown files across eight completed modules;
- twenty-seven connected learning sections;
- 295 original SVG diagrams plus repository-native Mermaid process flows;
- 148 original CSV datasets for worked analysis;
- 812 independently authored knowledge checks;
- eight integrated end-to-end capstones; and
- automated validation of internal navigation, Markdown structure, process-flow presence, quantitative dataset linkage, worked results, SVG accessibility, CSV consistency, and module-specific calculation controls.

The repository runs a read-only content-quality workflow on every push and pull request to detect broken links, malformed datasets, invalid or inaccessible SVGs, missing process flows, inconsistent calculations, weak assessment language, structural drift, unbalanced Markdown blocks, and drift from the shared module/section overview contract.

## Independence, attribution, and permitted use

This repository contains original educational material created for supply-chain practitioners and learners. It is not a substitute for professional advice.

- Do not upload or contribute material you do not own or have permission to publish.
- Explain concepts in your own words and use independently created examples and visuals.
- Cite external facts and ideas; do not treat a citation as permission to reproduce protected expression.
- Follow [ATTRIBUTION.md](./ATTRIBUTION.md), [CONTRIBUTING.md](./CONTRIBUTING.md), and the [disclaimer](./DISCLAIMER.md) before contributing.

Repository licensing is deliberately split: authored learning content and visual/data assets are all rights reserved; software code explicitly placed under the code license may be used under the MIT License. See [LICENSE.md](./LICENSE.md).

## Roadmap

Modules are published only after their content, calculations, visuals, navigation, and originality controls pass release review. See [ROADMAP.md](./ROADMAP.md).

## Author

Created and maintained by **Ankit Sharma** through **TheLeanX** as an independent supply-chain learning project.
