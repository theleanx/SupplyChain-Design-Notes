#!/usr/bin/env python3
"""Module 8 Section C completeness and calculation gate without weakening released-module checks."""
from __future__ import annotations
import csv,re,subprocess,sys,xml.etree.ElementTree as ET
from collections import Counter,defaultdict
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
MOD=ROOT/"08-optimization-sustainability-technology"
SEC=MOD/"section-c-technology-trends"
DATA=ROOT/"assets/data/module-8/section-c"
SVG=ROOT/"assets/diagrams/module-8/section-c"
REVIEW=SEC/"19-section-c-review.md"
TICKS=chr(96)*3
TOPIC=re.compile(r"^(?:0[1-9]|1[0-8])-[a-z0-9-]+\.md$")
LINK=re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
REQUIRED=("Learning objectives","Why it matters","Decision model and workflow","Practical process flow",
"Realistic example","Applied decision artifact or worked calculation","Decision logic",
"Trade-offs","Commonly confused with","Common mistakes","Original knowledge check",
"Practitioner perspective","Related concepts")
ERRORS=[]

def links(p,t):
    for raw in LINK.findall(t):
        if raw.startswith(("http://","https://","mailto:","#")):continue
        path=unquote(raw.split("#",1)[0].strip("<>"))
        if path and not (p.parent/path).resolve().exists():
            ERRORS.append(f"{p.relative_to(ROOT)}: broken link {path}")

def audit():
    lessons=sorted(p for p in SEC.glob("*.md") if TOPIC.fullmatch(p.name))
    if len(lessons)!=18:ERRORS.append(f"expected 18 lessons, got {len(lessons)}")
    text_use=defaultdict(set)
    for p in lessons:
        txt=p.read_text(encoding="utf-8")
        if len(txt.split())<500:ERRORS.append(f"{p.name}: <500 words")
        for h in REQUIRED:
            pat=r"^## Realistic example\b" if h=="Realistic example" else r"^## "+re.escape(h)+r"\s*$"
            if not re.search(pat,txt,re.M|re.I):ERRORS.append(f"{p.name}: missing {h}")
        if txt.count("<details>")!=1 or txt.count("</details>")!=1:ERRORS.append(f"{p.name}: one answered topic check required")
        for h in ("### Correct answer","### Why it is correct","### Why the other answers are wrong"):
            if h.lower() not in txt.lower():ERRORS.append(f"{p.name}: missing {h}")
        if txt.count(TICKS+"mermaid")!=1 or txt.count(TICKS)%2:ERRORS.append(f"{p.name}: Mermaid fence issue")
        if txt.count(".svg)")!=1 or ".csv)" not in txt:ERRORS.append(f"{p.name}: direct SVG/CSV link missing")
        links(p,txt)
        for para in re.split(r"\n\s*\n",txt):
            value=" ".join(re.sub(r"[*_\[\]()]", "",para).lower().split())
            if len(value)>=180 and not value.startswith(("|","a.","b.","c.","d.")):
                text_use[value].add(p.name)
    for value,ps in text_use.items():
        if len(ps)>=3:ERRORS.append("repeated long language: "+",".join(sorted(ps))+": "+value[:80])
    svgs=list(SVG.glob("*.svg"));datasets=list(DATA.glob("*.csv"))
    if len(svgs)!=18:ERRORS.append(f"expected 18 SVGs, got {len(svgs)}")
    if len(datasets)!=18:ERRORS.append(f"expected 18 CSVs, got {len(datasets)}")
    for p in svgs:
        try:root=ET.parse(p).getroot()
        except ET.ParseError as exc:ERRORS.append(f"{p.name}: malformed SVG {exc}");continue
        names={node.tag.rsplit("}",1)[-1] for node in root}
        if not {"title","desc"}<=names or root.get("role")!="img" or not root.get("aria-labelledby") or not root.get("viewBox"):
            ERRORS.append(f"{p.name}: SVG accessibility failure")
        if any(node.tag.rsplit("}",1)[-1]=="foreignObject" for node in root.iter()):
            ERRORS.append(f"{p.name}: unsafe SVG foreignObject")
    for p in datasets:
        with p.open(encoding="utf-8",newline="") as f:records=list(csv.reader(f))
        if not records or not all(records[0]) or any(len(row)!=len(records[0]) for row in records):
            ERRORS.append(f"{p.name}: malformed CSV")
    if not REVIEW.exists():ERRORS.append("missing section review")
    else:
        txt=REVIEW.read_text(encoding="utf-8")
        if txt.count("<details>")!=18 or txt.count("</details>")!=18:ERRORS.append("review requires 18 answered items")
        if len(re.findall(r"^## Question \d+$",txt,re.M))!=18:ERRORS.append("review question headings incomplete")
        if "## Completion/readiness checkpoint" not in txt:ERRORS.append("review readiness gate missing")
        keys=re.findall(r"### Correct answer\s+\*\*([ABCD])\.",txt)
        if Counter(keys)!=Counter({"A":5,"B":5,"C":4,"D":4}):ERRORS.append(f"review answer key distribution unexpected: {Counter(keys)}")
        links(REVIEW,txt)
    for p in (MOD/"README.md",SEC/"README.md",SEC/"REFERENCES.md",DATA/"README.md"):
        if not p.exists():ERRORS.append(f"missing index {p.relative_to(ROOT)}")
        else:links(p,p.read_text(encoding="utf-8"))
    text="\n".join(p.read_text(encoding="utf-8").lower() for p in lessons)
    for word in ("cloud","machine learning","control tower","quantum","blockchain","digital twin",
                 "roadmap","audit","gap analysis","cutover","raci","wbs","agile","kotter","maintenance"):
        if word not in text:ERRORS.append("uncovered scope term: "+word)
    if not ERRORS:
        p=subprocess.run([sys.executable,str(ROOT/"calculations/module8-section-c/replay.py")],capture_output=True,text=True)
        if p.returncode:ERRORS.append("calculation replay failed:\n"+(p.stdout+p.stderr)[-2300:])
        else:print(p.stdout)
    print(f"Section C: {len(lessons)} lessons, {len(svgs)} SVGs, {len(datasets)} CSVs")
    for issue in ERRORS:print("ERROR:",issue)
    if ERRORS:return 1
    print("MODULE 8 SECTION C QUALITY GATE PASSED")
    return 0
if __name__=="__main__":sys.exit(audit())
