#!/usr/bin/env python3
"""Apply the reviewed cross-module learning contract to Modules 1 and 2.

The profiles below are intentionally topic-specific. The script is idempotent: it adds
only missing standardized sections, upgrades Module 2 answer structures, and rebuilds
related-concept/navigation links without replacing the original lesson explanations.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
M1 = ROOT / "01-supply-chains-demand-forecasting"
M2 = ROOT / "02-network-design-digital-connectivity-performance"


@dataclass(frozen=True)
class Profile:
    outcome: str
    action: str
    tradeoff: str
    evidence: str


M1_PROFILES = {
    "section-a-introduction-to-supply-chains/01-supply-chain-fundamentals.md": Profile(
        "A local improvement can reduce end-to-end service when material, information, and cash consequences are separated.",
        "Map the customer promise, participating entities, three flows, decision owners, and the measure that proves the whole chain improved.",
        "Tighter coordination improves responsiveness but adds data-sharing, governance, and dependency obligations.",
        "the customer promise, entity-and-flow map, baseline measures, assumptions, owners, and review date",
    ),
    "section-a-introduction-to-supply-chains/02-entities-and-flows.md": Profile(
        "Unseen handoffs create shortages, excess inventory, delayed decisions, and cash disputes even when each organization performs its own task.",
        "Trace product, information, and funds across every tier and assign an owner and required timing to each material handoff.",
        "More visibility improves coordination, while unnecessary detail increases integration cost and can expose sensitive partner information.",
        "the tier map, flow direction, event timestamps, ownership transfer, source system, exception rule, and accountable role",
    ),
    "section-a-introduction-to-supply-chains/03-funds-value-balance.md": Profile(
        "Physical service can look healthy while payment terms and inventory ownership push unsustainable working-capital pressure onto a critical partner.",
        "Evaluate the physical and financial flow together, including cash-to-cash time, ownership points, payment timing, and value created for each party.",
        "Extending payment can improve the buyer's cash position but may raise supplier financing cost, price, or continuity risk.",
        "payment terms, inventory ownership, receivable and payable timing, financing assumptions, service impact, and partner-risk trigger",
    ),
    "section-a-introduction-to-supply-chains/04-vertical-vs-lateral-integration.md": Profile(
        "Ownership and collaboration choices change control, investment, flexibility, knowledge access, and exposure to partners.",
        "Separate the need for control from the need for coordination, then compare ownership, contract, and collaborative options against the same requirements.",
        "Vertical integration increases control and fixed commitment; lateral collaboration preserves flexibility but depends on incentives and governance.",
        "capability requirements, control points, investment, switching cost, intellectual-property exposure, partner incentives, and exit conditions",
    ),
    "section-a-introduction-to-supply-chains/05-supply-chain-maturity.md": Profile(
        "A strategy that assumes data, trust, or decision capabilities the organization does not possess will fail during execution.",
        "Assess maturity with operating evidence, identify the capability gap that blocks the target decision, and sequence improvement before advanced design.",
        "Higher maturity enables faster coordination but requires disciplined ownership, shared measures, and sustained behavior change.",
        "current and target maturity evidence, repeated failure patterns, capability owners, milestone criteria, and benefit measures",
    ),
    "section-a-introduction-to-supply-chains/06-supply-chain-examples.md": Profile(
        "Manufacturing, service, humanitarian, project, and closed-loop networks require different flow, capacity, and customer-response logic.",
        "Classify the operating context before copying a supply-chain practice, then adapt inventory, capacity, information, and service controls to the actual flow.",
        "Standard practices improve consistency, but excessive standardization can ignore perishability, simultaneity, project uniqueness, or recovery requirements.",
        "the service or product definition, demand pattern, capacity constraint, response time, recovery route, and customer consequence",
    ),
    "section-b-demand-analysis-and-patterns/01-demand-analysis-and-environmental-scan.md": Profile(
        "A forecast can be numerically precise yet misleading when the economic, competitive, regulatory, or customer drivers behind demand have changed.",
        "Create a dated driver register, separate observed facts from hypotheses, and translate material signals into forecast scenarios and decision triggers.",
        "A broad scan can reveal structural change but also creates noise; prioritize signals by likely demand impact and decision lead time.",
        "driver source and date, direction, affected family, confidence, lag, scenario range, owner, and trigger",
    ),
    "section-b-demand-analysis-and-patterns/02-swot-market-research-and-competition.md": Profile(
        "Strategy deteriorates when internal opinions, customer evidence, and competitor signals are blended without source or confidence.",
        "Use SWOT as a synthesis after research, document evidence separately, and show how each material finding changes demand, positioning, or capacity decisions.",
        "More research reduces uncertainty but consumes time; stop when additional evidence is unlikely to change the decision or range.",
        "research question, source, sample or method, finding, confidence, competitive implication, assumption, and decision affected",
    ),
    "section-b-demand-analysis-and-patterns/03-global-perspectives.md": Profile(
        "Demand signals, lead times, regulation, currency, and channel behavior vary by market and cannot safely be averaged into one global assumption.",
        "Build a common global baseline, then preserve market-specific assumptions and test scenarios for currency, policy, infrastructure, and volatility.",
        "Global standardization improves comparability and scale, while local adaptation captures market reality at added complexity and governance cost.",
        "market assumptions, local evidence, currency and policy scenarios, lead-time distribution, service promise, and escalation threshold",
    ),
    "section-b-demand-analysis-and-patterns/04-product-portfolio-and-classification.md": Profile(
        "Excess variants divide demand, reduce forecastability, increase changeovers, and trap inventory while apparent revenue remains attractive.",
        "Segment offerings by demand, lifecycle, margin, strategic role, service need, and complexity cost before setting differentiated planning policies.",
        "Broader variety may improve customer fit but increases inventory, data, sourcing, production, and service complexity.",
        "SKU-family hierarchy, demand and margin history, lifecycle stage, service rule, complexity cost, owner, and retirement trigger",
    ),
    "section-b-demand-analysis-and-patterns/05-product-life-cycle-and-services.md": Profile(
        "Demand evidence, supply risk, inventory exposure, and customer expectations change materially from introduction through decline.",
        "Assign a lifecycle stage using evidence and connect it to forecast method, capacity posture, inventory policy, service support, and exit decisions.",
        "Early capacity protects growth but risks stranded investment; late-life inventory protects service but increases obsolescence.",
        "stage evidence, demand range, installed base, capacity and inventory exposure, service obligation, and transition gate",
    ),
    "section-b-demand-analysis-and-patterns/06-macroeconomic-demand-patterns.md": Profile(
        "Inflation, interest rates, output, employment, and business cycles can alter volume, mix, timing, and customer affordability before internal orders reveal the change.",
        "Select indicators with a plausible causal path and lead time, test their historical relationship, and use scenarios instead of mechanical extrapolation.",
        "Leading indicators offer earlier warning but can revise, decouple, or signal conditions that do not affect the target market.",
        "indicator definition and vintage, causal hypothesis, lag, historical fit, scenario range, affected families, and review trigger",
    ),
    "section-b-demand-analysis-and-patterns/07-microeconomics-price-elasticity-marginal-analysis.md": Profile(
        "Price and volume decisions can increase revenue while reducing contribution or creating capacity and service costs that destroy value.",
        "Estimate elasticity over a stated range, calculate incremental revenue and cost, and approve changes on marginal profit and operational feasibility.",
        "A lower price may expand volume and utilization, but it can compress margin, overload constraints, and reset customer expectations.",
        "price range, baseline and response volume, elasticity method, variable and constraint cost, contribution, confidence, and guardrail",
    ),
    "section-b-demand-analysis-and-patterns/08-short-medium-term-demand-patterns.md": Profile(
        "Trend, seasonality, cycles, promotions, and random variation require different forecasts and different operational responses.",
        "Decompose the observed pattern, label known events, select a model for the planning horizon, and retain residual uncertainty for capacity and inventory decisions.",
        "A responsive method detects change sooner but may overreact to noise; a stable method reduces noise but can lag a genuine shift.",
        "time series, event calendar, decomposition choice, horizon, parameters, residual error, owner, and recalibration trigger",
    ),
    "section-c-demand-management/01-demand-management-foundations.md": Profile(
        "Uncoordinated forecasting, commercial activity, and supply response create promises that capacity, inventory, or profitability cannot support.",
        "Run demand management as a closed loop that senses demand, develops a consensus plan, influences feasible demand, and measures outcomes.",
        "Influencing demand can protect service and margin but may shift customers, channels, or revenue in unintended ways.",
        "baseline forecast, commercial assumptions, constraints, approved demand actions, owners, customer effect, and outcome measures",
    ),
    "section-c-demand-management/02-planning-demand-and-demand-plan.md": Profile(
        "A number without assumptions, horizon, ownership, and intended use cannot coordinate capacity, inventory, finance, or suppliers.",
        "Publish one controlled demand plan by family, period, and scenario, with documented assumptions and explicit uses at each planning horizon.",
        "One consensus plan improves alignment, while retaining scenario ranges prevents false precision when uncertainty is material.",
        "versioned demand plan, family hierarchy, units and currency, assumptions, events, confidence range, approvers, and consumers",
    ),
    "section-c-demand-management/03-communicating-demand.md": Profile(
        "The same demand signal can produce conflicting actions when functions receive different versions, units, timing, or confidence.",
        "Define the audience, decision, aggregation, timing, uncertainty, and feedback route before selecting the dashboard or message.",
        "More detail supports diagnosis but can obscure the decision; greater aggregation improves alignment but can hide mix and local risk.",
        "audience-decision matrix, approved version, units, horizon, assumptions, exception thresholds, acknowledgement, and feedback",
    ),
    "section-c-demand-management/04-demand-manager-and-dashboard.md": Profile(
        "A dashboard that displays numbers without assumptions, gaps, ownership, and required decisions becomes passive reporting.",
        "Design the demand review around changes from the prior plan, assumption movement, opportunity and risk ranges, gaps, and named decisions.",
        "A compact dashboard focuses attention, but excessive aggregation can conceal product, channel, or timing problems that need action.",
        "prior and current plan, variance drivers, opportunity and risk ranges, decision request, owner, due date, and outcome",
    ),
    "section-c-demand-management/05-influencing-demand-and-pdca.md": Profile(
        "Demand actions consume price, channel, inventory, and customer trust, so they must be treated as controlled experiments rather than assumptions.",
        "Define the problem and target, test one demand lever with guardrails, compare the outcome with baseline, and adopt, adapt, or stop through PDCA.",
        "A strong intervention can close a gap quickly but may erode margin, pull demand forward, or create a later service problem.",
        "baseline, hypothesis, target segment, action, cost, capacity check, guardrail, measured response, and learning decision",
    ),
    "section-c-demand-management/06-demand-shaping-and-four-ps.md": Profile(
        "Product, price, placement, and promotion decisions change both demand and the operational burden required to serve it.",
        "Evaluate each proposed market lever against incremental demand, contribution, capacity, inventory, lead time, channel conflict, and customer effect.",
        "Demand shaping can improve mix and utilization, but poorly timed actions can overload constraints or create low-quality revenue.",
        "target segment, lever and timing, expected lift, contribution, capacity and inventory impact, channel owner, and stop rule",
    ),
    "section-c-demand-management/07-product-life-cycle.md": Profile(
        "Using one demand and supply policy across introduction, growth, maturity, and decline creates predictable forecast, capacity, and inventory errors.",
        "Set stage-specific forecasting, capacity, inventory, channel, and service rules and review the stage when evidence changes.",
        "Early investment supports growth but increases downside exposure; late rationalization reduces cost but can damage service obligations.",
        "stage indicators, demand range, adoption or installed-base data, capacity posture, inventory rule, service commitment, and exit trigger",
    ),
    "section-c-demand-management/08-plm-and-new-product-introduction.md": Profile(
        "Product decisions made before launch determine supplier lead time, capacity, inventory, serviceability, compliance, and forecast risk.",
        "Use cross-functional gates that connect design maturity, demand scenarios, sourcing, capacity, quality, data, service, and launch readiness.",
        "Freezing design improves execution stability, while preserving late flexibility can capture learning at the cost of timing and control complexity.",
        "requirement baseline, design maturity, demand scenarios, supplier and capacity evidence, quality gates, master data, and launch decision",
    ),
    "section-c-demand-management/09-npi-frequency-and-demand-uncertainty.md": Profile(
        "High launch frequency and high demand uncertainty compound obsolescence, changeover, capacity, data, and supplier risk.",
        "Place the portfolio on the launch-frequency and uncertainty matrix, then choose commonality, postponement, capacity, inventory, and governance controls.",
        "Frequent introductions may sustain innovation, but they fragment demand and shorten the time available to learn and stabilize operations.",
        "launch calendar, demand range, common-platform percentage, differentiation point, capacity and inventory exposure, and gate owner",
    ),
    "section-d-forecasting/01-forecasting-principles-and-process.md": Profile(
        "Forecast value comes from disciplined decisions under uncertainty, not from presenting one number as certain.",
        "Define purpose, item and horizon, gather and clean data, select and validate a method, document assumptions, measure error, and improve the process.",
        "More sophisticated models may improve fit but reduce explainability, maintainability, and timely business challenge.",
        "forecast purpose, scope, data vintage, method and parameters, assumptions, error history, owner, and change log",
    ),
    "section-d-forecasting/02-qualitative-and-combination-methods.md": Profile(
        "New products, disruptions, and structural change often lack stable history, while expert judgment alone is vulnerable to bias and influence.",
        "Use a documented qualitative method, independent inputs where possible, explicit scenarios, and a controlled rule for combining judgment with data.",
        "Judgment captures information outside the data but can introduce optimism, anchoring, hierarchy, and double counting.",
        "expert selection, evidence supplied, independent estimates, scenario assumptions, combination weights, dissent, and later accuracy",
    ),
    "section-d-forecasting/03-time-series-forecasting-and-method-selection.md": Profile(
        "A method can fit history well yet fail operationally when its assumptions do not match trend, seasonality, intermittency, or the decision horizon.",
        "Classify the pattern, create a holdout test, compare simple credible methods, inspect residuals and bias, and select using business-relevant error.",
        "Responsive models adapt faster but may chase noise; stable models are easier to operate but can lag turning points.",
        "training and holdout periods, pattern classification, candidate methods, parameters, error by segment, bias, and selection rationale",
    ),
    "section-d-forecasting/04-seasonality-deseasonalizing-reseasonalizing.md": Profile(
        "Strong recurring peaks can be mistaken for growth and cause distorted base forecasts, capacity plans, and inventory targets.",
        "Calculate normalized seasonal indices from comparable history, remove seasonality, forecast the base, and restore the future seasonal effect.",
        "Stable indices simplify planning, but structural calendar, channel, or product changes can make historical seasonality misleading.",
        "source history, missing and event treatment, monthly averages, normalized indices, base forecast, future calendar, and refresh rule",
    ),
    "section-d-forecasting/05-moving-averages-and-exponential-smoothing.md": Profile(
        "The smoothing choice determines how quickly a plan reacts to real change and how much random variation enters operations.",
        "Compare moving-average windows, weights, and alpha on the same holdout period, then select the simplest method that meets error and bias needs.",
        "Greater smoothing stabilizes production and inventory but increases lag; higher responsiveness detects change faster but can amplify noise.",
        "actual history, forecast origin, window or alpha, initialization, holdout errors, bias, and approved parameter change",
    ),
    "section-d-forecasting/06-service-sector-and-associative-forecasting.md": Profile(
        "Services cannot inventory unused capacity, and their demand may depend more on appointments, weather, installed base, or events than past volume alone.",
        "Forecast at the time and location granularity where capacity is committed and test external predictors with a credible causal and timing relationship.",
        "Fine-grained forecasts improve staffing decisions but contain more noise and require timely local data.",
        "service interval and location, capacity unit, demand history, candidate drivers, lag, model error, staffing rule, and override reason",
    ),
    "section-d-forecasting/07-leading-indicators-regression-correlation.md": Profile(
        "A correlated predictor can create false confidence when timing, causality, data leakage, or structural stability is not tested.",
        "Define the causal hypothesis and lag before fitting regression, validate out of sample, inspect residuals, and monitor coefficient stability.",
        "Leading indicators provide earlier warning but may be revised, become unavailable, or stop representing the target relationship.",
        "predictor definition and vintage, lag, regression coefficients, correlation, holdout error, residual review, and stability trigger",
    ),
    "section-d-forecasting/08-forecast-error-bias-random-variation.md": Profile(
        "Error magnitude and error direction drive different decisions: variability affects buffers, while persistent bias requires a model or process correction.",
        "Freeze the error convention, calculate signed and absolute measures by segment, inspect cumulative direction, and investigate business causes.",
        "Aggregated accuracy simplifies reporting but can hide offsetting bias, high-value misses, and service-critical failures.",
        "actual and forecast vintage, error convention, segmentation, event flags, signed and absolute errors, root cause, and corrective action",
    ),
    "section-d-forecasting/09-mad-tracking-signal-standard-deviation.md": Profile(
        "Confusing bias measures with variability measures leads either to unnecessary buffers or continued systematic under- or overforecasting.",
        "Calculate MAD and cumulative signed error consistently, interpret the tracking signal, align variability to lead time, and set safety stock with an explicit service factor.",
        "Higher safety stock protects service but increases cash, space, obsolescence, and the risk of masking a biased plan.",
        "error series and convention, MAD, cumulative error, tracking limit, lead-time variability, service factor, units, and approval",
    ),
    "section-d-forecasting/10-mse-mape-and-error-measures.md": Profile(
        "Metric choice changes which errors receive attention and can reward a model that performs poorly on the decisions that matter.",
        "Select error measures by decision purpose, volume scale, zero-demand behavior, and penalty for large misses, then review more than one perspective.",
        "MSE emphasizes large misses but is scale-dependent; MAPE enables percentage comparison but becomes unstable near zero demand.",
        "actual and forecast vintage, metric definitions, exclusions, segment weights, error distribution, bias, and model-selection decision",
    ),
    "section-e-supply-demand-alignment/01-operations-planning-and-control.md": Profile(
        "Strategy, aggregate plans, master schedules, and execution fail when each horizon uses different assumptions or lacks a feedback path.",
        "Connect every planning level through defined inputs, outputs, time fences, owners, and variance escalation from execution back to planning.",
        "Central coordination improves alignment, while excessive control can slow local response to short-lived operating conditions.",
        "planning hierarchy, horizon and bucket, approved inputs, constraints, decision rights, schedule version, and variance feedback",
    ),
    "section-e-supply-demand-alignment/02-strategic-business-master-resource-planning.md": Profile(
        "A feasible short-term schedule cannot compensate for a long-term capacity gap or a business plan that was never translated into operational units.",
        "Reconcile strategic direction, financial plan, family demand, resource requirements, and the master schedule using consistent units and horizons.",
        "Early resource commitment protects growth but can strand capital if demand changes; delayed commitment preserves cash but narrows response options.",
        "volume and financial reconciliation, family hierarchy, resource rates, capacity limits, investment lead time, scenario, and approval gate",
    ),
    "section-e-supply-demand-alignment/03-sop-foundations-and-monthly-process.md": Profile(
        "Without a recurring decision cycle, functions optimize separate plans and unresolved gaps arrive in execution as expedites and service failures.",
        "Run data preparation, demand review, supply review, reconciliation, pre-S&OP, and executive approval with named inputs, outputs, and decisions.",
        "A fixed cadence creates discipline, but material exceptions still need event-driven escalation between monthly meetings.",
        "calendar, plan version, assumptions, demand and supply gaps, alternatives, financial effect, decision log, and follow-up",
    ),
    "section-e-supply-demand-alignment/04-demand-review-and-dashboard.md": Profile(
        "A demand review that debates one forecast number without drivers, ranges, and prior commitments cannot produce an accountable plan.",
        "Review actuals versus prior plan, identify assumption changes, quantify upside and downside, and escalate only decisions that need cross-functional authority.",
        "A stable baseline supports accountability, while legitimate new evidence must still be incorporated without turning every meeting into replanning from zero.",
        "prior and proposed plan, forecast error and bias, assumption changes, event effects, opportunity and risk, owner, and decision request",
    ),
    "section-e-supply-demand-alignment/05-supply-review-and-production-plan.md": Profile(
        "Supply feasibility must reflect material, labor, equipment, supplier, quality, and logistics constraints rather than nominal capacity alone.",
        "Convert the demand plan into resource requirements, identify timed gaps, develop feasible alternatives, and quantify service, inventory, cost, and risk.",
        "Adding capacity protects service but increases cost and commitment; using backlog or inventory preserves capacity but shifts customer or cash exposure.",
        "demand by family and period, resource rates, demonstrated capacity, constraints, inventory, alternatives, cost, and owner",
    ),
    "section-e-supply-demand-alignment/06-sop-inputs-outputs-and-functional-interfaces.md": Profile(
        "S&OP breaks down when functions provide incompatible inputs or leave the meeting with different interpretations of the approved plan.",
        "Define an input-output contract for commercial, planning, operations, procurement, finance, product, and executive roles.",
        "Broader participation improves decision quality, but unclear decision rights create review cycles without ownership.",
        "RACI, input definition and due date, source system, unit and horizon, output decision, recipient, acknowledgement, and escalation",
    ),
    "section-e-supply-demand-alignment/07-level-chase-hybrid-strategies.md": Profile(
        "The response strategy determines inventory, backlog, labor stability, overtime, subcontracting, service, and cost across the planning horizon.",
        "Build level, chase, and hybrid alternatives against the same demand and starting conditions, reconcile units monthly, and compare total business effects.",
        "Level plans stabilize labor and assets but build inventory; chase plans reduce inventory but increase capacity, workforce, and execution volatility.",
        "demand, opening inventory and backlog, regular and flexible capacity, unit costs, service rules, monthly balance, and sensitivity",
    ),
    "section-e-supply-demand-alignment/08-supply-demand-production-environments.md": Profile(
        "The customer-order decoupling point determines what may be forecast, stocked, configured, engineered, and promised before actual demand arrives.",
        "Choose MTS, ATO, MTO, ETO, or PTO by demand predictability, product variety, lead-time promise, modularity, capacity, and engineering content.",
        "Earlier commitment shortens response but increases forecast and inventory exposure; later commitment reduces exposure but lengthens customer lead time.",
        "decoupling point, forecast level, inventory position, configuration or engineering lead time, capacity reservation, and promise rule",
    ),
    "section-e-supply-demand-alignment/09-reconciliation-and-executive-sop.md": Profile(
        "Functional alternatives remain incomplete until their customer, operational, financial, and risk consequences are compared on one basis.",
        "Translate the demand-supply gap into enterprise alternatives, reconcile volume and value, define residual risk, and obtain an explicit executive decision.",
        "Escalation protects enterprise alignment but should not replace delegated authority for routine decisions within agreed thresholds.",
        "alternative calculations, income and cash effects, service and risk exposure, recommendation, decision rights, approval, and trigger",
    ),
    "section-e-supply-demand-alignment/10-implementing-sop.md": Profile(
        "A technically correct process will fail if leaders do not use it to make decisions or if teams cannot trust the data and commitments.",
        "Implement S&OP through a scoped pilot, stable definitions, visible decision rights, behavior measures, issue resolution, and staged expansion.",
        "A narrow pilot accelerates learning but may miss enterprise interdependencies; a broad launch increases coverage but multiplies change risk.",
        "baseline maturity, pilot scope, role charter, data definitions, meeting evidence, decision adherence, benefits, and scale gate",
    ),
    "section-e-supply-demand-alignment/11-demand-prioritization-and-customer-service.md": Profile(
        "When supply is constrained, allocation choices directly affect customer outcomes, revenue, fairness, contracts, and long-term trust.",
        "Apply a preapproved prioritization policy using mandatory commitments, customer consequence, alternatives, and total enterprise impact, then measure service outcomes.",
        "Protecting the highest immediate value may damage fairness or strategic relationships; equal allocation can ignore materially different consequences.",
        "available supply, eligible demand, policy criteria, contract and regulatory obligations, allocation record, approvals, and service result",
    ),
}


M1_MISSING_MISTAKES = {
    "section-a-introduction-to-supply-chains/06-supply-chain-examples.md": [
        "Copying a manufacturing inventory rule into a service or project environment without testing the flow",
        "Treating every network as if demand, capacity, and recovery can be managed at the same time scale",
        "Selecting a fashionable practice before defining the customer outcome and operating constraint",
    ],
    "section-c-demand-management/08-plm-and-new-product-introduction.md": [
        "Involving supply, quality, and service only after the product design is frozen",
        "Treating one launch forecast as a committed demand quantity despite material uncertainty",
        "Launching before supplier, capacity, quality, master-data, and end-of-life gates have objective evidence",
    ],
}


M2_PROFILES = {
    "section-a-network-design-and-technology-investment/01-strategy-to-network-design.md": Profile(
        "Network models optimize the criteria they are given, so a weak translation of strategy produces a precise design for the wrong customer promise.",
        "Translate competitive intent into segment-specific service, cost, resilience, sustainability, and growth requirements before generating network alternatives.",
        "A network built for responsiveness usually carries more capacity, inventory, or proximity cost than one designed only for efficiency.",
        "strategy statement, customer promise, design requirements, constraints, measures, assumptions, decision owner, and review trigger",
    ),
    "section-a-network-design-and-technology-investment/02-market-segmentation-and-service-choices.md": Profile(
        "One service policy forces low-value demand to consume expensive responsiveness or leaves critical demand underserved.",
        "Segment customers and products using behavior and economics, assign a measurable service promise, and test whether operations can execute it profitably.",
        "More service segments improve fit but add inventory, rules, master data, training, and exception complexity.",
        "segment definition, demand and margin evidence, promise, operating policy, exceptions, owner, and profitability guardrail",
    ),
    "section-a-network-design-and-technology-investment/03-network-configuration-and-flow-design.md": Profile(
        "Facility choices alter transportation, inventory, lead time, duty, fixed cost, resilience, and information requirements at the same time.",
        "Define feasible alternatives, calculate comparable economics and service, apply mandatory constraints, then test weighted results under changed assumptions.",
        "Additional regional nodes shorten response and improve recovery options but duplicate inventory, cost, processes, and governance.",
        "alternative definition, flow map, volumes, costs, inventory days, service and resilience scores, constraints, weights, and sensitivity",
    ),
    "section-a-network-design-and-technology-investment/04-efficiency-responsiveness-resilience.md": Profile(
        "Maximizing one capability can weaken the others and move exposure to customers, suppliers, cash, or recovery time.",
        "Set a minimum service and resilience boundary, compare the cost of feasible designs, and target buffers at the constraints that drive customer consequence.",
        "Extra capacity and redundancy improve response and recovery but reduce utilization and raise ongoing cost.",
        "customer consequence, bottleneck map, capacity and inventory buffers, recovery assumptions, utilization, cost, and activation trigger",
    ),
    "section-a-network-design-and-technology-investment/05-sourcing-footprint-and-partner-decisions.md": Profile(
        "A low purchase price can be offset by freight, inventory, quality, coordination, sub-tier dependence, and disruption exposure.",
        "Compare make, buy, partner, and location options on total delivered cost, capability, lead time, dependency, controls, and executable recovery.",
        "Consolidation creates leverage and simplicity but increases dependency; diversification improves options but adds qualification and management cost.",
        "requirement, qualified sources and sub-tiers, total-cost bridge, capacity, lead-time distribution, recovery plan, controls, and exit rights",
    ),
    "section-a-network-design-and-technology-investment/06-digital-requirements-and-information-latency.md": Profile(
        "Late or incomplete information turns a manageable deviation into a customer, cost, or inventory exception.",
        "Work backward from each decision to define the event, data fields, latency, quality, owner, threshold, and action required.",
        "Lower latency supports faster action but raises integration, monitoring, false-alert, and partner-readiness demands.",
        "decision-to-data card, event source, timestamp, required fields, latency target, quality rule, owner, and fallback",
    ),
    "section-a-network-design-and-technology-investment/07-technology-business-case-and-tco.md": Profile(
        "Technology value depends on adoption, process change, data quality, and benefit ownership—not licensed functionality alone.",
        "Build a time-phased total-cost and benefit model, separate cash from capacity and risk, calculate ROI and payback, and test volume, adoption, and timing sensitivity.",
        "A broader first release may promise more value but increases integration, change, schedule, and benefit-realization risk.",
        "cost and benefit rows by year, baseline, measurement basis, owner, adoption assumption, dependencies, sensitivity, and realization evidence",
    ),
    "section-a-network-design-and-technology-investment/08-capability-maturity-and-transformation-roadmap.md": Profile(
        "A roadmap fails when later capabilities depend on data, process, skills, or governance that earlier releases did not establish.",
        "Assess current capability with evidence, define the target decision behavior, map dependencies, and gate each release on measurable readiness and benefit.",
        "Rapid scope can demonstrate ambition but creates fragile dependencies; staged delivery reduces risk but delays some benefits.",
        "current and target maturity, dependency map, release outcomes, entry and exit criteria, owners, adoption, benefit, and stop decision",
    ),
    "section-a-network-design-and-technology-investment/09-governance-change-and-network-orchestration.md": Profile(
        "Cross-functional networks respond slowly or inconsistently when decision rights, partner roles, and escalation thresholds are undefined.",
        "Assign end-to-end ownership, delegated thresholds, consultation rules, partner obligations, evidence, and escalation for routine and material exceptions.",
        "Central governance improves consistency, while excessive escalation delays decisions that should be made close to the event.",
        "decision-right matrix, thresholds, named roles, partner commitments, exception log, response time, adoption evidence, and review",
    ),
    "section-b-connected-supply-networks-and-master-data/01-application-landscape-and-digital-thread.md": Profile(
        "Disconnected applications create duplicate records, delayed events, reconciliation work, and decisions that cannot be traced to one operating state.",
        "Map capabilities, systems of record, planning and execution services, events, identifiers, and decision consumers before choosing applications.",
        "A unified platform simplifies ownership and integration but may sacrifice specialized capability; best-of-breed tools add capability and interfaces.",
        "capability map, system-of-record decision, master identifiers, event lineage, interfaces, owner, service level, and retirement plan",
    ),
    "section-b-connected-supply-networks-and-master-data/02-core-platforms-vs-specialized-applications.md": Profile(
        "Application boundaries determine process continuity, upgradeability, data consistency, vendor dependence, and the cost of future change.",
        "Keep stable enterprise records and controls in the core, place differentiating capability where it creates measurable value, and define integration and exit boundaries.",
        "Core standardization reduces complexity; specialized applications improve fit but add contracts, data replication, interfaces, and support obligations.",
        "capability requirements, fit-gap evidence, record ownership, interfaces, lifecycle cost, vendor viability, upgrade path, and exit plan",
    ),
    "section-b-connected-supply-networks-and-master-data/03-advanced-planning-and-constraint-management.md": Profile(
        "Optimization can recommend infeasible or economically harmful actions when constraints, costs, priorities, or data freshness are incomplete.",
        "Define the planning decision, objective, hard constraints, soft penalties, horizon, data cut, exception route, and human approval boundary.",
        "More constraints improve realism but increase data maintenance, solve complexity, and the risk of embedding obsolete policies.",
        "model scope, objective and units, constraint register, source data and vintage, infeasibility handling, override, and outcome",
    ),
    "section-b-connected-supply-networks-and-master-data/04-event-management-and-control-towers.md": Profile(
        "Visibility creates value only when a trusted event changes a prioritized decision before avoidable impact occurs.",
        "Define material events, validate them, estimate business impact, route prioritized exceptions to an owner, record action, and learn from outcome.",
        "More alerts increase coverage but create fatigue; tighter filtering reduces noise but may miss emerging conditions.",
        "event definition, source and timestamp, validation status, affected objects, impact, priority, owner, response, and outcome",
    ),
    "section-b-connected-supply-networks-and-master-data/05-warehouse-management-systems.md": Profile(
        "Warehouse execution affects inventory accuracy, order priority, labor, traceability, capacity, and the reliability of every downstream promise.",
        "Design receiving, putaway, inventory status, replenishment, picking, packing, staging, and exception rules around measurable service and control requirements.",
        "Detailed system-directed work improves consistency and traceability but requires accurate master data, devices, discipline, and recovery procedures.",
        "warehouse process map, location and item rules, status ownership, task priorities, capacity, scan evidence, exceptions, and performance",
    ),
    "section-b-connected-supply-networks-and-master-data/06-transportation-management-systems.md": Profile(
        "Transportation choices change service, freight cost, capacity use, emissions, inventory in transit, and customer communication.",
        "Plan and tender comparable lanes using service and cost constraints, capture carrier events, manage exceptions, and settle against executed evidence.",
        "Cost-efficient modes and consolidation reduce freight expense but may increase lead time, variability, inventory, and response risk.",
        "lane master, shipment demand, mode and carrier constraints, rate and tender evidence, events, cost, service, emissions, and claims",
    ),
    "section-b-connected-supply-networks-and-master-data/07-information-architecture-and-data-platforms.md": Profile(
        "Data copied without ownership, semantics, lineage, and timing can make every application technically connected but operationally inconsistent.",
        "Assign authoritative records, define integration and analytical copies, preserve lineage and meaning, and match data freshness to the consuming decision.",
        "Centralized data improves consistency and governance, while distributed ownership can improve domain accountability and speed.",
        "business object and definition, authoritative source, lineage, refresh, transformation, access, retention, quality rule, and owner",
    ),
    "section-b-connected-supply-networks-and-master-data/08-cloud-saas-and-deployment-choices.md": Profile(
        "Deployment choices affect control, scalability, resilience, integration, upgrade timing, security, cost, and exit flexibility.",
        "Compare options against workload criticality, data obligations, latency, customization need, operating capability, recovery, lifecycle cost, and exit.",
        "SaaS accelerates standard capability and upgrades but limits modification and increases dependence on vendor service and release policy.",
        "requirement and classification, architecture option, shared-responsibility matrix, integration, recovery objective, cost, contract, and exit test",
    ),
    "section-b-connected-supply-networks-and-master-data/09-integration-patterns-apis-middleware-events.md": Profile(
        "The wrong integration pattern creates delay, duplication, brittle coupling, and ambiguous recovery when messages fail.",
        "Choose batch, synchronous API, asynchronous message, or event streaming according to decision latency, volume, coupling, replay, and failure behavior.",
        "Synchronous integration gives immediate response but couples availability; asynchronous patterns improve resilience but require ordering and reconciliation controls.",
        "interface contract, identifiers, schema version, timing, idempotency, acknowledgement, retry, monitoring, reconciliation, and owner",
    ),
    "section-b-connected-supply-networks-and-master-data/10-digital-commerce-and-order-connectivity.md": Profile(
        "A digital channel can increase demand while creating invalid promises, fragmented orders, returns, fraud, and service inconsistency.",
        "Connect offer, price, availability, promise, order, fulfillment, payment, status, cancellation, and return through shared identifiers and controls.",
        "Faster self-service improves reach and convenience but increases real-time data, availability, cybersecurity, and exception demands.",
        "channel promise, product and customer data, price and availability source, order status events, payment control, returns, and service owner",
    ),
    "section-b-connected-supply-networks-and-master-data/11-partner-visibility-and-data-sharing.md": Profile(
        "Sharing data that does not change a joint decision creates cost and exposure without demonstrated operating value.",
        "Define the decision and minimum necessary information, agree semantics and timing, protect access, assign response, and measure avoided impact.",
        "Greater transparency can improve coordination but increases confidentiality, misuse, quality, and dependency exposure.",
        "shared decision, fields and aggregation, permitted purpose, timing, quality, access, retention, response obligation, and value measure",
    ),
    "section-b-connected-supply-networks-and-master-data/12-inventory-collaboration-and-replenishment.md": Profile(
        "Replenishment authority, inventory ownership, payment timing, and service accountability are separate choices that must be designed explicitly.",
        "Select buyer-managed, supplier-managed, consigned, or collaborative rules using demand, visibility, lead time, economics, trust, and exception capability.",
        "Supplier management can reduce buyer workload and shortages but may increase dependence, gaming risk, or inventory if incentives are misaligned.",
        "inventory definition and status, ownership transfer, min-max or forecast rule, lead time, service target, payment event, exceptions, and reconciliation",
    ),
    "section-b-connected-supply-networks-and-master-data/13-legal-privacy-and-contract-controls.md": Profile(
        "Connected networks can create obligations and exposure across jurisdictions, data subjects, intellectual property, records, and partner actions.",
        "Map data and process flows, classify obligations, minimize collection, assign permitted use and accountability, and retain control evidence.",
        "Broader data use may improve planning and analytics but increases privacy, contractual, retention, localization, and breach exposure.",
        "data-flow map, legal basis and purpose, roles, contract terms, access, retention, location, incident duty, audit rights, and deletion evidence",
    ),
    "section-b-connected-supply-networks-and-master-data/14-cybersecurity-and-third-party-risk.md": Profile(
        "A connected partner or application can become an operational interruption, data-loss, fraud, safety, or recovery pathway.",
        "Classify critical services and data, assess controls, limit access, monitor activity, test recovery, manage vulnerabilities, and preserve an exit route.",
        "Stronger controls reduce exposure but can slow onboarding, increase operating effort, and constrain information sharing.",
        "asset and dependency inventory, access model, security evidence, monitoring, incident duties, recovery test, residual risk, and exception approval",
    ),
    "section-b-connected-supply-networks-and-master-data/15-master-data-domains-and-lifecycle.md": Profile(
        "Invalid item, customer, supplier, location, resource, or lane records propagate errors across planning, execution, compliance, and finance.",
        "Define each domain's owner, required attributes, creation and approval, effective dating, distribution, change control, monitoring, and retirement.",
        "Central control improves consistency, while domain stewardship keeps decisions close to business knowledge and requires coordinated governance.",
        "domain definition, required attributes, owner and steward, workflow, effective dates, downstream consumers, quality rules, and retirement evidence",
    ),
    "section-b-connected-supply-networks-and-master-data/16-automatic-identification-and-traceability.md": Profile(
        "Traceability fails when identifiers, events, locations, quantities, and transformations cannot be connected across organizations and systems.",
        "Choose identification and capture technology for the required granularity, record trusted events, link parent-child transformations, and test recall questions.",
        "Finer serialization improves traceability but raises label, scanning, data-volume, exception, and partner-adoption cost.",
        "identifier standard, label and reader rule, commissioning, event and location, aggregation, transformation, exception, and trace test",
    ),
    "section-b-connected-supply-networks-and-master-data/17-data-quality-cleansing-and-stewardship.md": Profile(
        "High average completeness can hide a small number of critical defects that block customs, planning, promise, production, or payment.",
        "Define decision-critical rules, prevent invalid creation, monitor defects, assess impact, correct and approve records, remove root causes, and verify improvement.",
        "Broad cleansing improves the baseline but can consume effort on low-impact fields; risk-based prioritization may leave noncritical defects visible longer.",
        "critical rule catalog, defect record, affected decision and objects, severity, owner, correction approval, root cause, and recurrence measure",
    ),
    "section-b-connected-supply-networks-and-master-data/18-decision-support-analytics-and-ai.md": Profile(
        "Analytics and AI can scale poor objectives, biased data, or unsafe actions faster than manual decision making.",
        "Define the decision and baseline, validate data and model performance, set human and automated boundaries, monitor drift, and retain override and outcome evidence.",
        "Greater automation improves speed and consistency but increases model, control, explainability, and failure-propagation risk.",
        "decision objective, training and test data, model version, performance by segment, guardrails, approval mode, override, drift, and outcome",
    ),
    "section-c-performance-and-financial-insight/01-measurement-system-design.md": Profile(
        "Measures change behavior, so an incomplete metric can improve its numerator while damaging service, cash, risk, or the end-to-end process.",
        "Start from the decision, define the outcome and diagnostic measures, balance dimensions, assign ownership, and set thresholds that trigger action.",
        "More measures improve diagnostic coverage but dilute attention, increase data cost, and create conflicting incentives.",
        "metric definition, purpose, formula and units, source, frequency, target, tolerance, owner, action, and balancing measure",
    ),
    "section-c-performance-and-financial-insight/02-strategy-to-metric-selection.md": Profile(
        "A metric portfolio loses value when it is inherited from available data rather than selected to test strategy and operating choices.",
        "Translate each strategic objective into an outcome, causal driver, risk, decision, measure, target, and action owner, then remove unused metrics.",
        "Strategic measures support alignment but may lag; operational drivers enable action but can encourage local optimization.",
        "strategy-to-measure trace, causal hypothesis, definition, target basis, owner, decision cadence, balancing metric, and retirement rule",
    ),
    "section-c-performance-and-financial-insight/03-dashboards-scorecards-and-cadence.md": Profile(
        "A visually polished dashboard still fails when it does not distinguish status, diagnosis, decision, ownership, and timing.",
        "Match dashboard or scorecard content to the audience and cadence, highlight exceptions and trends, and connect every material signal to action.",
        "Frequent real-time views accelerate response but can create noise; slower scorecards support reflection but may miss urgent deterioration.",
        "audience, decision and cadence, metric definitions, targets, trends, exception thresholds, drill path, owner, and action log",
    ),
    "section-c-performance-and-financial-insight/04-metric-hierarchies-and-process-ownership.md": Profile(
        "Enterprise outcomes cannot be improved reliably when leading drivers are split among functions with no end-to-end owner.",
        "Build a metric tree from outcome to controllable drivers, assign process and component owners, and define escalation for cross-functional gaps.",
        "Hierarchies improve causal visibility but become bureaucratic when too deep, duplicated, or disconnected from decisions.",
        "metric tree, causal links, calculation ownership, process owner, thresholds, drill-down path, actions, and outcome validation",
    ),
    "section-c-performance-and-financial-insight/05-benchmarking-and-gap-analysis.md": Profile(
        "A benchmark can misdirect investment when scope, mix, service, geography, accounting, maturity, or data definitions are not comparable.",
        "Normalize definitions, test comparability, calculate the gap, diagnose mechanisms, estimate value, and prioritize actions that fit strategy.",
        "External benchmarks create challenge but may lack context; internal benchmarks are comparable but can preserve a weak enterprise standard.",
        "benchmark source and period, definition, scope and normalization, comparable peer logic, gap, root cause, value case, and owner",
    ),
    "section-c-performance-and-financial-insight/06-perfect-order-and-customer-service.md": Profile(
        "Separate service averages can look strong while few orders satisfy every customer requirement at the same time.",
        "Define eligible orders and all required conditions, calculate the intersection as perfect order, and diagnose failures by reason and segment.",
        "A strict composite metric reflects customer experience but can hide which component caused failure without supporting diagnostics.",
        "eligible population, requested and promised dates, completeness, damage and documentation rules, order-level evidence, failure reason, and owner",
    ),
    "section-c-performance-and-financial-insight/07-speed-reliability-and-agility-metrics.md": Profile(
        "Average speed can improve while variability and recovery remain poor, leaving customers unable to rely on the promise.",
        "Measure cycle-time distribution, promise reliability, and response to a defined disruption or demand change, then connect each to customer consequence.",
        "Buffers improve reliability and agility but add inventory, capacity, time, or cost; removing them can expose variability.",
        "start and end events, time distribution, promise basis, on-time tolerance, disruption scenario, recovery measure, segment, and action",
    ),
    "section-c-performance-and-financial-insight/08-cost-profit-and-productivity.md": Profile(
        "Cost reduction and output growth do not create value when they reduce contribution, quality, service, or the effective use of constrained resources.",
        "Define the economic boundary, separate fixed and variable effects, connect productivity to accepted output, and test profit and service consequences.",
        "Higher utilization can lower unit cost but increase queues, lead time, failure exposure, and inflexibility at constrained resources.",
        "revenue and cost baseline, volume and mix, accepted output, resource input, constraint, margin effect, service balance, and owner",
    ),
    "section-c-performance-and-financial-insight/09-cash-to-cash-and-working-capital.md": Profile(
        "Inventory, receivables, and payables connect operational design to cash and can shift financing pressure across the network.",
        "Calculate all three day measures using consistent annual flows, compare scenarios, and explain the operating mechanism behind every change.",
        "Lower inventory releases cash but can reduce service or resilience; longer payables improve buyer cash while increasing supplier strain.",
        "average balances, annual revenue, COGS and purchases, day conventions, scenario assumptions, service effect, partner effect, and owner",
    ),
    "section-c-performance-and-financial-insight/10-asset-efficiency-and-inventory-turnover.md": Profile(
        "High turnover can reflect efficient flow or insufficient stock, and low turnover can reflect waste or a deliberate service and resilience policy.",
        "Calculate turnover and days on a consistent cost basis, segment inventory, diagnose the operating cause, and balance asset use with service and risk.",
        "Reducing assets improves turnover and cash but can remove capacity, inventory, or recovery options needed for reliable service.",
        "COGS, average inventory and other operating assets, valuation scope, segment, service and shortage data, cause, and action",
    ),
    "section-c-performance-and-financial-insight/11-sustainability-and-value-chain-measures.md": Profile(
        "Sustainability claims become misleading when boundaries, activity data, factors, allocation, and operational consequences are hidden.",
        "Define the decision and boundary, use the most specific credible activity data and factors, retain methodology, and pair impact with service and cost.",
        "Broader boundaries improve completeness but increase estimation uncertainty and dependence on partner data.",
        "organizational and value-chain boundary, activity data, factor source and version, allocation, uncertainty, owner, target, and action",
    ),
    "section-c-performance-and-financial-insight/12-financial-statements-for-supply-chain.md": Profile(
        "Supply-chain decisions affect profit, cash, and assets differently, so one favorable statement can conceal an adverse effect elsewhere.",
        "Map each operational mechanism to the income statement, balance sheet, and cash flow, separate recurring from one-time effects, and prevent double counting.",
        "Inventory reduction releases cash and assets but may not create equivalent recurring profit; capacity investment can protect service while depressing near-term cash.",
        "baseline statements, operational driver, timing, recurring and one-time classification, accounting assumption, owner, and reconciliation",
    ),
    "section-c-performance-and-financial-insight/13-standard-costing-and-variance-analysis.md": Profile(
        "A variance names a difference but does not identify the operational cause, controllability, or best response.",
        "Calculate price, quantity, rate, and efficiency effects using the approved standard, then trace material differences to process evidence and ownership.",
        "Stable standards support accountability, while outdated standards create large but uninformative variances and poor decisions.",
        "standard version and basis, actual price and quantity, allowed quantity, volume and mix, variance calculation, cause, owner, and corrective action",
    ),
    "section-c-performance-and-financial-insight/14-supplier-financial-health-and-credit-risk.md": Profile(
        "A financially weak supplier or customer can interrupt material, service, investment, collection, and the viability of the network design.",
        "Combine ratios, trends, payment behavior, dependency, qualitative evidence, and scenario exposure, then define proportionate monitoring and mitigation.",
        "Tighter credit or sourcing controls reduce loss exposure but can constrain sales, supply options, or a partner's recovery.",
        "financial statements and period, ratio definitions, trend, payment evidence, dependency, scenario exposure, mitigation, owner, and trigger",
    ),
    "section-c-performance-and-financial-insight/15-strategic-profit-model-and-roa.md": Profile(
        "Supply-chain actions influence return through both operating margin and asset turnover, and counting the same benefit twice overstates value.",
        "Map each initiative to revenue, operating cost, inventory, receivables, and fixed assets, calculate ROA, and reconcile one-time and recurring effects.",
        "Asset reduction improves turnover but may weaken service or resilience; added assets can protect growth while lowering near-term return.",
        "baseline revenue, profit and operating assets, initiative mechanisms, timing, one-time and recurring effects, sensitivity, and finance approval",
    ),
    "section-c-performance-and-financial-insight/16-operational-quality-capacity-and-maintenance.md": Profile(
        "Output, quality, schedule, capacity, and reliability measures interact; improving one can hide rework, waiting, overload, or failure risk.",
        "Use accepted first-pass output, schedule attainment, capacity load, utilization, failure, repair, and availability measures as one diagnostic system.",
        "Higher utilization may improve apparent productivity but reduce maintenance windows, response capacity, and schedule reliability.",
        "units and acceptance status, schedule tolerance, available and run hours, failures, repair time, capacity constraint, loss reason, and action",
    ),
}


M1_FORMULA_TOPICS = {
    "section-d-forecasting/04-seasonality-deseasonalizing-reseasonalizing.md",
    "section-d-forecasting/05-moving-averages-and-exponential-smoothing.md",
    "section-d-forecasting/06-service-sector-and-associative-forecasting.md",
    "section-d-forecasting/07-leading-indicators-regression-correlation.md",
    "section-d-forecasting/08-forecast-error-bias-random-variation.md",
    "section-d-forecasting/09-mad-tracking-signal-standard-deviation.md",
    "section-d-forecasting/10-mse-mape-and-error-measures.md",
}

M2_FORMULA_TOPICS = {
    "section-a-network-design-and-technology-investment/03-network-configuration-and-flow-design.md",
    "section-a-network-design-and-technology-investment/07-technology-business-case-and-tco.md",
    "section-b-connected-supply-networks-and-master-data/06-transportation-management-systems.md",
    "section-c-performance-and-financial-insight/06-perfect-order-and-customer-service.md",
    "section-c-performance-and-financial-insight/08-cost-profit-and-productivity.md",
    "section-c-performance-and-financial-insight/09-cash-to-cash-and-working-capital.md",
    "section-c-performance-and-financial-insight/10-asset-efficiency-and-inventory-turnover.md",
    "section-c-performance-and-financial-insight/13-standard-costing-and-variance-analysis.md",
    "section-c-performance-and-financial-insight/14-supplier-financial-health-and-credit-risk.md",
    "section-c-performance-and-financial-insight/15-strategic-profit-model-and-roa.md",
    "section-c-performance-and-financial-insight/16-operational-quality-capacity-and-maintenance.md",
}


def has_heading(body: str, heading: str) -> bool:
    return bool(re.search(rf"^## {re.escape(heading)}\s*$", body, re.MULTILINE | re.IGNORECASE))


def title(body: str) -> str:
    return body.splitlines()[0].removeprefix("# ").strip()


def add_objectives(body: str, lesson_title: str) -> str:
    if has_heading(body, "Learning objectives"):
        return body
    subject = re.sub(r"^\d+\.\s*", "", lesson_title)
    block = f"""

## Learning objectives

You should be able to:

- explain the operating logic behind {subject.lower()};
- apply the lesson to a realistic planning or supply-chain decision; and
- identify the evidence, trade-off, and trigger needed for responsible use.
"""
    first_break = body.find("\n")
    return body[:first_break] + block + body[first_break:]


def insert_before(body: str, marker_pattern: str, block: str) -> str:
    match = re.search(marker_pattern, body, re.MULTILINE | re.IGNORECASE)
    if not match:
        return body.rstrip() + "\n\n" + block.strip() + "\n"
    return body[: match.start()].rstrip() + "\n\n" + block.strip() + "\n\n" + body[match.start():]


def standard_sections(body: str, profile: Profile) -> str:
    sections: list[str] = []
    if not has_heading(body, "Why it matters"):
        sections.append(f"## Why it matters\n\n{profile.outcome}")
    if not has_heading(body, "Decision logic"):
        sections.append(
            "## Decision logic\n\n"
            + profile.action
            + " Do not approve the decision until mandatory conditions are feasible and the residual exposure has a named owner."
        )
    if not has_heading(body, "Evidence retained through the workflow"):
        sections.append(
            "## Evidence retained through the workflow\n\n"
            f"Retain {profile.evidence}. Record the decision date and the event or threshold that requires reassessment."
        )
    if not has_heading(body, "Trade-offs"):
        sections.append(f"## Trade-offs\n\n{profile.tradeoff}")
    if not has_heading(body, "Commonly confused with"):
        sections.append(
            "## Commonly confused with\n\n"
            "Do not confuse a preferred decision method with a guaranteed outcome. "
            f"{profile.action} Validate the result with {profile.evidence}; the evidence, not the method's label, determines whether the choice worked."
        )
    if sections:
        body = insert_before(body, r"^## Common mistakes?\s*$", "\n\n".join(sections))
    return body


def add_applied_artifact(body: str, profile: Profile, lesson_name: str) -> str:
    if has_heading(body, "Applied decision artifact"):
        return body
    block = f"""## Applied decision artifact

Use a one-page **{lesson_name} decision record** with these fields:

- **Decision and boundary:** {profile.action}
- **Required evidence:** {profile.evidence}.
- **Expected result:** {profile.outcome}
- **Balancing condition:** {profile.tradeoff}
- **Accountability:** name the decision owner, approval date, residual exposure owner, and measurable trigger for reassessment.

The record is complete only when another practitioner can reproduce the reasoning and identify the next action without relying on meeting memory."""
    return insert_before(body, r"^## Trade-offs\s*$", block)


def as_wrong_action(text: str) -> str:
    text = re.sub(r"[*_`]", "", text).strip().rstrip(".")
    substitutions = (
        (r"^Avoid treating\b", "Treat"),
        (r"^Avoid using\b", "Use"),
        (r"^Avoid assuming\b", "Assume"),
        (r"^Do not treat\b", "Treat"),
        (r"^Do not use\b", "Use"),
        (r"^Do not assume\b", "Assume"),
        (r"^Do not forecast\b", "Forecast"),
        (r"^A common mistake is to\b", ""),
    )
    for pattern, replacement in substitutions:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
    return text.strip()[0].upper() + text.strip()[1:]


def lower_initial(text: str) -> str:
    """Lower a sentence opening without corrupting acronyms such as MSE or S&OP."""
    first_word = re.match(r"[^\s,;:]+", text)
    if not first_word or first_word.group(0).isupper():
        return text
    return text[0].lower() + text[1:]


def title_phrase(text: str) -> str:
    """Turn a heading into a sentence phrase while preserving multi-letter acronyms."""
    words: list[str] = []
    for word in text.split():
        letters = "".join(character for character in word if character.isalpha())
        words.append(word if len(letters) > 1 and letters.isupper() else word.lower())
    return " ".join(words)


def common_mistakes(body: str, profile: Profile | None = None) -> list[str]:
    match = re.search(
        r"^## Common mistakes?\s*\n(?P<section>.*?)(?=^## |\Z)",
        body,
        re.MULTILINE | re.IGNORECASE | re.DOTALL,
    )
    mistakes: list[str] = []
    if match:
        for line in match.group("section").splitlines():
            if line.strip().startswith("- "):
                item = as_wrong_action(line.strip()[2:])
                if item:
                    mistakes.append(item)
        if not mistakes:
            plain = re.sub(r"\[[^]]+\]\([^)]+\)", "", match.group("section"))
            plain = re.sub(r"[*_`]", "", plain)
            sentences = re.split(r"(?<=[.!?])\s+", " ".join(plain.split()))
            if sentences and len(sentences[0]) > 20:
                mistakes.append(as_wrong_action(sentences[0]))
    if profile:
        downside_parts = re.split(r";|, while\s+|\bbut\b", profile.tradeoff, flags=re.IGNORECASE)
        downside = downside_parts[-1].strip().rstrip(".")
        fallbacks = [
            f"Treat the expected benefit as decisive without testing whether {downside[0].lower() + downside[1:]}",
            f"Approve the choice without retaining {profile.evidence}",
            "Treat the current result as permanent and omit the stated reassessment trigger",
        ]
    else:
        fallbacks = [
            "Choose the most familiar practice without validating the required evidence",
            "Optimize one local measure while ignoring the end-to-end consequence",
            "Treat the first result as permanent and omit a reassessment trigger",
        ]
    for fallback in fallbacks:
        if len(mistakes) >= 3:
            break
        mistakes.append(fallback)
    return mistakes[:3]


def add_missing_m1_mistakes(body: str, relative: str) -> str:
    if has_heading(body, "Common mistakes"):
        return body
    items = M1_MISSING_MISTAKES.get(relative)
    if not items:
        raise ValueError(f"No reviewed common-mistake profile for {relative}")
    block = "## Common mistakes\n\n" + "\n".join(f"- {item}." for item in items)
    return insert_before(body, r"^## Original knowledge check\s*$", block)


def add_m1_check_and_practice(body: str, profile: Profile) -> str:
    additions: list[str] = []
    lesson_title = re.sub(r"^\d+\.\s*", "", title(body))
    lesson_reference = title_phrase(lesson_title)
    distractors = (
        f"Use {lesson_reference} as a label for the preferred option before defining the decision outcome, constraints, or owner.",
        f"Choose the apparent upside without evaluating this balancing condition: {profile.tradeoff}",
        f"Approve the choice without retaining {profile.evidence}; omit the reassessment trigger as well.",
    )
    check = f"""## Original knowledge check

**Question.** NorthStar is deciding how to apply {lesson_reference}. Which proposal is most defensible?

A. {distractors[0]}
B. {profile.action}
C. {distractors[1]}
D. {distractors[2]}

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. {profile.action}**

### Why it is correct

{profile.outcome} The recommended action connects the operating choice to evidence, ownership, and a measurable outcome.

### Why the other answers are wrong

- **A** reverses the decision sequence. The team should first do the required work: {lower_initial(profile.action)}
- **C** optimizes one visible result and omits the balancing effects: {lower_initial(profile.tradeoff)}
- **D** leaves the approval unauditable. A reviewer would be missing {profile.evidence}, as well as the trigger needed to revisit the decision when conditions change.

Those approaches ignore the governing trade-off: {lower_initial(profile.tradeoff)}

</details>"""
    check_pattern = re.compile(
        r"^## Original knowledge check\s*\n.*?(?=^## |\Z)",
        re.MULTILINE | re.IGNORECASE | re.DOTALL,
    )
    if check_pattern.search(body):
        body = check_pattern.sub(check.rstrip() + "\n\n", body, count=1)
    else:
        additions.append(check)
    if not has_heading(body, "Practitioner perspective"):
        additions.append(
            "## Practitioner perspective\n\n"
            f"A review should be able to reconstruct the choice from {profile.evidence}. "
            "If those records cannot explain what changed, who decided, and when the decision will be revisited, the process is not yet controlled."
        )
    if additions:
        body = insert_before(body, r"^## Related concepts\s*$", "\n\n".join(additions))
    return body


def merge_related_sections(body: str) -> str:
    footer = ""
    footer_match = re.search(
        r"\n---\n\n\[(?:Section overview|Previous:).*\]\([^\n]+\)\s*$",
        body,
        re.DOTALL,
    )
    if footer_match:
        footer = footer_match.group(0).strip()
        body = body[: footer_match.start()].rstrip()

    pattern = re.compile(
        r"^## Related concepts\s*\n(?P<section>.*?)(?=^## |\Z)",
        re.MULTILINE | re.IGNORECASE | re.DOTALL,
    )
    sections = [match.group("section").strip() for match in pattern.finditer(body)]
    if len(sections) <= 1:
        return body.rstrip() + (("\n\n" + footer) if footer else "") + "\n"

    body = pattern.sub("", body).rstrip()
    lines: list[str] = []
    seen: set[str] = set()
    for section in sections:
        for line in section.splitlines():
            cleaned = line.rstrip()
            key = cleaned.strip().lower()
            if key and key not in seen:
                lines.append(cleaned)
                seen.add(key)
            elif not key and lines and lines[-1] != "":
                lines.append("")
    while lines and not lines[-1]:
        lines.pop()
    related = "## Related concepts\n\n" + "\n".join(lines)
    result = body + "\n\n" + related
    if footer:
        result += "\n\n" + footer
    return result.rstrip() + "\n"


def reorder_standard_tail(body: str) -> str:
    footer = ""
    footer_match = re.search(
        r"\n---\n\n\[(?:Section overview|Previous:).*\]\([^\n]+\)\s*$",
        body,
        re.DOTALL,
    )
    if footer_match:
        footer = footer_match.group(0).strip()
        body = body[: footer_match.start()].rstrip()

    matches = list(re.finditer(r"^## (?P<heading>.+?)\s*$", body, re.MULTILINE))
    if not matches:
        return body.rstrip() + (("\n\n" + footer) if footer else "") + "\n"
    preamble = body[: matches[0].start()].rstrip()
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        sections.append((match.group("heading").strip().lower(), body[match.start() : end].strip()))

    tail_order = (
        "why it matters",
        "decision logic",
        "evidence retained through the workflow",
        "applied decision artifact",
        "trade-offs",
        "commonly confused with",
        "common mistakes",
        "original knowledge check",
        "practitioner perspective",
        "related concepts",
    )
    tail = {heading: section for heading, section in sections if heading in tail_order}
    core = [section for heading, section in sections if heading not in tail_order]
    ordered = core + [tail[heading] for heading in tail_order if heading in tail]
    result = preamble + "\n\n" + "\n\n".join(ordered)
    if footer:
        result += "\n\n" + footer
    return result.rstrip() + "\n"


def add_formula_reference(body: str, module_number: int, relative: str) -> str:
    required = M1_FORMULA_TOPICS if module_number == 1 else M2_FORMULA_TOPICS
    if relative not in required or "formula-sheet.md" in body:
        return body
    target = (
        "../../calculations/forecasting/formula-sheet.md"
        if module_number == 1
        else "../../calculations/network-performance/formula-sheet.md"
    )
    label = "Forecasting formula sheet" if module_number == 1 else "Network and performance formula sheet"
    heading = re.search(r"^## Related concepts\s*$", body, re.MULTILINE | re.IGNORECASE)
    if not heading:
        raise ValueError(f"Missing related-concepts section in {relative}")
    return body[: heading.end()] + f"\n\n- [{label}]({target})" + body[heading.end() :]


def upgrade_m2_answer(body: str, profile: Profile) -> str:
    mistakes = common_mistakes(body, profile)
    legacy = re.compile(
        r"<details>\s*<summary>Answer</summary>\s*\n(?P<answer>.*?)\n</details>",
        re.DOTALL | re.IGNORECASE,
    )
    structured = re.compile(
        r"<details>\s*<summary>Answer and rationale</summary>\s*\n\s*### Correct answer\s*\n(?P<answer>.*?)\n### Why it is correct.*?</details>",
        re.DOTALL | re.IGNORECASE,
    )
    match = legacy.search(body) or structured.search(body)
    if not match:
        raise ValueError(f"Could not find Module 2 answer in {title(body)}")
    existing = match.group("answer").strip()

    prefix = body[: match.start()]
    options = {
        letter: text.strip()
        for letter, text in re.findall(r"^([A-D])\.\s+(.+)$", prefix, re.MULTILINE)
    }
    answer_letter_match = re.match(r"\*\*([A-D])(?:\.|\b)", existing)
    answer_letter = answer_letter_match.group(1) if answer_letter_match else None
    if options and answer_letter in options:
        wrong_letters = [letter for letter in "ABCD" if letter in options and letter != answer_letter]
        wrong_lines = []
        for index, letter in enumerate(wrong_letters):
            misconception = mistakes[min(index, len(mistakes) - 1)]
            wrong_lines.append(
                f'- **{letter} — {options[letter]}** This reflects the failure mode "{misconception.lower()}" and does not satisfy the required decision evidence.'
            )
        wrong_text = "\n".join(wrong_lines) + f"\n\nThe governing trade-off remains explicit: {profile.tradeoff}"
    else:
        wrong_text = (
            "Alternative responses reproduce failure modes already discussed:\n\n"
            + "\n".join(f"- {item.rstrip('.')}." for item in mistakes)
            + f"\n\nThey do not preserve the lesson's decision boundary or evidence. The governing trade-off remains explicit: {profile.tradeoff}"
        )

    replacement = f"""<details>
<summary>Answer and rationale</summary>

### Correct answer

{existing}

### Why it is correct

{profile.outcome} {profile.action}

### Why the other answers are wrong

{wrong_text}

</details>"""
    return body[: match.start()] + replacement + body[match.end() :]


def add_m2_practice(body: str, profile: Profile) -> str:
    if has_heading(body, "Practitioner perspective"):
        return body
    block = (
        "## Practitioner perspective\n\n"
        f"Use {profile.evidence} as the minimum review record. The artifact should let another practitioner reproduce the conclusion, identify the remaining exposure, and know which trigger reopens the decision."
    )
    return insert_before(body, r"^## Original knowledge check\s*$", block)


def topic_paths(module: Path) -> list[Path]:
    return sorted(
        path
        for path in module.glob("section-*/*.md")
        if re.match(r"\d{2}-", path.name)
        and not re.match(r"\d{2}-section-[a-z]-review\.md$", path.name)
    )


def add_related_links_and_navigation(module: Path, body_by_path: dict[Path, str]) -> dict[Path, str]:
    groups: dict[Path, list[Path]] = {}
    for path in body_by_path:
        groups.setdefault(path.parent, []).append(path)

    for directory, paths in groups.items():
        paths.sort()
        review = next(directory.glob("*-section-*-review.md"))
        for index, path in enumerate(paths):
            body = body_by_path[path]
            previous = paths[index - 1] if index else directory / "README.md"
            following = paths[index + 1] if index + 1 < len(paths) else review
            previous_label = "Section overview" if index == 0 else f"Previous: {re.sub(r'^\d+\.\s*', '', title(body_by_path[previous]))}"
            following_label = "Section review" if following == review else f"Next: {re.sub(r'^\d+\.\s*', '', title(body_by_path[following]))}"

            if module == M1:
                section = directory.name.split("-")[1]
                cross_targets = {
                    "a": M2 / "section-a-network-design-and-technology-investment/01-strategy-to-network-design.md",
                    "b": M2 / "section-a-network-design-and-technology-investment/02-market-segmentation-and-service-choices.md",
                    "c": M2 / "section-b-connected-supply-networks-and-master-data/03-advanced-planning-and-constraint-management.md",
                    "d": M2 / "section-c-performance-and-financial-insight/01-measurement-system-design.md",
                    "e": M2 / "section-a-network-design-and-technology-investment/03-network-configuration-and-flow-design.md",
                }
                cross = cross_targets[section]
                cross_label = "Module 2 continuation"
            else:
                section = directory.name.split("-")[1]
                cross_targets = {
                    "a": ROOT / "03-sourcing-strategy-product-design-supplier-execution/section-a-sourcing-alignment-and-total-cost/01-strategic-sourcing-from-demand.md",
                    "b": ROOT / "03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/01-purchasing-flow-and-selection-routes.md",
                    "c": ROOT / "03-sourcing-strategy-product-design-supplier-execution/section-d-supplier-selection-contracting-and-procurement/02-supplier-criteria-and-scorecards.md",
                }
                cross = cross_targets[section]
                cross_label = "Module 3 continuation"

            rel = lambda target: Path(re.sub(r"\\", "/", str(target.relative_to(path.parent))) if target.is_relative_to(path.parent) else "")
            # pathlib cannot calculate a relative path across siblings without os.path.
            import os

            related = (
                f"\n- [Section overview](./README.md)"
                f"\n- [{cross_label}]({Path(os.path.relpath(cross, path.parent)).as_posix()})"
            )
            related_match = re.search(r"^## Related concepts\s*$", body, re.MULTILINE | re.IGNORECASE)
            if not related_match:
                body = body.rstrip() + "\n\n## Related concepts\n" + related + "\n"
            else:
                insert_at = related_match.end()
                after = body[insert_at:]
                if cross_label not in after.split("\n## ", 1)[0]:
                    body = body[:insert_at] + "\n" + related + body[insert_at:]

            footer = (
                f"[{previous_label}]({Path(os.path.relpath(previous, path.parent)).as_posix()})"
                f" · [{following_label}]({Path(os.path.relpath(following, path.parent)).as_posix()})"
            )
            if footer not in body:
                body = body.rstrip() + "\n\n---\n\n" + footer + "\n"
            body_by_path[path] = body
    return body_by_path


def harmonize(module: Path, profiles: dict[str, Profile], module_number: int) -> None:
    paths = topic_paths(module)
    expected = {str(path.relative_to(module)) for path in paths}
    if expected != set(profiles):
        missing = sorted(expected - set(profiles))
        extra = sorted(set(profiles) - expected)
        raise ValueError(f"Profile mismatch for Module {module_number}: missing={missing}, extra={extra}")

    bodies: dict[Path, str] = {}
    for path in paths:
        profile = profiles[str(path.relative_to(module))]
        body = path.read_text(encoding="utf-8")
        body = re.sub(r"^## Common mistake\s*$", "## Common mistakes", body, flags=re.MULTILINE | re.IGNORECASE)
        body = re.sub(r"^## Common confusion\s*$", "## Commonly confused with", body, flags=re.MULTILINE | re.IGNORECASE)
        body = add_objectives(body, title(body))
        body = standard_sections(body, profile)
        body = add_applied_artifact(
            body,
            profile,
            title_phrase(re.sub(r"^\d+\.\s*", "", title(body))),
        )
        if module_number == 1:
            body = add_missing_m1_mistakes(body, str(path.relative_to(module)))
            body = add_m1_check_and_practice(body, profile)
        else:
            body = add_m2_practice(body, profile)
            body = upgrade_m2_answer(body, profile)
        bodies[path] = body

    bodies = add_related_links_and_navigation(module, bodies)
    for path, body in bodies.items():
        relative = str(path.relative_to(module))
        body = add_formula_reference(body, module_number, relative)
        body = merge_related_sections(body)
        path.write_text(reorder_standard_tail(body), encoding="utf-8")


def main() -> None:
    harmonize(M1, M1_PROFILES, 1)
    harmonize(M2, M2_PROFILES, 2)
    print(f"Harmonized {len(M1_PROFILES)} Module 1 and {len(M2_PROFILES)} Module 2 topics.")


if __name__ == "__main__":
    main()
