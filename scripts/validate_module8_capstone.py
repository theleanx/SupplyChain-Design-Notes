#!/usr/bin/env python3
"""Independent development-quality gate for the Module 8 integrated AlderGate capstone.

Does not edit or weaken the published Modules 1–7 validator.
"""
from __future__ import annotations

import csv
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MOD = ROOT / "08-optimization-sustainability-technology"
CASE = MOD / "capstone"
DATA = ROOT / "assets/data/module-8/capstone"
VIS = ROOT / "assets/diagrams/module-8/capstone"
CALC = ROOT / "calculations/module8-capstone"
REQUIRED_DATA = {
    "executive-policy.csv", "network-sustainability.csv",
    "manual-work-benefits.csv", "program-costs.csv",
    "benefit-sensitivity.csv", "governance-actions.csv",
}
REQUIRED_SVGS = {
    "aldergate-gated-program-decision.svg",
    "aldergate-npv-adoption-sensitivity.svg",
    "aldergate-network-capacity-and-footprint.svg",
}
LINK = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
errors = []


def check_links(path: Path, markdown: str) -> None:
    for ref in LINK.findall(markdown):
        if ref.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = unquote(ref.split("#", 1)[0].strip("<>"))
        if local and not (path.parent / local).resolve().exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative reference {local}")


def check_svgs() -> None:
    actual = {p.name for p in VIS.glob("*.svg")}
    if actual != REQUIRED_SVGS:
        errors.append(f"capstone SVG inventory differs: {sorted(actual ^ REQUIRED_SVGS)}")
    for path in VIS.glob("*.svg"):
        try:
            svg = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{path.name}: malformed XML {exc}")
            continue
        labels = {item.tag.rsplit("}", 1)[-1] for item in svg}
        if not {"title", "desc"} <= labels:
            errors.append(f"{path.name}: missing accessible title or description")
        if svg.get("role") != "img" or not svg.get("aria-labelledby") or not svg.get("viewBox"):
            errors.append(f"{path.name}: invalid image role, ARIA labels, or viewBox")
        if any(child.tag.rsplit("}", 1)[-1] == "foreignObject" for child in svg.iter()):
            errors.append(f"{path.name}: foreignObject is not permitted")
        # Numerical visual labels should not silently lose source units and caveats.
        raw = path.read_text(encoding="utf-8")
        if not any(unit in raw for unit in ("units/week", "CO₂e", "NPV")):
            errors.append(f"{path.name}: decision-specific quantitative labels absent")


def check_data() -> None:
    actual = {p.name for p in DATA.glob("*.csv")}
    if actual != REQUIRED_DATA:
        errors.append(f"capstone CSV inventory differs: {sorted(actual ^ REQUIRED_DATA)}")
    for path in DATA.glob("*.csv"):
        with path.open(encoding="utf-8", newline="") as stream:
            records = list(csv.reader(stream))
        if len(records) < 2 or not all(records[0]) or len(set(records[0])) != len(records[0]):
            errors.append(f"{path.name}: missing/duplicated CSV header or data")
        elif any(len(row) != len(records[0]) for row in records):
            errors.append(f"{path.name}: inconsistent CSV width")


def validate() -> int:
    assignment = CASE / "README.md"
    solution = CASE / "solution-guide.md"
    data_index = DATA / "README.md"
    formula = CALC / "formula-sheet.md"
    replay = CALC / "replay.py"
    index = MOD / "README.md"
    files = [assignment, solution, data_index, formula, replay, index]
    for path in files:
        if not path.exists():
            errors.append(f"missing required capstone resource {path.relative_to(ROOT)}")
    if errors:
        for msg in errors:print("ERROR:",msg)
        return 1
    assignment_text = assignment.read_text(encoding="utf-8")
    solution_text = solution.read_text(encoding="utf-8")
    if len(assignment_text.split()) < 1600:
        errors.append("assignment below 1600 word integrated-study floor")
    if len(solution_text.split()) < 2500:
        errors.append("solution below 2500 word worked-analysis floor")
    if len(re.findall(r"^### Task [1-8] —", assignment_text, re.M)) != 8:
        errors.append("student assignment must have exactly eight explicit numbered tasks")
    if len(re.findall(r"^## (?:[1-9]|10)\. ", solution_text, re.M)) != 10:
        errors.append("worked guide must have 10 numbered solution sections")
    for label in (
        "Section A","Section B","Section C","sustainability","capacity",
        "financial","technology","cutover","change","75%","67%","185,000",
        "35,813","58,250","break-even","worker","Finance","rollback",
        "source","sensitivity","30/60/90",
    ):
        if label.lower() not in (assignment_text+"\n"+solution_text).lower():
            errors.append(f"integrated capstone decision missing thematic requirement: {label}")
    for f in REQUIRED_DATA:
        if f not in assignment_text:
            errors.append(f"assignment lacks direct link to original capstone CSV {f}")
    for f in (
        "location-design-alternatives.csv","recycling-lineage.csv",
        "technology-selection.csv","change-coalition.csv","cutover-acceptance.csv",
    ):
        if f not in assignment_text:
            errors.append(f"assignment lacks existing Section A/B/C source link {f}")
    for f in REQUIRED_SVGS:
        if f not in assignment_text and f not in solution_text:
            errors.append(f"capstone original SVG not used: {f}")
    for path in (assignment, solution, data_index, formula, index):
        check_links(path,path.read_text(encoding="utf-8"))
    check_svgs()
    check_data()
    if not errors:
        result = subprocess.run([sys.executable,str(replay)],capture_output=True,text=True)
        if result.returncode:
            errors.append("independent calculation replay FAILED:\n"+(result.stdout+result.stderr)[-3500:])
        else:
            print(result.stdout)
    print(f"Capstone audit: 2 learning documents, {len(list(DATA.glob('*.csv')))} original CSV inputs, "
          f"{len(list(VIS.glob('*.svg')))} original SVGs, formula sheet and independent replay")
    for msg in errors:print("ERROR:",msg)
    if errors:
        return 1
    print("MODULE 8 CAPSTONE DEVELOPMENT QUALITY GATE PASSED — final full repository release approval still pending")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
