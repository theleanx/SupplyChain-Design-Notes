# Visual and Data Asset Guide

This directory contains independently created assets used by the learning notes.

```text
assets/
├── diagrams/module-1/section-x/   Original standalone SVG diagrams
├── data/module-1/section-x/       Original section datasets
└── data/module-1/capstone/        Integrated case-study data
```

Sections without standalone files use repository-native Mermaid diagrams or Markdown tables within their topic pages.

## Adding a diagram or process flow

1. Decide whether Mermaid, SVG, or a Markdown table communicates the relationship most clearly.
2. Name standalone assets with lower-case kebab case, such as `supplier-risk-response-flow.svg`.
3. Place the asset under `diagrams/module-N/section-x/` and link it with a relative path.
4. Add meaningful alternative text and a short explanation in the learning page.
5. Explain its instructional purpose on the page where it is used.
6. Confirm that the design is original and satisfies [`../ATTRIBUTION.md`](../ATTRIBUTION.md).

## Mermaid process-flow placeholder

Copy and replace the labels; do not retain a node that adds no instructional value.

```mermaid
flowchart TD
    A[Trigger or input] --> B[Decision or transformation]
    B --> C{Decision criterion}
    C -->|Option 1| D[Outcome 1]
    C -->|Option 2| E[Outcome 2]
```

## SVG placeholder requirements

An original SVG should include a descriptive `<title>`, a useful `<desc>`, readable text, a `viewBox`, and no embedded raster image or external script. Keep the source editable and avoid copying the composition of a third-party diagram.

## Dataset requirements

- Use fictional entities and non-confidential values.
- Include a header row and consistent columns.
- State units, time periods, assumptions, and whether values are illustrative.
- Link the dataset from the page that explains its learning purpose.
