# Content Quality Standard

Every learning section should be accurate, practical, navigable, and independently authored.

## Required elements

- Clear concept explanation in plain language
- Business relevance and decision logic
- Original visual, structured table, or process flow where useful
- A visual model suited to the topic; one generic layout must not be repeated across unrelated concepts
- Realistic fictional example
- Worked calculation when the topic is quantitative
- Trade-offs and common points of confusion
- Original knowledge-check question
- Related-concept navigation
- Clear assumptions, units, and decision implications
- Topic-specific explanation rather than reusable filler or repeated stock advice
- A decision artifact: evidence table, calculation, matrix, checklist, or control record that a practitioner could use

## Verification

Before publication, confirm that:

- relative links resolve;
- diagrams render at both full-page and narrow-page widths with no clipped, overlapping, or unreadable labels;
- visual review uses a rasterized preview of the final SVG—not XML validity alone;
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

Automated checks are necessary but not sufficient. A reviewer must inspect the rendered learning pages and visual-contact sheet before publication. A passing workflow must never be described as proof of visual or editorial quality by itself.

## Release standard

A module is released only when its public content is complete. Empty module shells, internal research records, comparison notes, source files, and unfinished drafting artifacts do not belong on the default branch. Release review covers content completeness, rendered visuals at multiple widths, calculations, navigation, terminology, originality, repeated-language review, and a manual read of every lesson.
