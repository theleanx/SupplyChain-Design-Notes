#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the public learning repository using only Python's standard library."""

from __future__ import annotations

import csv
import copy
import hashlib
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

        if path.is_relative_to(MODULE_3) and f"{FENCE}mermaid" in body:
            errors.append(
                f"{relative}: Module 3 uses render-tested SVGs instead of client-rendered Mermaid"
            )

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
    errors = markdown_errors + validate_svg(svg) + validate_csv(datasets)

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
