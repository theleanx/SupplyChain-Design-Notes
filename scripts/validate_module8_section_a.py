#!/usr/bin/env python3
"""Quality gate for completed Module 8 Section A, preserving the 1–7 release validator."""
from __future__ import annotations
import csv, re, subprocess, sys, xml.etree.ElementTree as ET
from collections import Counter,defaultdict
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
MOD=ROOT/"08-optimization-sustainability-technology"
SEC=MOD/"section-a-optimizing-supply-chain-strategy-and-tactics"
D=ROOT/"assets/data/module-8/section-a"
V=ROOT/"assets/diagrams/module-8/section-a"
REVIEW=SEC/"13-section-a-review.md"
FENCE=chr(96)*3
LINK=re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
HEADINGS=["Learning objectives","Why it matters","Decision model and workflow","Practical process flow","Realistic example","Applied decision artifact or worked calculation","Decision logic","Trade-offs","Commonly confused with","Common mistakes","Original knowledge check","Practitioner perspective","Related concepts"]
errors=[]
def links(p,t):
    for raw in LINK.findall(t):
        if raw.startswith(("http://","https://","mailto:","#")):continue
        raw=unquote(raw.split("#",1)[0].strip("<>"))
        if raw and not (p.parent/raw).resolve().exists():errors.append(f"{p.relative_to(ROOT)}: invalid link {raw}")
def main():
    lessons=sorted(p for p in SEC.glob("*.md") if re.fullmatch(r"(?:0[1-9]|1[0-2])-[a-z0-9-]+\.md",p.name))
    if len(lessons)!=12:errors.append(f"expected 12 lessons, found {len(lessons)}")
    paragraph_uses=defaultdict(set)
    for p in lessons:
        t=p.read_text(encoding="utf-8")
        if len(t.split())<500:errors.append(f"{p.name}: less than 500 words")
        for h in HEADINGS:
            pattern=(r"^## Realistic example\b.*$" if h=="Realistic example" else r"^## "+re.escape(h)+r"\s*$")
            if not re.search(pattern,t,re.M|re.I):errors.append(f"{p.name}: missing {h}")
        if t.count("<details>")!=1 or t.count("</details>")!=1:errors.append(f"{p.name}: topic answer blocks invalid")
        if t.count(FENCE+"mermaid")!=1 or t.count(FENCE)%2:errors.append(f"{p.name}: Mermaid/fence mismatch")
        if t.count(".svg)")!=1:errors.append(f"{p.name}: requires an original SVG")
        if ".csv)" not in t:errors.append(f"{p.name}: missing directly linked data")
        for h in ["### Correct answer","### Why it is correct","### Why the other answers are wrong"]:
            if h.lower() not in t.lower():errors.append(f"{p.name}: missing {h}")
        links(p,t)
        for para in re.split(r"\n\s*\n",t):
            norm=" ".join(re.sub(r"[*_\[\]()]", "", para).lower().split())
            if len(norm)>=180 and not norm.startswith(("|","a.","b.","c.","d.","flowchart ",""+FENCE)):
                paragraph_uses[norm].add(p.name)
    for line,paths in paragraph_uses.items():
        if len(paths)>=3:errors.append(f"repeated generic paragraph in {sorted(paths)}: {line[:75]}")
    svgs=list(V.glob("*.svg"));csvs=list(D.glob("*.csv"))
    if len(svgs)!=12:errors.append(f"expected 12 SVGs, got {len(svgs)}")
    if len(csvs)!=11:errors.append(f"expected 11 CSVs, got {len(csvs)}")
    for p in svgs:
        try:r=ET.parse(p).getroot()
        except ET.ParseError as e:errors.append(f"{p.name}: bad XML {e}");continue
        tags={c.tag.rsplit("}",1)[-1] for c in r}
        if not {"title","desc"}<=tags or r.get("role")!="img" or not r.get("aria-labelledby") or not r.get("viewBox"):
            errors.append(f"{p.name}: accessible SVG contract failed")
        if any(c.tag.rsplit("}",1)[-1]=="foreignObject" for c in r.iter()):
            errors.append(f"{p.name}: foreignObject disallowed")
    for p in csvs:
        with p.open(encoding="utf-8",newline="") as f:rows=list(csv.reader(f))
        if not rows or not all(rows[0]) or any(len(row)!=len(rows[0]) for row in rows):errors.append(f"{p.name}: invalid CSV")
    if not REVIEW.exists():errors.append("no Section A review")
    else:
        t=REVIEW.read_text(encoding="utf-8")
        if t.count("<details>")!=12 or t.count("</details>")!=12:errors.append("review requires twelve answer blocks")
        if len(re.findall(r"^## Question \d+$",t,re.M))!=12:errors.append("review question headings incomplete")
        if not re.search(r"^## Completion/readiness checkpoint$",t,re.M):errors.append("readiness checkpoint missing")
        keys=re.findall(r"### Correct answer\s+\*\*([ABCD])\.",t)
        if Counter(keys)!=Counter({"A":3,"B":3,"C":3,"D":3}):errors.append(f"review answers unbalanced {Counter(keys)}")
        links(REVIEW,t)
    for p in [MOD/"README.md",MOD/"REFERENCES.md",SEC/"README.md",D/"README.md"]:
        if not p.exists():errors.append(f"missing index {p.relative_to(ROOT)}")
        else:links(p,p.read_text(encoding="utf-8"))
    if not errors:
        cmd=[sys.executable,str(ROOT/"calculations/module8-section-a/replay.py")]
        run=subprocess.run(cmd,capture_output=True,text=True)
        if run.returncode:errors.append("calculation replay failed: "+(run.stdout+run.stderr)[-1500:])
        else:print(run.stdout)
    print(f"Section A: {len(lessons)} lessons, {len(svgs)} original SVGs, {len(csvs)} fictional CSVs")
    for e in errors:print("ERROR:",e)
    if errors:return 1
    print("MODULE 8 SECTION A QUALITY GATE PASSED; FULL MODULE 8 NOT YET RELEASED")
    return 0
if __name__=="__main__":sys.exit(main())
