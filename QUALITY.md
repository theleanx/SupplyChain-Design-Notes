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

## Shared lesson contract

The same minimum contract applies to every published module. Presentation may vary by
topic, but a release cannot rely on a stronger standard for only the newest module.

Every topic must contain:

- learning objectives, a plain-language concept, and explicit business relevance;
- decision logic, evidence requirements, trade-offs, common confusion, and failure modes;
- a topic-appropriate original visual; process-oriented topics also need an operational
  flow showing sequence, gates, loops, or escalation;
- a fictional applied example and a usable decision artifact or reproducible calculation;
- one original knowledge check with the correct answer, why it is correct, and why the
  alternatives fail;
- a practitioner perspective, linked related concepts, and sequential navigation; and
- at least 500 words of topic-specific learning content, excluding reusable navigation.

The visual rule is deliberately **appropriate, not identical**: a conceptual topic does
not need a decorative process flow, and a process topic cannot substitute a conceptual
picture for its operating sequence.

## Shared capstone contract

Each module must end with one integrated fictional decision that connects all sections.
The assignment links every required dataset directly and states the horizon, units,
assumptions, outputs, and decision checks. The solution must perform—not merely request—
the calculations, populate the core decision artifacts, apply gates before ranking,
show a sensitivity or failure case, and provide owners and implementation triggers.

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
- quantitative lessons link their source dataset directly and use explicit units and horizons;
- process-flow blocks contain the actual decision sequence and are not substituted by a conceptual image;
- mandatory gates are applied before weighted ranking;
- assessment distractors are plausible misconceptions rather than joke or absolute answers;
- capstone solutions show reproducible calculations, decision artifacts, controls, and implementation gates; and
- one shared validator applies the lesson, assessment, navigation, dataset, capstone,
  and asset gates to every completed module;
- the complete repository passes a final content-policy and terminology scan.

Run the repository checks locally with:

```bash
python3 scripts/validate_repository.py
```

The same checks run automatically for every push and pull request.

Automated checks are necessary but not sufficient. A reviewer must inspect the rendered learning pages and visual-contact sheet before publication. A passing workflow must never be described as proof of visual or editorial quality by itself.

## Release standard

A module is released only when its public content is complete. Empty module shells, internal research records, comparison notes, source files, and unfinished drafting artifacts do not belong on the default branch. Release review covers content completeness, rendered visuals at multiple widths, calculations, navigation, terminology, originality, repeated-language review, and a manual read of every lesson.
