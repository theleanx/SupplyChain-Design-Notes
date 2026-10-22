# 2. AI, Machine Learning, Expert Systems, and Data Analytics

## Learning objectives

Differentiate the relevant technologies, select business-fit evidence and define a feasible operating decision with accountable ownership.

## Concept in plain English

The CSCP learning source introduces artificial intelligence, machine learning, expert systems, heuristics and analytics as different mechanisms that can improve planning, exception response and pattern recognition. **Analytics** transforms data into information and decisions. **Machine learning** identifies relationships from data, whereas an **expert system** can use explicit domain rules. Mathematical optimization does not require an AI model, and a generative text system is not equivalent to a validated warehouse controller.

Predictive applications can flag abnormal machine condition, order-fraud patterns or at-risk shipments. A recommendation must still be judged against safety, commercial restrictions and decision rights. A model trained on historic normal operations may degrade when a new product launches or a supplier fails. Input lineage, labels, handling of missing data, testing on unseen periods, drift monitoring and fallback are essential, particularly when rare failures create severe losses.

Different metrics answer different questions. Accuracy can look strong in a data set where most assets never fail; recall indicates the fraction of actual failures detected, while precision tells operators how many issued alerts were true. The business needs the economic consequence of missed events and unnecessary investigation, not simply a high model score. Production use should retain overrides, version records and qualified escalation.

AI and analytics do not replace accountability. Data teams own technical performance, maintenance owns safe action, and management authorizes the scope of automation. A model's predictions are not physical facts. AlderGate must observe the actual change in machine downtime, emergency repairs and personnel workload compared with a credible baseline. Current AI governance frameworks can supplement the conceptual curriculum, but their version-specific requirements should be verified separately.

**Source alignment:** CSCP Module 8 pp. 225–227; slides 51–52. Course terms determine the scope; all AlderGate cases, decision graphics and calculations are independent examples.

## Why it matters

Rare press failures drive service loss even when a model appears accurate on mostly healthy machines. AlderGate should measure failure recall, precision and consequences of missed events before assigning technicians to an automated recommendation.

## Decision model and workflow

![Original AI, Machine Learning, Expert Systems, and Data Analytics graphic](../../assets/diagrams/module-8/section-c/ai-machine-learning-and-data-analytics.svg)

### Evidence retained through the workflow

| Topic-specific evidence | Required check |
| --- | --- |
| Training evidence | Source, system boundary, accountable reviewer and disposition |
| False alerts | Source, system boundary, accountable reviewer and disposition |
| Missed failures | Source, system boundary, accountable reviewer and disposition |
| Authorized intervention | Source, system boundary, accountable reviewer and disposition |

## Practical process flow

```mermaid
flowchart TD
    A[Define safety relevant failure cases] --> B[Audit labels and training periods]
    B --> C{Mandatory gates passed?}
    C -- No --> D[Compare recall precision and misses]
    D --> B
    C -- Yes --> E[Approve technician decision boundary]
    E --> F[Monitor model drift]
```

## Realistic example — AlderGate Motion Products

AlderGate evaluates condition alerts for repair presses. Maintenance reviews each proposed intervention, including whether a machine can safely continue, while the analytics team monitors false positives, missed failures and changes in input signals.

## Applied decision artifact or worked calculation

[Download the original fictional dataset](../../assets/data/module-8/section-c/ai-failure-detection.csv)

The training pilot detects **18 of 20** actual machine failures (**90% recall**). It issues 48 alerts, of which 18 are true (**37.5% precision**). Classification accuracy is (18 + 150)/200 = **84%**. These three ratios express different realities and cannot establish downtime savings without comparing actions, safety and costs.

## Decision logic

- Test on held out operating periods and product variants.
- Count false alerts and undetected failures separately.
- Require qualified human confirmation of safety actions.
- Retest after drift or changed equipment state.

## Trade-offs

| Design question | Consideration |
| --- | --- |
| Fast deployment versus assurance | Integration and qualification may set a hard pace limit |
| Automatic decisions versus accountable review | A fast false conclusion can be more costly than a slow verified decision |
| New capabilities versus ongoing ownership | Future maintenance, vendor dependency and data governance must be funded |

## Commonly confused with

A rules-based expert system is not identical to a model trained from examples. Classification accuracy is not the same as failure recall; a predictive maintenance alert is a hypothesis, not a confirmed breakdown. Optimization can exist without machine learning.

## Common mistakes

- Evaluating a rare-event model only by overall accuracy.
- Automating machine shutdown without validated operational authority.
- Ignoring changed operating regimes and model drift.

## Original knowledge check

**Question.** Which metric directly measures the proportion of actual failures detected by the pilot?

A. Annual AI software spending

B. Failure recall, with missed-event consequences

C. Number of dashboard screenshots

D. Total supplier count

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Failure recall, with missed-event consequences**

### Why it is correct

Recall divides detected failures by all actual failures; the two missed failures still require a severity review.

### Why the other answers are wrong

- **A.** Software spending is not model detection.
- **C.** Dashboard count cannot measure model detection.
- **D.** Supplier count is not failure recall.

</details>

## Practitioner perspective

Data owners should version input signals, labels and models; maintenance owners should record the disposition of each significant alert. Monitoring needs action outcomes, not only algorithm scores.

## Related concepts

- [Previous learning step](./01-cloud-service-models-and-operating-tradeoffs.md)
- [Module 2 digital supply-chain design](../../02-network-design-digital-connectivity-performance/README.md)
- [Module 7 continuity governance](../../07-supply-chain-risk/README.md)

---

[Section C overview](./README.md) · [Previous learning step](./01-cloud-service-models-and-operating-tradeoffs.md)
