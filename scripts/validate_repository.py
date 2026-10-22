#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Validate the public learning repository using only Python's standard library."""

from __future__ import annotations

import csv
import subprocess
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
MODULE_4 = ROOT / "04-internal-operations-inventory"
MODULE_5 = ROOT / "05-forward-reverse-logistics"
MODULE_6 = ROOT / "06-supply-chain-relationships"
MODULE_7 = ROOT / "07-supply-chain-risk"
MODULE_8 = ROOT / "08-optimization-sustainability-technology"
MODULES = {
    "Module 1": (MODULE_1, 44),
    "Module 2": (MODULE_2, 43),
    "Module 3": (MODULE_3, 35),
    "Module 4": (MODULE_4, 51),
    "Module 5": (MODULE_5, 54),
    "Module 6": (MODULE_6, 32),
    "Module 7": (MODULE_7, 31),
    "Module 8": (MODULE_8, 42),
}
# Preserve the exact published inventory and substantive release checks for Modules 1–7;
# extend the shared lesson/capstone rules to authored Module 8 without claiming it
# has already been merged or released from the draft review PR.
RELEASED_MODULES = {label: spec for label, spec in MODULES.items() if label != "Module 8"}
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
    "Commonly confused with",
    "Common mistakes",
    "Original knowledge check",
    "Practitioner perspective",
    "Related concepts",
)
MODULE_OVERVIEW_REQUIRED_HEADINGS = (
    "Learning outcomes",
    "Module path",
    "Module resources",
    "Cross-module handoffs",
    "How each lesson is structured",
    "Module snapshot",
)
SECTION_OVERVIEW_REQUIRED_HEADINGS = (
    "Learning outcomes",
    "Learning path",
    "Working data and visuals",
    "How to study the section",
)
MODULE_RESOURCE_INDEXES = {
    MODULE_1: (
        ROOT / "assets/data/module-1/README.md",
        ROOT / "calculations/forecasting/README.md",
    ),
    MODULE_2: (
        ROOT / "assets/data/module-2/README.md",
        ROOT / "calculations/network-performance/README.md",
    ),
    MODULE_3: (
        ROOT / "assets/data/module-3/README.md",
        ROOT / "calculations/sourcing-procurement/README.md",
    ),
    MODULE_4: (
        ROOT / "assets/data/module-4/README.md",
        ROOT / "calculations/internal-operations/README.md",
    ),
    MODULE_5: (
        ROOT / "assets/data/module-5/README.md",
        ROOT / "calculations/logistics-trade-reverse/README.md",
    ),
    MODULE_6: (
        ROOT / "assets/data/module-6/README.md",
        ROOT / "calculations/relationship-performance/README.md",
    ),
    MODULE_7: (
        ROOT / "assets/data/module-7/README.md",
        ROOT / "calculations/risk-response/README.md",
    ),
    MODULE_8: (
        ROOT / "assets/data/module-8/README.md",
        ROOT / "calculations/module8-capstone/README.md",
    ),
}
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
MODULE_4_DATASET_LINKS = {
    "section-a-planning-operations/02-master-scheduling-and-the-master-scheduling-grid.md": "master-schedule.csv",
    "section-a-planning-operations/04-projected-available-balance-and-mps-logic.md": "master-schedule.csv",
    "section-a-planning-operations/05-allocation-order-promising-and-available-to-promise.md": "master-schedule.csv",
    "section-a-planning-operations/07-mrp-logic-inputs-and-demand-types.md": "mrp-planning.csv",
    "section-a-planning-operations/08-bills-of-material-and-explosion.md": "bom-structure.csv",
    "section-a-planning-operations/10-lead-time-offsetting-planned-receipts-and-releases.md": "mrp-planning.csv",
    "section-a-planning-operations/13-push-pull-and-distribution-requirements-planning.md": "drp-network.csv",
    "section-b-capacity-and-production-activity-control/04-rough-cut-capacity-planning-and-bottleneck-validation.md": "capacity-plan.csv",
    "section-b-capacity-and-production-activity-control/05-capacity-requirements-planning-load-and-manufacturing-lead-time.md": "capacity-work-centers.csv",
    "section-b-capacity-and-production-activity-control/07-measuring-capacity-utilization-efficiency-rated-and-demonstrated-capacity.md": "capacity-work-centers.csv",
    "section-b-capacity-and-production-activity-control/08-balancing-load-and-capacity.md": "capacity-work-centers.csv",
    "section-c-inventory/06-abc-classification-and-pareto-based-control.md": "inventory-item-master.csv",
    "section-c-inventory/07-inventory-and-the-financial-statements.md": "inventory-financials.csv",
    "section-c-inventory/08-order-quantities-lot-for-lot-foq-and-eoq.md": "replenishment-models.csv",
    "section-c-inventory/09-ordering-systems-order-point-periodic-review-and-min-max.md": "replenishment-models.csv",
    "section-c-inventory/12-product-traceability-configuration-and-chain-of-custody.md": "traceability-cycle-count.csv",
    "section-c-inventory/14-end-of-life-obsolescence-returns-and-disposition.md": "returns-disposition.csv",
    "section-d-performance-and-continuous-improvement/01-metrics-kpis-and-performance-architecture.md": "operations-kpis.csv",
    "section-d-performance-and-continuous-improvement/06-basic-quality-tools-i-process-maps-and-control-charts.md": "quality-tools-data.csv",
    "section-d-performance-and-continuous-improvement/07-basic-quality-tools-ii-pareto-and-cause-and-effect.md": "quality-tools-data.csv",
    "section-d-performance-and-continuous-improvement/13-just-in-time-production-and-pull-execution.md": "lean-flow.csv",
    "section-d-performance-and-continuous-improvement/14-six-sigma-and-dmaic.md": "improvement-projects.csv",
    "section-d-performance-and-continuous-improvement/15-theory-of-constraints-and-drum-buffer-rope.md": "improvement-projects.csv",
}
MODULE_5_DATASET_LINKS = {
    "section-a-logistics-and-distribution/01-logistics-scope-functions-and-value-proposition.md": "logistics-strategy.csv",
    "section-a-logistics-and-distribution/02-logistics-objectives-tactics-and-cross-functional-coordination.md": "logistics-strategy.csv",
    "section-a-logistics-and-distribution/03-supply-chain-integration-information-substitution-partner-reduction-and-risk-pooling.md": "logistics-strategy.csv",
    "section-a-logistics-and-distribution/04-3pl-and-4pl-strategy-outsourcing-and-contract-governance.md": "logistics-strategy.csv",
    "section-a-logistics-and-distribution/05-warehousing-strategy-objectives-and-ownership-choices.md": "warehouse-network.csv",
    "section-a-logistics-and-distribution/06-warehouse-network-count-and-location-decisions.md": "warehouse-network.csv",
    "section-a-logistics-and-distribution/07-warehouse-layout-slotting-and-stock-location-strategy.md": "warehouse-network.csv",
    "section-a-logistics-and-distribution/08-warehouse-capacity-forecasting-and-space-sizing.md": "warehouse-capacity.csv",
    "section-a-logistics-and-distribution/09-materials-handling-strategy-and-mechanized-systems.md": "material-handling.csv",
    "section-a-logistics-and-distribution/10-warehouse-automation-systems-and-automation-trade-offs.md": "material-handling.csv",
    "section-a-logistics-and-distribution/11-transportation-strategy-product-movement-and-temporary-storage.md": "transportation-capacity.csv",
    "section-a-logistics-and-distribution/12-transportation-capacity-constraints-and-transport-economics.md": "transportation-capacity.csv",
    "section-a-logistics-and-distribution/13-transportation-capacity-forecasting-planning-and-carrier-readiness.md": "transportation-capacity.csv",
    "section-b-distribution-services-and-transportation-choices/01-warehouse-execution-activities-receive-put-away-pick-pack-move-and-ship.md": "warehouse-operations.csv",
    "section-b-distribution-services-and-transportation-choices/02-value-added-distribution-services-consolidation-break-bulk-cross-dock-and-postponement.md": "warehouse-operations.csv",
    "section-b-distribution-services-and-transportation-choices/03-stockpiling-spot-stocking-assortment-and-mixing.md": "warehouse-operations.csv",
    "section-b-distribution-services-and-transportation-choices/04-channel-design-supply-and-distribution-channels-and-service-outputs.md": "fulfillment-strategies.csv",
    "section-b-distribution-services-and-transportation-choices/05-order-channels-and-fulfillment-strategy-design.md": "fulfillment-strategies.csv",
    "section-b-distribution-services-and-transportation-choices/06-integrated-and-dedicated-fulfillment.md": "fulfillment-strategies.csv",
    "section-b-distribution-services-and-transportation-choices/07-pool-direct-store-store-and-flow-through-fulfillment.md": "fulfillment-strategies.csv",
    "section-b-distribution-services-and-transportation-choices/08-comparing-distribution-strategies.md": "fulfillment-strategies.csv",
    "section-b-distribution-services-and-transportation-choices/09-distribution-network-architectures-manufacturer-distributor-and-aggregator-models.md": "distribution-networks.csv",
    "section-b-distribution-services-and-transportation-choices/10-drop-ship-direct-delivery-and-order-fulfillment-channel-comparison.md": "distribution-networks.csv",
    "section-b-distribution-services-and-transportation-choices/11-transportation-mode-selection-and-value-packaging-density.md": "transport-mode-selection.csv",
    "section-b-distribution-services-and-transportation-choices/12-rail-and-motor-carrier-transport.md": "transport-mode-selection.csv",
    "section-b-distribution-services-and-transportation-choices/13-water-pipeline-and-air-transport.md": "transport-mode-selection.csv",
    "section-b-distribution-services-and-transportation-choices/14-intermodal-package-delivery-and-container-services.md": "transport-mode-selection.csv",
    "section-b-distribution-services-and-transportation-choices/15-carrier-classifications-and-carrier-selection.md": "carrier-options.csv",
    "section-c-trade-considerations/01-trade-compliance-operating-model.md": "trade-compliance-register.csv",
    "section-c-trade-considerations/03-import-export-requirements-and-border-readiness.md": "trade-compliance-register.csv",
    "section-c-trade-considerations/08-incoterms-2020-selection.md": "incoterms-decision-cases.csv",
    "section-c-trade-considerations/11-classification-valuation-duties-and-drawback.md": "border-cost-classification-cases.csv",
    "section-d-reverse-flow/01-reverse-logistics-operating-model.md": "reverse-flow-cases.csv",
    "section-d-reverse-flow/04-reverse-logistics-economics-and-total-cost-analysis.md": "reverse-cost-cases.csv",
    "section-d-reverse-flow/10-waste-hierarchy-and-the-four-rs.md": "waste-disposition-cases.csv",
}

MODULE_6_DATASET_LINKS = {
    "section-a-customer-relationships/02-customer-segmentation-and-customer-focused-marketing.md": "customer-segments.csv",
    "section-a-customer-relationships/03-customer-value-pareto-profitability-and-lifetime-potential.md": "customer-segments.csv",
    "section-a-customer-relationships/05-contact-channel-strategy-and-cost-to-serve-trade-offs.md": "customer-channel-preferences.csv",
    "section-a-customer-relationships/06-customer-information-voc-business-intelligence-and-data-warehouses.md": "customer-voc-interactions.csv",
    "section-a-customer-relationships/08-relationship-lifecycle-prospects-vulnerable-loyal-win-back-churn-and-loyalty.md": "customer-lifecycle-accounts.csv",
    "section-a-customer-relationships/09-lifetime-customer-relationships-and-retention-economics.md": "crm-technology-cases.csv",
    "section-a-customer-relationships/11-crm-technology-architecture-and-customer-data-integration.md": "crm-technology-cases.csv",
    "section-a-customer-relationships/14-customer-service-metrics-satisfaction-feedback-and-service-recovery.md": "customer-service-performance.csv",
    "section-b-supplier-and-supply-chain-relationships/02-supplier-segmentation-and-relationship-fit.md": "supplier-segmentation.csv",
    "section-b-supplier-and-supply-chain-relationships/06-single-sole-and-multisourcing-concentration-and-relationship-risk.md": "supplier-sourcing-relationships.csv",
    "section-b-supplier-and-supply-chain-relationships/08-strategic-partner-selection-and-alliance-rationale.md": "strategic-alliance-cases.csv",
    "section-b-supplier-and-supply-chain-relationships/11-supplier-performance-measurement-and-kpi-governance.md": "supplier-performance.csv",
    "section-b-supplier-and-supply-chain-relationships/12-supplier-certification-rating-systems-and-qualification-evidence.md": "supplier-certification.csv",
    "section-b-supplier-and-supply-chain-relationships/13-supplier-performance-reporting-error-control-claims-and-remediation.md": "supplier-performance.csv",
    "section-b-supplier-and-supply-chain-relationships/17-communication-purpose-audience-channel-feedback-and-management-plans.md": "relationship-communications.csv",
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



def has_plain_language_concept(body: str) -> bool:
    """Accept the shared concept heading or an equivalent substantive concept block."""
    if has_heading(body, "Concept in plain English"):
        return True

    objectives = re.search(
        r"^## Learning objectives\s*$",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    why = re.search(
        r"^## Why it matters\s*$",
        body,
        re.MULTILINE | re.IGNORECASE,
    )
    if not objectives or not why or why.start() <= objectives.end():
        return False

    between = body[objectives.end():why.start()]
    first_concept_heading = re.search(r"^## (?!Why it matters).+?$", between, re.MULTILINE)
    if not first_concept_heading:
        return False

    concept_block = between[first_concept_heading.start():]
    plain = re.sub(r"[^A-Za-z0-9 -]", " ", concept_block)
    words = re.findall(r"\b\w+\b", plain)
    return len(words) >= 40


def validate_module_overviews_and_reviews() -> list[str]:
    """Keep module/section navigation and assessment scaffolding aligned across releases."""
    errors: list[str] = []

    for label, (module, _) in MODULES.items():
        module_readme = module / "README.md"
        if not module_readme.exists():
            errors.append(f"{label}: missing module overview")
            continue

        module_body = module_readme.read_text(encoding="utf-8")
        for heading in MODULE_OVERVIEW_REQUIRED_HEADINGS:
            if not has_heading(module_body, heading):
                errors.append(f"{module.name}/README.md: missing aligned overview section (## {heading})")

        if "status:" not in module_body.lower() or "complete" not in module_body.lower():
            errors.append(f"{module.name}/README.md: module status must explicitly state completion")

        for required_resource in ("../LEARNING-PATHS.md", "../GLOSSARY.md"):
            if required_resource not in module_body:
                errors.append(
                    f"{module.name}/README.md: missing shared repository resource link ({required_resource})"
                )

        for other_module, _ in MODULES.values():
            if other_module == module:
                continue
            # Preserve published Modules 1–7 content while requiring Module 8
            # to link back to every earlier completed module.
            if other_module == MODULE_8 and module in {m for m, _ in RELEASED_MODULES.values()}:
                continue
            target = f"../{other_module.name}/README.md"
            if target not in module_body:
                errors.append(
                    f"{module.name}/README.md: missing cross-module handoff link ({target})"
                )

        section_dirs = sorted(path for path in module.glob("section-*") if path.is_dir())
        if not section_dirs:
            errors.append(f"{label}: no section directories found")

        for section in section_dirs:
            section_readme = section / "README.md"
            if not section_readme.exists():
                errors.append(f"{section.relative_to(ROOT)}: missing section overview")
                continue

            section_body = section_readme.read_text(encoding="utf-8")
            for heading in SECTION_OVERVIEW_REQUIRED_HEADINGS:
                if not has_heading(section_body, heading):
                    errors.append(
                        f"{section_readme.relative_to(ROOT)}: missing aligned section overview (## {heading})"
                    )

            review_files = sorted(section.glob("*-section-*-review.md"))
            if len(review_files) != 1:
                errors.append(
                    f"{section.relative_to(ROOT)}: expected exactly one section review, found {len(review_files)}"
                )
                continue

            review_body = review_files[0].read_text(encoding="utf-8")
            if review_body.count("<details>") < 10:
                errors.append(
                    f"{review_files[0].relative_to(ROOT)}: section review requires at least 10 answer blocks"
                )
            if not re.search(
                r"^## (?:.*completion.*|readiness check|final self-check|final checklist|final memory anchors|module completion step)\s*$",
                review_body,
                re.MULTILINE | re.IGNORECASE,
            ):
                errors.append(
                    f"{review_files[0].relative_to(ROOT)}: missing completion/readiness checkpoint"
                )

        for resource_index in MODULE_RESOURCE_INDEXES[module]:
            if not resource_index.exists():
                errors.append(
                    f"{label}: missing shared resource index ({resource_index.relative_to(ROOT)})"
                )

    return errors


def validate_shared_module_content() -> list[str]:
    """Apply the same minimum lesson contract to every completed module."""
    errors: list[str] = []
    paragraph_uses: dict[str, list[Path]] = {}
    data_links = {
        MODULE_1: MODULE_1_DATASET_LINKS,
        MODULE_2: MODULE_2_DATASET_LINKS,
        MODULE_3: MODULE_3_DATASET_LINKS,
        MODULE_4: MODULE_4_DATASET_LINKS,
        MODULE_5: MODULE_5_DATASET_LINKS,
        MODULE_6: MODULE_6_DATASET_LINKS,
        MODULE_7: {},
        MODULE_8: {},
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
            if not has_plain_language_concept(body):
                errors.append(f"{relative}: missing substantive plain-language concept section")
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
            module_4_flow_exceptions = {
                "section-a-planning-operations/12-mrp-evolution-closed-loop-mrp-mrp-ii-erp-and-ddmrp-context.md",
                "section-c-inventory/01-inventory-fundamentals-types-and-functions.md",
                "section-c-inventory/02-inventory-cost-structure.md",
            }
            module_5_flow_exceptions = {
                "section-a-logistics-and-distribution/01-logistics-scope-functions-and-value-proposition.md",
                "section-b-distribution-services-and-transportation-choices/08-comparing-distribution-strategies.md",
                "section-b-distribution-services-and-transportation-choices/12-rail-and-motor-carrier-transport.md",
                "section-b-distribution-services-and-transportation-choices/13-water-pipeline-and-air-transport.md",
                "section-c-trade-considerations/13-trade-blocs-rules-of-origin-and-agreement-status.md",
                "section-d-reverse-flow/13-product-stewardship-weee-rohs-and-e-waste.md",
            }
            lesson_key = str(path.relative_to(module))
            requires_process_flow = (
                module in (MODULE_2, MODULE_3, MODULE_6, MODULE_7, MODULE_8)
                or (module == MODULE_4 and lesson_key not in module_4_flow_exceptions)
                or (module == MODULE_5 and lesson_key not in module_5_flow_exceptions)
            )
            if requires_process_flow and body.count(f"{FENCE}mermaid") != 1:
                errors.append(f"{relative}: requires exactly one practical Mermaid process flow")
            elif requires_process_flow and (
                not re.search(r"^flowchart (?:TD|LR)\s*$", body, re.MULTILINE)
                or body.count("-->") < 3
            ):
                errors.append(
                    f"{relative}: process flow requires a directed flowchart with at least three transitions"
                )

            if not re.search(
                r"^#{2,3} Evidence retained through the workflow\s*$",
                body,
                re.MULTILINE | re.IGNORECASE,
            ):
                errors.append(f"{relative}: missing workflow evidence")

            if not re.search(
                r"^## (?:Applied|Worked) .+",
                body,
                re.MULTILINE | re.IGNORECASE,
            ):
                errors.append(f"{relative}: missing reusable applied decision or worked-calculation section")

            if not re.search(r"\b(example|northstar|asterworks|rivermark|pinehaven|harborpeak|clearspan|stonebridge|aldergate)\b", body, re.IGNORECASE):
                errors.append(f"{relative}: missing fictional applied example")

            related = re.search(
                r"^## Related concepts\s*\n(?P<section>.*?)(?:\n---\n|\Z)",
                body,
                re.MULTILINE | re.IGNORECASE | re.DOTALL,
            )
            if not related or related.group("section").count("](") < 2:
                errors.append(f"{relative}: related concepts require at least two working links")
            original_footer = bool(re.search(r"\n---\n\n\[(?:Section overview|Previous(?::[^]]*)?)\]", body))
            module8_footer = (module == MODULE_8 and bool(re.search(
                r"\n---\n\n\[(?:Section [ABC] overview|Previous study step|Previous learning step|Previous topic|Section overview)\]",body)))
            if not (original_footer or module8_footer):
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



def validate_module_4_calculations() -> list[str]:
    """Independently reproduce Module 4 calculations used for operating decisions."""
    errors: list[str] = []

    master = sorted(
        csv_dicts("assets/data/module-4/master-schedule.csv"),
        key=lambda row: int(row["week"]),
    )
    prior_pab = float(master[0]["beginning_inventory_units"])
    for row in master:
        week = int(row["week"])
        dtf = int(row["demand_time_fence_end_week"])
        forecast = float(row["forecast_units"])
        orders = float(row["customer_orders_units"])
        mps = float(row["mps_receipt_units"])
        demand = orders if week <= dtf else max(forecast, orders)
        pab = prior_pab + mps - demand
        if not math.isclose(pab, float(row["projected_available_balance_units"]), abs_tol=0.005):
            errors.append(f"Module 4 master schedule: week {week} PAB is inconsistent")
        if not math.isclose(demand, float(row["demand_used_for_pab_units"]), abs_tol=0.005):
            errors.append(f"Module 4 master schedule: week {week} demand basis is inconsistent")
        prior_pab = pab

    receipt_indexes = [i for i, row in enumerate(master) if float(row["mps_receipt_units"]) > 0]
    for position, i in enumerate(receipt_indexes):
        row = master[i]
        end = receipt_indexes[position + 1] if position + 1 < len(receipt_indexes) else len(master)
        orders_to_next_receipt = sum(float(item["customer_orders_units"]) for item in master[i:end])
        supply = float(row["mps_receipt_units"])
        if i == 0:
            supply += float(row["beginning_inventory_units"])
        atp = supply - orders_to_next_receipt
        recorded = row["available_to_promise_units"]
        if not recorded or not math.isclose(atp, float(recorded), abs_tol=0.005):
            errors.append(f"Module 4 master schedule: week {row['week']} ATP is inconsistent")

    capacity = csv_dicts("assets/data/module-4/capacity-work-centers.csv")
    for row in capacity:
        available = (
            float(row["hours_operation_per_day"])
            * float(row["days_per_period"])
            * float(row["number_of_resources"])
        )
        actual = float(row["actual_hours_worked"])
        standard = float(row["standard_hours_of_output"])
        utilization = actual / available * 100
        efficiency = standard / actual * 100
        rated = available * (utilization / 100) * (efficiency / 100)
        demonstrated = statistics.mean(
            float(row[column])
            for column in (
                "demonstrated_output_period_1_standard_hours",
                "demonstrated_output_period_2_standard_hours",
                "demonstrated_output_period_3_standard_hours",
            )
        )
        checks = (
            (available, float(row["available_hours"]), "available hours"),
            (utilization, float(row["utilization_pct"]), "utilization"),
            (efficiency, float(row["efficiency_pct"]), "efficiency"),
            (rated, float(row["rated_capacity_standard_hours"]), "rated capacity"),
            (demonstrated, float(row["demonstrated_capacity_standard_hours"]), "demonstrated capacity"),
        )
        for calculated, recorded, label in checks:
            if not math.isclose(calculated, recorded, abs_tol=0.02):
                errors.append(
                    f"Module 4 capacity dataset: {row['work_center']} {label} is inconsistent"
                )

    item_master = csv_dicts("assets/data/module-4/inventory-item-master.csv")
    for row in item_master:
        annual_value = float(row["annual_usage_units"]) * float(row["unit_value_usd"])
        if not math.isclose(annual_value, float(row["annual_monetary_volume_usd"]), abs_tol=0.01):
            errors.append(
                f"Module 4 inventory item master: {row['sku']} annual monetary volume is inconsistent"
            )

    financials = csv_dicts("assets/data/module-4/inventory-financials.csv")
    for row in financials:
        average_inventory = (
            float(row["beginning_inventory_usd"]) + float(row["ending_inventory_usd"])
        ) / 2
        turns = float(row["annual_cogs_usd"]) / average_inventory
        equation = (
            float(row["total_assets_usd"])
            - float(row["total_liabilities_usd"])
            - float(row["owners_equity_usd"])
        )
        if not math.isclose(average_inventory, float(row["average_inventory_usd"]), abs_tol=0.01):
            errors.append(f"Module 4 inventory financials: {row['scenario']} average inventory is inconsistent")
        if not math.isclose(turns, float(row["inventory_turns"]), abs_tol=0.001):
            errors.append(f"Module 4 inventory financials: {row['scenario']} inventory turns are inconsistent")
        if not math.isclose(equation, float(row["accounting_equation_check_usd"]), abs_tol=0.01):
            errors.append(f"Module 4 inventory financials: {row['scenario']} accounting equation is inconsistent")

    replenishment = {
        row["sku"]: row for row in csv_dicts("assets/data/module-4/replenishment-models.csv")
    }
    for sku, row in replenishment.items():
        demand = float(row["annual_demand_units"])
        order_cost = float(row["ordering_cost_usd"])
        carrying_rate = float(row["annual_carrying_rate"])
        unit_cost = float(row["unit_cost_usd"])
        eoq = math.sqrt((2 * demand * order_cost) / (carrying_rate * unit_cost))
        if not math.isclose(eoq, float(row["eoq_units"]), abs_tol=0.02):
            errors.append(f"Module 4 replenishment dataset: {sku} EOQ is inconsistent")
        order_point = (
            float(row["demand_units_per_day"]) * float(row["lead_time_days"])
            + float(row["safety_stock_units"])
        )
        if not math.isclose(order_point, float(row["order_point_units"]), abs_tol=0.02):
            errors.append(f"Module 4 replenishment dataset: {sku} order point is inconsistent")

    periodic = replenishment["PH-CNK500"]
    maximum = (
        float(periodic["demand_units_per_day"])
        * (float(periodic["review_interval_days"]) + float(periodic["lead_time_days"]))
        + float(periodic["safety_stock_units"])
    )
    order_quantity = maximum - float(periodic["on_hand_units"])
    if not math.isclose(maximum, float(periodic["periodic_review_max_level_units"]), abs_tol=0.01):
        errors.append("Module 4 replenishment dataset: periodic-review maximum is inconsistent")
    if not math.isclose(order_quantity, float(periodic["periodic_review_order_quantity_units"]), abs_tol=0.01):
        errors.append("Module 4 replenishment dataset: periodic-review order quantity is inconsistent")

    fuse = replenishment["PH-FUSE7"]
    if float(fuse["max_level_units"]) - float(fuse["on_hand_units"]) != 1550:
        errors.append("Module 4 replenishment dataset: PH-FUSE7 min-max order should be 1,550 units")

    lean = csv_dicts("assets/data/module-4/lean-flow.csv")
    for row in lean:
        takt = (
            float(row["available_production_time_min_per_shift"])
            / float(row["customer_demand_units_per_shift"])
        )
        if not math.isclose(takt, float(row["takt_time_min_per_unit"]), abs_tol=0.001):
            errors.append(f"Module 4 lean dataset: {row['process_step']} takt time is inconsistent")

    quality = csv_dicts("assets/data/module-4/quality-tools-data.csv")
    pareto = [row for row in quality if row["record_type"] == "pareto"]
    total_defects = sum(int(row["defect_count"]) for row in pareto)
    top_three = sum(sorted((int(row["defect_count"]) for row in pareto), reverse=True)[:3])
    if total_defects != 66 or not math.isclose(top_three / total_defects * 100, 80.3030, abs_tol=0.01):
        errors.append("Module 4 quality dataset: Pareto total or cumulative share is inconsistent")
    control_values = [
        float(row["measurement"]) for row in quality if row["record_type"] == "control_chart"
    ]
    if not math.isclose(statistics.mean(control_values), 5.0241667, abs_tol=0.0001):
        errors.append("Module 4 quality dataset: control-chart mean is inconsistent")
    if not math.isclose(statistics.stdev(control_values), 0.04776, abs_tol=0.0001):
        errors.append("Module 4 quality dataset: control-chart sample standard deviation is inconsistent")

    improvements = csv_dicts("assets/data/module-4/improvement-projects.csv")
    toc = next(row for row in improvements if row["project_or_constraint"] == "Burn-in test cell")
    if (float(toc["capacity_or_throughput_before"]), float(toc["capacity_or_throughput_after"])) != (144.0, 154.0):
        errors.append("Module 4 improvement dataset: TOC burn-in capacity case is inconsistent")

    solution = (MODULE_4 / "capstone/solution-guide.md").read_text(encoding="utf-8")
    for required in (
        "154 standard hours/week",
        "11 standard hours remaining overload",
        "306.85 units",
        "1,100 units",
        "886 units",
        "80.30%",
        "5.0242 mm",
    ):
        if required not in solution:
            errors.append(f"Module 4 capstone solution: missing verified result ({required})")

    return errors



def validate_module_5_calculations() -> list[str]:
    """Independently reproduce Module 5 logistics, trade, and reverse-flow controls."""
    errors: list[str] = []

    def rows(name: str) -> list[dict[str, str]]:
        return csv_dicts(f"assets/data/module-5/{name}")

    def close(calculated: float, recorded: float, label: str, tol: float = 0.02) -> None:
        if not math.isclose(float(calculated), float(recorded), abs_tol=tol, rel_tol=1e-9):
            errors.append(
                f"Module 5 {label}: calculated {calculated}, recorded {recorded}"
            )

    for row in rows("logistics-strategy.csv"):
        total = sum(
            float(row[column])
            for column in (
                "transport_cost",
                "warehouse_cost",
                "inventory_cost",
                "failure_exposure_cost",
            )
        )
        close(total, float(row["total_logistics_cost"]), f"logistics total {row['option']}", 0.01)

    capacity_rows = rows("warehouse-capacity.csv")
    for row in capacity_rows:
        year = row["year"]
        pallet_cube = (
            float(row["pallet_length_m"])
            * float(row["pallet_width_m"])
            * float(row["loaded_height_m"])
        )
        close(pallet_cube, float(row["cube_per_pallet_m3"]), f"{year} pallet cube")
        base_bays = float(row["forecast_inventory_cube_m3"]) / pallet_cube
        close(base_bays, float(row["base_bays"]), f"{year} base bays")
        adjusted_bays = base_bays * float(row["partial_pallet_factor"])
        close(adjusted_bays, float(row["adjusted_bays"]), f"{year} adjusted bays")
        raw = adjusted_bays * float(row["pallet_floor_footprint_m2"])
        close(raw, float(row["raw_inventory_footprint_m2"]), f"{year} raw footprint")
        handling = raw * float(row["movement_aisle_factor"])
        close(
            handling,
            float(row["handling_adjusted_footprint_m2"]),
            f"{year} handling footprint",
        )
        vertical = handling / float(row["vertical_storage_levels"])
        close(
            vertical,
            float(row["vertical_adjusted_area_m2"]),
            f"{year} vertical area",
        )
        core = vertical / float(row["target_utilization"])
        close(core, float(row["required_core_area_m2"]), f"{year} core area")
        total = core + float(row["bulk_storage_allowance_m2"])
        close(total, float(row["required_total_area_m2"]), f"{year} total area")

    for row in rows("transportation-capacity.csv"):
        required = (
            float(row["base_forecast_units_week"])
            + float(row["promotion_adjustment_units_week"])
        )
        close(
            required,
            float(row["required_capacity_units_week"]),
            f"lane required {row['lane']}",
            0.001,
        )
        gap = float(row["reserved_capacity_units_week"]) - required
        close(
            gap,
            float(row["capacity_gap_units_week"]),
            f"lane gap {row['lane']}",
            0.001,
        )

    for row in rows("transport-mode-selection.csv"):
        value_density = float(row["cargo_value_usd"]) / float(row["packed_volume_m3"])
        packaging_density = float(row["units"]) / float(row["packed_volume_m3"])
        close(
            value_density,
            float(row["value_density_usd_m3"]),
            f"value density {row['shipment']} {row['mode']}",
        )
        close(
            packaging_density,
            float(row["packaging_density_units_m3"]),
            f"packaging density {row['shipment']} {row['mode']}",
        )

    for row in rows("border-cost-classification-cases.csv"):
        value = float(row["training_customs_value_usd"])
        duty = value * float(row["training_duty_rate_decimal"])
        tax = value * float(row["training_import_tax_rate_decimal"])
        landed = (
            value
            + duty
            + tax
            + float(row["international_freight_usd"])
            + float(row["broker_and_entry_fees_usd"])
        )
        close(duty, float(row["expected_training_duty_usd"]), f"duty {row['case_id']}")
        close(tax, float(row["expected_training_import_tax_usd"]), f"tax {row['case_id']}")
        close(
            landed,
            float(row["expected_training_landed_cost_usd"]),
            f"landed cost {row['case_id']}",
        )

    expected_return_rates = {
        "RF-01": 5.0,
        "RF-02": 12.0,
        "RF-03": 4.0,
        "RF-04": 12.0,
        "RF-05": 6.0,
    }
    for row in rows("reverse-flow-cases.csv"):
        rate = float(row["units_returned"]) / float(row["units_shipped"]) * 100
        close(rate, expected_return_rates[row["case_id"]], f"return rate {row['case_id']}", 0.0001)

    expected_reverse_net = {
        "RC-01": 23000.0,
        "RC-02": -52300.0,
        "RC-03": -31700.0,
        "RC-04": -4100.0,
    }
    for row in rows("reverse-cost-cases.csv"):
        cost = sum(
            float(row[column])
            for column in (
                "return_credits_usd",
                "reverse_transport_usd",
                "processing_handling_usd",
                "repair_parts_usd",
                "reverse_warehousing_usd",
                "disposal_compliance_usd",
            )
        )
        benefit = sum(
            float(row[column])
            for column in (
                "resale_liquidation_revenue_usd",
                "repair_fee_revenue_usd",
                "recycling_revenue_usd",
                "restocking_fee_revenue_usd",
                "incentive_value_usd",
                "estimated_warranty_sales_uplift_usd",
            )
        )
        close(
            benefit - cost,
            expected_reverse_net[row["case_id"]],
            f"reverse result {row['case_id']}",
            0.01,
        )

    networks: dict[str, dict[str, float | bool]] = {}
    for row in rows("warehouse-network.csv"):
        aggregate = networks.setdefault(
            row["network_option"],
            {
                "cost": 0.0,
                "coverage": 0.0,
                "response_num": 0.0,
                "service_num": 0.0,
                "all_pass": True,
            },
        )
        coverage = float(row["service_coverage_pct"])
        aggregate["coverage"] = float(aggregate["coverage"]) + coverage
        aggregate["cost"] = float(aggregate["cost"]) + sum(
            float(row[column])
            for column in (
                "transport_cost_annual",
                "inventory_cost_annual",
                "overhead_annual",
            )
        )
        aggregate["response_num"] = (
            float(aggregate["response_num"])
            + coverage * float(row["customer_response_days"])
        )
        aggregate["service_num"] = (
            float(aggregate["service_num"])
            + coverage * float(row["services_score_5"])
        )
        aggregate["all_pass"] = bool(aggregate["all_pass"]) and (
            row["labor_flag"] == "PASS" and row["regulatory_flag"] == "PASS"
        )

    two_dc = networks["2-DC owned"]
    three_dc = networks["3-DC hybrid"]
    close(float(two_dc["cost"]), 8350000.0, "2-DC owned aggregate cost", 0.01)
    close(
        float(two_dc["response_num"]) / float(two_dc["coverage"]),
        2.44,
        "2-DC owned weighted response",
        0.001,
    )
    close(float(three_dc["cost"]), 8670000.0, "3-DC hybrid aggregate cost", 0.01)
    close(
        float(three_dc["response_num"]) / float(three_dc["coverage"]),
        1.629,
        "3-DC hybrid weighted response",
        0.001,
    )

    row_2030 = next(row for row in capacity_rows if row["year"] == "2030")
    close(
        float(row_2030["required_total_area_m2"]),
        8239.26,
        "2030 required total area",
        0.01,
    )
    row_2031 = next(row for row in capacity_rows if row["year"] == "2031")
    sensitivity = (
        float(row_2031["handling_adjusted_footprint_m2"])
        / 4
        / float(row_2031["target_utilization"])
        + float(row_2031["bulk_storage_allowance_m2"])
    )
    close(sensitivity, 9322.22, "2031 four-level sensitivity", 0.01)

    supplier_lane = next(
        row
        for row in rows("transportation-capacity.csv")
        if row["lane"] == "Supplier Bay-Cedar"
    )
    close(float(supplier_lane["capacity_gap_units_week"]), -15.0, "Supplier Bay-Cedar gap", 0.001)

    tc_007 = next(
        row
        for row in rows("trade-compliance-register.csv")
        if row["shipment_id"] == "TC-007"
    )
    if tc_007["compliance_risk"] != "Critical":
        errors.append("Module 5 trade-compliance register: TC-007 risk must remain Critical")

    solution = (MODULE_5 / "capstone/solution-guide.md").read_text(encoding="utf-8")
    for required in ("8,239.26", "9,322.22", "1.629", "90,250", "−15 units/week"):
        if required not in solution:
            errors.append(f"Module 5 capstone solution: missing verified result ({required})")

    return errors

def validate_module_6_calculations() -> list[str]:
    """Independently reproduce Module 6 relationship-management controls."""
    errors: list[str] = []

    def rows(name: str) -> list[dict[str, str]]:
        return csv_dicts(f"assets/data/module-6/{name}")

    def close(calculated: float, recorded: float, label: str, tol: float = 0.02) -> None:
        if not math.isclose(float(calculated), float(recorded), abs_tol=tol, rel_tol=1e-9):
            errors.append(
                f"Module 6 {label}: calculated {calculated}, recorded {recorded}"
            )

    # Customer-segment economics.
    segments = rows("customer-segments.csv")
    for row in segments:
        gross_profit = float(row["annual_revenue_usd"]) * float(row["gross_margin_pct"]) / 100
        avg_order = float(row["annual_revenue_usd"]) / float(row["annual_orders"])
        revenue_account = float(row["annual_revenue_usd"]) / float(row["active_accounts"])
        close(gross_profit, float(row["annual_gross_profit_usd"]), f"gross profit {row['segment_id']}", 0.01)
        close(avg_order, float(row["avg_order_value_usd"]), f"average order value {row['segment_id']}", 0.01)
        close(revenue_account, float(row["revenue_per_account_usd"]), f"revenue/account {row['segment_id']}", 0.01)

    # Channel preference percentages and dominant channel.
    for row in rows("customer-channel-preferences.csv"):
        respondents = float(row["respondents"])
        counts = {
            "Portal": float(row["portal_count"]),
            "Email": float(row["email_count"]),
            "Phone / chat": float(row["phone_chat_count"]),
            "Field representative": float(row["field_rep_count"]),
        }
        if not math.isclose(sum(counts.values()), respondents, abs_tol=0.001):
            errors.append(f"Module 6 channel preferences: counts do not total respondents for {row['segment_id']}")
        for count_col, pct_col in (
            ("portal_count", "portal_pct"),
            ("email_count", "email_pct"),
            ("phone_chat_count", "phone_chat_pct"),
            ("field_rep_count", "field_rep_pct"),
        ):
            calculated = float(row[count_col]) / respondents * 100
            close(calculated, float(row[pct_col]), f"channel percentage {row['segment_id']} {pct_col}")
        dominant_name, dominant_count = max(counts.items(), key=lambda item: item[1])
        if row["dominant_channel"] != dominant_name:
            errors.append(f"Module 6 channel preferences: dominant channel is inconsistent for {row['segment_id']}")
        close(dominant_count / respondents * 100, float(row["dominant_channel_pct"]), f"dominant channel percentage {row['segment_id']}")

    # Selected lifecycle diagnostic sample.
    lifecycle = rows("customer-lifecycle-accounts.csv")
    active_start = sum(int(row["active_at_period_start"]) for row in lifecycle)
    churned = sum(int(row["churn_flag"]) for row in lifecycle)
    retained = sum(int(row["retained_flag"]) for row in lifecycle)
    if (active_start, churned, retained) != (16, 5, 11):
        errors.append("Module 6 lifecycle sample: start/churn/retention counts are inconsistent")
    churn_rate = churned / active_start * 100
    retention_rate = retained / active_start * 100
    close(churn_rate, 31.25, "selected-sample churn rate", 0.0001)
    close(retention_rate, 68.75, "selected-sample retention rate", 0.0001)
    vulnerable_current = sum(
        float(row["current_12m_revenue_usd"])
        for row in lifecycle
        if row["relationship_type"].lower() == "vulnerable"
    )
    churned_prior = sum(
        float(row["prior_12m_revenue_usd"])
        for row in lifecycle
        if int(row["churn_flag"]) == 1
    )
    close(vulnerable_current, 2377000.0, "vulnerable-account current revenue", 0.01)
    close(churned_prior, 2667000.0, "churned-account prior revenue", 0.01)

    # VOC response and corrective-action closure.
    voc = rows("customer-voc-interactions.csv")
    response_required = [row for row in voc if int(row["requires_response"]) == 1]
    response_attainment = (
        sum(int(row["response_met_target"]) for row in response_required)
        / len(response_required)
        * 100
    )
    corrective_due = [row for row in voc if int(row["corrective_action_due"]) == 1]
    corrective_closure = (
        sum(int(row["corrective_action_closure_flag"]) for row in corrective_due)
        / len(corrective_due)
        * 100
    )
    close(response_attainment, 54.5454545, "VOC response attainment", 0.01)
    close(corrective_closure, 46.1538462, "VOC corrective-action closure", 0.01)

    # CRM economics, feasibility, and decision-changing adoption sensitivity.
    crm = rows("crm-technology-cases.csv")
    for row in crm:
        tco = (
            float(row["implementation_usd"])
            + 3 * float(row["annual_subscription_usd"])
            + float(row["integration_usd"])
            + float(row["training_usd"])
        )
        annual_benefit = (
            float(row["annual_labor_savings_usd"])
            + float(row["annual_retention_margin_uplift_usd"])
        )
        benefit = 3 * annual_benefit * float(row["expected_adoption_pct"]) / 100
        net = benefit - tco
        close(tco, float(row["three_year_tco_usd"]), f"CRM TCO {row['case_id']}", 0.01)
        close(benefit, float(row["three_year_realized_benefit_usd"]), f"CRM benefit {row['case_id']}", 0.01)
        close(net, float(row["three_year_net_benefit_usd"]), f"CRM net benefit {row['case_id']}", 0.01)
        expected_gate = "PASS" if all(
            row[column] == "PASS"
            for column in ("process_fit_gate", "data_access_gate", "security_gate")
        ) else "FAIL"
        if row["feasibility_gate"] != expected_gate:
            errors.append(f"Module 6 CRM dataset: feasibility gate is inconsistent for {row['case_id']}")

    crm02 = next(row for row in crm if row["case_id"] == "CRM-02")
    close(float(crm02["three_year_tco_usd"]), 1135000.0, "CRM-02 TCO", 0.01)
    close(float(crm02["three_year_realized_benefit_usd"]), 1377000.0, "CRM-02 benefit", 0.01)
    close(float(crm02["three_year_net_benefit_usd"]), 242000.0, "CRM-02 net benefit", 0.01)
    annual_benefit = float(crm02["annual_labor_savings_usd"]) + float(crm02["annual_retention_margin_uplift_usd"])
    sensitivity_benefit = 3 * annual_benefit * 0.70
    sensitivity_net = sensitivity_benefit - float(crm02["three_year_tco_usd"])
    break_even = float(crm02["three_year_tco_usd"]) / (3 * annual_benefit) * 100
    close(sensitivity_benefit, 1071000.0, "CRM-02 70 percent benefit", 0.01)
    close(sensitivity_net, -64000.0, "CRM-02 70 percent net benefit", 0.01)
    close(break_even, 74.1830065, "CRM-02 break-even adoption", 0.001)

    # Customer-service measures.
    service = rows("customer-service-performance.csv")
    for row in service:
        eligible_orders = float(row["eligible_orders"])
        checks = (
            (float(row["orders_shipped_complete"]) / eligible_orders * 100, row["orders_shipped_complete_pct"], "complete"),
            (float(row["on_time_receipts"]) / float(row["eligible_receipts"]) * 100, row["on_time_delivery_pct"], "OTD"),
            (float(row["units_shipped_on_schedule"]) / float(row["units_ordered"]) * 100, row["unit_fill_rate_pct"], "unit fill"),
            (float(row["orders_complete_and_on_time"]) / eligible_orders * 100, row["otif_pct"], "OTIF"),
            (float(row["stockout_events"]) / float(row["item_availability_checks"]) * 100, row["stockout_frequency_pct"], "stockout"),
            (float(row["complaints"]) / eligible_orders * 100, row["complaint_rate_per_100_orders"], "complaint rate"),
            (float(row["responses_within_target"]) / float(row["customer_inquiries_requiring_response"]) * 100, row["response_time_attainment_pct"], "response attainment"),
        )
        for calculated, recorded, label in checks:
            close(calculated, float(recorded), f"{label} {row['segment_id']}")
    service_networks = next(row for row in service if row["segment_name"] == "Service Networks")
    close(float(service_networks["otif_pct"]), 86.23, "Service Networks OTIF", 0.001)

    # Sourcing concentration logic.
    sourcing = rows("supplier-sourcing-relationships.csv")
    for row in sourcing:
        share = float(row["supplier_spend_usd"]) / float(row["category_spend_usd"]) * 100
        close(share, float(row["supplier_share_pct"]), f"supplier share {row['supplier_id']}")
        if row["source_strategy"] == "sole" or share >= 90 or int(row["qualified_alternates"]) == 0:
            expected = "Critical"
        elif share >= 70 or int(row["qualified_alternates"]) <= 1:
            expected = "High"
        elif share >= 40:
            expected = "Moderate"
        else:
            expected = "Low"
        if row["concentration_risk"] != expected:
            errors.append(f"Module 6 sourcing relationships: concentration risk is inconsistent for {row['supplier_id']}")

    # Alliance gates and weighted ranking.
    alliances = rows("strategic-alliance-cases.csv")
    alliance_weights = {
        "value_add_score": 20,
        "market_access_score": 10,
        "operations_strength_score": 15,
        "technology_strength_score": 15,
        "strategic_growth_score": 15,
        "learning_score": 10,
        "financial_strength_score": 15,
    }
    feasible_scores: list[tuple[str, float]] = []
    for row in alliances:
        score = sum(float(row[column]) / 5 * weight for column, weight in alliance_weights.items())
        close(score, float(row["weighted_alliance_score_0_to_100"]), f"alliance score {row['case_id']}", 0.01)
        expected_gate = "PASS" if all(
            row[column] == "PASS"
            for column in (
                "strategy_fit_gate",
                "ethics_compliance_gate",
                "financial_viability_gate",
                "ip_security_gate",
                "capacity_continuity_gate",
            )
        ) else "FAIL"
        if row["feasibility_gate"] != expected_gate:
            errors.append(f"Module 6 alliance dataset: feasibility gate is inconsistent for {row['case_id']}")
        if expected_gate == "PASS":
            feasible_scores.append((row["case_id"], score))
    feasible_scores.sort(key=lambda item: item[1], reverse=True)
    ranks = {case_id: rank for rank, (case_id, _) in enumerate(feasible_scores, 1)}
    for row in alliances:
        recorded = row["feasible_rank"].strip()
        if row["feasibility_gate"] == "PASS":
            if recorded != str(ranks[row["case_id"]]):
                errors.append(f"Module 6 alliance dataset: feasible rank is inconsistent for {row['case_id']}")
        elif recorded:
            errors.append(f"Module 6 alliance dataset: failed alliance {row['case_id']} must not have a feasible rank")
    if feasible_scores[0][0] != "AL-01":
        errors.append("Module 6 alliance dataset: NorthRiver Joint Innovation must remain the top feasible alliance")

    # Supplier performance.
    performance = rows("supplier-performance.csv")
    for row in performance:
        otd = float(row["on_time_receipts"]) / float(row["eligible_receipts"]) * 100
        defect = float(row["defect_units"]) / float(row["inspected_units"]) * 100
        closure = float(row["corrective_actions_closed"]) / float(row["corrective_actions_due"]) * 100
        quality_score = max(0.0, 100 - defect * 10)
        cost_score = min(100.0, float(row["cost_reduction_pct"]) / 3.0 * 100)
        weighted = (
            otd * 0.25
            + quality_score * 0.20
            + closure * 0.15
            + float(row["internal_customer_score_1_to_5"]) * 20 * 0.10
            + float(row["technology_integration_score_1_to_5"]) * 20 * 0.10
            + cost_score * 0.10
            + float(row["response_flexibility_score_1_to_5"]) * 20 * 0.10
        )
        close(otd, float(row["supplier_on_time_delivery_pct"]), f"supplier OTD {row['supplier_id']}")
        close(defect, float(row["supplier_defect_rate_pct"]), f"supplier defect {row['supplier_id']}")
        close(closure, float(row["corrective_action_closure_pct"]), f"supplier corrective closure {row['supplier_id']}")
        close(weighted, float(row["weighted_supplier_performance_score_0_to_100"]), f"supplier weighted score {row['supplier_id']}")
    bluemesa = next(row for row in performance if row["supplier_id"] == "S04")
    close(float(bluemesa["weighted_supplier_performance_score_0_to_100"]), 72.19, "BlueMesa supplier score", 0.01)

    # Supplier certification status logic.
    for row in rows("supplier-certification.csv"):
        audit = float(row["audit_score_pct"])
        critical = int(row["critical_nonconformances"])
        major = int(row["major_nonconformances"])
        documents = row["required_documents_complete"] == "YES"
        delivery = row["delivery_gate"] == "PASS"
        quality = row["quality_system_gate"] == "PASS"
        safety = row["safety_gate"] == "PASS"
        actions = int(row["open_corrective_actions"])
        if critical > 0 or not quality or not safety:
            expected_status, months = "NOT CERTIFIED", 3
        elif audit >= 90 and major <= 1 and documents and delivery and actions == 0:
            expected_status, months = "CERTIFIED", 12
        elif audit >= 80 and major <= 2 and documents and delivery and actions <= 2:
            expected_status, months = "CONDITIONAL", 6
        else:
            expected_status, months = "REMEDIATION", 3
        if row["certification_status"] != expected_status or int(row["requalification_months"]) != months:
            errors.append(f"Module 6 supplier certification: status logic is inconsistent for {row['supplier_id']}")
    blue_cert = next(row for row in rows("supplier-certification.csv") if row["supplier_id"] == "S04")
    if blue_cert["certification_status"] != "NOT CERTIFIED":
        errors.append("Module 6 supplier certification: BlueMesa must remain NOT CERTIFIED")

    # Communication calculations and structural controls.
    for row in rows("relationship-communications.csv"):
        planned = float(row["planned_messages"])
        sent = float(row["messages_sent"])
        acknowledgements = float(row["acknowledgements_received"])
        feedback_expected = float(row["feedback_expected"])
        feedback_received = float(row["feedback_received"])
        actions_due = float(row["actions_due"])
        actions_closed = float(row["actions_closed"])
        close(sent / planned * 100, float(row["message_delivery_pct"]), f"message delivery {row['communication_id']}")
        close(acknowledgements / sent * 100, float(row["acknowledgement_pct"]), f"acknowledgement {row['communication_id']}")
        close(feedback_received / feedback_expected * 100, float(row["feedback_rate_pct"]), f"feedback {row['communication_id']}")
        close(actions_closed / actions_due * 100, float(row["action_closure_pct"]), f"action closure {row['communication_id']}")
        structural_pass = all(
            row[field].strip()
            for field in ("responsible_owner", "accountable_owner", "medium", "cadence")
        ) and sent <= planned and acknowledgements <= sent and feedback_received <= feedback_expected and actions_closed <= actions_due
        expected_control = "PASS" if structural_pass else "FAIL"
        if row["communication_control_pass"] != expected_control:
            errors.append(f"Module 6 communication controls: structural control is inconsistent for {row['communication_id']}")

    solution = (MODULE_6 / "capstone/solution-guide.md").read_text(encoding="utf-8")
    for required in ("31.25%", "86.23%", "$242,000", "72.19", "74.18%", "88/100"):
        if required not in solution:
            errors.append(f"Module 6 capstone solution: missing verified result ({required})")

    return errors


def validate_module_6_assessment_distribution() -> list[str]:
    """Prevent predictable answer-position bias in Module 6 assessments."""
    errors: list[str] = []

    def correct_letters(path: Path) -> list[str]:
        body = path.read_text(encoding="utf-8")
        return re.findall(
            r"^### Correct answer\s*\n\s*\*\*([A-D])\.",
            body,
            re.MULTILINE,
        )

    topic_paths = sorted(
        path
        for path in MODULE_6.glob("section-*/*.md")
        if re.match(r"\d{2}-", path.name)
        and not re.match(r"\d{2}-section-[a-z]-review\.md$", path.name)
    )
    topic_letters = [letter for path in topic_paths for letter in correct_letters(path)]
    if len(topic_letters) != 32:
        errors.append(f"Module 6 assessments: expected 32 topic answers, found {len(topic_letters)}")
    else:
        counts = {letter: topic_letters.count(letter) for letter in "ABCD"}
        if any(count < 6 or count > 10 for count in counts.values()):
            errors.append(f"Module 6 assessments: topic answer positions are imbalanced ({counts})")

    review_paths = [
        MODULE_6 / "section-a-customer-relationships/15-section-a-review.md",
        MODULE_6 / "section-b-supplier-and-supply-chain-relationships/19-section-b-review.md",
    ]
    review_letters = [letter for path in review_paths for letter in correct_letters(path)]
    if len(review_letters) != 32:
        errors.append(f"Module 6 assessments: expected 32 section-review answers, found {len(review_letters)}")
    else:
        counts = {letter: review_letters.count(letter) for letter in "ABCD"}
        if any(count < 6 or count > 10 for count in counts.values()):
            errors.append(f"Module 6 assessments: section-review answer positions are imbalanced ({counts})")

    capstone_letters = correct_letters(MODULE_6 / "capstone/README.md")
    if len(capstone_letters) != 5:
        errors.append(f"Module 6 assessments: expected 5 capstone answers, found {len(capstone_letters)}")
    else:
        counts = {letter: capstone_letters.count(letter) for letter in "ABCD"}
        if set(capstone_letters) != set("ABCD") or max(counts.values()) > 2:
            errors.append(f"Module 6 assessments: capstone answer positions are imbalanced ({counts})")

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
        "Module 4": (
            MODULE_4,
            1800,
            15,
            ("154 standard hours/week", "11 standard hours remaining overload", "306.85 units"),
        ),
        "Module 5": (
            MODULE_5,
            1800,
            16,
            ("8,239.26", "9,322.22", "1.629", "90,250", "−15 units/week"),
        ),
        "Module 6": (
            MODULE_6,
            2200,
            12,
            ("31.25%", "86.23%", "$242,000", "72.19", "74.18%", "88/100"),
        ),
        "Module 7": (MODULE_7, 2200, 12, ("$45,000", "$28,600", "$36,500", "$11,500")),
        "Module 8": (MODULE_8, 2500, 11, ("$35,813", "$185,000", "$108,000", "66%", "−$153,726")),
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
        # Retain the exact legacy Modules 1–7 table check; Module 8 also
        # permits valid Markdown separators written with spaces (| --- |).
        module8_spaced_tables = (label == "Module 8" and len(re.findall(
            r"(?m)^\|\s*-{3,}", solution)) >= 2)
        if solution.count("|---") < 2 and not module8_spaced_tables:
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

    module_markdown = [path for path in markdown if any(path.is_relative_to(module) for module, _ in RELEASED_MODULES.values())]
    details = sum(path.read_text(encoding="utf-8").count("<details>") for path in module_markdown)
    if len(module_markdown) != 369:
        errors.append(f"Repository inventory: expected 369 module Markdown files, found {len(module_markdown)}")
    # Baseline inventory counts describe the seven *released* modules.
    # Draft Module 8 assets still pass the universal SVG/CSV/link/orphan gates
    # and the separate Section A development validator, but must not alter
    # the immutable released baseline snapshot before the full Module 8 release.
    released_svg = [p for p in svg if not p.is_relative_to(ROOT / "assets/diagrams/module-8")]
    released_data = [p for p in datasets if not p.is_relative_to(ROOT / "assets/data/module-8")]
    if len(released_svg) != 250:
        errors.append(f"Repository inventory: expected 250 released SVG files, found {len(released_svg)}")
    if len(released_data) != 101:
        errors.append(f"Repository inventory: expected 101 released CSV files, found {len(released_data)}")
    if details != 723:
        errors.append(f"Repository inventory: expected 723 knowledge checks, found {details}")

    # Keep v7 baseline immutable while testing the completed eighth-module draft.
    module8_md = [p for p in markdown if p.is_relative_to(MODULE_8)]
    module8_svgs = [p for p in svg if p.is_relative_to(ROOT / "assets/diagrams/module-8")]
    module8_csvs = [p for p in datasets if p.is_relative_to(ROOT / "assets/data/module-8")]
    module8_answer_blocks = sum(p.read_text(encoding="utf-8").count("<details>") for p in module8_md)
    for name, actual, expected in (
        ("module Markdown learning/reference files",len(module8_md),54),
        ("module original SVGs",len(module8_svgs),45),
        ("module original CSVs",len(module8_csvs),47),
        ("module knowledge-check answer blocks",module8_answer_blocks,89),
    ):
        if actual != expected:
            errors.append(f"Module 8 authoring inventory: expected {expected} {name}, found {actual}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for statement in (
        "369 structured Markdown files",
        "across seven completed modules",
        "250 original SVG diagrams",
        "101 original CSV datasets",
        "723 independently authored knowledge checks",
        "./calculations/risk-response/formula-sheet.md",
        "07-supply-chain-risk/",
        "assets/diagrams/module-7/",
        "assets/data/module-7/",
        "calculations/risk-response/",
    ):
        if statement not in readme:
            errors.append(f"README inventory is missing the current statement ({statement})")

    learning_paths = (ROOT / "LEARNING-PATHS.md").read_text(encoding="utf-8")
    if "All seven modules can be read" not in learning_paths:
        errors.append("LEARNING-PATHS.md: completed-module count is not seven")

    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")
    for statement in (
        "Seven end-to-end case studies",
        "Shared module and section overview contract across Modules 1–7",
        "Modules 1–7 are complete.",
    ):
        if statement not in roadmap:
            errors.append(f"ROADMAP.md: missing Module 7 release statement ({statement})")
    if "- [ ] Supply-chain risk" in roadmap:
        errors.append("ROADMAP.md: completed Module 7 is still listed as future work")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    if "## Version 7.0.0 — Module 7" not in changelog:
        errors.append("CHANGELOG.md: missing Module 7 release entry")
    release_dir = ROOT / ".github/releases"
    release_manifests = sorted(
        (path for path in release_dir.glob("v*.md") if re.fullmatch(r"v\d+\.\d+\.\d+", path.stem)),
        key=lambda path: tuple(int(part) for part in path.stem[1:].split(".")),
    )
    if not release_manifests:
        errors.append("Release metadata: no semantic-versioned release manifest found")
    else:
        latest_version = release_manifests[-1].stem[1:]
        changelog_release = re.search(
            rf"^## Version {re.escape(latest_version)}\b.*?^Release target: (\d{{4}}-\d{{2}}-\d{{2}})$",
            changelog,
            re.MULTILINE | re.DOTALL,
        )
        if not changelog_release:
            errors.append(f"CHANGELOG.md: missing release target for latest version {latest_version}")
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
        release_metadata = [f"version: {latest_version}", "supply chain risk management", "business continuity"]
        if changelog_release:
            release_metadata.append(f"date-released: {changelog_release.group(1)}")
        for statement in release_metadata:
            if statement not in citation:
                errors.append(f"CITATION.cff: missing latest release metadata ({statement})")

    module_snapshot_claims = {
        MODULE_1: ("**59** structured Markdown learning/reference pages", "**44** topic lessons", "**128** independently authored knowledge checks"),
        MODULE_2: ("**53** structured Markdown learning/reference pages", "**43** topic lessons", "**109** independently authored knowledge checks"),
        MODULE_3: ("**47** structured Markdown learning/reference pages", "**35** topic lessons", "**82** independently authored knowledge checks"),
        MODULE_4: ("**63** structured Markdown learning/reference pages", "**51** topic lessons", "**126** knowledge checks"),
        MODULE_5: ("**68** structured Markdown learning/reference pages", "**54** topic lessons", "**137** independently authored knowledge checks"),
        MODULE_6: ("**40** structured Markdown learning/reference pages", "**32** topic lessons", "**69** independently authored knowledge checks"),
        MODULE_7: ("**39** structured Markdown learning/reference pages", "**31** topic lessons", "**72** independently authored knowledge checks"),
    }
    module_snapshot_claims[MODULE_8] = ("**45 original SVGs**", "**47 fictional CSV datasets**", "42 original lessons")
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
        + validate_module_overviews_and_reviews()
        + validate_shared_module_content()
        + validate_svg(svg)
        + validate_csv(datasets)
        + validate_module_1_2_calculations()
        + validate_module_3_content()
        + validate_module_4_calculations()
        + validate_module_5_calculations()
        + validate_module_6_calculations()
        + validate_module_6_assessment_distribution()
        + validate_capstones_and_inventory(markdown, svg, datasets)
    )

    # The one shared runner now owns all specialized eighth-module quality gates.
    for label, validator in (
        ("Module 8 Section A", "validate_module8_section_a.py"),
        ("Module 8 Section B", "validate_module8_section_b.py"),
        ("Module 8 Section C", "validate_module8_section_c.py"),
        ("Module 8 Capstone", "validate_module8_capstone.py"),
    ):
        result = subprocess.run([sys.executable, str(ROOT / "scripts" / validator)],
            cwd=ROOT, text=True, capture_output=True, check=False)
        print(result.stdout, end="")
        if result.returncode:
            errors.append(f"{label} integrated shared validation failed:\n" + result.stdout + result.stderr)

    module7_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts/validate_module7.py")],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    print(module7_check.stdout, end="")
    if module7_check.returncode:
        errors.append("Module 7 specific validation failed:\n" + module7_check.stdout + module7_check.stderr)

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
