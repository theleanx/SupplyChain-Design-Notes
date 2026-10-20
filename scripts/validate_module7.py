#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Module 7 release gates that complement scripts/validate_repository.py.

Standalone validation is safe on the original repository checkout plus the
Module 7 release overlay; no proprietary CSCP source files are required.
Run: python3 scripts/validate_module7.py
"""
from __future__ import annotations

from collections import defaultdict
import csv
import hashlib
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / '07-supply-chain-risk'
DATA = ROOT / 'assets/data/module-7'
VIS = ROOT / 'assets/diagrams/module-7'
CASE = ROOT / 'calculations/risk-response'
SECTIONS = {
    'section-a-risk-management-and-supply-chain-risks': 12,
    'section-b-risk-analysis-and-response': 19,
}
REQUIRED = [
    'Learning objectives', 'Why it matters', 'Decision logic',
    'Trade-offs', 'Commonly confused with', 'Common mistakes',
    'Original knowledge check', 'Practitioner perspective',
    'Related concepts',
]
MODULE_HEADINGS = ['Learning outcomes','Module path','Module resources',
                   'Cross-module handoffs','How each lesson is structured','Module snapshot']
SECTION_HEADINGS = ['Learning outcomes','Learning path','Working data and visuals',
                    'How to study the section']
LINKS = re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
IMAGES = re.compile(r'!\[([^\]]+)\]\(([^)]+)\)')


def has_heading(text: str, heading: str) -> bool:
    return bool(re.search(r'^## '+re.escape(heading)+r'\s*$',text,re.M|re.I))


def main() -> int:
    failures: list[str] = []
    overlay_only = '--overlay-only' in sys.argv
    if not MOD.is_dir():
        print('ERROR: Module 7 overlay is missing from the checkout. Do not release an empty module.')
        return 1
    sections = sorted(MOD.glob('section-*'))
    if {p.name for p in sections} != set(SECTIONS):
        failures.append('Module 7 needs exactly the two specified sections')
    all_md = sorted(MOD.rglob('*.md')) + sorted(CASE.rglob('*.md'))
    svg = sorted(VIS.rglob('*.svg'))
    data = sorted(DATA.glob('*.csv'))
    topic_count = 0
    knowledge_checks = 0
    paragraphs: dict[str, set[str]] = defaultdict(set)
    ref_count = 0
    for h in MODULE_HEADINGS:
        if not has_heading((MOD/'README.md').read_text(),h):
            failures.append(f'Module overview missing {h}')
    module_overview = (MOD/'README.md').read_text()
    if '**Status: released in v7.0.0.**' not in module_overview:
        failures.append('Module overview release status is stale or missing')
    for stale in ('awaiting full-repository CI', 'final full-repository release gate pending',
                  'do not publish as a finished module', 'validated release candidate',
                  'awaiting final human approval', 'unmerged pending final human approval'):
        if stale in module_overview:
            failures.append(f'Module overview retains stale release-gate text: {stale}')
    roadmap = (ROOT/'ROADMAP.md').read_text(encoding='utf-8')
    if '- [x] Obtain final release approval and publish v7.0.0' not in roadmap:
        failures.append('ROADMAP.md: Module 7 final approval/release gate is incomplete')
    release_record = (ROOT/'MODULE7-IMPORT-AND-REVIEW-CHECKLIST.md').read_text(encoding='utf-8')
    if '> **RELEASED.**' not in release_record:
        failures.append('Module 7 import/review record does not show the completed release')
    for stale in ('DRAFT ONLY', 'is not yet committed', 'Keep the PR in draft',
                  'Do not merge before'):
        if stale in release_record:
            failures.append(f'Module 7 import/review record retains stale release text: {stale}')
    for p in sections:
        if not p.is_dir(): continue
        overview=p/'README.md'
        if not overview.is_file():
            failures.append(f'{p.name}: missing section README')
            continue
        for h in SECTION_HEADINGS:
            if not has_heading(overview.read_text(),h):
                failures.append(f'{p.name}: section README missing {h}')
        topics = sorted(f for f in p.glob('[0-9][0-9]-*.md') if '-section-' not in f.name)
        if len(topics) != SECTIONS[p.name]:
            failures.append(f'{p.name}: expected {SECTIONS[p.name]} lessons, found {len(topics)}')
        reviews=list(p.glob('*-section-*-review.md'))
        if len(reviews)!=1:
            failures.append(f'{p.name}: expected exactly one section review')
        else:
            r=reviews[0].read_text()
            n=r.count('<details>')
            if n<10 or n!=r.count('</details>'):
                failures.append(f'{reviews[0].name}: incomplete 10+ review explanations')
            if not re.search(r'^## .*?(?:completion|readiness|self-check)',r,re.I|re.M):
                failures.append(f'{reviews[0].name}: missing completion checkpoint')
            knowledge_checks+=n
        for f in topics:
            topic_count+=1
            text=f.read_text(encoding='utf-8')
            rel=f.relative_to(ROOT).as_posix()
            if len(text.split()) < 500:
                failures.append(f'{rel}: fewer than 500 words')
            for h in REQUIRED:
                if not has_heading(text,h):
                    failures.append(f'{rel}: missing {h}')
            if not has_heading(text,'Concept in plain English'):
                failures.append(f'{rel}: missing plain-language concept')
            if 'Stonebridge' not in text and 'example' not in text.lower():
                failures.append(f'{rel}: missing fictional scenario')
            if not re.search(r'^#{2,3} Evidence retained through the workflow\s*$',text,re.M|re.I):
                failures.append(f'{rel}: missing workflow evidence')
            if not re.search(r'^## (?:Applied|Worked) .+',text,re.M|re.I):
                failures.append(f'{rel}: missing decision artifact')
            if text.count('```mermaid') != 1 or text.count('-->') < 3:
                failures.append(f'{rel}: missing practical directed Mermaid workflow')
            if len(IMAGES.findall(text))<1:
                failures.append(f'{rel}: missing original image')
            n=text.count('<details>')
            knowledge_checks+=n
            if n!=1 or text.count('</details>')!=1:
                failures.append(f'{rel}: expected one original answer disclosure')
            for tag in ('### Correct answer','### Why it is correct','### Why the other answers are wrong'):
                if tag.lower() not in text.lower():
                    failures.append(f'{rel}: missing {tag}')
            if '## Related concepts' in text and text.split('## Related concepts',1)[1].split('\n---\n',1)[0].count('](')<2:
                failures.append(f'{rel}: fewer than two related links')
            if not re.search(r'\n---\n\n\[(?:Section overview|Previous)',text):
                failures.append(f'{rel}: missing sequential navigation')
            for paragraph in re.split(r'\n\s*\n',text):
                normalized=' '.join(re.sub(r'[`*_\[\]()]','',paragraph).lower().split())
                if len(normalized)>=180 and not normalized.startswith(('flowchart ','|','a. ','- section overview')):
                    paragraphs[normalized].add(rel)
    if topic_count!=31: failures.append(f'Expected 31 Module 7 lesson files; found {topic_count}')
    for para, locations in paragraphs.items():
        if len(locations)>=3:
            failures.append('Repeated long paragraph in '+', '.join(sorted(locations)[:3]))
    cap=MOD/'capstone/README.md';sol=MOD/'capstone/solution-guide.md'
    if not cap.is_file() or not sol.is_file(): failures.append('Missing capstone assignment or solved guide')
    else:
        assignment=cap.read_text();worked=sol.read_text()
        answer_blocks=re.findall(r'<details>.*?</details>',assignment,re.S)
        if len(answer_blocks)!=10 or assignment.count('</details>')!=10:
            failures.append('Capstone assessment requires exactly 10 original answer rationale blocks')
        knowledge_checks+=len(answer_blocks)
        answer_expectations = (
            ('B', ('Safety clearance', 'one-day deadline')),
            ('C', ('$45,000', '0.25×80,000')),
            ('D', ('Monitored hardening', '$28,600')),
            ('A', ('10% eligibility gate', '17% stress')),
            ('B', ('two weeks', '240÷120=2')),
            ('D', ('Zero backup capacity', '450 units of building throughput')),
            ('C', ('release path remains unproven', '160-minute result')),
            ('B', ('$11,500', '11,000+7,500+18,000−25,000')),
            ('A', ('$56,000', '€800,000×$0.07/€')),
            ('D', ('Do not automatically aggregate', 'Shared dependency')),
        )
        for index, (letter, markers) in enumerate(answer_expectations, start=1):
            if index > len(answer_blocks):
                break
            block=answer_blocks[index-1]
            if f'**Correct answer: {letter}.**' not in block:
                failures.append(f'Capstone assessment question {index}: answer key mismatch')
            for marker in markers:
                if marker not in block:
                    failures.append(f'Capstone assessment question {index}: rationale missing {marker}')
        if 'complete item-specific explanation' in assignment:
            failures.append('Capstone assessment contains a generic placeholder rationale')
        if assignment.count('```mermaid')!=1 or assignment.count('-->')<5:
            failures.append('Capstone lacks an end-to-end gated process flow')
        if len(worked.split())<2200: failures.append('Capstone solution below 2200 words')
        for h in ('Executive recommendation','Sensitivity and failure cases','Implementation roadmap','Evaluation rubric'):
            if not has_heading(worked,h):failures.append('Capstone solution missing '+h)
        for n in ('$45,000','$28,600','$36,500','$11,500'):
            if n not in worked:failures.append('Capstone solution missing verified result '+n)
        if assignment.count('.csv)')<12:
            failures.append('Capstone assignment does not link 12 directly relevant datasets')
    if len(svg)!=33:failures.append(f'Expected 33 SVG diagrams; found {len(svg)}')
    if len(data)!=32:failures.append(f'Expected 32 CSV datasets; found {len(data)}')
    referenced: set[Path]=set()
    for f in all_md:
        body=f.read_text(encoding='utf-8')
        if not body.startswith('# '):failures.append(f'{f.relative_to(ROOT)}: no top-level heading')
        if body.count('```')%2:failures.append(f'{f.relative_to(ROOT)}: unbalanced fenced blocks')
        for url in [*LINKS.findall(body),*[u for _,u in IMAGES.findall(body)]]:
            ref_count+=1
            t=url.strip().split('#')[0]
            if not t or t.startswith(('http://','https://','mailto:')):continue
            dest=(f.parent/t).resolve()
            referenced.add(dest)
            # In a full checkout ALL internal links must exist, including Modules 1–6.
            if not dest.exists():
                if overlay_only and dest.is_relative_to(ROOT) and dest.relative_to(ROOT).parts[0] in (
                    '01-supply-chains-demand-forecasting',
                    '02-network-design-digital-connectivity-performance',
                    '03-sourcing-strategy-product-design-supplier-execution',
                    '04-internal-operations-inventory','05-forward-reverse-logistics',
                    '06-supply-chain-relationships','LEARNING-PATHS.md','GLOSSARY.md'
                ):
                    continue  # Separately verified against GitHub main; NOT a full-checkout pass.
                failures.append(f'{f.relative_to(ROOT)}: broken link {url}')
    for f in svg:
        rel=f.relative_to(ROOT)
        try:
            el=ET.parse(f).getroot()
            immediate={c.tag.rsplit('}',1)[-1]:c for c in el}
            if not {'title','desc'}<=immediate.keys(): failures.append(f'{rel}: SVG title/description missing')
            if el.get('role')!='img' or not el.get('aria-labelledby') or not el.get('viewBox'):
                failures.append(f'{rel}: SVG accessibility/viewBox missing')
            if any(x.tag.rsplit('}',1)[-1]=='foreignObject' for x in el.iter()):
                failures.append(f'{rel}: foreignObject is prohibited')
            visible_text=' '.join(''.join(x.itertext()) for x in el.iter() if x.tag.rsplit('}',1)[-1]=='text')
            if '…' in visible_text or re.search(r'\b(?:assura|recover|administrative c)$',visible_text):
                failures.append(f'{rel}: SVG contains visibly truncated text')
        except ET.ParseError as ex: failures.append(f'{rel}: malformed SVG {ex}')
        if f.resolve() not in referenced:failures.append(f'{rel}: orphaned diagram')
    for f in data:
        rel=f.relative_to(ROOT)
        with f.open(encoding='utf-8-sig',newline='') as h:rows=list(csv.reader(h))
        if not rows or any(not x.strip() for x in rows[0]) or any(len(x)!=len(rows[0]) for x in rows):
            failures.append(f'{rel}: invalid CSV schema')
        if f.resolve() not in referenced:failures.append(f'{rel}: orphaned dataset')
    for f in CASE.glob('*.py'):
        if f.name=='capstone_replay.py' and 'assert_eq' not in f.read_text():
            failures.append('Capstone replay must assert expected values')
    banned=sorted(f for f in ROOT.rglob('*') if f.is_file() and f.suffix.lower() in {'.pdf','.pptx','.docx','.docm','.zip'})
    if banned:failures.append('Source-like files are present in repository overlay: '+str([str(x.relative_to(ROOT)) for x in banned[:5]]))
    print(f'Module 7: {topic_count} lessons, {len(svg)} SVGs, {len(data)} CSVs, {knowledge_checks} answer blocks, {ref_count} local/external reference occurrences.')
    if failures:
        for msg in failures[:150]:print('ERROR:',msg)
        print('Total errors:',len(failures))
        return 1
    print('Module 7 overlay-only validation passed (existing-module links were verified separately).' if overlay_only else 'Module 7 release validation passed (full checkout).')
    return 0

if __name__=='__main__':sys.exit(main())
