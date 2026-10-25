# Module 8 — Published v8.0.0 Integration and Release Audit

**Repository:** [theleanx/SupplyChain-Design-Notes](https://github.com/theleanx/SupplyChain-Design-Notes)  
**Development branch:** `feature/module-8-optimization-sustainability-technology` (merged into `main` through PR #17)  
**Merged PR:** [#17](https://github.com/theleanx/SupplyChain-Design-Notes/pull/17) — merge commit [`fdeaf54`](https://github.com/theleanx/SupplyChain-Design-Notes/commit/fdeaf54a351a94a5561572529b53495141c7ccf3)  
**Most recent validated content commit before owner-review record:** [GitHub Actions run #39807192677](https://github.com/theleanx/SupplyChain-Design-Notes/actions/runs/39807192677) (commit `30c1cbd30edaddad40424f75cb9195841863b91c`)  
**Release disposition 2026-10-25:** The owner reviewed all 45 visuals and the editorial content without reported issues, waived an external independent-review requirement, explicitly authorized merging PR #17 (completed at `fdeaf54`), and subsequently authorized the `v8.0.0` metadata/tag/release. The shared Modules 1–8 validation succeeded after merge ([run 40233275974](https://github.com/theleanx/SupplyChain-Design-Notes/actions/runs/40233275974)). This is owner-reviewed educational content, not outside certification. [Release v8.0.0](https://github.com/theleanx/SupplyChain-Design-Notes/releases/tag/v8.0.0).

## 1. Scope and baseline preservation

The previously released seven modules were checked against `main` in the GitHub pull-request comparison. **No files under the original `01-` through `07-` module directories are modified by PR #17.** The protected pre-merge baseline was `dbd5890edb7a20480f3007ce402f9f79406cbab7`; the merge was `fdeaf54a351a94a5561572529b53495141c7ccf3`. PR #17 touched only Module 8 content/assets/scripts and shared navigation/quality tooling, not any original Modules 1–7 lesson files. This v8.0.0 metadata commit updates the published version, citation and release manifest after separate authorization.

The shared [repository validator](./scripts/validate_repository.py) now checks Module 8 as a **42-topic released module** and the complete eight-module inventory, while retaining the exact old seven-module inventory and substantive quality expectations independently. The CI workflow calls this **one shared validator**; Section A/B/C/capstone and SVG-source checks are invoked from it, not redundantly as four separate CI workflow steps.

## 2. Audited Module 8 development inventory

| Artifact | Section A | Section B | Section C | Capstone | Module total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original topic lessons | 12 | 12 | 18 | — | **42** |
| Independent section review cases | 12 | 12 | 18 | — | **42** |
| Original SVG diagrams | 12 | 12 | 18 | 3 | **45** |
| Original fictional CSV datasets | 11 | 12 | 18 | 6 | **47** |
| Student-facing capstone self-check cases | — | — | — | 5 | **5** |

Module 8 includes **54 structured Markdown learning/reference pages** within its module directory, which comprise 42 lessons plus 12 module/section overview, reference, review and capstone pages. The capstone contains a separate integrated assignment, fully worked solution, owners/actions, sensitivity, and an independent calculation replay.

Across Module 8 the automated checks count **89 answered assessment blocks**: 42 one-per-lesson checks, 42 section-review answers, and five capstone self-checks. These are independently authored **educational** questions; they are not proprietary APICS certification items.

## 3. End-to-end source, arithmetic and gate validation

- [x] Original [Section A](./08-optimization-sustainability-technology/section-a-optimizing-supply-chain-strategy-and-tactics/README.md): strategy, network/constraints, economic measures, calculations and review quality gates.
- [x] Original [Section B](./08-optimization-sustainability-technology/section-b-sustainability/README.md): triple bottom line; economic/environment/social duties; supplier and legal controls; scope-bounded reporting; official standard/edition source notes.
- [x] Original [Section C](./08-optimization-sustainability-technology/section-c-technology-trends/README.md): cloud, AI, sensing, emerging automation, IoT/digital twins, blockchain, selection, project delivery, change and ongoing maintenance.
- [x] [AlderGate integrated assignment](./08-optimization-sustainability-technology/capstone/README.md): every source dataset directly linked, eight tasks, five original decision checks, an actual Mermaid sequence and a hard-gate-first decision.
- [x] [Worked solution](./08-optimization-sustainability-technology/capstone/solution-guide.md): completed network and sustainability tables, vendor screening, financial ledger, NPV, break-even, adoption and cutover findings, stress, owners, implementation and evaluation rubric.
- [x] [Independent replay](./calculations/module8-capstone/replay.py): source-driven calculations for network capacity and annual cost; energy/outbound t CO₂e; two-site weighted recycling; eligible vendors, independent cost budgets, distinct process populations, NPV and payback; stress; requirements and owner actions.
- [x] Explicitly distinguish model assumptions from observed outcomes; **cash avoidability and actual emissions remain unverified in the fictional case**. A positive modeled NPV is *not* a permission to waive critical production/safety/security requirements.
- [x] Preserve cross-module conceptual ownership: Module 1 demand, 2 network/data architecture, 3 supplier/contract, 4 manufacturing/inventory, 5 freight/reverse flows, 6 partner relationships and 7 risk/continuity. Module 8 integrates the choices without treating unrelated prior-module synthetic data as one real business population.

**Reference correctness rule:** course taxonomy comes from the privately supplied 2026 Module 8 source. Public authoritative supplemental standards are linked in [Section B references](./08-optimization-sustainability-technology/section-b-sustainability/REFERENCES.md) and [Section C references](./08-optimization-sustainability-technology/section-c-technology-trends/REFERENCES.md). Real applicability, jurisdiction, standard edition and a supplier's certification scope require separately dated evidence.

## 4. Whole-repository validation — passing result

**GitHub Actions #39806691865 (2026-10-22):** The unified Python validation completed with:

| Automated check | Result |
| --- | --- |
| All published Modules 1–7 lesson/overview/calculation/capstone/asset gates | **PASS** |
| Module 8 Sections A/B/C individual lessons and assessment checks | **PASS** |
| Module 8 integrated AlderGate capstone and all quantitative replays | **PASS** |
| Single repository-wide Markdown/link checks | **PASS** |
| SVG/CSV structural and accessibility checks | **PASS** |
| Module 8 visual source audit (metadata, topic metrics, approximate text bounds, shape diversity) | **PASS** |
| Shared release inventory preservation | **PASS** |

The checked PR snapshot included **481 Markdown files**, **3,426 internal links**, **295 SVG files**, and **148 CSV files**. These are total repository counts at run #39806691865, not only Module 8 learning files. Future README/review-file changes may increment Markdown and link counts without changing the locked Module 8 lesson/diagram/data inventories.

The improved Module 8 diagrams have at least **6** structural arrangements in Section A, **8** in Section B, **10** in Section C and **3** in the capstone. Earlier topic-generic Section A and C diagrams were replaced with original case-data charts and decision graphics. The source audit is a heuristic; it does not establish exact on-screen legibility.

## 5. Copyright, originality and source boundaries

- [x] Public repository tree does **not** include uploaded APICS/ASCM course PDFs, slide decks, term cards or the proprietary question bank.
- [x] Module 8 cases, spreadsheet-style CSV inputs, diagrams and knowledge checks are fictional and independently authored in this project. The repository validator screens exact repeated long explanatory paragraphs across lessons.
- [x] Retain source/edition and public reference registers; historic curriculum language must be separated from currently applicable regulations.
- [x] **Owner editorial review on 2026-10-22:** owner reported reviewing Module 8 content and finding no issues or comments. This is owner self-attestation, not a separate independent assessment.
- [x] **Owner waived separate independent editorial/originality review (2026-10-25).** The owner-approved release process relies on the completed owner content review and automated checks. No independent professional plagiarism, legal, or standards-compliance certification is claimed or implied; copyright and accuracy responsibilities remain applicable.

## 6. GitHub rendering and actual visual sign-off

- [x] Markdown lesson/resource destinations and relative image links verified at repository-wide scale.
- [x] GitHub repository **blob/lesson content is retrievable** for the actual feature-branch paths.
- [x] [Actual GitHub visual review gallery](./MODULE8-VISUAL-REVIEW.md) provides every committed Module 8 SVG at a 720-pixel wide and a 320-pixel narrow embedded review size.
- [x] All 45 original SVG source files pass structural, accessibility, text-bound heuristic and visual-diversity automated checks.
- [x] **Owner visual review on 2026-10-22:** owner reports reviewing all 45 diagrams, with no issues or fixes requested, following the wide/narrow review instructions. The self-report is accepted as owner visual sign-off, not an independent raster verification.
- [x] **Additional outside browser/reviewer inspection not required by owner (2026-10-25).** Owner accepted the 45-diagram and editorial inspection plus existing automated Markdown/Mermaid/asset checks. Exact real-browser interaction beyond this evidence is not separately attested; this is a disclosed verification limit, not a release blocker.
- [x] No defects reported in the owner's visual/editorial review. Any future discovered defect must still be corrected and validated before claiming its resolution.

## 7. Owner approval, merge and v8.0.0 publication

- [x] Owner visual and editorial acceptance (all 45 diagrams, no issues reported).
- [x] Owner waived the separate external review as a *project* gate; no independent certification is claimed.
- [x] Shared Module 1–8 check passed on the reviewed PR head and again on merged `main`, including Sections A/B/C and AlderGate scenario replay.
- [x] Owner authorized and completed merge of [PR #17](https://github.com/theleanx/SupplyChain-Design-Notes/pull/17) at commit [`fdeaf54`](https://github.com/theleanx/SupplyChain-Design-Notes/commit/fdeaf54a351a94a5561572529b53495141c7ccf3).
- [x] Owner separately authorized publishing the `v8.0.0` version metadata and GitHub release on 2026-10-25.
- [x] [Versioned GitHub release](https://github.com/theleanx/SupplyChain-Design-Notes/releases/tag/v8.0.0) and the committed [manifest](./.github/releases/v8.0.0.md) identify the published baseline.

**Final scope:** The release contains original educational material, with fictional examples and modeled outcomes. A passing automated validator and owner sign-off are not regulatory, legal, plagiarism, or professional standards certification. Subsequent changes must pass the established quality pipeline.
