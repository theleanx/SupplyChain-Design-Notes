#!/usr/bin/env python3
"""Section B completeness and correctness gate; preserves Modules 1-7 CI."""
from pathlib import Path
from collections import Counter,defaultdict
from urllib.parse import unquote
import csv,re,subprocess,sys,xml.etree.ElementTree as ET

R=Path(__file__).resolve().parents[1]
M=R/"08-optimization-sustainability-technology"
S=M/"section-b-sustainability"
V=R/"assets/diagrams/module-8/section-b"
D=R/"assets/data/module-8/section-b"
A=S/"13-section-b-review.md"
TICKS=chr(96)*3
H=["Learning objectives","Why it matters","Decision model and workflow","Practical process flow",
"Realistic example","Applied decision artifact or worked calculation","Decision logic","Trade-offs",
"Commonly confused with","Common mistakes","Original knowledge check","Practitioner perspective","Related concepts"]
LINK=re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
err=[]

def links(p,t):
    for raw in LINK.findall(t):
        if raw.startswith(("http://","https://","mailto:","#")):continue
        path=unquote(raw.split("#",1)[0].strip("<>"))
        if path and not (p.parent/path).resolve().exists():err.append(f"{p.relative_to(R)} broken link: {raw}")

def run():
    topic=sorted(p for p in S.glob("*.md") if re.fullmatch(r"(?:0[1-9]|1[0-2])-[a-z0-9-]+\.md",p.name))
    if len(topic)!=12:err.append(f"12 lessons expected, found {len(topic)}")
    seen=defaultdict(set)
    for p in topic:
        t=p.read_text(encoding="utf-8")
        if len(t.split())<500:err.append(f"{p.name} below word floor")
        for h in H:
            pat=r"^## Realistic example\b" if h=="Realistic example" else r"^## "+re.escape(h)+r"\s*$"
            if not re.search(pat,t,re.M|re.I):err.append(f"{p.name} missing heading {h}")
        if t.count("<details>")!=1 or t.count("</details>")!=1:err.append(f"{p.name} topic answer blocks")
        if t.count(TICKS+"mermaid")!=1 or t.count(TICKS)%2:err.append(f"{p.name} Mermaid fences")
        if t.count(".svg)")!=1:err.append(f"{p.name} needs one SVG")
        if ".csv)" not in t:err.append(f"{p.name} needs linked CSV")
        for h in ["### Correct answer","### Why it is correct","### Why the other answers are wrong"]:
            if h.lower() not in t.lower():err.append(f"{p.name} missing {h}")
        links(p,t)
        for para in re.split(r"\n\s*\n",t):
            v=" ".join(re.sub(r"[*_\[\]()]", "",para).lower().split())
            if len(v)>=180 and not v.startswith(("|","a.","b.","c.","d.")):
                seen[v].add(p.name)
    for k,names in seen.items():
        if len(names)>=3:err.append("repeated long text across "+",".join(sorted(names))+": "+k[:65])
    svg=list(V.glob("*.svg"));datasets=list(D.glob("*.csv"))
    if len(svg)!=12:err.append(f"12 SVGs expected, got {len(svg)}")
    if len(datasets)!=12:err.append(f"12 CSVs expected, got {len(datasets)}")
    for p in svg:
        try:x=ET.parse(p).getroot()
        except ET.ParseError as e:err.append(f"bad SVG {p.name}: {e}");continue
        tags={v.tag.rsplit("}",1)[-1] for v in x}
        if not {"title","desc"}<=tags or x.get("role")!="img" or not x.get("aria-labelledby") or not x.get("viewBox"):
            err.append(f"{p.name} SVG accessibility contract failed")
        if any(v.tag.rsplit("}",1)[-1]=="foreignObject" for v in x.iter()):err.append(f"{p.name} unsafe SVG element")
    for p in datasets:
        with p.open(encoding="utf-8",newline="") as f:z=list(csv.reader(f))
        if not z or not all(z[0]) or any(len(r)!=len(z[0]) for r in z):err.append(f"{p.name} invalid CSV")
    if not A.exists():err.append("missing Section B review")
    else:
        t=A.read_text(encoding="utf-8")
        if t.count("<details>")!=12 or t.count("</details>")!=12:err.append("review answer count")
        if len(re.findall(r"^## Question \d+$",t,re.M))!=12:err.append("review questions missing")
        if "## Completion/readiness checkpoint" not in t:err.append("no readiness checkpoint")
        keys=re.findall(r"### Correct answer\s+\*\*([ABCD])\.",t)
        if Counter(keys)!=Counter({"A":3,"B":3,"C":3,"D":3}):err.append("unbalanced answers "+str(Counter(keys)))
        links(A,t)
    for p in [M/"README.md",S/"README.md",S/"REFERENCES.md",D/"README.md"]:
        if not p.exists():err.append(f"missing reference {p}")
        else:links(p,p.read_text(encoding="utf-8"))
    all_text="\n".join(p.read_text(encoding="utf-8") for p in topic)
    for key in ["GRI 3","SA8000","ISO 26000","UN Global Compact","OECD","3TG","triple bottom line"]:
        if key.lower() not in all_text.lower():err.append(f"source scope missing {key}")
    if not err:
        p=subprocess.run([sys.executable,str(R/"calculations/module8-section-b/replay.py")],capture_output=True,text=True)
        if p.returncode:err.append("replay failed: "+(p.stdout+p.stderr)[-1600:])
        else:print(p.stdout)
    print(f"Section B audit: {len(topic)} lessons, {len(svg)} SVGs, {len(datasets)} CSVs")
    for e in err:print("ERROR:",e)
    if err:return 1
    print("MODULE 8 SECTION B QUALITY GATE PASSED; MODULE 8 NOT YET RELEASED")
    return 0
if __name__=="__main__":sys.exit(run())
