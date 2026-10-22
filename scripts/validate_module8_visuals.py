#!/usr/bin/env python3
"""Source-level Module 8 SVG visual audit (NOT a raster/browser substitute).

Checks every committed Section A/B/C and capstone SVG for accessibility,
topic differentiation, basic viewport/text bounds, unsupported embedded
content and source-referenced metric annotations.
"""
from __future__ import annotations
from collections import Counter,defaultdict
from pathlib import Path
import math,re,sys,xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"assets/diagrams/module-8"
EXPECTED={"section-a":12,"section-b":12,"section-c":18,"capstone":3}
KEYWORDS={
"section-a/strategy-alignment-decision-chain.svg":("73%","93%"),
"section-a/competitive-positioning-service-cost-matrix.svg":("222,000","181,500"),
"section-a/segment-uncertainty-policy-map.svg":("0.075","0.60"),
"section-a/business-plan-competency-bridge.svg":("54","420"),
"section-a/network-alternative-feasibility.svg":("1,000","850"),
"section-a/linear-program-product-mix.svg":("120","2,150"),
"section-a/discounted-cash-flow-payback.svg":("NPV","9,539"),
"section-b/sustainability-kpi-evidence-and-greenwashing-controls.svg":("66%",),
"section-c/ai-machine-learning-and-data-analytics.svg":("18","2","30","150"),
"section-c/technology-selection-feasibility-tco-and-value.svg":("116k","108k","89k"),
"section-c/implementation-integration-testing-and-cutover.svg":("190","200"),
"section-c/change-management-kotter-urgency-and-coalitions.svg":("90%","67%"),
"section-c/technology-maintenance-support-and-lifecycle-renewal.svg":("135","103"),
"capstone/aldergate-npv-adoption-sensitivity.svg":("NPV","75%"),
}
errors=[]
metrics={}
def local_name(e):return e.tag.rsplit("}",1)[-1]
def coords(s):
    try:return [float(k) for k in re.split(r"[ ,]+",s.strip()) if k]
    except (ValueError,AttributeError):return []
def audit(path):
    rel=path.relative_to(BASE).as_posix()
    src=path.read_text(encoding="utf-8")
    try:root=ET.fromstring(src)
    except ET.ParseError as exc:
        errors.append(f"{rel}: malformed XML {exc}");return
    if local_name(root)!="svg":errors.append(f"{rel}: wrong root tag")
    box=coords(root.get("viewBox",""))
    if len(box)!=4 or box[2]<=0 or box[3]<=0:errors.append(f"{rel}: missing/invalid viewBox");return
    _,_,width,height=box
    if root.get("role")!="img" or not root.get("aria-labelledby"):
        errors.append(f"{rel}: missing image role/accessibility reference")
    nodes=list(root.iter())
    titled=[x for x in nodes if local_name(x)=="title"]
    described=[x for x in nodes if local_name(x)=="desc"]
    if not titled or not described or not (titled[0].text or "").strip() or not (described[0].text or "").strip():
        errors.append(f"{rel}: title/desc missing or empty")
    ids={node.get("id") for node in nodes if node.get("id")}
    for key in (root.get("aria-labelledby") or "").split():
        if key not in ids:errors.append(f"{rel}: aria-labelledby target {key} not found")
    if any(local_name(e) in ("script","foreignObject","iframe","image") for e in nodes):
        errors.append(f"{rel}: external/active/unsupported SVG node")
    if re.search(r'<[^>]+\s(?:onload|onclick|onerror|href|xlink:href)=',src,re.I):
        errors.append(f"{rel}: external reference or event handler")
    text_nodes=[n for n in nodes if local_name(n)=="text"]
    if len(text_nodes)<6:errors.append(f"{rel}: too few graphical labels ({len(text_nodes)})")
    if not any(local_name(n) in ("rect","circle","line","path","polygon","polyline") for n in nodes):
        errors.append(f"{rel}: no visual shapes")
    parent_map={child: parent for parent in nodes for child in parent}
    for n in text_nodes:
        value="".join(n.itertext()).strip()
        if not value:errors.append(f"{rel}: empty visible label");continue
        try:x=float(n.get("x","0"));y=float(n.get("y","0"));sz=float(n.get("font-size","19"))
        except ValueError:errors.append(f"{rel}: invalid text coordinates");continue
        # Loose heuristic, not exact font metrics. Still catches clipped titles.
        est_width=len(value)*sz*.44
        anchor=n.get("text-anchor")
        parent=parent_map.get(n)
        while anchor is None and parent is not None:
            anchor=parent.get("text-anchor")
            parent=parent_map.get(parent)
        anchor=anchor or "start"
        left=x-(est_width if anchor=="end" else est_width/2 if anchor=="middle" else 0)
        right=left+est_width
        if left<-40 or right>width+40 or y<-10 or y>height+12:
            errors.append(f"{rel}: potential viewport clipping in {value[:65]!r} (x={x}, y={y}, approx={left:.0f}..{right:.0f})")
    if rel in KEYWORDS:
        for expected in KEYWORDS[rel]:
            if expected not in src:
                errors.append(f"{rel}: missing required case-specific numerical annotation {expected}")
    fingerprint=tuple((local_name(n) for n in nodes if local_name(n) in
        ("rect","circle","line","path","polygon","polyline")))
    metrics[rel]={"labels":len(text_nodes),"bytes":len(src),"shape_fingerprint":fingerprint}
def main():
    for folder,n in EXPECTED.items():
        p=BASE/folder
        paths=sorted(p.glob("*.svg"))
        if len(paths)!=n:errors.append(f"{folder}: expected {n} SVGs, found {len(paths)}")
        for path in paths:audit(path)
        fingerprints={metrics[x]["shape_fingerprint"] for x in metrics if x.startswith(folder+"/")}
        minimum={"section-a":6,"section-b":5,"section-c":10,"capstone":2}[folder]
        if len(fingerprints)<minimum:
            errors.append(f"{folder}: {len(fingerprints)} distinct shape layouts below {minimum} required")
        print(f"{folder}: {len(paths)} SVGs, {len(fingerprints)} distinct shape-layout signatures")
    for x in errors:print("ERROR:",x)
    if errors:return 1
    print("MODULE 8 SVG SOURCE-LEVEL VISUAL AUDIT PASSED")
    print("NOTE: Raster and actual GitHub browser rendering remain a separate manual sign-off.")
    return 0
if __name__=="__main__":sys.exit(main())
