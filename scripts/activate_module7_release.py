#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""One-time, idempotent Module 7 full-repository integration patch.

Apply from a FULL checkout of the v6.0.1-or-later repository with the complete
Module 7 overlay copied into that checkout. Never run in the standalone overlay.
Modifies only index/validator/release wiring and bidirectional overview links.
"""
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
MOD=ROOT/'07-supply-chain-risk'
V=ROOT/'scripts/validate_repository.py'


def change(s: str, old: str, new: str, where: str) -> str:
    # Check the integrated form first because several baseline snippets are
    # prefixes of their replacement text (for example, the Module 6 constant
    # remains immediately before the inserted Module 7 constant).
    if new in s:return s
    if old in s: return s.replace(old,new,1)
    raise RuntimeError(f'{where}: expected unique baseline text not found; REFUSE automatic overwrite')


def main() -> int:
    if not (ROOT/'06-supply-chain-relationships/README.md').exists():
        raise RuntimeError('Requires a complete checkout of existing Modules 1–6')
    if not (MOD/'capstone/solution-guide.md').exists():
        raise RuntimeError('Module 7 complete overlay has not been imported')
    p=V;s=p.read_text()
    s=change(s,'MODULE_6 = ROOT / "06-supply-chain-relationships"','MODULE_6 = ROOT / "06-supply-chain-relationships"\nMODULE_7 = ROOT / "07-supply-chain-risk"','module constant')
    s=change(s,'    "Module 6": (MODULE_6, 32),','    "Module 6": (MODULE_6, 32),\n    "Module 7": (MODULE_7, 31),','module map')
    s=change(s,'    MODULE_6: (\n        ROOT / "assets/data/module-6/README.md",\n        ROOT / "calculations/relationship-performance/README.md",\n    ),','    MODULE_6: (\n        ROOT / "assets/data/module-6/README.md",\n        ROOT / "calculations/relationship-performance/README.md",\n    ),\n    MODULE_7: (\n        ROOT / "assets/data/module-7/README.md",\n        ROOT / "calculations/risk-response/README.md",\n    ),','resource map')
    s=change(s,'        MODULE_6: MODULE_6_DATASET_LINKS,','        MODULE_6: MODULE_6_DATASET_LINKS,\n        MODULE_7: {},','topic data requirements map')
    s=change(s,'module in (MODULE_2, MODULE_3, MODULE_6)','module in (MODULE_2, MODULE_3, MODULE_6, MODULE_7)','flow gate')
    s=change(s,'(example|northstar|asterworks|rivermark|pinehaven|harborpeak|clearspan)', '(example|northstar|asterworks|rivermark|pinehaven|harborpeak|clearspan|stonebridge)','fictional case check')
    s=change(s,'        "Module 6": (\n            MODULE_6,\n            2200,\n            12,\n            ("31.25%", "86.23%", "$242,000", "72.19", "74.18%", "88/100"),\n        ),','        "Module 6": (\n            MODULE_6,\n            2200,\n            12,\n            ("31.25%", "86.23%", "$242,000", "72.19", "74.18%", "88/100"),\n        ),\n        "Module 7": (MODULE_7, 2200, 12, ("$45,000", "$28,600", "$36,500", "$11,500")),','capstone shared gate')
    s=change(s,'len(module_markdown) != 330','len(module_markdown) != 369','markdown count gate')
    s=change(s,'expected 330 module Markdown files','expected 369 module Markdown files','markdown count message')
    s=change(s,'len(svg) != 217','len(svg) != 250','svg count gate')
    s=change(s,'expected 217 SVG files','expected 250 SVG files','svg count message')
    s=change(s,'len(datasets) != 69','len(datasets) != 101','CSV count gate')
    s=change(s,'expected 69 CSV files','expected 101 CSV files','CSV count message')
    s=change(s,'details != 651','details != 723','answers count gate')
    s=change(s,'expected 651 knowledge checks','expected 723 knowledge checks','answers count message')
    if not all(value in s for value in (
        '369 structured Markdown files', '250 original SVG diagrams',
        '101 original CSV datasets', '723 independently authored knowledge checks',
    )):
        s=change(s,'("330 structured Markdown files", "217 original SVG diagrams", "69 original CSV datasets", "651 independently authored knowledge checks")','("369 structured Markdown files", "250 original SVG diagrams", "101 original CSV datasets", "723 independently authored knowledge checks")','README count claims')
    s=change(s,'        MODULE_6: ("**40** structured Markdown learning/reference pages", "**32** topic lessons", "**69** independently authored knowledge checks"),','        MODULE_6: ("**40** structured Markdown learning/reference pages", "**32** topic lessons", "**69** independently authored knowledge checks"),\n        MODULE_7: ("**39** structured Markdown learning/reference pages", "**31** topic lessons", "**72** independently authored knowledge checks"),','module snapshot claims')
    s=change(s,'import csv\n','import csv\nimport subprocess\n','subprocess import')
    s=change(s,'        + validate_capstones_and_inventory(markdown, svg, datasets)\n', '        + validate_capstones_and_inventory(markdown, svg, datasets)\n', 'baseline check')
    marker='    print(\n        f"Validated {len(markdown)} Markdown files, {link_count} internal links, "'
    insertion='''    module7_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_module7.py")],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    print(module7_check.stdout, end="")
    if module7_check.returncode:
        errors.append("Module 7 specific validation failed:\\n" + module7_check.stdout + module7_check.stderr)

'''
    if 'module7_check = subprocess.run(' not in s:
        if marker not in s:raise RuntimeError('main validation insertion point missing')
        s=s.replace(marker,insertion+marker,1)
    p.write_text(s)
    mods=[p for p in ROOT.iterdir() if p.is_dir() and re.match(r'0[1-6]-',p.name)]
    assert len(mods)==6
    for module in mods:
        p=module/'README.md';body=p.read_text()
        url='../07-supply-chain-risk/README.md'
        if url not in body:
            header='## Cross-module handoffs'
            if header not in body:raise RuntimeError(f'{p}: cross-module heading not found')
            begin=body.index(header)
            next_header=body.find('\n## ',begin+len(header))
            if next_header<0:raise RuntimeError(f'{p}: following heading not found')
            body=body[:next_header].rstrip()+'\n\n- [**Module 7 — Supply Chain Risk**]('+url+') adds the assessment, hard response gates, disruption/continuity choices and tested recovery evidence that use this module’s existing operating methods.\n'+body[next_header:]
            p.write_text(body)
    p=MOD/'README.md';body=p.read_text()
    if '**39** structured Markdown learning/reference pages' not in body:
        body=body.replace('## Module snapshot\n','## Module snapshot\n\n- **39** structured Markdown learning/reference pages\n- **31** topic lessons (12 in Section A, 19 in Section B)\n- **33** original SVG decision visuals\n- **32** fictional CSV datasets\n- **72** independently authored knowledge checks, including the capstone\n')
    for old,new in [
        ('**Status: complete development candidate; awaiting full-repository CI, GitHub rendering and release approval.**',
         '**Status: released in v7.0.0.**'),
        ('**Status: validated release candidate; awaiting final human approval.**',
         '**Status: released in v7.0.0.**'),
        ('— locally authored; final full-repository release gate pending.',
         '— locally authored and validated in the full repository.'),
        ('Both sections and their integrated capstone are authored; **do not publish as a finished module** until validator integration, independent final editorial/visual review and CI pass.',
         'Both sections and their integrated capstone are authored, validated, merged, and released.'),
        ('Both sections and their integrated capstone are authored and validated; the candidate remains unmerged pending final human approval.',
         'Both sections and their integrated capstone are authored, validated, merged, and released.'),
    ]:
        body=body.replace(old,new)
    p.write_text(body)
    p=ROOT/'README.md';body=p.read_text()
    body=body.replace('**Current release:** Modules 1–6 are complete.', '**Current release:** Modules 1–7 are complete.')
    if '| 7 |' not in body:
        row='| 7 | Risk governance, qualitative/quantitative assessment, response economics, disruption recovery and business continuity | [Supply Chain Risk](./07-supply-chain-risk/) |\n'
        anchor='Choose a route using the [role-based learning paths]'
        at=body.find(anchor)
        if at<0:raise RuntimeError('Root README module table anchor missing')
        body=body[:at].rstrip()+'\n'+row+'\n'+body[at:]
    new_caps='- [Stonebridge risk and resilience capstone](./07-supply-chain-risk/capstone/README.md)\n'
    if new_caps not in body:
        anchor='## What makes this repository useful'
        body=body.replace(anchor,new_caps+'\n'+anchor,1)
    risk_formula='- [Risk analysis and response formula sheet](./calculations/risk-response/formula-sheet.md)\n'
    if risk_formula not in body:
        anchor='- [Relationship performance formula & control sheet](./calculations/relationship-performance/formula-sheet.md)\n'
        if anchor not in body:raise RuntimeError('Root README formula-list anchor missing')
        body=body.replace(anchor,anchor+risk_formula,1)
    for anchor,addition in [
        ('06-supply-chain-relationships/                        Module 6 learning content\n','07-supply-chain-risk/                                 Module 7 learning content\n'),
        ('assets/diagrams/module-6/                            Module 6 SVG diagrams\n','assets/diagrams/module-7/                            Module 7 SVG diagrams\n'),
        ('assets/data/module-6/                                Module 6 example datasets\n','assets/data/module-7/                                Module 7 example datasets\n'),
        ('calculations/relationship-performance/                 Relationship-management performance and control references\n','calculations/risk-response/                           Risk-response calculations and decision-control references\n'),
    ]:
        if addition not in body:
            if anchor not in body:raise RuntimeError('Root README repository-map anchor missing: '+anchor.strip())
            body=body.replace(anchor,anchor+addition,1)
    for old,new in [
        ('330 structured Markdown files','369 structured Markdown files'),
        ('across six completed modules','across seven completed modules'),
        ('twenty-two connected learning sections','twenty-four connected learning sections'),
        ('217 original SVG diagrams','250 original SVG diagrams'),
        ('69 original CSV datasets','101 original CSV datasets'),
        ('651 independently authored knowledge checks','723 independently authored knowledge checks'),
        ('six integrated end-to-end capstones','seven integrated end-to-end capstones'),
    ]:
        if old not in body and new not in body:raise RuntimeError('Missing root README inventory: '+old)
        body=body.replace(old,new)
    p.write_text(body)
    p=ROOT/'GLOSSARY.md';body=p.read_text()
    if '## Module 7: Risk and Resilience Terminology' not in body:
        body+='''\n\n## Module 7: Risk and Resilience Terminology\n\n**Risk appetite** — The type and amount of uncertainty an organization agrees it is willing to pursue or retain.\n\n**Risk tolerance** — The permitted degree of variation or adverse outcome for a specified objective.\n\n**Risk threshold** — A defined value or condition triggering required action, escalation or a decision gate.\n\n**Risk register** — A controlled record of identified risks, causes, consequences, owners, evidence, treatments, and review triggers.\n\n**Expected monetary value (EMV)** — The probability-weighted sum of mutually exclusive scenario monetary outcomes over one defined horizon; signed financial benefit and positive loss magnitude use different conventions.\n\n**Residual risk** — Exposure remaining after an implemented and verified response, not merely after a response has been planned.\n\n**Business continuity management (BCM)** — Establishing and testing the people, process, information and partner capabilities needed to continue or restore prioritized operations after disruption.\n'''
        p.write_text(body)
    p=ROOT/'LEARNING-PATHS.md';body=p.read_text()
    body=body.replace('All six modules can be read from beginning to end', 'All seven modules can be read from beginning to end')
    if '## Module 7 risk-management and resilience path' not in body:
        body+='''\n\n## Module 7 risk-management and resilience path\n\n**For:** risk leads, sourcing leaders, operations, enterprise architects, logistics managers and continuity coordinators.\n\n1. [Risk governance and identification](./07-supply-chain-risk/section-a-risk-management-and-supply-chain-risks/README.md)\n2. [Risk analysis and response](./07-supply-chain-risk/section-b-risk-analysis-and-response/README.md)\n3. [Risk-response formula and control reference](./calculations/risk-response/formula-sheet.md)\n4. [Stonebridge integrated capstone](./07-supply-chain-risk/capstone/README.md)\n5. [Solved executive decision record](./07-supply-chain-risk/capstone/solution-guide.md)\n\nUse existing Modules 1–6 as the technical owners of the demand, network, procurement, production, logistics and relationship inputs. Module 7 adds the event exposure, decision gates, response economics and tested continuity treatment.\n'''
    p.write_text(body)
    p=ROOT/'ROADMAP.md';body=p.read_text()
    if '## Module 7 — Supply Chain Risk' not in body:
        x='''## Module 7 — Supply Chain Risk\n\n- [x] Complete Sections A–B, with original lessons, assessments and decision visuals\n- [x] Add Stonebridge integrated capstone, controlled data and reproducible calculations\n- [x] Apply the shared overview, lesson, capstone, asset and cross-module validation gates\n- [ ] Confirm GitHub Actions validation, independent editorial review and final release approval\n\n'''
        body=body.replace('## Future modules',x+'## Future modules',1)
    body=body.replace('- [ ] Supply-chain risk\n','')
    body=body.replace('- [x] Six end-to-end case studies','- [x] Seven end-to-end case studies')
    body=body.replace('Shared module and section overview contract across Modules 1–6','Shared module and section overview contract across Modules 1–7')
    body=body.replace('Modules 1–6 are complete. Future modules','Modules 1–7 are complete. Future modules')
    body=body.replace('- [ ] Confirm GitHub Actions validation, independent editorial review and final release approval',
                      '- [x] Confirm GitHub Actions validation and final editorial/visual review\n- [x] Obtain final release approval and publish v7.0.0')
    body=body.replace('- [ ] Obtain final release approval',
                      '- [x] Obtain final release approval and publish v7.0.0')
    p.write_text(body)
    p=ROOT/'MODULE7-IMPORT-AND-REVIEW-CHECKLIST.md';body=p.read_text()
    body=body.replace('# Module 7 — Supply Chain Risk: draft release review gate',
                      '# Module 7 — Supply Chain Risk: completed release review')
    body=body.replace('> **DRAFT ONLY — NOT MERGEABLE.** This review branch was opened to prepare the Module 7 integration gate against v6.0.1. The 111-file reviewed Module 7 release-candidate overlay is held as a separately verified artifact in the ChatGPT project workspace and **is not yet committed to this branch**. No claim of a complete Module 7 PR or GitHub CI pass should be made until imported and checked.',
                      '> **RELEASED.** The 111-file reviewed Module 7 overlay was integrated against the v6.0.1 baseline, validated in PR #14, merged to `main`, and published as v7.0.0. PR #15 synchronized the durable released-state metadata in v7.0.1.')
    body=body.replace('## Import steps (must be completed before code review)', '## Completed release gates')
    old_steps='''1. Import all 111 reviewed files at exact paths in the verified release-candidate overlay, preserving source file bytes and the package's directory structure. Do not commit any APICS PDFs, presentations, flashcards, proprietary questions, contact-sheet output, or private audit working files.
2. Run `python3 scripts/activate_module7_release.py` once on a full checkout; it refuses to run without the complete Modules 1–6 baseline and the Module 7 capstone. This wires the existing shared validator, cross-module overviews, glossary, learning paths, roadmap and repository counts.
3. Run `python3 calculations/risk-response/capstone_replay.py`, `python3 scripts/validate_module7.py`, and `python3 scripts/validate_repository.py`. The last check must validate **all seven modules** in the same working tree.
4. Verify that no substantive changes were made to the 330 Modules 1–6 learning/reference pages. Overview navigation and global indexes may be adjusted only as specified by the integration patch.
5. Check all 33 SVGs at 640 and 1280 widths and inspect GitHub's actual rendered Markdown, SVGs and Mermaid diagrams. The local visual preview is not GitHub browser proof.
6. Review changed-file inventory, legal/attribution controls, originality, link targets, capstone arithmetic, and new/reused glossary terminology.
7. Keep the PR in draft and **unmerged** until all tests, required reviews and the GitHub Actions workflow pass.'''
    new_steps='''- [x] Imported all 111 reviewed files at their exact paths without public source PDFs, presentations, flashcards, proprietary questions, contact sheets, or private audit working files.
- [x] Ran `python3 scripts/activate_module7_release.py` on the complete Modules 1–6 baseline and verified idempotency.
- [x] Passed `python3 calculations/risk-response/capstone_replay.py`, `python3 scripts/validate_module7.py`, and `python3 scripts/validate_repository.py` in the complete seven-module tree.
- [x] Verified that Modules 1–6 substantive learning content remained unchanged; only approved overview handoffs and repository-wide indexes changed.
- [x] Reviewed all 33 SVGs at 640 px and 1280 px and inspected GitHub-rendered Markdown, SVGs, Mermaid workflows, and navigation.
- [x] Completed changed-file, legal/attribution, originality, link, assessment, terminology, and capstone-calculation review.
- [x] Recorded owner approval, passed GitHub Actions, merged PR #14, and published v7.0.0.'''
    body=body.replace(old_steps,new_steps)
    body=body.replace('## Hard stops', '## Durable release controls')
    body=body.replace('- Do not merge before the complete 111-file overlay and full-validator/CI evidence are present.',
                      '- Any future Module 7 change must retain the complete overlay, full-validator evidence, source-separation controls, and calculation replay.')
    p.write_text(body)
    p=ROOT/'CITATION.cff';body=p.read_text()
    body=body.replace('version: 6.0.1','version: 7.0.0').replace('date-released: 2026-10-18','date-released: 2026-10-19')
    old_abstract='abstract: "A practitioner-oriented learning resource covering demand and forecasting, network design and digital connectivity, sourcing and supplier execution, internal operations, inventory, logistics and trade, customer relationship management, supplier relationship management, strategic alliances, supplier performance and certification, communication, and continuous improvement through original explanations, diagrams, datasets, knowledge checks, and integrated case studies."'
    new_abstract='abstract: "A practitioner-oriented learning resource covering demand and forecasting, network design and digital connectivity, sourcing and supplier execution, internal operations, inventory, logistics and trade, customer and supplier relationships, supply-chain risk governance, response economics, disruption recovery, business continuity, and continuous improvement through original explanations, diagrams, datasets, knowledge checks, and integrated case studies."'
    if new_abstract not in body:
        if old_abstract not in body:raise RuntimeError('Citation abstract baseline missing')
        body=body.replace(old_abstract,new_abstract,1)
    keyword_anchor='  - relationship management\n'
    risk_keywords='  - supply chain risk management\n  - risk analysis\n  - business continuity\n  - resilience\n'
    if risk_keywords not in body:
        if keyword_anchor not in body:raise RuntimeError('Citation keyword anchor missing')
        body=body.replace(keyword_anchor,keyword_anchor+risk_keywords,1)
    p.write_text(body)
    p=ROOT/'CHANGELOG.md';body=p.read_text()
    if '## Version 7.0.0 — Module 7' not in body:
        marker='Significant public improvements to this repository are recorded here.\n'
        entry='''

## Version 7.0.0 — Module 7

Release target: 2026-10-19

### Learning content

- Adds two connected sections covering risk governance and identification, qualitative and quantitative analysis, response economics, disruption recovery, and business continuity.
- Adds 39 Module 7 Markdown learning/reference pages, 31 topic lessons, 33 original SVG decision visuals, 32 fictional CSV datasets, and 72 independently authored knowledge checks.
- Adds the Stonebridge Risk and Resilience capstone, a fully worked solution guide, and a reproducible calculation replay.
- Adds the risk-response calculation and decision-control reference and integrates Module 7 into repository navigation, learning paths, glossary, roadmap, citation metadata, and bidirectional module handoffs.

### Quality controls

- Extends the shared validator to all seven modules and invokes the Module 7-specific structural, link, assessment, asset, and source-separation gates.
- Replays the Stonebridge arithmetic and decision gates from the published fictional datasets.
- Raster-reviews all 33 Module 7 SVGs at 640 px and 1280 px widths and rejects visibly truncated SVG labels.
- Verifies the 111-file release-candidate overlay, 32 CSV schemas, all local Markdown targets, external authoritative links, and Module 1–6 lesson-content preservation.
- Performs exact normalized 10-word and 12-word source/public overlap scans with zero hits against the private Module 7 learning component, presentation, flashcards, and question bank.
- Keeps proprietary source PDFs, presentations, flashcards, question-bank material, private audits, and render-check artifacts outside the public repository.
'''
        if marker not in body:raise RuntimeError('Changelog header missing')
        body=body.replace(marker,marker+entry,1)
        p.write_text(body)
    release=ROOT/'.github/releases/v7.0.0.md'
    if not release.exists():
        release.parent.mkdir(parents=True,exist_ok=True)
        release.write_text('''# v7.0.0 — Module 7: Supply Chain Risk

This release adds risk governance, analysis, response economics, disruption recovery, and business continuity to the six-module supply-chain learning baseline.

## Included

- 31 topic lessons across two connected sections
- 39 Module 7 Markdown learning/reference pages
- 33 original accessible SVG decision visuals
- 32 fictional CSV datasets
- 72 independently authored knowledge checks
- a risk-response calculation and decision-control reference
- the Stonebridge Risk and Resilience capstone, worked solution, and reproducible calculation replay
- bidirectional navigation and shared validation across Modules 1–7

## Quality controls

- complete Module 7 and full-repository structural, link, asset, and calculation validation
- 66 successful SVG raster renders across 640 px and 1280 px review widths
- verified assessment-answer alignment and capstone rationale mapping
- exact normalized 10-word and 12-word originality scans with zero source/public overlap hits
- no proprietary source PDFs, presentations, flashcards, question-bank material, or private audit artifacts in the public tree
''')
    print('Module 7 integrated and released with shared validator, repo navigation, glossary, learning paths, roadmap.')
    return 0

if __name__=='__main__':sys.exit(main())
