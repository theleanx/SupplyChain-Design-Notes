#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the public learning repository using only Python's standard library."""

from __future__ import annotations

import csv
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
MARKDOWN_IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
FENCE = "`" * 3


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
