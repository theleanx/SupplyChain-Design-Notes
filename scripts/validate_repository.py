#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the public learning repository using only Python's standard library."""

from __future__ import annotations

import csv
import copy
import hashlib
import math
import re
import statistics
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_1 = ROOT / "01-supply-chains-demand-forecasting"
MODULE_2 = ROOT / "02-network-design-digital-connectivity-performance"
MODULE_3 = ROOT / "03-sourcing-strategy-product-design-supplier-execution"
MODULES = {
    "Module 1": (MODULE_1, 44),
    "Module 2": (MODULE_2, 43),
    "Module 3": (MODULE_3, 35),
}
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
SHARED_REQUIRED_HEADINGS = (
    "Learning objectives",
    "Why it matters",
    "Decision logic",
    "Trade-offs",
    "Common mistakes",
    "Original knowledge check",
    "Practitioner perspective",
    "Related concepts",
)
MODULE_1_DATASET_LINKS = {
    "section-d-forecasting/04-seasonality-deseasonalizing-reseasonalizing.md": "northstar-seasonal-demand.csv",
    "section-d-forecasting/05-moving-averages-and-exponential-smoothing.md": "forecast-method-comparison.csv",
    "section-d-forecasting/06-service-sector-and-associative-forecasting.md": "service-hourly-demand.csv",
    "section-d-forecasting/07-leading-indicators-regression-correlation.md": "associative-regression-example.csv",
    "section-d-forecasting/08-forecast-error-bias-random-variation.md": "forecast-error-example.csv",
    "section-d-forecasting/09-mad-tracking-signal-standard-deviation.md": "forecast-error-example.csv",
    "section-d-forecasting/10-mse-mape-and-error-measures.md": "forecast-error-example.csv",
    "section-e-supply-demand-alignment/04-demand-review-and-dashboard.md": "demand-review-example.csv",
}
MODULE_2_DATASET_LINKS = {
    "section-a-network-design-and-technology-investment/03-network-configuration-and-flow-design.md": "network-alternatives.csv",
    "section-a-network-design-and-technology-investment/07-technology-business-case-and-tco.md": "technology-business-case.csv",
    "section-b-connected-supply-networks-and-master-data/04-event-management-and-control-towers.md": "network-exceptions.csv",
    "section-b-connected-supply-networks-and-master-data/06-transportation-management-systems.md": "transport-lanes.csv",
    "section-b-connected-supply-networks-and-master-data/17-data-quality-cleansing-and-stewardship.md": "master-data-quality.csv",
    "section-c-performance-and-financial-insight/06-perfect-order-and-customer-service.md": "customer-service-metrics.csv",
    "section-c-performance-and-financial-insight/09-cash-to-cash-and-working-capital.md": "working-capital.csv",
    "section-c-performance-and-financial-insight/14-supplier-financial-health-and-credit-risk.md": "supplier-health.csv",
    "section-c-performance-and-financial-insight/16-operational-quality-capacity-and-maintenance.md": "operations-scorecard.csv",
}
ASSESSMENT_DEFECTS = (
    "without testing whether can ",
    "without testing whether may ",
    "without testing whether stop ",
    "without testing whether they ",
    "without testing whether retaining ",
)


def public_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def is_topic(path: Path, module: Path) -> bool:
    return (
        path.parent.parent == module
        and path.parent.name.startswith("section-")
        and bool(re.match(r"\d{2}-", path.name))
        and not bool(re.match(r"\d{2}-section-[a-z]-review\.md$", path.name))
    )


def has_heading(body: str, heading: str) -> bool:
    return bool(
        re.search(
            rf"^## {re.escape(heading)}\s*$",
            body,
            re.MULTILINE | re.IGNORECASE,
        )
    )


def validate_shared_module_content() -> list[str]:
    """Apply the same minimum lesson contract to every completed module."""
    errors: list[str] = []
    paragraph_uses: dict[str, list[Path]] = {}
    data_links = {
        MODULE_1: MODULE_1_DATASET_LINKS,
        MODULE_2: MODULE_2_DATASET_LINKS,
        MODULE_3: MODULE_3_DATASET_LINKS,
    }

    for label, (module, expected_count) in MODULES.items():
        topics = sorted(path for path in module.glob("section-*/*.md") if is_topic(path, module))
        if len(topics) != expected_count:
            errors.append(f"{label}: expected {expected_count} topic lessons, found {len(topics)}")

        for path in topics:
            body = path.read_text(encoding="utf-8")
            relative = path.relative_to(ROOT)
            if len(body.split()) < 500:
                errors.append(f"{relative}: topic is below the shared 500-word content floor")
            for heading in SHARED_REQUIRED_HEADINGS:
                if not has_heading(body, heading):
                    errors.append(f"{relative}: missing shared quality element (## {heading})")
            for heading in ("### Correct answer", "### Why it is correct", "### Why the other answers are wrong"):
                if heading.lower() not in body.lower():
                    errors.append(f"{relative}: incomplete answer rationale ({heading})")
            for phrase in ASSESSMENT_DEFECTS:
                if phrase in body.lower():
                    errors.append(f"{relative}: malformed assessment language ({phrase.strip()})")
            if body.count("<details>") != 1 or body.count("</details>") != 1:
                errors.append(f"{relative}: requires exactly one topic knowledge-check answer block")

            has_mermaid = f"{FENCE}mermaid" in body
            has_svg = bool(re.search(r"!\[[^]]+\]\([^)]+\.svg\)", body, re.IGNORECASE))
            if not (has_mermaid or has_svg):
                errors.append(f"{relative}: requires a topic-appropriate Mermaid or SVG visual")
            if module in (MODULE_2, MODULE_3) and body.count(f"{FENCE}mermaid") != 1:
                errors.append(f"{relative}: requires exactly one practical Mermaid process flow")
            elif module in (MODULE_2, MODULE_3) and (
                not re.search(r"^flowchart (?:TD|LR)\s*$", body, re.MULTILINE)
                or body.count("-->") < 3
            ):
                errors.append(
                    f"{relative}: process flow requires a directed flowchart with at least three transitions"
                )

            if module in (MODULE_1, MODULE_2):
                if not has_heading(body, "Evidence retained through the workflow"):
                    errors.append(f"{relative}: missing decision-evidence record")
                if not has_heading(body, "Applied decision artifact"):
                    errors.append(f"{relative}: missing reusable applied decision artifact")
            elif "### Evidence retained through the workflow" not in body:
                errors.append(f"{relative}: missing workflow evidence")

            if not re.search(r"\b(example|northstar|asterworks|rivermark)\b", body, re.IGNORECASE):
                errors.append(f"{relative}: missing fictional applied example")

            related = re.search(
                r"^## Related concepts\s*\n(?P<section>.*?)(?:\n---\n|\Z)",
                body,
                re.MULTILINE | re.IGNORECASE | re.DOTALL,
            )
            if not related or related.group("section").count("](") < 2:
                errors.append(f"{relative}: related concepts require at least two working links")
            if not re.search(r"\n---\n\n\[(?:Section overview|Previous:)", body):
                errors.append(f"{relative}: missing sequential navigation footer")

            h2 = [line.lower() for line in body.splitlines() if line.startswith("## ")]
            duplicates = sorted({heading for heading in h2 if h2.count(heading) > 1})
            if duplicates:
                errors.append(f"{relative}: duplicate level-two sections ({', '.join(duplicates)})")

            lesson_relative = str(path.relative_to(module))
            required_dataset = data_links[module].get(lesson_relative)
            if required_dataset and required_dataset not in body:
                errors.append(f"{relative}: quantitative lesson must link {required_dataset} directly")

            for paragraph in re.split(r"\n\s*\n", body):
                normalized = " ".join(re.sub(r"[`*_\[\]()]", "", paragraph).lower().split())
                if len(normalized) >= 180 and not normalized.startswith(("flowchart ", "|", "a. ", "- section overview")):
                    paragraph_uses.setdefault(normalized, []).append(path)

    for paragraph, paths in paragraph_uses.items():
        unique = sorted(set(paths))
        if len(unique) >= 3:
            sample = ", ".join(str(path.relative_to(ROOT)) for path in unique[:3])
            errors.append(f"Repeated long paragraph appears in {len(unique)} topics ({sample})")

    return errors


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


def csv_dicts(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def validate_module_1_2_calculations() -> list[str]:
    """Independently reproduce the numerical claims most likely to affect decisions."""
    errors: list[str] = []

    seasonal = csv_dicts("assets/data/module-1/section-d/northstar-seasonal-demand.csv")
    monthly = [
        statistics.mean(float(row[column]) for column in ("Year 1", "Year 2", "Year 3"))
        for row in seasonal
    ]
    overall = statistics.mean(monthly)
    january_index = monthly[0] / overall
    if not math.isclose(overall, 104.1388888889, abs_tol=0.0001):
        errors.append("Module 1 seasonal dataset: overall average is inconsistent")
    if not math.isclose(january_index, 1.2483328888, abs_tol=0.0001):
        errors.append("Module 1 seasonal dataset: January index is inconsistent")

    regression = csv_dicts("assets/data/module-1/section-d/associative-regression-example.csv")
    x = [float(row["Commercial Building Permits Index"]) for row in regression]
    y = [float(row["Pump Quote Requests"]) for row in regression]
    xbar, ybar = statistics.mean(x), statistics.mean(y)
    slope = sum((a - xbar) * (b - ybar) for a, b in zip(x, y)) / sum((a - xbar) ** 2 for a in x)
    intercept = ybar - slope * xbar
    correlation = sum((a - xbar) * (b - ybar) for a, b in zip(x, y)) / math.sqrt(
        sum((a - xbar) ** 2 for a in x) * sum((b - ybar) ** 2 for b in y)
    )
    if not (math.isclose(intercept, 11.7247, abs_tol=0.001) and math.isclose(slope, 0.4752, abs_tol=0.001)):
        errors.append("Module 1 regression dataset: fitted equation is inconsistent")
    if not math.isclose(correlation**2, 0.8725, abs_tol=0.001):
        errors.append("Module 1 regression dataset: r-squared is inconsistent")

    forecast_errors = csv_dicts("assets/data/module-1/section-d/forecast-error-example.csv")
    signed = [float(row["Error Actual-Forecast"]) for row in forecast_errors]
    absolute = [float(row["Absolute Error"]) for row in forecast_errors]
    squared = [float(row["Squared Error"]) for row in forecast_errors]
    ape = [float(row["Absolute Percentage Error"]) for row in forecast_errors]
    expected = (sum(signed), sum(absolute), sum(squared), statistics.mean(absolute), statistics.mean(squared), statistics.mean(ape))
    target = (5.0, 21.0, 61.0, 2.625, 7.625, 2.3975)
    if any(not math.isclose(value, wanted, abs_tol=0.0001) for value, wanted in zip(expected, target)):
        errors.append("Module 1 forecast-error dataset: error totals or averages are inconsistent")

    comparison = csv_dicts("assets/data/module-1/section-d/forecast-method-comparison.csv")
    actual = [float(row["Actual"]) for row in comparison]
    for index, row in enumerate(comparison):
        if index >= 3:
            moving = sum(actual[index - 3 : index]) / 3
            weighted = (actual[index - 3] + 2 * actual[index - 2] + 3 * actual[index - 1]) / 6
            if not math.isclose(moving, float(row["3-Period Moving Average"]), abs_tol=0.011):
                errors.append(f"Module 1 forecast comparison: moving average error in period {index + 1}")
            if not math.isclose(weighted, float(row["Weighted Moving Average"]), abs_tol=0.011):
                errors.append(f"Module 1 forecast comparison: weighted average error in period {index + 1}")
        smoothed = 104.0 if index == 0 else 0.3 * actual[index - 1] + 0.7 * float(comparison[index - 1]["Exponential Smoothing alpha=0.30"])
        if not math.isclose(smoothed, float(row["Exponential Smoothing alpha=0.30"]), abs_tol=0.011):
            errors.append(f"Module 1 forecast comparison: smoothing error in period {index + 1}")

    history = csv_dicts("assets/data/module-1/capstone/northstar-demand-history.csv")
    recent = history[-4:]
    recent_errors = [float(row["actual_units"]) - float(row["baseline_forecast_units"]) for row in recent]
    capstone_values = (
        statistics.mean(float(row["actual_units"]) for row in history[-3:]),
        statistics.mean(abs(value) for value in recent_errors),
        statistics.mean(abs(float(row["actual_units"]) - float(row["baseline_forecast_units"])) / float(row["actual_units"]) * 100 for row in recent),
        sum(recent_errors) / statistics.mean(abs(value) for value in recent_errors),
    )
    capstone_target = (1216.6667, 50.0, 4.0980, 4.0)
    if any(not math.isclose(value, wanted, abs_tol=0.01) for value, wanted in zip(capstone_values, capstone_target)):
        errors.append("Module 1 capstone: forecast calculations are inconsistent")

    technology = csv_dicts("assets/data/module-2/section-a/technology-business-case.csv")
    year_columns = ("year_0_usd", "year_1_usd", "year_2_usd", "year_3_usd")
    costs = sum(float(row[column]) for row in technology if row["type"] == "Cost" for column in year_columns)
    benefits = sum(float(row[column]) for row in technology if row["type"] == "Benefit" for column in year_columns)
    annual_net = [
        sum((1 if row["type"] == "Benefit" else -1) * float(row[column]) for row in technology)
        for column in year_columns[1:]
    ]
    if (costs, benefits, annual_net) != (510000.0, 690000.0, [110000.0, 190000.0, 210000.0]):
        errors.append("Module 2 technology dataset: cost, benefit, or annual cash flow is inconsistent")

    network = csv_dicts("assets/data/module-2/section-a/network-alternatives.csv")
    lower_better = ("annual_operating_cost_usd", "inventory_days", "one_time_investment_usd")
    normalized: dict[str, dict[str, float]] = {row["alternative"]: {} for row in network}
    for column in lower_better:
        values = [float(row[column]) for row in network]
        low, high = min(values), max(values)
        for row in network:
            normalized[row["alternative"]][column] = 1 + 4 * (high - float(row[column])) / (high - low)
    base_weights = (0.25, 0.25, 0.20, 0.10, 0.10, 0.10)
    sensitivity_weights = (0.15, 0.35, 0.25, 0.10, 0.10, 0.05)
    base_scores: dict[str, float] = {}
    sensitivity_scores: dict[str, float] = {}
    for row in network:
        values = (
            normalized[row["alternative"]]["annual_operating_cost_usd"],
            float(row["service_score"]),
            float(row["resilience_score"]),
            float(row["implementation_score"]),
            normalized[row["alternative"]]["inventory_days"],
            normalized[row["alternative"]]["one_time_investment_usd"],
        )
        base_scores[row["alternative"]] = sum(weight * value for weight, value in zip(base_weights, values))
        sensitivity_scores[row["alternative"]] = sum(weight * value for weight, value in zip(sensitivity_weights, values))
    if max(base_scores, key=base_scores.get) != "Postponement center" or not math.isclose(base_scores["Postponement center"], 4.00665, abs_tol=0.001):
        errors.append("Module 2 network dataset: base weighted ranking is inconsistent")
    if max(sensitivity_scores, key=sensitivity_scores.get) != "Postponement center" or not math.isclose(sensitivity_scores["Postponement center"], 4.14721, abs_tol=0.001):
        errors.append("Module 2 network dataset: sensitivity ranking is inconsistent")
    expected_base = {
        "Central network": 3.65,
        "Regional stock hub": 3.45731,
        "Postponement center": 4.00665,
        "Regional production plant": 2.944,
    }
    expected_sensitivity = {
        "Central network": 3.2,
        "Regional stock hub": 3.62218,
        "Postponement center": 4.14721,
        "Regional production plant": 3.544,
    }
    if any(not math.isclose(base_scores[name], value, abs_tol=0.001) for name, value in expected_base.items()):
        errors.append("Module 2 network dataset: one or more base scores are inconsistent")
    if any(
        not math.isclose(sensitivity_scores[name], value, abs_tol=0.001)
        for name, value in expected_sensitivity.items()
    ):
        errors.append("Module 2 network dataset: one or more sensitivity scores are inconsistent")

    exceptions = csv_dicts("assets/data/module-2/section-b/network-exceptions.csv")
    exception_summary: dict[str, tuple[int, float, float]] = {}
    for severity in {row["severity"] for row in exceptions}:
        selected = [row for row in exceptions if row["severity"] == severity]
        exception_summary[severity] = (
            len(selected),
            statistics.mean(float(row["response_minutes"]) for row in selected),
            sum(float(row["estimated_revenue_at_risk_usd"]) for row in selected),
        )
    if exception_summary.get("critical") != (2, 19.0, 548000.0):
        errors.append("Module 2 exception dataset: critical-case summary is inconsistent")
    if exception_summary.get("high") != (5, 40.4, 849000.0):
        errors.append("Module 2 exception dataset: high-case summary is inconsistent")

    transport = csv_dicts("assets/data/module-2/section-b/transport-lanes.csv")
    transport_utilization = {
        row["lane_id"]: float(row["loaded_weight_kg"]) / float(row["usable_capacity_kg"]) * 100
        for row in transport
    }
    expected_utilization = {
        "L-101": 83.3333,
        "L-102": 80.0,
        "L-103": 72.2222,
        "L-104": 66.6667,
        "L-105": 75.0,
        "L-106": 75.0,
    }
    if any(
        not math.isclose(transport_utilization[name], value, abs_tol=0.005)
        for name, value in expected_utilization.items()
    ):
        errors.append("Module 2 transportation dataset: lane utilization is inconsistent")

    working_capital = csv_dicts("assets/data/module-2/section-c/working-capital.csv")
    for row in working_capital:
        inventory_days = float(row["average_inventory_usd"]) / float(row["annual_cogs_usd"]) * 365
        receivable_days = float(row["average_receivables_usd"]) / float(row["annual_revenue_usd"]) * 365
        payable_days = float(row["average_payables_usd"]) / float(row["annual_purchases_usd"]) * 365
        cash_to_cash = inventory_days + receivable_days - payable_days
        if not math.isclose(cash_to_cash, float(row["cash_to_cash_days"]), abs_tol=0.11):
            errors.append(f"Module 2 working-capital dataset: {row['scenario']} cash-to-cash is inconsistent")

    customer = csv_dicts("assets/data/module-2/section-c/customer-service-metrics.csv")
    customer_totals = {
        column: sum(float(row[column]) for row in customer)
        for column in (
            "eligible_orders",
            "perfect_orders",
            "complete_orders",
            "on_time_to_request",
            "on_time_to_promise",
            "damage_free_orders",
            "documentation_correct_orders",
        )
    }
    expected_customer_totals = {
        "eligible_orders": 1000.0,
        "perfect_orders": 930.0,
        "complete_orders": 976.0,
        "on_time_to_request": 938.0,
        "on_time_to_promise": 967.0,
        "damage_free_orders": 994.0,
        "documentation_correct_orders": 989.0,
    }
    if customer_totals != expected_customer_totals:
        errors.append("Module 2 customer-service dataset: capstone totals are inconsistent")

    operations = csv_dicts("assets/data/module-2/section-c/operations-scorecard.csv")
    operation_totals = {
        column: sum(float(row[column]) for row in operations)
        for column in (
            "units_entered",
            "first_pass_units",
            "planned_orders_due",
            "planned_orders_on_time",
            "available_hours",
            "run_hours",
            "failures",
            "corrective_repair_hours",
            "accepted_units",
        )
    }
    operation_results = (
        operation_totals["first_pass_units"] / operation_totals["units_entered"] * 100,
        operation_totals["planned_orders_on_time"] / operation_totals["planned_orders_due"] * 100,
        operation_totals["run_hours"] / operation_totals["available_hours"] * 100,
        operation_totals["accepted_units"] / operation_totals["units_entered"] * 100,
        operation_totals["run_hours"] / operation_totals["failures"],
        operation_totals["corrective_repair_hours"] / operation_totals["failures"],
    )
    operation_targets = (94.4864, 93.3962, 86.5842, 97.8947, 180.0952, 7.2381)
    if any(
        not math.isclose(value, target, abs_tol=0.005)
        for value, target in zip(operation_results, operation_targets)
    ):
        errors.append("Module 2 operations dataset: capstone KPIs are inconsistent")

    data_quality = csv_dicts("assets/data/module-2/section-b/master-data-quality.csv")
    defect_rates = {
        row["domain"]: float(row["records_with_critical_defect"]) / float(row["records_evaluated"]) * 100
        for row in data_quality
    }
    expected_defect_rates = {
        "Item": 3.5833,
        "Customer": 2.4419,
        "Supplier": 5.7143,
        "Location": 9.4595,
        "Resource": 10.9375,
        "Lane": 8.4783,
        "Finance": 2.6316,
    }
    if max(defect_rates, key=defect_rates.get) != "Resource" or any(
        not math.isclose(defect_rates[name], value, abs_tol=0.005)
        for name, value in expected_defect_rates.items()
    ):
        errors.append("Module 2 master-data dataset: critical-defect ranking is inconsistent")

    supplier_health = csv_dicts("assets/data/module-2/section-c/supplier-health.csv")
    supplier_ratios: dict[str, tuple[float, float, float, float]] = {}
    for row in supplier_health:
        supplier_ratios[row["supplier"]] = (
            float(row["current_assets_usd"]) / float(row["current_liabilities_usd"]),
            float(row["cash_and_receivables_usd"]) / float(row["current_liabilities_usd"]),
            float(row["total_debt_usd"]) / float(row["equity_usd"]),
            float(row["ebit_usd"]) / float(row["interest_expense_usd"]),
        )
    expected_supplier_ratios = {
        "Atlas Controls": (1.55, 0.775, 1.0833, 3.0556),
        "BlueRiver Metals": (1.7451, 0.8235, 0.3684, 7.6190),
        "Cedar Sensorics": (1.1429, 0.4286, 2.75, 1.5833),
        "Delta Packaging": (1.9615, 1.1154, 0.2545, 8.0833),
    }
    if any(
        not math.isclose(value, target, abs_tol=0.005)
        for supplier, targets in expected_supplier_ratios.items()
        for value, target in zip(supplier_ratios[supplier], targets)
    ):
        errors.append("Module 2 supplier-health dataset: one or more ratios are inconsistent")

    return errors


def validate_capstones_and_inventory(markdown: list[Path], svg: list[Path], datasets: list[Path]) -> list[str]:
    errors: list[str] = []
    capstone_requirements = {
        "Module 1": (MODULE_1, 850, 1, ("1,216.7", "4.10%", "$29,600")),
        "Module 2": (
            MODULE_2,
            1400,
            9,
            (
                "4.01",
                "2.14 years",
                "−$27,000",
                "19 minutes",
                "$548,000",
                "10.94%",
                "93.0%",
                "180.10 hours",
                "84.1 days",
            ),
        ),
        "Module 3": (MODULE_3, 1400, 10, ("$8,232,000", "$6,546,000", "3,888")),
    }
    for label, (module, solution_floor, data_count, results) in capstone_requirements.items():
        assignment = (module / "capstone/README.md").read_text(encoding="utf-8")
        solution = (module / "capstone/solution-guide.md").read_text(encoding="utf-8")
        if f"{FENCE}mermaid" not in assignment or assignment.count("-->") < 5:
            errors.append(f"{label} capstone: missing end-to-end process flow")
        if assignment.count(".csv)") < data_count:
            errors.append(f"{label} capstone: expected at least {data_count} directly linked datasets")
        if assignment.count("<details>") < 5:
            errors.append(f"{label} capstone: requires at least five decision checks")
        if len(solution.split()) < solution_floor:
            errors.append(f"{label} capstone solution: below the {solution_floor}-word floor")
        if solution.count("|---") < 2:
            errors.append(f"{label} capstone solution: requires completed decision tables")
        for heading in (
            "Executive recommendation",
            "Sensitivity and failure cases",
            "Implementation roadmap",
            "Evaluation rubric",
        ):
            if not has_heading(solution, heading):
                errors.append(f"{label} capstone solution: missing shared section (## {heading})")
        for result in results:
            if result not in solution:
                errors.append(f"{label} capstone solution: missing verified result ({result})")

    module_markdown = [path for path in markdown if any(path.is_relative_to(module) for module, _ in MODULES.values())]
    details = sum(path.read_text(encoding="utf-8").count("<details>") for path in module_markdown)
    if len(module_markdown) != 159:
        errors.append(f"Repository inventory: expected 159 module Markdown files, found {len(module_markdown)}")
    if len(svg) != 80:
        errors.append(f"Repository inventory: expected 80 SVG files, found {len(svg)}")
    if len(datasets) != 26:
        errors.append(f"Repository inventory: expected 26 CSV files, found {len(datasets)}")
    if details != 319:
        errors.append(f"Repository inventory: expected 319 knowledge checks, found {details}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for statement in ("159 structured Markdown files", "80 original SVG diagrams", "26 original CSV datasets", "319 independently authored knowledge checks"):
        if statement not in readme:
            errors.append(f"README inventory is missing the current statement ({statement})")

    module_snapshot_claims = {
        MODULE_1: ("59 structured Markdown learning pages", "44 topic checks", "five capstone checks"),
        MODULE_2: ("53 structured Markdown learning pages", "43 topic lessons", "109 knowledge checks"),
        MODULE_3: ("47 structured Markdown learning pages", "35 topic lessons", "82 knowledge checks"),
    }
    for module, statements in module_snapshot_claims.items():
        module_readme = (module / "README.md").read_text(encoding="utf-8")
        for statement in statements:
            if statement not in module_readme:
                errors.append(f"{module.name}/README.md: missing module snapshot claim ({statement})")

    referenced: set[Path] = set()
    for path in markdown:
        body = path.read_text(encoding="utf-8")
        for raw in [*MARKDOWN_LINK.findall(body), *(target for _, target in MARKDOWN_IMAGE.findall(body))]:
            target = raw.strip().split()[0].strip("<>").split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            referenced.add((path.parent / target).resolve())
    for asset in [*svg, *datasets]:
        if asset.resolve() not in referenced:
            errors.append(f"{asset.relative_to(ROOT)}: orphaned asset is not referenced by Markdown")

    for label, (module, _) in MODULES.items():
        if not (module / "REFERENCES.md").exists():
            errors.append(f"{label}: missing reference register")
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

        if path.is_relative_to(ROOT / "assets" / "diagrams"):
            if root.get("role") != "img" or not root.get("aria-labelledby"):
                errors.append(f"{relative}: SVG requires role=img and aria-labelledby")
            if not root.get("viewBox"):
                errors.append(f"{relative}: SVG requires a viewBox for responsive scaling")
            descendants = list(root.iter())
            if any(node.tag.rsplit("}", 1)[-1] == "foreignObject" for node in descendants):
                errors.append(
                    f"{relative}: foreignObject is prohibited because browser text can be clipped"
                )
            if path.is_relative_to(ROOT / "assets" / "diagrams" / "module-3") and path.name.endswith("-workflow.svg"):
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

            if path.is_relative_to(ROOT / "assets" / "diagrams" / "module-3"):
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
        + validate_shared_module_content()
        + validate_svg(svg)
        + validate_csv(datasets)
        + validate_module_1_2_calculations()
        + validate_module_3_content()
        + validate_capstones_and_inventory(markdown, svg, datasets)
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
