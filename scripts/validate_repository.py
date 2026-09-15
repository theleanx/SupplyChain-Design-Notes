#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the public learning repository using only Python's standard library."""

from __future__ import annotations

import csv
import copy
import hashlib
import math
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_3 = ROOT / "03-sourcing-strategy-product-design-supplier-execution"
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
FENCE = "`" * 3
MODULE_3_REQUIRED_HEADINGS = (
    "## Decision model and workflow",
    "### Evidence retained through the workflow",
    "## Practical process flow",
    "## Realistic example",
    "**Decision insight.**",
    "## Trade-offs",
    "## Common mistakes",
    "## Original knowledge check",
    "### Why it is correct",
    "### Why the other answers are wrong",
)
MODULE_3_REJECTED_BOILERPLATE = (
    "Confirm the decision boundary, inputs, and accountable owner before analysis begins.",
    "Use comparable evidence and keep assumptions visible as the decision develops.",
    "Quantify the benefit and the exposure using the same scope and horizon.",
    "Set a guardrail, owner, and review trigger instead of assuming one permanent answer.",
)
MODULE_3_WEAK_DISTRACTORS = (
    "supplier's logo",
    "buyer's job title",
    "choose the shortest presentation",
    "ignore because spend is low",
    "all three are identical",
    "only if cheapest",
    "only if incumbent",
    "run a price-only auction",
)
MODULE_3_DATASET_LINKS = {
    "section-a-sourcing-alignment-and-total-cost/02-make-buy-and-core-capability.md": "make-buy-options.csv",
    "section-a-sourcing-alignment-and-total-cost/06-landed-cost-and-total-cost-of-ownership.md": "total-cost-options.csv",
    "section-b-category-strategy-and-supply-base/02-category-architecture.md": "category-spend.csv",
    "section-b-category-strategy-and-supply-base/03-portfolio-analysis.md": "category-portfolio.csv",
    "section-b-category-strategy-and-supply-base/06-spend-analysis-and-market-intelligence.md": "category-spend.csv",
    "section-b-category-strategy-and-supply-base/07-supply-base-right-sizing.md": "supplier-shares.csv",
    "section-c-product-design-for-supply-chain/01-design-as-economic-lever.md": "design-alternatives.csv",
    "section-c-product-design-for-supply-chain/03-design-for-supply-chain-and-logistics.md": "design-alternatives.csv",
    "section-c-product-design-for-supply-chain/04-standardization-commonality-and-universality.md": "design-alternatives.csv",
    "section-c-product-design-for-supply-chain/05-modular-versus-integral-design.md": "design-alternatives.csv",
    "section-c-product-design-for-supply-chain/06-simplification-dfma-and-serviceability.md": "design-alternatives.csv",
    "section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md": "supplier-evaluation.csv",
    "section-d-supplier-selection-contracting-and-procurement/05-contract-deployment-and-compliance.md": "contract-obligations.csv",
    "section-d-supplier-selection-contracting-and-procurement/07-terms-slas-and-incentives.md": "contract-obligations.csv",
    "section-d-supplier-selection-contracting-and-procurement/10-receiving-and-three-way-match.md": "three-way-match.csv",
    "section-d-supplier-selection-contracting-and-procurement/11-order-tracking-exceptions-and-expediting.md": "open-order-exceptions.csv",
}


def public_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def validate_markdown(paths: list[Path]) -> tuple[int, list[str]]:
    checked_links = 0
    errors: list[str] = []

    for path in paths:
        body = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        if not body.startswith("# "):
            errors.append(f"{relative}: missing level-one heading")

        fence_count = sum(line.startswith(FENCE) for line in body.splitlines())
        if fence_count % 2:
            errors.append(f"{relative}: unbalanced fenced block")

        if (
            path.is_relative_to(MODULE_3)
            and re.match(r"\d{2}-", path.name)
            and "review" not in path.name
        ):
            if len(body.split()) < 500:
                errors.append(f"{relative}: topic is below the 500-word content floor")
            for heading in MODULE_3_REQUIRED_HEADINGS:
                if heading not in body:
                    errors.append(f"{relative}: missing quality element ({heading})")
            for phrase in MODULE_3_REJECTED_BOILERPLATE:
                if phrase in body:
                    errors.append(f"{relative}: contains rejected generic boilerplate")
            mermaid_count = body.count(f"{FENCE}mermaid")
            if mermaid_count != 1:
                errors.append(
                    f"{relative}: requires exactly one practical Mermaid process flow"
                )
            elif "flowchart TD" not in body or body.count("-->") < 4:
                errors.append(
                    f"{relative}: process flow requires a top-down flowchart with at least four transitions"
                )
            if not re.search(r"^## (Applied|Worked) decision", body, re.MULTILINE):
                errors.append(f"{relative}: missing topic-specific applied decision section")

            lesson_relative = str(path.relative_to(MODULE_3))
            required_dataset = MODULE_3_DATASET_LINKS.get(lesson_relative)
            if required_dataset and required_dataset not in body:
                errors.append(
                    f"{relative}: quantitative lesson must link {required_dataset} directly"
                )

            related_match = re.search(
                r"^## Related concepts\n\n(?P<body>.*?)(?:\n\n---)",
                body,
                re.MULTILINE | re.DOTALL,
            )
            if not related_match or related_match.group("body").count("](") < 4:
                errors.append(
                    f"{relative}: related concepts require at least two topic-specific links"
                )

        if path.is_relative_to(MODULE_3):
            lowered = body.lower()
            for phrase in MODULE_3_WEAK_DISTRACTORS:
                if phrase in lowered:
                    errors.append(f"{relative}: contains weak distractor phrase ({phrase})")

        for alt_text, target in MARKDOWN_IMAGE.findall(body):
            if not alt_text.strip():
                errors.append(f"{relative}: image has empty alternative text ({target})")

        for raw_target in MARKDOWN_LINK.findall(body):
            target = raw_target.strip().split()[0].strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            checked_links += 1
            if not (path.parent / target).resolve().exists():
                errors.append(f"{relative}: broken link ({target})")

    return checked_links, errors


def validate_module_3_content() -> list[str]:
    """Check calculations and learning-design guarantees that generic checks miss."""
    errors: list[str] = []
    topic_paths = sorted(
        path
        for path in MODULE_3.glob("section-*/*.md")
        if re.match(r"\d{2}-", path.name) and "review" not in path.name
    )
    if len(topic_paths) != 35:
        errors.append(f"Module 3: expected 35 topic lessons, found {len(topic_paths)}")

    h2_sequences = {
        tuple(line for line in path.read_text(encoding="utf-8").splitlines() if line.startswith("## "))
        for path in topic_paths
    }
    if len(h2_sequences) < 20:
        errors.append(
            "Module 3: lesson structures are overly repetitive; fewer than 20 heading sequences"
        )

    total_cost_path = ROOT / "assets/data/module-3/section-a/total-cost-options.csv"
    with total_cost_path.open(newline="", encoding="utf-8") as handle:
        total_rows = list(csv.DictReader(handle))
    components = [row for row in total_rows if row["cost_element"] != "Total"]
    totals = next(row for row in total_rows if row["cost_element"] == "Total")
    for source in ("local_source", "distant_source"):
        calculated = sum(float(row[source]) for row in components)
        if not math.isclose(calculated, float(totals[source]), abs_tol=0.005):
            errors.append(f"{total_cost_path.relative_to(ROOT)}: {source} total is inconsistent")

    landed = (
        MODULE_3
        / "section-a-sourcing-alignment-and-total-cost"
        / "06-landed-cost-and-total-cost-of-ownership.md"
    ).read_text(encoding="utf-8")
    for required in ("$13 quote advantage", "$3.40 total-cost disadvantage", "$79.20 per unit"):
        if required not in landed:
            errors.append(f"Module 3 landed-cost lesson: missing verified statement ({required})")
    if "$21 quote" in landed or "annualized total is $79.20" in landed:
        errors.append("Module 3 landed-cost lesson: contains a known unit or arithmetic error")

    make_buy_path = ROOT / "assets/data/module-3/section-a/make-buy-options.csv"
    with make_buy_path.open(newline="", encoding="utf-8") as handle:
        make_buy_rows = list(csv.DictReader(handle))
    if {row["evaluation_horizon_years"] for row in make_buy_rows} != {"3"}:
        errors.append(f"{make_buy_path.relative_to(ROOT)}: requires one explicit three-year horizon")
    if {row["discount_rate_pct"] for row in make_buy_rows} != {"0"}:
        errors.append(f"{make_buy_path.relative_to(ROOT)}: base-case discount rate must be explicit")

    score_path = ROOT / "assets/data/module-3/section-d/supplier-evaluation.csv"
    weights = (25, 20, 15, 15, 15, 10)
    with score_path.open(newline="", encoding="utf-8") as handle:
        score_rows = list(csv.DictReader(handle))
    for row in score_rows:
        raw = [float(value) for value in list(row.values())[1:7]]
        calculated = sum(score / 5 * weight for score, weight in zip(raw, weights))
        if not math.isclose(calculated, float(row["weighted_total_100"]), abs_tol=0.2):
            errors.append(
                f"{score_path.relative_to(ROOT)}: {row['supplier']} weighted total is inconsistent"
            )

    shares_path = ROOT / "assets/data/module-3/section-b/supplier-shares.csv"
    with shares_path.open(newline="", encoding="utf-8") as handle:
        share_rows = list(csv.DictReader(handle))
    share_totals: dict[str, float] = {}
    for row in share_rows:
        share_totals[row["category"]] = share_totals.get(row["category"], 0) + float(row["share_pct"])
    for category, total in share_totals.items():
        if not math.isclose(total, 100, abs_tol=0.005):
            errors.append(f"{shares_path.relative_to(ROOT)}: {category} shares total {total}, not 100")

    capstone = (MODULE_3 / "capstone/README.md").read_text(encoding="utf-8")
    solution = (MODULE_3 / "capstone/solution-guide.md").read_text(encoding="utf-8")
    if f"{FENCE}mermaid" not in capstone or capstone.count("-->") < 7:
        errors.append("Module 3 capstone: missing end-to-end process flow")
    if len(solution.split()) < 1400:
        errors.append("Module 3 capstone solution: below the 1,400-word worked-solution floor")
    for required in ("$8,232,000", "$6,546,000", "3,888", "$4,900", "$160"):
        if required not in solution:
            errors.append(f"Module 3 capstone solution: missing worked result ({required})")

    return errors


def validate_svg(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    module_3_fingerprints: dict[str, list[Path]] = {}

    for path in paths:
        relative = path.relative_to(ROOT)
        try:
            root = ET.parse(path).getroot()
        except ET.ParseError as exc:
            errors.append(f"{relative}: invalid SVG XML ({exc})")
            continue

        child_names = {child.tag.rsplit("}", 1)[-1] for child in list(root)}
        if "title" not in child_names or "desc" not in child_names:
            errors.append(f"{relative}: SVG requires title and description elements")

        if path.is_relative_to(ROOT / "assets" / "diagrams" / "module-3"):
            if root.get("role") != "img" or not root.get("aria-labelledby"):
                errors.append(f"{relative}: SVG requires role=img and aria-labelledby")
            if not root.get("viewBox"):
                errors.append(f"{relative}: SVG requires a viewBox for responsive scaling")
            descendants = list(root.iter())
            if any(node.tag.rsplit("}", 1)[-1] == "foreignObject" for node in descendants):
                errors.append(
                    f"{relative}: foreignObject is prohibited because browser text can be clipped"
                )
            if path.name.endswith("-workflow.svg"):
                tspans = [
                    node
                    for node in descendants
                    if node.tag.rsplit("}", 1)[-1] == "tspan"
                ]
                if len(tspans) < 5 or any(
                    node.get("x") is None or node.get("y") is None for node in tspans
                ):
                    errors.append(
                        f"{relative}: workflow labels require explicit multiline coordinates"
                    )

            # Ignore wording and compare the actual geometry/style. Topic visuals
            # may share a design language, but one repeated diagram template must
            # not stand in for every decision model.
            geometry = copy.deepcopy(root)
            for parent in geometry.iter():
                for child in list(parent):
                    if child.tag.rsplit("}", 1)[-1] in {"title", "desc", "text"}:
                        parent.remove(child)
            serialized = ET.tostring(geometry, encoding="unicode")
            fingerprint = hashlib.sha256(serialized.encode("utf-8")).hexdigest()
            module_3_fingerprints.setdefault(fingerprint, []).append(path)

    module_3_count = sum(len(group) for group in module_3_fingerprints.values())
    if module_3_count >= 10:
        if len(module_3_fingerprints) < 10:
            errors.append(
                "assets/diagrams/module-3: fewer than 10 topic-specific visual structures"
            )
        largest = max(module_3_fingerprints.values(), key=len)
        if len(largest) > 5:
            errors.append(
                "assets/diagrams/module-3: one visual template is reused for more than five topics"
            )

    return errors


def validate_csv(paths: list[Path]) -> list[str]:
    errors: list[str] = []

    for path in paths:
        relative = path.relative_to(ROOT)
        with path.open(newline="", encoding="utf-8-sig") as handle:
            rows = list(csv.reader(handle))

        if not rows:
            errors.append(f"{relative}: empty dataset")
            continue
        if not all(rows[0]):
            errors.append(f"{relative}: header contains an empty column")
        if any(len(row) != len(rows[0]) for row in rows):
            errors.append(f"{relative}: inconsistent column count")

    return errors


def main() -> int:
    files = public_files()
    markdown = [path for path in files if path.suffix.lower() == ".md"]
    svg = [path for path in files if path.suffix.lower() == ".svg"]
    datasets = [path for path in files if path.suffix.lower() == ".csv"]

    link_count, markdown_errors = validate_markdown(markdown)
    errors = (
        markdown_errors
        + validate_svg(svg)
        + validate_csv(datasets)
        + validate_module_3_content()
    )

    print(
        f"Validated {len(markdown)} Markdown files, {link_count} internal links, "
        f"{len(svg)} SVG files, and {len(datasets)} CSV files."
    )

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
