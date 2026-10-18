# Relationship Performance Formula and Control Sheet

This sheet supports **Module 6 — Supply Chain Relationships**. It distinguishes source-supported relationship/service measures from repository-defined training controls. It does not present invented calculations as ASCM formulas.

## Customer relationship and service measures

| Measure | Controlled calculation | Interpretation / denominator rule |
|---|---|---|
| Unit fill rate / customer service ratio | `units shipped on schedule / units ordered × 100%` | Training implementation of the source-supported customer-service/fill-rate concept. Preserve the same eligibility period for numerator and denominator. |
| On-time delivery | `on-time receipts / eligible receipts × 100%` | Count only receipts subject to the agreed delivery-date rule. |
| OTIF | `orders both complete and on time / eligible orders × 100%` | One order counts only when both conditions are satisfied. |
| Orders shipped complete | `complete orders / eligible orders × 100%` | Completeness is independent of timeliness unless using OTIF. |
| Stockout frequency | `stockout events / item availability checks × 100%` | Repository-controlled implementation of the source-supported stockout-frequency concept; the availability-check event must remain stable. |
| Complaint rate | `complaints / eligible orders × 100` | **Repository-defined training rate** reported as complaints per 100 eligible orders. |
| Churn rate | `accounts active at period start that became inactive / accounts active at period start × 100%` | **Repository-defined training calculation.** New accounts are excluded from the starting denominator. |
| Retention rate | `accounts active at both period start and end / accounts active at period start × 100%` | **Repository-defined training calculation.** `retention + churn = 100%` only when every starting account is classified into one of those two outcomes. |
| Response-time attainment | `responses within target / inquiries requiring response × 100%` | Target time is defined before performance is measured. |
| Corrective-action closure | `actions closed / actions due × 100%` | Use the due set for the same review window. |

## Supplier relationship measures

| Measure | Controlled calculation | Interpretation / denominator rule |
|---|---|---|
| Supplier on-time delivery | `on-time receipts / eligible receipts × 100%` | Supplier-side application of the delivery-performance concept. |
| Supplier defect rate | `defect units / inspected units × 100%` | **Repository-defined training implementation.** Inspection scope must be consistent. |
| Supplier corrective-action closure | `closed actions / actions due × 100%` | Relationship control; it does not replace root-cause analysis. |
| Weighted supplier performance score | `Σ(component score × weight)` | **Repository-defined training score.** Current weights: delivery 25%, quality 20%, corrective closure 15%, internal-customer satisfaction 10%, technology integration 10%, cost reduction 10%, responsiveness/flexibility 10%. |
| Quality component score | `max(0, 100 − 10 × defect_rate_pct)` | **Repository-defined training normalization**, used only for the fictional dataset. |
| Internal-customer / technology / response component | `rating_1_to_5 × 20` | **Repository-defined training normalization.** |
| Cost-reduction component | `min(100, actual_cost_reduction_pct / 3.0% × 100)` | **Repository-defined training normalization** with a fictional 3% target. |

## Alliance feasibility and ranking control

**Hard gate precedes ranking.**

A candidate is feasible only when all five fictional controls are `PASS`:

1. strategy fit;
2. ethics/compliance;
3. financial viability;
4. IP/security;
5. capacity/continuity.

Only feasible candidates receive a rank. The weighted alliance score is a **repository-defined training score**:

`weighted score = Σ(criterion rating 1–5 × criterion weight) / 5`

Current fictional weights:

- value added 20%;
- market access 10%;
- operations strength 15%;
- technology strength 15%;
- strategic growth 15%;
- learning/insight 10%;
- financial strength 15%.

A high numerical score cannot override a failed hard gate.

## Supplier certification status control

The fictional certification dataset uses a transparent training decision rule:

- **NOT CERTIFIED** — any critical nonconformance, failed safety gate, or failed quality-system gate.
- **CERTIFIED** — audit score ≥ 90%, no critical nonconformance, ≤ 1 major nonconformance, required documents complete, delivery gate pass, and zero open corrective actions.
- **CONDITIONAL** — audit score ≥ 80%, no critical nonconformance, ≤ 2 major nonconformances, required documents complete, delivery gate pass, and ≤ 2 open corrective actions.
- **REMEDIATION** — does not meet the above conditions without triggering the hard-fail rule.

Requalification cadence in the fictional data is 12 months for certified, 6 months for conditional, and 3 months for remediation/not-certified status.

## Communication-plan evidence control

Each communication item should retain:

- a defined target audience and purpose;
- one responsible owner;
- one accountable owner;
- consulted/informed parties as appropriate;
- a defined medium and cadence;
- retention and confidentiality treatment where relevant;
- delivery/acknowledgment/feedback evidence;
- open actions and closure status.

The dataset calculates:

- message delivery = `messages sent / planned messages × 100%`;
- acknowledgment = `acknowledgments / messages sent × 100%`;
- feedback rate = `feedback received / feedback expected × 100%`;
- action closure = `actions closed / actions due × 100%`.

These are **repository-defined training controls**, not universal communication-management formulas.

## CRM technology case controls

Module 6 does not reteach Module 2 technology-business-case architecture. The fictional CRM case data uses simple three-year comparison fields only to keep the relationship decision reproducible:

- `three-year TCO = implementation + integration + training + 3 × annual subscription`;
- `three-year realized benefit = 3 × (annual labor savings + annual retention margin uplift) × expected adoption%`;
- `three-year net benefit = realized benefit − TCO`;
- feasibility requires process-fit, data-access, and security gates all to pass.

Use these values as CRM relationship-enablement evidence, not as a replacement for the broader Module 2 technology-investment method.

## Control notes

- Do not average unlike denominators.
- Do not combine a failed hard gate into a weighted average and call the result acceptable.
- Do not infer customer satisfaction solely from operational service metrics; direct customer feedback remains separate evidence.
- Do not use complaint volume alone as a complete customer-satisfaction measure.
- Do not treat supplier certification as a substitute for ongoing supplier-performance measurement.
- Preserve the exact fictional training thresholds if reproducing the capstone; if a threshold changes, recalculate all dependent outputs.
