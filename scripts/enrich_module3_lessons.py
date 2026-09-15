#!/usr/bin/env python3
"""Add the reviewed process and application layer to every Module 3 topic.

The content is intentionally explicit and topic-specific. Running the script twice is
safe: the second run verifies that all expected sections are already present.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "03-sourcing-strategy-product-design-supplier-execution"


LESSONS = {
    "section-a-sourcing-alignment-and-total-cost/01-strategic-sourcing-from-demand.md": {
        "flow": """flowchart TD
    A[\"Validate demand signal\"] --> B[\"Define requirement and service need\"]
    B --> C[\"Assess supply market and risk\"]
    C --> D{\"Requirement contestable?\"}
    D -->|Yes| E[\"Select sourcing route\"]
    D -->|No| F[\"Redesign or justify direct source\"]
    E --> G[\"Contract, execute, and review\"]
    F --> G""",
        "heading": "Applied decision artifact — demand-to-source brief",
        "applied": """Before contacting suppliers, create a one-page brief with six controlled fields: demand quantity and timing, customer/service consequence, specification maturity, incumbent constraints, supply-market capacity, and decision owner. Record the source and date for each input.

Use a release gate: the event may begin only when the requirement is measurable, the forecast range is visible, and the chosen route is justified. If demand is volatile, issue scenarios rather than one false-precision volume. The artifact becomes the baseline for later bid comparison and prevents a sourcing event from optimizing a requirement that planning or engineering has already changed.""",
        "related": [
            "[Sourcing Requirements and Timing](./05-sourcing-requirements-and-timing.md)",
            "[Purchasing Flow and Selection Routes](../section-d-supplier-selection-contracting-and-procurement/01-purchasing-flow-and-selection-routes.md)",
        ],
    },
    "section-a-sourcing-alignment-and-total-cost/02-make-buy-and-core-capability.md": {
        "flow": """flowchart TD
    A[\"Define capability boundary\"] --> B{\"Creates defensible advantage?\"}
    B -->|Yes| C{\"Internal capability sustainable?\"}
    B -->|No| D{\"Capable supply market?\"}
    C -->|Yes| E[\"Make and protect\"]
    C -->|No| F[\"Hybrid or capability investment\"]
    D -->|Yes| G[\"Buy with controls\"]
    D -->|No| F
    E --> H[\"Set review and exit triggers\"]
    F --> H
    G --> H""",
        "heading": "Worked decision — three-year make-or-buy comparison",
        "applied": """The [make-or-buy dataset](../../assets/data/module-3/section-a/make-buy-options.csv) uses 24,000 units per year, a three-year horizon, and a 0% discount rate so the arithmetic is reproducible. For each option:

`three-year cost = 3 × (annual volume × unit conversion cost + annual fixed cost) + transition cost`

| Option | Calculation | Three-year cost |
|---|---:|---:|
| Internal cell | `3 × (24,000 × $86 + $620,000) + $180,000` | **$8,232,000** |
| Domestic partner | `3 × (24,000 × $101 + $110,000) + $260,000` | **$7,862,000** |
| Nearshore partner | `3 × (24,000 × $78 + $170,000) + $420,000` | **$6,546,000** |
| Hybrid | `3 × (24,000 × $93 + $390,000) + $310,000` | **$8,176,000** |

Nearshore is the modeled cost leader, but it also has an 11-month readiness period, lower knowledge control, and higher continuity risk. The decision record must therefore state whether the $1.63 million cost difference versus hybrid is sufficient compensation for those exposures; cost ranking alone does not decide the capability boundary.""",
        "related": [
            "[Make-or-buy dataset](../../assets/data/module-3/section-a/make-buy-options.csv)",
            "[Transition Risk and Knowledge Retention](./04-transition-risk-and-knowledge-retention.md)",
            "[Landed Cost and Total Cost of Ownership](./06-landed-cost-and-total-cost-of-ownership.md)",
        ],
    },
    "section-a-sourcing-alignment-and-total-cost/03-outsourcing-offshoring-and-nearshoring.md": {
        "flow": """flowchart TD
    A[\"Define process and service boundary\"] --> B[\"Decide ownership model\"]
    B --> C[\"Compare location options\"]
    C --> D[\"Model landed cost, lead time, and risk\"]
    D --> E{\"Controls and recovery viable?\"}
    E -->|Yes| F[\"Approve footprint option\"]
    E -->|No| G[\"Redesign boundary or location\"]
    G --> D""",
        "heading": "Applied decision artifact — ownership-location matrix",
        "applied": """Evaluate ownership and geography as separate axes. Build a matrix whose rows are internal, captive, contract manufacturer, and specialist supplier, and whose columns are local, nearshore, and offshore. Score only combinations that are legally and operationally feasible.

For each feasible cell, retain comparable evidence for lead-time distribution, duty and freight, intellectual-property exposure, labor and capacity, currency, recovery time, and required management bandwidth. A low-cost cell should not advance unless the recovery design identifies alternative tooling access, data ownership, emergency logistics, and a named transition owner. This prevents “outsourcing” and “offshoring” from being treated as one indivisible choice.""",
        "related": [
            "[Make-or-Buy and Core Capability](./02-make-buy-and-core-capability.md)",
            "[Payment, Trade Finance, and Currency Exposure](../section-d-supplier-selection-contracting-and-procurement/08-payment-trade-finance-and-currency.md)",
        ],
    },
    "section-a-sourcing-alignment-and-total-cost/04-transition-risk-and-knowledge-retention.md": {
        "flow": """flowchart TD
    A[\"Baseline process and failure modes\"] --> B[\"Capture knowledge and control plan\"]
    B --> C[\"Supplier shadow and training\"]
    C --> D[\"Parallel production and validation\"]
    D --> E{\"Exit criteria met?\"}
    E -->|No| C
    E -->|Yes| F[\"Controlled cutover\"]
    F --> G[\"Stabilize and retain fallback\"]""",
        "heading": "Applied decision artifact — transition gate register",
        "applied": """Use a gate register rather than a date-only project plan. Each gate needs an entry criterion, objective evidence, approver, fallback, and latest safe decision date. Typical gates cover documentation completeness, trained operators, tooling acceptance, first-article quality, sustained-rate capacity, system readiness, and inventory buffer.

Define cutover quantitatively—for example, three conforming lots at the required takt with no critical escape—before schedule pressure appears. Keep the old path available until the new path has demonstrated both output and recovery behavior. Record which knowledge must remain internal, who owns it, and how often it will be exercised after transfer.""",
        "related": [
            "[Make-or-Buy and Core Capability](./02-make-buy-and-core-capability.md)",
            "[Order Tracking, Exceptions, and Expediting](../section-d-supplier-selection-contracting-and-procurement/11-order-tracking-exceptions-and-expediting.md)",
        ],
    },
    "section-a-sourcing-alignment-and-total-cost/05-sourcing-requirements-and-timing.md": {
        "flow": """flowchart TD
    A[\"Confirm business need\"] --> B[\"Translate need into measurable specification\"]
    B --> C[\"Separate mandatory gates from preferences\"]
    C --> D[\"Validate demand and award timing\"]
    D --> E[\"Choose event and evaluation plan\"]
    E --> F{\"Cross-functional approval?\"}
    F -->|No| B
    F -->|Yes| G[\"Release sourcing brief\"]""",
        "heading": "Applied decision artifact — requirement quality test",
        "applied": """Challenge every requirement with four questions: Is it measurable? Is its business reason documented? Does it discriminate among viable solutions? Can compliance be verified before award? Put non-negotiable legal, safety, cyber, and technical conditions in a gate table; put value-creating preferences in the weighted scorecard.

Back-plan the event from the required operational date through contract approval, supplier qualification, tooling, validation, and transition buffer. If the calendar cannot support those activities, escalate the timing conflict instead of compressing supplier due diligence invisibly. Freeze a numbered requirement baseline for bids and log every later clarification so all suppliers compete against the same scope.""",
        "related": [
            "[Strategic Sourcing from Demand](./01-strategic-sourcing-from-demand.md)",
            "[Supplier Criteria and Weighted Evaluation](../section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)",
        ],
    },
    "section-a-sourcing-alignment-and-total-cost/06-landed-cost-and-total-cost-of-ownership.md": {
        "flow": """flowchart TD
    A[\"Fix volume, horizon, destination, and service\"] --> B[\"Normalize quotes and currency\"]
    B --> C[\"Add freight, duty, and pipeline inventory\"]
    C --> D[\"Add quality, control, and continuity costs\"]
    D --> E[\"Test favorable and adverse scenarios\"]
    E --> F[\"Compare cost, service, cash, and residual risk\"]""",
        "heading": "Worked decision — quote-to-total-cost bridge",
        "applied": """The [total-cost dataset](../../assets/data/module-3/section-a/total-cost-options.csv) is denominated in USD per unit. The local-source total is:

`$74.00 + $1.20 + $0.00 + $0.55 + $1.35 + $1.10 + $1.00 = $79.20 per unit`

The distant-source total is:

`$61.00 + $4.80 + $3.10 + $3.40 + $4.20 + $3.00 + $3.10 = $82.60 per unit`

The distant quote is **$13.00 lower**, yet its modeled total cost is **$3.40 higher per unit**. At 24,000 units, that total-cost disadvantage is `$3.40 × 24,000 = $81,600 per year`. Keep uncertain quality and continuity estimates visible as scenarios; do not disguise them as audited cash costs.""",
        "related": [
            "[Total-cost dataset](../../assets/data/module-3/section-a/total-cost-options.csv)",
            "[Should-Cost and the Sourcing Business Case](./07-should-cost-and-business-case.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },
    "section-a-sourcing-alignment-and-total-cost/07-should-cost-and-business-case.md": {
        "flow": """flowchart TD
    A[\"Define product and process assumptions\"] --> B[\"Build material and conversion model\"]
    B --> C[\"Add overhead, logistics, and reasonable margin\"]
    C --> D[\"Validate drivers with evidence\"]
    D --> E[\"Run sensitivity cases\"]
    E --> F[\"Convert gaps into operational hypotheses\"]
    F --> G[\"Approve benefit, investment, and owner\"]""",
        "heading": "Worked decision — should-cost bridge",
        "applied": """For the enclosure example, the transparent cost stack is:

`$54.60 material + $12.80 conversion + $7.00 overhead + $4.00 logistics + $10.00 margin = $88.40`

Against a $96.00 quotation, the modeled gap is **$7.60 per unit**. Do not label that gap “savings.” First test the assumptions most likely to explain it: actual material yield, production lot size, changeover time, utilization, and supplier-specific capital. Then translate validated opportunities into a business case:

`net benefit = gross recurring benefit − implementation cost − transition cost − expected disruption cost`

Assign each benefit a source, baseline date, implementation milestone, finance owner, and confidence range. A credible case distinguishes negotiated price movement from engineering or process changes that still require execution.""",
        "related": [
            "[Landed Cost and Total Cost of Ownership](./06-landed-cost-and-total-cost-of-ownership.md)",
            "[Design for Supply Chain and Logistics](../section-c-product-design-for-supply-chain/03-design-for-supply-chain-and-logistics.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },

    "section-b-category-strategy-and-supply-base/01-supply-plan-governance.md": {
        "flow": """flowchart TD
    A[\"Consolidate demand, capacity, inventory, and risk\"] --> B[\"Cross-functional challenge\"]
    B --> C[\"Identify gaps and decisions\"]
    C --> D{\"Within delegated authority?\"}
    D -->|Yes| E[\"Approve supply actions\"]
    D -->|No| F[\"Escalate decision with options\"]
    E --> G[\"Execute and track variance\"]
    F --> G
    G --> A""",
        "heading": "Applied decision artifact — governance decision log",
        "applied": """A useful governance meeting ends with decisions, not presentation notes. Maintain a log containing decision statement, alternatives considered, evidence date, accountable owner, due date, financial/service exposure, and escalation trigger. Link every action to the specific demand-capacity gap it resolves.

Use a two-horizon agenda: near-term exceptions that threaten customer or production commitments, and structural actions such as capacity reservations, qualification, inventory policy, or redesign. Close the loop by comparing the approved assumption with actual demand, delivery, and cost at the next review. Repeated variance should change the model or policy, not merely create another action.""",
        "related": [
            "[Category Architecture and Strategy](./02-category-architecture.md)",
            "[Strategic Sourcing from Demand](../section-a-sourcing-alignment-and-total-cost/01-strategic-sourcing-from-demand.md)",
        ],
    },
    "section-b-category-strategy-and-supply-base/02-category-architecture.md": {
        "flow": """flowchart TD
    A[\"Collect spend and demand records\"] --> B[\"Normalize suppliers, units, and currency\"]
    B --> C[\"Build category hierarchy\"]
    C --> D[\"Assign business and technical owners\"]
    D --> E[\"Test whether each category is actionable\"]
    E --> F{\"Stable decision boundary?\"}
    F -->|No| C
    F -->|Yes| G[\"Launch category strategy\"]""",
        "heading": "Applied decision artifact — category boundary test",
        "applied": """A category is useful when its demand shares meaningful cost drivers, supplier markets, specifications, and decision owners. Test each proposed node against those four dimensions. If two items have different qualification rules or supply markets, do not combine them merely because accounting assigned the same commodity code.

Document a category charter with inclusions, exclusions, parent-child hierarchy, spend owner, technical owner, geography, and refresh rule. Reconcile supplier legal entities to parent groups before measuring concentration. The [category-spend dataset](../../assets/data/module-3/section-b/category-spend.csv) illustrates why: 41 supplier records for electronic controls become 29 legal suppliers and 24 parent groups, three materially different measures of source breadth.""",
        "related": [
            "[Category-spend dataset](../../assets/data/module-3/section-b/category-spend.csv)",
            "[Spend Analysis and Supply-Market Intelligence](./06-spend-analysis-and-market-intelligence.md)",
        ],
    },
    "section-b-category-strategy-and-supply-base/03-portfolio-analysis.md": {
        "flow": """flowchart TD
    A[\"Define business-impact scale\"] --> B[\"Define supply-risk scale\"]
    B --> C[\"Score categories with evidence\"]
    C --> D[\"Place category in portfolio\"]
    D --> E[\"Select quadrant-specific action\"]
    E --> F[\"Set triggers and review cadence\"]
    F --> C""",
        "heading": "Worked decision — portfolio classification",
        "applied": """Apply one documented scale to the [category-portfolio dataset](../../assets/data/module-3/section-b/category-portfolio.csv). Compressor assemblies score 5 for business impact and 5 for supply risk, so they are strategic; fasteners score 1 and 1, so they are routine. The label is a starting hypothesis, not the analysis itself.

For each placement, attach evidence and a response: strategic categories need joint capacity and continuity; bottlenecks need qualification or redesign; leverage categories need competitive and specification actions; routine categories need standardization and automation. Set an event trigger—such as capacity loss, regulation, sole-source status, or spend change—because a portfolio position can move before the annual refresh.""",
        "related": [
            "[Category-portfolio dataset](../../assets/data/module-3/section-b/category-portfolio.csv)",
            "[Supply-Base Right-Sizing](./07-supply-base-right-sizing.md)",
        ],
    },
    "section-b-category-strategy-and-supply-base/04-supplier-attractiveness-and-segmentation.md": {
        "flow": """flowchart TD
    A[\"Measure supplier value to buyer\"] --> B[\"Estimate buyer attractiveness to supplier\"]
    B --> C[\"Validate view with supplier evidence\"]
    C --> D[\"Select segment and access strategy\"]
    D --> E[\"Set governance and investment\"]
    E --> F[\"Monitor movement and dependence\"]
    F --> A""",
        "heading": "Applied decision artifact — two-way segmentation evidence",
        "applied": """Build two scores separately. Supplier importance may reflect switching time, technical uniqueness, spend at risk, and customer consequence. Buyer attractiveness may reflect profitable growth, strategic fit, payment behavior, innovation access, and ease of doing business. Do not infer the second score from your own spend alone.

Validate the supplier’s perspective through account plans, executive conversations, capacity-allocation behavior, and comparative growth opportunities. Then prescribe a segment-specific action. A critical supplier that sees the buyer as unattractive needs an access plan; calling the relationship “strategic” does not create attention or capacity. Reassess after acquisitions, volume shifts, payment deterioration, or technology change.""",
        "related": [
            "[Supplier Relationship Models](./05-relationship-models.md)",
            "[Principled Negotiation and BATNA](../section-d-supplier-selection-contracting-and-procurement/04-principled-negotiation-and-batna.md)",
        ],
    },
    "section-b-category-strategy-and-supply-base/05-relationship-models.md": {
        "flow": """flowchart TD
    A[\"Assess value, dependency, and switching difficulty\"] --> B[\"Choose relationship model\"]
    B --> C[\"Define decisions and information shared\"]
    C --> D[\"Assign cadence, roles, and escalation\"]
    D --> E[\"Run joint performance review\"]
    E --> F{\"Model still justified?\"}
    F -->|No| B
    F -->|Yes| E""",
        "heading": "Applied decision artifact — relationship operating charter",
        "applied": """For each material supplier, state the relationship model and the behavior it requires. A charter should define joint decisions, information shared, meeting cadence, executive sponsors, improvement pipeline, intellectual-property rules, escalation, and exit criteria. The resource load must match the expected value.

Use evidence to distinguish a preferred supplier from a strategic relationship. Preferred status may reward reliable execution; strategic governance is justified only when interdependence, switching difficulty, innovation, or joint investment requires it. Review the model when dependency, technology, or supplier performance changes. Continuing high-touch governance without a joint agenda creates ceremony, while under-governing a coupled relationship hides risk.""",
        "related": [
            "[Supplier Attractiveness and Segmentation](./04-supplier-attractiveness-and-segmentation.md)",
            "[Terms, Service Levels, and Incentives](../section-d-supplier-selection-contracting-and-procurement/07-terms-slas-and-incentives.md)",
        ],
    },
    "section-b-category-strategy-and-supply-base/06-spend-analysis-and-market-intelligence.md": {
        "flow": """flowchart TD
    A[\"Collect PO, invoice, contract, and demand data\"] --> B[\"Clean names, units, and currency\"]
    B --> C[\"Classify to category hierarchy\"]
    C --> D[\"Enrich with capacity, cost, and risk signals\"]
    D --> E[\"Size opportunity and exposure\"]
    E --> F[\"Convert insight into category action\"]
    F --> G[\"Track realized result\"]""",
        "heading": "Worked decision — spend concentration baseline",
        "applied": """From the [category-spend dataset](../../assets/data/module-3/section-b/category-spend.csv), total annual spend is:

`$8.40m + $6.20m + $4.10m + $0.98m + $0.42m + $0.76m = $20.86m`

Compressor assemblies therefore represent `$8.40m ÷ $20.86m = 40.27%` of covered spend. That concentration is an inquiry trigger, not an automatic savings target. Enrich it with capacity, cost drivers, qualification lead time, and parent-company exposure.

The analysis output should name the decision it enables—for example, capacity reservation, specification harmonization, competitive event, index formula, or risk mitigation—and a baseline against which finance can verify realized value. A dashboard without an action owner remains descriptive reporting.""",
        "related": [
            "[Category-spend dataset](../../assets/data/module-3/section-b/category-spend.csv)",
            "[Category Architecture and Strategy](./02-category-architecture.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },
    "section-b-category-strategy-and-supply-base/07-supply-base-right-sizing.md": {
        "flow": """flowchart TD
    A[\"Map demand, capacity, qualification, and parent exposure\"] --> B[\"Calculate concentration and switching constraints\"]
    B --> C{\"Aggregation benefit exceeds resilience loss?\"}
    C -->|Yes| D[\"Consolidate with continuity controls\"]
    C -->|No| E[\"Diversify or qualify alternate\"]
    D --> F[\"Set allocation and trigger limits\"]
    E --> F
    F --> G[\"Monitor performance and concentration\"]""",
        "heading": "Worked decision — parent-level concentration",
        "applied": """Use the [supplier-share dataset](../../assets/data/module-3/section-b/supplier-shares.csv), which reconciles suppliers to parent groups. Compressor-assembly shares are 52%, 28%, and 20%, producing:

`HHI = 52² + 28² + 20² = 3,888`

Refrigerant sensors have one qualified parent at 100%, so `HHI = 100² = 10,000`. The calculation exposes concentration but does not prescribe an arbitrary supplier count. Compare the benefit of consolidation with capacity headroom, recovery time, tooling portability, qualification expense, geographic correlation, and supplier investment. Set allocation limits and a trigger—for example, a capacity or financial event—that causes the sourcing team to activate an alternate path.""",
        "related": [
            "[Supplier-share dataset](../../assets/data/module-3/section-b/supplier-shares.csv)",
            "[Category Portfolio Analysis](./03-portfolio-analysis.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },

    "section-c-product-design-for-supply-chain/01-design-as-economic-lever.md": {
        "flow": """flowchart TD
    A[\"Frame design choice and alternatives\"] --> B[\"Quantify cost and cash effects\"]
    B --> C[\"Test service and supply-risk effects\"]
    C --> D[\"Assess sustainability and recovery\"]
    D --> E[\"Resolve trade-offs at design gate\"]
    E --> F[\"Release assumptions and owners\"]
    F --> G[\"Measure lifecycle outcome\"]""",
        "heading": "Applied decision artifact — lifecycle design scorecard",
        "applied": """At each architecture gate, compare alternatives using the same demand, service, and lifecycle horizon. The scorecard should show unit material and conversion cost, inventory and working-capital effect, source options, lead time, service labor, field failure, packaging and transport, energy, and end-of-life route.

Keep cash, risk, and environmental measures separate rather than forcing them into one opaque score. Record the design owner for every assumption and the evidence needed before release. A choice that saves recurring cost but creates a large conversion expense or validation risk should display payback and milestone risk explicitly. The [design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv) provides that trade-off rather than a uniformly dominant option.""",
        "related": [
            "[Design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv)",
            "[Landed Cost and Total Cost of Ownership](../section-a-sourcing-alignment-and-total-cost/06-landed-cost-and-total-cost-of-ownership.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/02-collaborative-design-and-early-involvement.md": {
        "flow": """flowchart TD
    A[\"Frame customer need and design freedom\"] --> B[\"Select capable suppliers for input\"]
    B --> C[\"Compare concepts and process constraints\"]
    C --> D[\"Agree interfaces and evidence ownership\"]
    D --> E[\"Validate tooling, quality, and capacity\"]
    E --> F{\"Gate evidence complete?\"}
    F -->|No| C
    F -->|Yes| G[\"Industrialize and control changes\"]""",
        "heading": "Applied decision artifact — early-involvement charter",
        "applied": """Invite supplier input while design alternatives still exist, but establish boundaries before sharing sensitive information. The charter should define the problem to solve, decision dates, expected technical evidence, intellectual-property ownership, confidentiality, compensation if appropriate, and how proposals will be evaluated.

Ask suppliers for process capability, material availability, tolerance evidence, tooling lead time, capacity assumptions, failure modes, and alternative architectures—not merely a quotation. At each gate, record which recommendation was accepted or rejected and why. This creates traceability and prevents late supplier involvement from becoming a request to manufacture a frozen, uneconomic design.""",
        "related": [
            "[Supplier Relationship Models](../section-b-category-strategy-and-supply-base/05-relationship-models.md)",
            "[Quality, Customer Translation, and Robust Design](./07-quality-qfd-and-robust-design.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/03-design-for-supply-chain-and-logistics.md": {
        "flow": """flowchart TD
    A[\"Map product across source, move, store, use, and return\"] --> B[\"Generate design alternatives\"]
    B --> C[\"Calculate cube, weight, handling, and damage effects\"]
    C --> D[\"Validate packaging and material availability\"]
    D --> E[\"Test service, source depth, and postponement\"]
    E --> F[\"Approve trade-off or return to design\"]""",
        "heading": "Worked decision — logistics effect of a modular platform",
        "applied": """Using the [design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv), moving from the current integral design to the modular platform changes four downstream measures:

| Measure | Current | Modular | Change |
|---|---:|---:|---:|
| Units per pallet | 6 | 8 | **+33.3%** |
| Assembly minutes | 46 | 34 | **−26.1%** |
| Service minutes | 18 | 7 | **−61.1%** |
| Annual packaging cost | $310,000 | $224,000 | **−$86,000 / −27.7%** |

Those recurring improvements must be weighed against $650,000 conversion cost and validation risk rated 4 of 5. Confirm pallet stability, damage, handling ergonomics, line balance, source availability, and repair performance in physical trials before approving the forecast benefit.""",
        "related": [
            "[Design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv)",
            "[Modular versus Integral Design](./05-modular-versus-integral-design.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/04-standardization-commonality-and-universality.md": {
        "flow": """flowchart TD
    A[\"Map variants, parts, and customer requirements\"] --> B[\"Identify common functional needs\"]
    B --> C[\"Propose standard platform or interface\"]
    C --> D[\"Test cost, performance, regulatory, and market exceptions\"]
    D --> E{\"Exception creates net value?\"}
    E -->|No| F[\"Adopt common solution\"]
    E -->|Yes| G[\"Approve controlled variant\"]
    F --> H[\"Track complexity and compliance\"]
    G --> H""",
        "heading": "Worked decision — commonality baseline",
        "applied": """The [design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv) reduces unique parts from 184 to 139 in the modular option:

`part-count reduction = (184 − 139) ÷ 184 = 24.5%`

Do not approve commonality on part count alone. Build an exception register that records customer value, regulatory need, performance impact, incremental tooling, inventory, quality controls, and an expiry or review date. Standardize interfaces and specifications where the economic benefit is repeatable; permit a variant only when its incremental lifecycle value exceeds the complexity it creates. Monitor actual unique parts, low-volume stock, changeovers, and service coverage after launch.""",
        "related": [
            "[Design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv)",
            "[Postponement, Mass Customization, and Localization](./08-postponement-mass-customization-and-localization.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/05-modular-versus-integral-design.md": {
        "flow": """flowchart TD
    A[\"Map functions and performance coupling\"] --> B{\"Independent change or replacement valuable?\"}
    B -->|Yes| C[\"Define modular interfaces\"]
    B -->|No| D[\"Evaluate integral optimization\"]
    C --> E[\"Validate interface, tolerance, and architecture risk\"]
    D --> E
    E --> F[\"Compare lifecycle economics and conversion effort\"]
    F --> G[\"Release architecture and control interfaces\"]""",
        "heading": "Applied decision artifact — architecture trade-off record",
        "applied": """Record the functions, physical components, interfaces, and performance couplings before choosing an architecture. For modularity, quantify variant flexibility, service replacement, supplier substitution, inventory pooling, and interface cost. For an integral design, quantify performance, size, weight, efficiency, and the consequences of coupled change.

In the [design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv), the modular platform has the best recurring operating measures but also the highest one-time conversion cost ($650,000) and validation risk (4 of 5). The gate decision should therefore include payback, technical evidence, change-control ownership, and a fallback—not a generic preference for modularity.""",
        "related": [
            "[Design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv)",
            "[Simplification, DFMA, and Serviceability](./06-simplification-dfma-and-serviceability.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/06-simplification-dfma-and-serviceability.md": {
        "flow": """flowchart TD
    A[\"Observe assembly, test, and service work\"] --> B[\"Challenge each part, motion, tool, and tolerance\"]
    B --> C[\"Eliminate, combine, or standardize\"]
    C --> D[\"Prototype assembly and repair\"]
    D --> E[\"Measure time, defects, access, and recovery\"]
    E --> F{\"Requirements still met?\"}
    F -->|No| B
    F -->|Yes| G[\"Release and update work instructions\"]""",
        "heading": "Worked decision — DFMA and service effect",
        "applied": """Compare the current and modular alternatives in the [design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv):

- assembly time falls from 46 to 34 minutes: `(46 − 34) ÷ 46 = 26.1%`;
- estimated field failures fall from 14 to 8 per 1,000: `(14 − 8) ÷ 14 = 42.9%`;
- service time falls from 18 to 7 minutes: `(18 − 7) ÷ 18 = 61.1%`.

Validate those modeled gains with timed builds and service trials across representative operators. Record any added tooling, training, diagnostic, or interface risk. The released design must update the bill of material, work instructions, quality plan, service documentation, and benefit owner; otherwise the simplification remains a prototype result.""",
        "related": [
            "[Design-alternatives dataset](../../assets/data/module-3/section-c/design-alternatives.csv)",
            "[Quality, Customer Translation, and Robust Design](./07-quality-qfd-and-robust-design.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/07-quality-qfd-and-robust-design.md": {
        "flow": """flowchart TD
    A[\"Capture customer needs in measurable language\"] --> B[\"Prioritize needs and failure consequences\"]
    B --> C[\"Translate needs into technical responses\"]
    C --> D[\"Resolve response conflicts and set targets\"]
    D --> E[\"Test variation and noise conditions\"]
    E --> F{\"Capability and robustness demonstrated?\"}
    F -->|No| C
    F -->|Yes| G[\"Release control plan\"]""",
        "heading": "Applied decision artifact — requirement-to-control trace",
        "applied": """Create a trace from each high-priority customer need to a measurable technical response, design target, validation method, process control, and accountable owner. For “quiet operation,” for example, define the sound metric, operating condition, limit, measurement method, and relevant variation sources rather than repeating the customer phrase.

Use QFD to expose weak or conflicting technical coverage, then test robustness against realistic noise: material lots, operators, voltage, temperature, transport, wear, and supplier processes. A passing nominal prototype is not enough. Release the requirement only when the measurement system, capability evidence, reaction plan, and post-launch signal are defined.""",
        "related": [
            "[Collaborative Design and Early Involvement](./02-collaborative-design-and-early-involvement.md)",
            "[Supplier Criteria and Weighted Evaluation](../section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/08-postponement-mass-customization-and-localization.md": {
        "flow": """flowchart TD
    A[\"Map variant demand and forecast error\"] --> B[\"Identify common platform\"]
    B --> C[\"Choose feasible differentiation activities\"]
    C --> D[\"Locate inventory decoupling point\"]
    D --> E[\"Test capacity, lead time, and data rules\"]
    E --> F[\"Configure or localize to actual demand\"]
    F --> G[\"Measure service, inventory, and obsolescence\"]""",
        "heading": "Applied decision artifact — postponement boundary test",
        "applied": """List every differentiating activity—software load, label, language pack, accessory, color, packaging, or final assembly—and test whether it can move downstream without violating lead time, quality, regulation, or capacity. Quantify demand variability at the common and finished-good levels.

Choose the decoupling point where a common unit can still absorb uncertainty and downstream resources can complete the variant within the customer promise. Define configuration data, component availability, work instructions, and error-proofing. Measure pooled inventory, finished-goods obsolescence, completion lead time, and late-stage capacity. Postponement creates value only when the downstream process is controlled and fast enough to serve actual demand.""",
        "related": [
            "[Standardization, Commonality, and Universality](./04-standardization-commonality-and-universality.md)",
            "[Supply-Plan Governance](../section-b-category-strategy-and-supply-base/01-supply-plan-governance.md)",
        ],
    },
    "section-c-product-design-for-supply-chain/09-circular-and-sustainable-design.md": {
        "flow": """flowchart TD
    A[\"Set lifecycle and circularity objective\"] --> B[\"Map material, energy, durability, and recovery\"]
    B --> C[\"Design for repair, disassembly, and identification\"]
    C --> D[\"Build reverse-flow and inspection route\"]
    D --> E{\"Recovered value viable?\"}
    E -->|Reuse or remanufacture| F[\"Return component to use\"]
    E -->|Recycle| G[\"Return material to supply\"]
    E -->|No| H[\"Redesign or document responsible disposal\"]
    F --> B
    G --> B""",
        "heading": "Applied decision artifact — circularity operating case",
        "applied": """A circular design needs an operating route, not only a material claim. Define expected return volume, collection channel, ownership, transport, data and product identification, inspection criteria, disassembly method, recovered yield, secondary demand, and responsible residual handling.

Compare alternatives over a stated lifecycle using material and energy impact, repair time, recovery cost, avoided virgin material, and realized reuse or remanufacture value. Verify supplier claims with traceable evidence and separate design potential from actual collection performance. Set a pilot gate with minimum recovery yield and economics before scaling. If the reverse network is absent, record who must create it and when.""",
        "related": [
            "[Product Design as a Supply-Chain Lever](./01-design-as-economic-lever.md)",
            "[Contract Deployment and Compliance](../section-d-supplier-selection-contracting-and-procurement/05-contract-deployment-and-compliance.md)",
        ],
    },

    "section-d-supplier-selection-contracting-and-procurement/01-purchasing-flow-and-selection-routes.md": {
        "flow": """flowchart TD
    A[\"Approve need and measurable specification\"] --> B{\"Which route fits market and scope?\"}
    B -->|RFQ| C[\"Comparable price competition\"]
    B -->|RFP| D[\"Evaluate solution and commercial response\"]
    B -->|Direct| E[\"Document exception and negotiation plan\"]
    C --> F[\"Qualify and evaluate suppliers\"]
    D --> F
    E --> F
    F --> G[\"Approve award, contract, and PO\"]""",
        "heading": "Applied decision artifact — sourcing-route record",
        "applied": """Before release, document why the route fits the requirement. Use an RFQ when scope and comparison units are stable; use an RFP when solution design and non-price value matter; use direct negotiation when a justified constraint prevents meaningful competition. Record any exception approval.

The route record should include qualified market depth, specification maturity, evaluation method, confidentiality, communication rules, conflict checks, approval authority, and timetable. Keep qualification gates ahead of weighted ranking. After award, preserve the bid baseline, approvals, negotiated changes, contract, and supplier-notification evidence so the purchase order executes the approved decision.""",
        "related": [
            "[Sourcing Requirements and Timing](../section-a-sourcing-alignment-and-total-cost/05-sourcing-requirements-and-timing.md)",
            "[Competitive Bidding and Direct Negotiation](./03-competitive-bidding-and-direct-negotiation.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md": {
        "flow": """flowchart TD
    A[\"Define mandatory gates and weighted criteria\"] --> B[\"Publish scales and evidence rules\"]
    B --> C[\"Collect raw evaluator scores\"]
    C --> D[\"Normalize and calculate weighted totals\"]
    D --> E[\"Check gates and scoring consensus\"]
    E --> F[\"Run sensitivity and due diligence\"]
    F --> G[\"Approve eligible award\"]""",
        "heading": "Worked decision — transparent weighted evaluation",
        "applied": """The [supplier-evaluation dataset](../../assets/data/module-3/section-d/supplier-evaluation.csv) stores raw scores on a 1–5 scale and embeds each criterion weight in the column name. Calculate:

`weighted total = Σ(raw score ÷ 5 × criterion weight)`

NorthPeak earns `(4.40/5×25) + (3.75/5×20) + (4.67/5×15) + (4.33/5×15) + (3.67/5×15) + (4.00/5×10) ≈ 83`. BlueHarbor scores 78. VectorTherm also scores 78 but fails a mandatory gate and is therefore ineligible until the failure is resolved and reapproved.

Test whether plausible weight changes reverse the ranking, preserve evaluator evidence and comments, and complete due diligence before award. The score supports judgment; it does not replace gates or approval.""",
        "related": [
            "[Supplier-evaluation dataset](../../assets/data/module-3/section-d/supplier-evaluation.csv)",
            "[Purchasing Flow and Selection Routes](./01-purchasing-flow-and-selection-routes.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/03-competitive-bidding-and-direct-negotiation.md": {
        "flow": """flowchart TD
    A[\"Assess specification clarity and qualified market depth\"] --> B{\"Comparable competition viable?\"}
    B -->|Yes| C[\"Design controlled bid event\"]
    B -->|No| D[\"Approve direct-negotiation rationale\"]
    C --> E[\"Evaluate compliant offers\"]
    D --> F[\"Use fact base, BATNA, and objective criteria\"]
    E --> G[\"Negotiate clarifications and award\"]
    F --> G""",
        "heading": "Applied decision artifact — event integrity checklist",
        "applied": """For a competitive event, establish one specification baseline, response template, question channel, deadline, evaluation team, conflict declaration, and change log. Release material clarifications to all participants. Do not introduce an auction unless offers are truly comparable and qualified suppliers understand the rules.

For direct negotiation, record the constraint, alternatives considered, approval, fact base, objectives, BATNA, authority, and independent reasonableness check. Competition can reveal market price but may suppress collaboration when the solution is not defined; negotiation can create joint value but weakens price discovery. The decision record should make that trade-off auditable.""",
        "related": [
            "[Principled Negotiation and BATNA](./04-principled-negotiation-and-batna.md)",
            "[Digital Procurement, Marketplaces, and Auctions](./12-digital-procurement-marketplaces-and-auctions.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/04-principled-negotiation-and-batna.md": {
        "flow": """flowchart TD
    A[\"Identify interests, issues, and stakeholders\"] --> B[\"Build BATNA and walk-away boundaries\"]
    B --> C[\"Prepare objective criteria and tradable packages\"]
    C --> D[\"Exchange information and test assumptions\"]
    D --> E[\"Trade across variables, not positions\"]
    E --> F{\"Agreement better than BATNA?\"}
    F -->|Yes| G[\"Document complete agreement\"]
    F -->|No| H[\"Pause, escalate, or use BATNA\"]""",
        "heading": "Applied decision artifact — negotiation preparation sheet",
        "applied": """Prepare each issue with target, limit, evidence, authority, and tradable variables. Include price structure, indexation, payment, volume flexibility, capacity, lead time, warranty, intellectual property, liability, implementation, and governance. Estimate the supplier’s likely interests without presenting assumptions as facts.

Build a credible BATNA with owner, timing, switching cost, and probability; a theoretical alternative is not negotiating leverage. Design packages that exchange variables with different value to each side—for example, a longer commitment for capacity reservation and transparent indexation. Before closing, compare the complete package with the BATNA and document contingent terms, definitions, and unresolved items.""",
        "related": [
            "[Competitive Bidding and Direct Negotiation](./03-competitive-bidding-and-direct-negotiation.md)",
            "[Contract Types and Risk Allocation](./06-contract-types-and-risk-allocation.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/05-contract-deployment-and-compliance.md": {
        "flow": """flowchart TD
    A[\"Extract contract obligations and decision rights\"] --> B[\"Assign owners and evidence sources\"]
    B --> C[\"Configure prices, catalogs, systems, and users\"]
    C --> D[\"Execute orders and service\"]
    D --> E[\"Monitor compliance and exceptions\"]
    E --> F[\"Correct leakage and resolve disputes\"]
    F --> G[\"Use evidence for renewal or exit\"]""",
        "heading": "Applied decision artifact — obligation-control register",
        "applied": """Translate the signed contract into an operational register. The [contract-obligations dataset](../../assets/data/module-3/section-d/contract-obligations.csv) shows the required fields: obligation, owner, evidence, frequency, threshold, and response. Add effective date, system configuration, escalation, and renewal notice.

Test deployment by sampling transactions: approved price loaded, index formula current, catalog accessible, forecast transmitted, receipt data captured, rebate accrued, and SLA evidence reproducible. Route exceptions to named owners and distinguish supplier nonperformance from buyer process leakage. At renewal, use the register to calculate realized value and open exposure rather than reconstructing obligations from memory.""",
        "related": [
            "[Contract-obligations dataset](../../assets/data/module-3/section-d/contract-obligations.csv)",
            "[Terms, Service Levels, and Incentives](./07-terms-slas-and-incentives.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/06-contract-types-and-risk-allocation.md": {
        "flow": """flowchart TD
    A[\"Define scope uncertainty and desired outcome\"] --> B[\"Identify controllable cost and performance risks\"]
    B --> C[\"Select contract and pricing mechanism\"]
    C --> D[\"Allocate each risk to party able to control it\"]
    D --> E[\"Set ceilings, adjustments, incentives, and evidence\"]
    E --> F[\"Approve governance and change control\"]
    F --> G[\"Monitor behavior and exposure\"]""",
        "heading": "Applied decision artifact — risk-allocation table",
        "applied": """List each material uncertainty—scope, volume, commodity, labor, productivity, design change, schedule, quality, and outcome—and identify which party can influence it and what evidence exists. Then select a mechanism: fixed price, unit rate, time and materials, cost reimbursable, indexed, incentive, or outcome based.

For every allocation, state the trigger, formula, ceiling or floor, audit evidence, notice, approval, and dispute route. Transferring uncontrollable risk usually increases price or creates claims; retaining controllable supplier risk weakens accountability. Test incentives for gaming and ensure change control distinguishes legitimate scope change from performance failure.""",
        "related": [
            "[Principled Negotiation and BATNA](./04-principled-negotiation-and-batna.md)",
            "[Terms, Service Levels, and Incentives](./07-terms-slas-and-incentives.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/07-terms-slas-and-incentives.md": {
        "flow": """flowchart TD
    A[\"Define business outcome and service boundary\"] --> B[\"Specify metric, formula, source, and exclusions\"]
    B --> C[\"Set target, threshold, and review window\"]
    C --> D[\"Link response, credit, or incentive\"]
    D --> E[\"Validate data and dispute process\"]
    E --> F[\"Monitor, correct, and review behavior\"]""",
        "heading": "Worked decision — service-level boundary",
        "applied": """The [contract-obligations dataset](../../assets/data/module-3/section-d/contract-obligations.csv) sets delivery reliability at **at least 98%**. If 196 of 200 eligible order lines arrive within the defined window:

`on-time delivery = 196 ÷ 200 × 100 = 98.0%`

That result meets the threshold exactly. At 195 lines, `195 ÷ 200 × 100 = 97.5%`, which triggers the agreed corrective action. The SLA must also define the eligible population, requested versus confirmed date, partial lines, buyer-caused delay, data source, correction period, and dispute path.

Pair consequences with the behavior desired. A service credit may protect the buyer but does not itself restore supply; improvement milestones and positive incentives can be more effective when the supplier controls the outcome.""",
        "related": [
            "[Contract-obligations dataset](../../assets/data/module-3/section-d/contract-obligations.csv)",
            "[Order Tracking, Exceptions, and Expediting](./11-order-tracking-exceptions-and-expediting.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/08-payment-trade-finance-and-currency.md": {
        "flow": """flowchart TD
    A[\"Set currency, Incoterm, title, and payment terms\"] --> B[\"Map shipment, document, and bank events\"]
    B --> C[\"Measure cash, counterparty, and FX exposure\"]
    C --> D[\"Choose control, hedge, or finance instrument\"]
    D --> E[\"Ship, receive, and validate documents\"]
    E --> F[\"Settle payment and currency\"]
    F --> G[\"Reconcile fees, variances, and claims\"]""",
        "heading": "Worked decision — early-payment economics",
        "applied": """For terms of `2/10, net 30`, the buyer can take a 2% discount by paying 20 days early. The supplier’s approximate annualized cost of declining that discount is:

`0.02 ÷ 0.98 × 365 ÷ 20 = 37.2%`

That rate supports a fact-based payment discussion, but the transaction design must also align currency, Incoterm, title transfer, transport insurance, documentary requirements, tax, banking fees, and foreign-exchange ownership. Map the event at which each exposure moves. Where a hedge or trade-finance instrument is used, record notional amount, period, counterparty, approvals, settlement evidence, and residual basis risk.""",
        "related": [
            "[Receiving and Three-Way Match](./10-receiving-and-three-way-match.md)",
            "[Sourcing and procurement formula sheet](../../calculations/sourcing-procurement/formula-sheet.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/09-purchase-orders-and-blanket-orders.md": {
        "flow": """flowchart TD
    A[\"Confirm demand pattern and commitment authority\"] --> B{\"Recurring demand under stable terms?\"}
    B -->|No| C[\"Issue standard purchase order\"]
    B -->|Yes| D[\"Create blanket arrangement with ceiling and period\"]
    D --> E[\"Release quantities and dates\"]
    C --> F[\"Supplier acknowledgment\"]
    E --> F
    F --> G[\"Receive, match, close, and monitor expiry\"]""",
        "heading": "Applied decision artifact — order-control checklist",
        "applied": """Use a standard PO for a discrete authorized quantity and date. Use a blanket arrangement only when recurring demand, stable commercial terms, a defined period, and controlled release behavior justify it. State whether forecasts are informational or binding.

For both instruments, control supplier, item or service, specification revision, quantity, price and currency, delivery location, Incoterm, tax, payment, contract reference, approval, and acknowledgment. A blanket order also needs a monetary or quantity ceiling, release authority, consumption report, remaining balance, and expiry rule. Review open commitments before renewal so unissued forecasts are not mistaken for contractual volume.""",
        "related": [
            "[Purchasing Flow and Selection Routes](./01-purchasing-flow-and-selection-routes.md)",
            "[Receiving and Three-Way Match](./10-receiving-and-three-way-match.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/10-receiving-and-three-way-match.md": {
        "flow": """flowchart TD
    A[\"Approve purchase order\"] --> B[\"Record physical or service receipt\"]
    B --> C[\"Capture supplier invoice\"]
    C --> D{\"PO, receipt, invoice agree within tolerance?\"}
    D -->|Yes| E[\"Release approved amount for payment\"]
    D -->|No| F[\"Hold exception and assign cause\"]
    F --> G[\"Correct receipt, price, quantity, or invoice\"]
    G --> D""",
        "heading": "Worked decision — three-way-match exception",
        "applied": """In the [three-way-match dataset](../../assets/data/module-3/section-d/three-way-match.csv), PO 4500810 authorizes 100 units at $50, only 98 are received, and 100 are invoiced. The authorized received value is:

`98 × $50 = $4,900`

The remaining `$5,000 − $4,900 = $100` is a quantity exception and should be held unless approved tolerance or contract terms support another treatment. PO 4500812 has a price exception: `$129 − $125 = $4` per unit, or `$160` across 40 units.

Route each mismatch to the party that can correct the evidence. Do not alter receipt or PO data merely to make the invoice pass; preserve the audit trail and root cause.""",
        "related": [
            "[Three-way-match dataset](../../assets/data/module-3/section-d/three-way-match.csv)",
            "[Purchase Orders and Blanket Arrangements](./09-purchase-orders-and-blanket-orders.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/11-order-tracking-exceptions-and-expediting.md": {
        "flow": """flowchart TD
    A[\"Receive supplier commit, shipment, and forecast signals\"] --> B[\"Compare with need date and inventory cover\"]
    B --> C[\"Quantify customer, production, and financial impact\"]
    C --> D{\"Intervention justified?\"}
    D -->|No| E[\"Monitor at normal cadence\"]
    D -->|Yes| F[\"Recover, reallocate, expedite, or escalate\"]
    F --> G[\"Confirm outcome and cost\"]
    G --> H[\"Remove root cause\"]""",
        "heading": "Applied decision artifact — exception priority board",
        "applied": """Use the [open-order exception dataset](../../assets/data/module-3/section-d/open-order-exceptions.csv) to prioritize impact, not lateness alone. The refrigerant sensor is forecast 12 days late with only two days of cover and a final-test stoppage; it requires immediate recovery. The compressor is nine days late with three days of cover and two priority units affected. The filter kit is on time with 26 days of cover and requires no action.

For each intervention, record customer or production consequence, recovery option, incremental cost, authority, owner, supplier commitment, and next check. After stabilization, classify the root cause and prevention owner. Repeated premium freight without corrective action is not exception management.""",
        "related": [
            "[Open-order exception dataset](../../assets/data/module-3/section-d/open-order-exceptions.csv)",
            "[Terms, Service Levels, and Incentives](./07-terms-slas-and-incentives.md)",
        ],
    },
    "section-d-supplier-selection-contracting-and-procurement/12-digital-procurement-marketplaces-and-auctions.md": {
        "flow": """flowchart TD
    A[\"Define demand and transaction pattern\"] --> B[\"Qualify suppliers, content, and data\"]
    B --> C{\"Which digital channel fits?\"}
    C -->|Recurring standard buy| D[\"Catalog or supplier portal\"]
    C -->|Discovery| E[\"Controlled marketplace\"]
    C -->|Comparable competition| F[\"Electronic auction\"]
    D --> G[\"Apply approval, security, tax, and audit controls\"]
    E --> G
    F --> G
    G --> H[\"Analyze adoption, compliance, value, and risk\"]""",
        "heading": "Applied decision artifact — digital-channel control design",
        "applied": """Choose the channel from the transaction need. Catalogs suit repeatable, approved items; supplier portals support direct collaboration; marketplaces broaden discovery; auctions support structured competition only when specifications, bid units, and qualification are comparable.

Before launch, define supplier onboarding, identity and role access, catalog ownership, item and tax data, approval routing, budget checks, cybersecurity, privacy, sanctions and compliance screening, bid rules, integration, exception handling, and audit retention. Measure adoption, price and contract compliance, cycle time, supplier participation, data quality, and off-channel leakage. Automation should make the approved process easier while preserving human review for risk, qualification, and ambiguous scope.""",
        "related": [
            "[Competitive Bidding and Direct Negotiation](./03-competitive-bidding-and-direct-negotiation.md)",
            "[Contract Deployment and Compliance](./05-contract-deployment-and-compliance.md)",
        ],
    },
}


def apply_lesson(relative: str, spec: dict[str, object]) -> bool:
    path = MODULE / relative
    body = path.read_text(encoding="utf-8")
    changed = False

    process_heading = "## Practical process flow"
    if process_heading not in body:
        block = (
            f"{process_heading}\n\n"
            f"```mermaid\n{spec['flow']}\n```\n\n"
        )
        anchor = "## Realistic example"
        if anchor not in body:
            raise ValueError(f"{relative}: missing realistic-example anchor")
        body = body.replace(anchor, block + anchor, 1)
        changed = True

    repeated_process_intro = (
        "The decision model above defines what evidence is required. The process below shows "
        "how a practitioner moves that evidence to an approved, controlled outcome.\n\n"
    )
    if repeated_process_intro in body:
        body = body.replace(repeated_process_intro, "", 1)
        changed = True

    applied_heading = f"## {spec['heading']}"
    if applied_heading not in body:
        block = f"{applied_heading}\n\n{spec['applied']}\n\n"
        anchor = "## Decision logic"
        if anchor not in body:
            raise ValueError(f"{relative}: missing decision-logic anchor")
        body = body.replace(anchor, block + anchor, 1)
        changed = True

    related = [
        "[Module 3 overview](../README.md)",
        "[Section overview](./README.md)",
        *spec["related"],
    ]
    replacement = "## Related concepts\n\n" + "\n".join(f"- {item}" for item in related) + "\n\n---"
    updated, count = re.subn(r"## Related concepts\n\n.*?\n\n---", replacement, body, count=1, flags=re.DOTALL)
    if count != 1:
        raise ValueError(f"{relative}: related-concepts block not found exactly once")
    if updated != body:
        body = updated
        changed = True

    if changed:
        path.write_text(body, encoding="utf-8")
    return changed


def main() -> None:
    changed = sum(apply_lesson(relative, spec) for relative, spec in LESSONS.items())
    if len(LESSONS) != 35:
        raise ValueError(f"Expected 35 Module 3 topic lessons, found {len(LESSONS)}")
    print(f"Verified 35 Module 3 lessons; updated {changed} files.")


if __name__ == "__main__":
    main()
