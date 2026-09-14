# Content Quality Standard

Every learning section should be accurate, practical, navigable, and independently authored.

## Required elements

- Clear concept explanation in plain language
- Business relevance and decision logic
- Original visual, structured table, or process flow where useful
- Realistic fictional example
- Worked calculation when the topic is quantitative
- Trade-offs and common points of confusion
- Original knowledge-check question
- Related-concept navigation
- Clear assumptions, units, and decision implications

## Verification

Before publication, confirm that:

- relative links resolve;
- diagrams render and SVG files parse;
- CSV files contain headers and consistent columns;
- formulas, assumptions, units, and illustrative values are clearly labeled;
- fictional examples contain no confidential client information;
- prose, questions, diagrams, and datasets are original or properly licensed; and
- the section follows the repository structure and naming conventions;
- no source-working files, drafting notes, or source-identifying metadata entered the public tree;
- quantitative examples have been recalculated independently; and
- the complete repository passes a final content-policy and terminology scan.

Run the repository checks locally with:

```bash
python3 scripts/validate_repository.py
```

The same checks run automatically for every push and pull request.

## Release standard

A module is released only when its public content is complete. Empty module shells, internal research records, comparison notes, source files, and unfinished drafting artifacts do not belong on the default branch. Release review covers content completeness, visual rendering, calculations, navigation, terminology, and originality.
