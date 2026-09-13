# Attribution and Copyright-Safe Authoring Guide

This guide governs all public contributions to this repository. It is a practical editorial standard, not legal advice.

## Safe contribution standard

Contributions should add independently expressed knowledge. A contributor may learn from legitimate sources, but the resulting explanation, example, question, table, and visual must be newly authored.

### Acceptable

- Explain a generally recognized supply-chain concept in original language.
- Cite a reliable source for a fact, standard, framework, or definition that requires attribution.
- Create a new scenario with fictional organizations, independently selected values, and a distinct narrative.
- Design a diagram from the underlying concept using a new layout, labels, hierarchy, and visual treatment.
- Quote a short passage only when necessary, clearly mark it as a quotation, and cite the source.
- Link readers to official or authoritative material instead of reproducing it.

### Not acceptable

- Copying or lightly paraphrasing books, articles, training materials, assessments, or answer explanations.
- Recoloring, tracing, redrawing, or rearranging a proprietary figure while retaining its protected expression.
- Reproducing screenshots, page images, branded tables, or paywalled content.
- Publishing reconstructed knowledge-check questions, distinctive distractors, or material obtained under confidentiality terms.
- Assuming that educational intent, a citation, or a disclaimer automatically makes copying permissible.

## Attribution format

For an external factual or conceptual source, add a short source note near the relevant section or under a `Sources and further reading` heading:

```markdown
## Sources and further reading

- Organization or Author, *Title*, edition or date, direct URL.
```

Prefer primary and authoritative sources. Links should point to the source itself, not a search-results page. Record the edition or access date when the material changes over time.

## Visuals and datasets

Every contributed visual or dataset must be created for this repository, contributed by its rights holder under compatible terms, or accompanied by documented third-party permission and attribution.

For third-party assets, add a neighboring `SOURCE.md` file containing the creator, title, source URL, license, modifications, and access date. When licensing is unclear, do not commit the asset.

## Before opening a pull request

- Confirm that the prose is independently written.
- Confirm that examples and numeric values are independently constructed.
- Confirm that questions and distractors are original.
- Confirm that all local links work and all SVG files parse.
- Identify every third-party element and document its permission or license.
- Remove confidential working files and any artifact containing protected third-party expression.
