# Worked Solution — ClearSpan Customer-Supplier Relationship Stabilization

This solution uses the locked Module 6 datasets and the [Relationship Performance Formula & Control Sheet](../../calculations/relationship-performance/formula-sheet.md). All values are fictional training data. Capstone-specific thresholds are labeled as such and are not presented as universal standards.

## Executive recommendation

ClearSpan should stabilize both sides of the relationship system rather than treating CRM and SRM as separate software or sourcing projects.

The recommended base path is to:

1. **Protect Strategic OEM relationships and urgently stabilize Service Networks**, while keeping differentiated contact models by segment.
2. **Launch a formal service/VOC recovery loop** because selected-interaction response attainment and corrective-action closure are materially below the capstone targets.
3. **Select Cloud CRM Accelerate for the base case**, but govern adoption as a decision-critical assumption because a 70% adoption sensitivity changes the recommendation.
4. **Contain BlueMesa Electronics rather than deepen the relationship**: it is sole source, critically concentrated, below the urgent-remediation performance threshold, and NOT CERTIFIED.
5. **Advance NorthRiver Joint Innovation as the first feasible alliance**, while maintaining explicit concentration and performance controls.
6. **Close communication/action gaps** in customer recovery, service-network escalation, supplier remediation/certification, alliance steering, digital incidents, and executive portfolio review.

The relationship program should be governed as one closed loop: customer evidence shapes service and demand priorities; supplier evidence shapes supply reliability and collaboration; communication and corrective-action evidence show whether the relationship system is actually learning.

## 1. Customer relationship portfolio

### Segment gross-profit concentration

From `customer-segments.csv`:

| Segment | Annual gross profit | Share of modeled gross profit | Primary service model |
|---|---:|---:|---|
| Strategic OEM | $6,426,000 | **34.43%** | Named account team + engineering coordination |
| Growth Distributors | $4,536,000 | **24.30%** | Portal + channel manager |
| Service Networks | $3,225,600 | **17.28%** | Fast-response service desk |
| Digital SMB | $2,883,000 | **15.45%** | Digital self-service + pooled support |
| Projects / New Logos | $1,595,000 | **8.55%** | Solution selling + onboarding |
| **Total** | **$18,665,600** | **100%** | — |

The largest two segments represent:

`($6,426,000 + $4,536,000) / $18,665,600 = 58.73%`

The largest three represent:

`($6,426,000 + $4,536,000 + $3,225,600) / $18,665,600 = 76.01%`

This concentration supports differentiated relationship effort, but the decision should not use gross profit alone. Service failure and relationship state also matter.

### Selected-account lifecycle sample

The lifecycle dataset contains **16 accounts active at period start**. Five became inactive and eleven remained active.

Selected-sample churn:

`5 / 16 = 31.25%`

Selected-sample retention:

`11 / 16 = 68.75%`

The current revenue of accounts labeled vulnerable is:

`$910,000 + $480,000 + $126,000 + $351,000 + $510,000 = $2,377,000`

Prior-period revenue represented by the five churned accounts is:

`$1,120,000 + $455,000 + $142,000 + $360,000 + $590,000 = $2,667,000`

These figures are useful diagnostic exposure measures. They are **not** a statistically valid enterprise churn estimate because the file is a selected training sample.

### Contact treatment

`customer-channel-preferences.csv` supports different primary treatments:

- **Strategic OEM:** field representative is the largest preference at **55%**. Keep named-account/engineering contact as the primary relationship path, supported by digital evidence rather than replaced by self-service.
- **Service Networks:** phone/chat leads at **40%**. Fast-response assisted service should remain central, with portal visibility as a support channel.
- **Digital SMB:** portal leads at **70%**. Self-service should be the default, with escalation to assisted support for exceptions.

### Priority decision

**Protect Strategic OEM.** It contributes 34.43% of modeled gross profit and includes both a vulnerable account (Vertex Controls) and a churned account (Helix Robotics). Its service metrics are not the weakest, so the relationship response should focus on protecting high-value accounts and learning from churn rather than redesigning every service process.

**Urgently stabilize Service Networks.** It contributes 17.28% of modeled gross profit but has the weakest OTIF and response performance in the service file. RapidFix Network is vulnerable and PrimeCare Service churned. This is the strongest combined signal of operating service failure and relationship deterioration.

**Give Projects / New Logos a targeted recovery/onboarding program.** Its aggregate gross profit is lower, but the service data shows the highest complaint rate and weak OTIF, while the selected account sample includes one vulnerable and one churned project account. Poor project governance at this stage can prevent future lifetime value from developing.

Growth Distributors also require portal/service improvement, while Digital SMB should retain a lower-cost digital model unless incident evidence shows escalation is needed.

## 2. Customer service, VOC, and recovery controls

### Service-performance diagnosis

From `customer-service-performance.csv`:

| Segment | OTIF | Response-time attainment | Complaint rate / 100 orders | Stockout frequency |
|---|---:|---:|---:|---:|
| Strategic OEM | 93.82% | 89.61% | 4.71 | 3.31% |
| Growth Distributors | 89.58% | 83.98% | 6.17 | 6.17% |
| **Service Networks** | **86.23%** | **76.97%** | **7.66** | **8.62%** |
| Digital SMB | 92.27% | 89.19% | 4.53 | 5.82% |
| Projects / New Logos | 86.25% | 83.90% | **8.75** | 7.32% |

The strongest service-recovery priority is **Service Networks** because it is worst on OTIF, response-time attainment, and stockout frequency. Projects / New Logos is almost equally weak on OTIF and has the highest complaint rate.

### Selected VOC interaction controls

There are 22 interactions requiring a response and 12 met the stated target:

`12 / 22 = 54.55% response-time attainment`

There are 13 corrective actions due and 6 closed:

`6 / 13 = 46.15% corrective-action closure`

These figures explain why relationship recovery cannot be judged from customer-service metrics alone. The operating system is also slow to respond and close actions in the selected interactions.

At segment level, the selected VOC file shows particularly weak corrective-action closure for Service Networks: the two due corrective actions associated with the relevant complaint/service-failure records remain open, producing **0% closure in that selected subset**. Growth Distributors and Projects / New Logos each close only one of three due actions in their selected records.

### Customer-facing communication control

Using the capstone's fictional targets of 100% delivery, at least 90% feedback, and at least 90% action closure:

| Communication | Delivery | Feedback | Action closure | Result |
|---|---:|---:|---:|---|
| COM-01 Customer recovery — Strategic OEM | 100% | 87.50% | 83.33% | **Miss** |
| COM-03 Service-network escalation | 87.50% | 85.71% | 71.43% | **Miss** |
| COM-10 Customer VOC loop | 100% | 100% | 100% | Pass |
| COM-11 Digital SMB incident bulletin | 100% | 80.00% | 66.67% | **Miss** |

COM-03 should be escalated first because its weak communication evidence aligns with the weakest customer-service segment. ClearSpan should not merely send more messages; it should define the owner for each open action, close the loop with the affected service partner, and verify that the recovery changed the customer outcome.

## 3. CRM enablement and decision-changing adoption sensitivity

### Feasibility gates

`crm-technology-cases.csv` applies three hard gates: process fit, data access, and security.

- CRM-01 Unified Enterprise CRM — PASS
- CRM-02 Cloud CRM Accelerate — PASS
- CRM-03 Best-of-Breed Sales Stack — **FAIL data-access gate**
- CRM-04 Low-Cost Point CRM — **FAIL process-fit gate**

Only CRM-01 and CRM-02 are ranked economically.

### Base economics

**Cloud CRM Accelerate (CRM-02)**

Three-year TCO:

`$210,000 + $140,000 + $65,000 + 3 × $240,000 = $1,135,000`

Three-year realized benefit at 90% expected adoption:

`3 × ($290,000 + $220,000) × 0.90 = $1,377,000`

Three-year net benefit:

`$1,377,000 − $1,135,000 = +$242,000`

**Unified Enterprise CRM (CRM-01)** has a locked three-year TCO of **$1,310,000**, realized benefit of **$1,353,000**, and net benefit of **+$43,000**.

The base recommendation is therefore **Cloud CRM Accelerate**, because both feasible options pass the hard gates and CRM-02 has the larger modeled net benefit.

### 70% adoption sensitivity

Hold every CRM-02 input constant except adoption = 70%.

Realized benefit:

`3 × ($290,000 + $220,000) × 0.70 = $1,071,000`

Net benefit:

`$1,071,000 − $1,135,000 = −$64,000`

At 70% adoption, the base recommendation changes: CRM-02 becomes negative while CRM-01 remains at **+$43,000** under its locked base assumptions.

Approximate CRM-02 break-even adoption is:

`$1,135,000 / [3 × ($290,000 + $220,000)] = 74.18%`

**Decision implication:** adoption is not a soft implementation metric. ClearSpan should treat approximately **74.2% sustained adoption** as an economic break-even trigger for this fictional case. A forecast or realized trend below that level should force adoption remediation and a business-case review rather than automatic continuation.

## 4. Supplier concentration and relationship depth

### Strategic-supplier spend concentration

Suppliers classified as Strategic in `supplier-segmentation.csv` are:

- NorthRiver Sensors — $4,200,000
- BlueMesa Electronics — $3,800,000
- Summit Industrial Software — $1,600,000

Strategic-supplier spend:

`$4,200,000 + $3,800,000 + $1,600,000 = $9,600,000`

Total modeled supplier spend:

`$18,870,000`

Strategic share:

`$9,600,000 / $18,870,000 = 50.87%`

A large share of modeled spend therefore sits in relationships that need active governance rather than transactional purchasing treatment.

### Concentration exposures

| Supplier | Strategy | Supplier share | Qualified alternates | Switch lead time | Buffer | Concentration risk |
|---|---|---:|---:|---:|---:|---|
| **BlueMesa Electronics** | **Sole** | **100%** | **0** | **180 days** | 60 days | **Critical** |
| NorthRiver Sensors | Single | 80.77% | 1 | 120 days | 45 days | High |
| Redwood Machining | Single | 75.00% | 2 | 90 days | 35 days | High |
| Summit Industrial Software | Single | 84.21% | 1 | 150 days | 60 days | High |

**BlueMesa is the most urgent continuity exposure.** Sole source means an alternate is not currently available, and the 180-day switch lead time is much longer than the 60-day continuity buffer. ClearSpan cannot solve this by simply issuing a new sourcing policy; it needs containment, supplier remediation, design/qualification work, and a credible continuity path.

**NorthRiver and Summit justify deep governance**, but not because concentration is inherently bad. Both are strategic, innovation-intensive relationships with limited alternates. Their governance should combine collaboration with explicit continuity review.

**Redwood requires concentration reduction/alternate-readiness attention** while maintaining collaborative treatment because its customization is high and replacement is not immediate.

**Prairie Packaging remains appropriate for transactional treatment** in the modeled portfolio: lower criticality/risk, six qualified alternates, a 21-day switch lead time, and low concentration risk.

## 5. Supplier performance, certification, and alliance selection

### Urgent supplier remediation

Under the capstone's fictional below-80 urgent-remediation trigger, only **BlueMesa Electronics** is below threshold at **72.19/100**.

Its locked performance evidence is:

- on-time delivery = `361 / 430 = 83.95%`
- defect rate = `396 / 22,000 = 1.80%`
- corrective-action closure = `8 / 15 = 53.33%`
- weighted supplier performance score = **72.19/100**

These are not isolated weaknesses. BlueMesa is also the sole source with critical concentration risk.

### Certification gate

BlueMesa's certification evidence shows:

- audit score = 78%
- critical nonconformances = 1
- major nonconformances = 3
- quality-system gate = PASS
- safety gate = PASS
- delivery gate = **FAIL**
- open corrective actions = 4
- status = **NOT CERTIFIED**

The formula/control sheet treats a critical nonconformance or failed delivery/safety/quality gate as a hard-fail condition. ClearSpan therefore should **not expand BlueMesa's strategic commitment** until the evidence is remediated and requalification supports a different status.

Because the source is sole, the near-term decision is not “terminate immediately.” The appropriate response is to contain the dependency, protect customer supply, close critical corrective actions, improve delivery performance, accelerate alternate/design qualification where feasible, and re-evaluate after the three-month requalification interval in the fictional data.

### Alliance ranking

The hard gates are applied before the numerical score:

| Candidate | Score | Gate result | Feasible rank |
|---|---:|---|---:|
| **NorthRiver Joint Innovation** | **88** | PASS | **1** |
| Summit Connected Services Alliance | 87 | PASS | 2 |
| Apex Regional Capacity Alliance | 81 | PASS | 3 |
| BlueMesa Co-Development | **89** | **FAIL — IP/security** | Not ranked |
| LowCost Consortium | 66 | **FAIL — strategy fit** | Not ranked |

BlueMesa Co-Development is the clearest gate-discipline test: **89/100 does not beat 88/100** because it is not feasible under the current hard-gate evidence.

The recommended first alliance is **NorthRiver Joint Innovation**. The supplier is also CERTIFIED and has a weighted supplier-performance score of 90.09. However, NorthRiver remains a high-concentration single-source relationship (80.77% share, one qualified alternate, 120-day switch lead time). Alliance governance must therefore preserve continuity planning rather than confusing collaboration with risk elimination.

A practical alliance condition is to include delivery, corrective-action closure, capacity/continuity evidence, innovation outcomes, and alternate-readiness review in the monthly governance cadence.

## 6. Communication and action-control model

Using the capstone targets of 100% message delivery, at least 90% feedback, and at least 90% action closure, the following programs miss at least one threshold:

| Program | Delivery | Feedback | Closure | Primary issue |
|---|---:|---:|---:|---|
| COM-01 Customer recovery — Strategic OEM | 100% | 87.50% | 83.33% | feedback + closure |
| COM-03 Service-network escalation | 87.50% | 85.71% | 71.43% | all three |
| COM-06 BlueMesa remediation | 100% | 87.50% | 58.33% | feedback + closure |
| COM-07 Apex alliance steering | 100% | 100% | 80.00% | closure |
| COM-08 Supplier certification | 100% | 100% | 66.67% | closure |
| COM-11 Digital SMB incident bulletin | 100% | 80.00% | 66.67% | feedback + closure |
| COM-12 Executive relationship portfolio | 100% | 100% | 87.50% | closure |

This list shows why communication success cannot be measured only by whether a message was sent. Several programs deliver every planned message but still leave actions open.

## Implementation roadmap

### 30/60/90-day roadmap

| Horizon | Accountable owner | Action | Measure / gate | Trigger and response |
|---|---|---|---|---|
| 0–30 days | VP Commercial | Launch Strategic OEM and Service Network recovery cells around vulnerable/churn evidence | SEG-C OTIF and response baseline; COM-01/03 actions assigned | Escalate any critical customer action without owner/due date |
| 0–30 days | VP Supply Chain | Place BlueMesa under formal remediation/continuity control | Performance 72.19; certification NOT CERTIFIED; 100% sole share | No expanded volume/alliance commitment while hard gate remains open |
| 0–30 days | CIO + CRM Product Owner | Confirm CRM-02 feasibility and instrument adoption measurement | Process/data/security PASS; adoption baseline captured | Reopen business case if forecast/actual adoption trends toward <74.2% |
| 0–30 days | Relationship PMO Lead | Close ownership gaps in all seven communication programs missing targets | Delivery 100%; feedback ≥90%; closure ≥90% capstone targets | Escalate overdue actions at executive monthly review |
| 31–60 days | Service Operations Lead | Redesign Service Network response path around phone/chat preference and stockout/service evidence | Improve response attainment and action closure from baseline | Add capacity/process countermeasure if metrics do not improve |
| 31–60 days | Supplier Quality Manager | Close BlueMesa critical/major findings and certification evidence | Critical NC = 0; delivery gate restored; open actions reduced | Continue containment if requalification evidence remains insufficient |
| 31–60 days | Alliance Manager | Charter NorthRiver alliance with continuity and performance controls | All alliance hard gates PASS; monthly pulse check defined | Pause expansion if a hard gate or critical supplier control deteriorates |
| 31–60 days | Customer Insights Lead | Convert VOC themes into owned service/product actions | Response and corrective closure trend upward | Escalate recurring themes without closure evidence |
| 61–90 days | CIO + Finance | Reconcile CRM adoption and realized-benefit assumptions | Adoption ≥74.2% break-even and benefits traceable | Rework adoption plan or revisit CRM-01 if economics no longer hold |
| 61–90 days | VP Supply Chain + Procurement | Review alternate qualification for BlueMesa/NorthRiver/Redwood/Summit | Switch-time and alternate-readiness evidence improved | Fund qualification/design change if exposure remains above tolerance |
| 61–90 days | COO | Review integrated customer-supplier relationship portfolio | Customer recovery, supplier remediation, alliance, communication actions | Reallocate governance effort where value/risk evidence changes |

The roadmap uses the same management principle on both sides of the supply chain: relationship intensity is earned by value and dependency, while trust is maintained by evidence and closed actions.

## Sensitivity and failure cases

### CRM adoption sensitivity

The base CRM-02 recommendation changes when adoption falls from 90% to 70%:

- base realized benefit = **$1,377,000**
- base net benefit = **+$242,000**
- 70% realized benefit = **$1,071,000**
- 70% net benefit = **−$64,000**
- approximate break-even adoption = **74.18%**

This is decision-changing because CRM-01 remains at **+$43,000** under its locked base assumptions. The implementation plan must therefore treat adoption as an economic control, not merely a training KPI.

### Other failure triggers

Reopen the relationship design if any of the following occurs:

- Service Network OTIF/response performance fails to improve while VOC actions remain open;
- a high-value customer moves from vulnerable to churned or a new material churn pattern appears in a broader population dataset;
- CRM process, data-access, or security feasibility changes;
- CRM-02 adoption falls below the modeled break-even region without a credible recovery plan;
- BlueMesa retains a hard certification failure, its continuity buffer becomes inadequate, or customer supply is threatened;
- NorthRiver or another strategic supplier loses certification or a critical alliance gate;
- a feasible alliance fails strategy, ethics, financial, IP/security, or capacity/continuity review;
- communication delivery/feedback/action closure remains below the capstone targets for a critical relationship program; or
- the business changes the weighting, threshold, or time horizon used in a repository-defined training control without recalculating dependent results.

## Completed executive decision record

| Decision | Mandatory gate | Evidence | Strongest rejected alternative / unresolved exposure | Trigger |
|---|---|---|---|---|
| Protect Strategic OEM; urgently stabilize Service Networks | Use economic + lifecycle + service/VOC evidence; no unsupported composite | SEG-A = 34.43% GP; SEG-C OTIF 86.23%, response 76.97% | Projects/New Logos also weak and needs targeted onboarding/recovery | Service/VOC trend worsens or vulnerable account moves to churn |
| Cloud CRM Accelerate base case | Process, data, security PASS | $1.135M TCO; $1.377M realized benefit; +$242k net at 90% adoption | CRM-01 gives +$43k; becomes preferable in 70% CRM-02 sensitivity | Adoption trends below ~74.2% or a feasibility gate fails |
| Contain/remediate BlueMesa; do not expand strategic commitment | Certification hard gate; continuity control | 72.19 score; 83.95% OTD; 53.33% closure; NOT CERTIFIED; 100% sole-source share | Immediate exit is constrained by zero alternates and 180-day switch | Certification/performance improves or continuity exposure changes |
| Advance NorthRiver Joint Innovation first | All five alliance gates PASS | Alliance score 88/rank 1; supplier score 90.09; Certified | BlueMesa alliance scores 89 but fails IP/security | Any hard gate, certification, or critical performance control fails |
| Tighten relationship communication closure | 100% delivery; ≥90% feedback; ≥90% closure capstone targets | Seven programs miss at least one target | Message delivery alone can look healthy while actions remain open | Critical action overdue or monthly portfolio target remains missed |

## Evaluation rubric

A strong response should demonstrate all of the following:

- **Customer judgment:** segment economics, lifecycle state, service metrics, VOC, and channel preference are interpreted together.
- **Sample discipline:** the selected lifecycle churn/retention result is not generalized to the enterprise.
- **Gate discipline:** failed CRM, alliance, or certification gates are never averaged away by economics or weighted scores.
- **Supplier judgment:** concentration risk is evaluated together with alternate availability, switch lead time, performance, certification, and customer impact.
- **Reproducibility:** the gross-profit shares, 31.25%/68.75% lifecycle rates, VOC controls, CRM economics/sensitivity, supplier metrics, and alliance ranking reproduce from the linked data.
- **Communication discipline:** message delivery, feedback, and action closure are treated as separate controls.
- **Implementation quality:** every major recommendation has an owner, measure, trigger, review cadence, and response when evidence deteriorates.

[Return to the capstone assignment](./README.md) · [Return to Module 6](../README.md)
