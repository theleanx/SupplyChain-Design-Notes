# Contributing

Thank you for helping improve these learning notes. Contributions are welcome when they preserve the repository's instructional quality and copyright-safe design.

## Contribution workflow

1. Open an issue describing the learning gap, correction, or proposed module topic.
2. Create a focused branch and use [`_templates/topic-template.md`](./_templates/topic-template.md).
3. Add original explanatory content, a realistic example, and a visual or process-flow treatment where it improves understanding.
4. Update navigation and the appropriate coverage register.
5. Run the checks below and open a pull request explaining the instructional change and its sources.

## Required checks

- All relative Markdown links resolve.
- SVG files are valid XML and contain no embedded third-party images.
- Markdown fences are balanced and Mermaid diagrams render on GitHub.
- CSV files have a header and consistent column counts.
- No confidential, proprietary, or unlicensed third-party material is included.
- New prose, examples, questions, diagrams, and datasets satisfy [`ATTRIBUTION.md`](./ATTRIBUTION.md).

## Writing and visual conventions

- Write for practitioners first: define the concept, show the decision, then explain the trade-off.
- Use descriptive file names in lower-case kebab case.
- Prefer Mermaid for process logic and SVG for charts or layouts requiring controlled presentation.
- Keep SVGs editable and accessible; add a descriptive title and useful alternative text.
- Use fictional organization names and avoid confidential client data.
- Label estimates and illustrative values clearly.

## Pull-request checklist

- [ ] I authored the contribution independently.
- [ ] I did not reproduce restricted or proprietary materials.
- [ ] I documented all required citations and third-party licenses.
- [ ] I verified links, visuals, data files, and navigation.
- [ ] I updated the appropriate audit or coverage record.

By contributing, you confirm that you have the right to submit the material and grant the repository owner permission to publish it under the applicable terms in [`LICENSE.md`](./LICENSE.md).
