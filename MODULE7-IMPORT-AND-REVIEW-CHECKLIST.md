# Module 7 — Supply Chain Risk: draft release review gate

> **DRAFT ONLY — NOT MERGEABLE.** This review branch was opened to prepare the Module 7 integration gate against v6.0.1. The 111-file reviewed Module 7 release-candidate overlay is held as a separately verified artifact in the ChatGPT project workspace and **is not yet committed to this branch**. No claim of a complete Module 7 PR or GitHub CI pass should be made until imported and checked.

## Integration baseline

- Base: `main`, commit `2e471355ccc7c96dd13eae2ffc26738cd98e87a4` (v6.0.1).
- Folder: `07-supply-chain-risk/`, with Sections A (12 lessons), B (19 lessons), two section reviews, full Stonebridge capstone and solution.
- New companion directories: `assets/data/module-7/` (32 CSV datasets), `assets/diagrams/module-7/` (33 SVGs), `calculations/risk-response/` (replay and reference).
- Independent learning assessments: 72 answer rationale blocks; source question-bank overlap was screened on 60 extracted new question stems, without a high-similarity match.
- Release-candidate file count: 111, including two validator/integration scripts.
- Reviewed archive SHA-256: `9c4eae948449d4a13e66c7965ec15b80f45479203b78da2123d7b4bd8804133c` (verify bytes after transfer).

## Import steps (must be completed before code review)

1. Import all 111 reviewed files at exact paths in the verified release-candidate overlay, preserving source file bytes and the package's directory structure. Do not commit any APICS PDFs, presentations, flashcards, proprietary questions, contact-sheet output, or private audit working files.
2. Run `python3 scripts/activate_module7_release.py` once on a full checkout; it refuses to run without the complete Modules 1–6 baseline and the Module 7 capstone. This wires the existing shared validator, cross-module overviews, glossary, learning paths, roadmap and repository counts.
3. Run `python3 calculations/risk-response/capstone_replay.py`, `python3 scripts/validate_module7.py`, and `python3 scripts/validate_repository.py`. The last check must validate **all seven modules** in the same working tree.
4. Verify that no substantive changes were made to the 330 Modules 1–6 learning/reference pages. Overview navigation and global indexes may be adjusted only as specified by the integration patch.
5. Check all 33 SVGs at 640 and 1280 widths and inspect GitHub's actual rendered Markdown, SVGs and Mermaid diagrams. The local visual preview is not GitHub browser proof.
6. Review changed-file inventory, legal/attribution controls, originality, link targets, capstone arithmetic, and new/reused glossary terminology.
7. Keep the PR in draft and **unmerged** until all tests, required reviews and the GitHub Actions workflow pass.

## Corrections already made in the local reviewed overlay

- Added accessibility metadata to 17 Section B SVGs.
- Replaced one repeated Section B disclaimer paragraph across lessons with topic-specific wording.
- Linked three orphaned datasets from their teaching lessons.
- Reconciled the degraded-hardening scenario with its stated 10% security gate.
- Aligned the capstone assignment's process flow, question rationale blocks and solution headings with the established shared release contract.

## Hard stops

- An empty or partial Module 7 folder cannot be called a completed release.
- Passing link/CSV/XML checks alone does not prove visual or editorial quality.
- No model-probability scores may silently override mandatory safety, security, quality, funding or physical-carrier gates.
- Do not merge before the complete 111-file overlay and full-validator/CI evidence are present.
