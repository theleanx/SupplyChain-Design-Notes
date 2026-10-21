# 1. Cloud Service Models and Operating Trade-offs

## Learning objectives

Differentiate the relevant technologies, select business-fit evidence and define a feasible operating decision with accountable ownership.

## Concept in plain English

Cloud computing makes applications, capacity and data services accessible over networks instead of requiring all infrastructure to be permanently owned and hosted by the supply-chain organization. The CSCP source describes its flexible resource allocation, scaling and shared-service potential. **Software as a service (SaaS)** generally supplies a usable application; **platform as a service (PaaS)** supplies an environment for building and operating applications; **infrastructure as a service (IaaS)** supplies configurable computing and storage. These layers have different customer-versus-provider responsibilities.

AlderGate evaluates a cloud transportation application so qualified suppliers and carriers can view relevant events. Faster vendor onboarding and provider-managed upgrades may be attractive. Yet a monthly subscription is not free integration: identity management, access controls, master-data compatibility, support, monitoring and exit arrangements remain necessary. The source also warns about connectivity dependency, recurring payment, third-party custody of sensitive data and response-time requirements. Local machine-control systems can remain at the edge when their physical response threshold cannot safely depend on the public internet.

An application vendor may advertise automatic upgrades, but AlderGate still needs regression tests for interfaces, authorization and downstream processes. A contract ending or a connectivity outage must have a documented continuity and data-extraction plan. A network service that works in a sales demonstration may fail a heavily loaded warehouse or a partner whose event definitions differ from the original design.

The selection should therefore begin with a customer/service target, permitted data sharing and measurable latency/recovery conditions. Total cost compares equivalent horizons and includes implementation, subscription, staff, integration, cyber controls and change management. Module 2 retains detailed information architecture, while Section C owns emerging-technology selection and adoption.

**Source alignment:** CSCP Module 8 pp. 223–225; presentation slide 51. Course terms determine the scope; all AlderGate cases, decision graphics and calculations are independent examples.

## Why it matters

Cloud services can shorten implementation for supply-chain partners, but an attractive subscription price may hide continuing support and interoperability burdens. A controlled pilot must show that shipment status becomes more useful, secure and timely.

## Decision model and workflow

![Original Cloud Service Models and Operating Trade-offs graphic](../../assets/diagrams/module-8/section-c/cloud-service-models-and-operating-tradeoffs.svg)

### Evidence retained through the workflow

| Topic-specific evidence | Required check |
| --- | --- |
| Cloud service layer | Source, system boundary, accountable reviewer and disposition |
| Data and identity | Source, system boundary, accountable reviewer and disposition |
| Latency and recovery | Source, system boundary, accountable reviewer and disposition |
| Three-year economics | Source, system boundary, accountable reviewer and disposition |

## Practical process flow

```mermaid
flowchart TD
    A[Define use case and customer outcome] --> B[Validate relevant data and physical constraints]
    B --> C{Safety, quality, privacy and recovery gates satisfied?}
    C -- No --> D[Hold and correct the proposed option]
    D --> B
    C -- Yes --> E[Compare full benefit and operating cost]
    E --> F[Approve controlled pilot, owner and monitoring]
```

## Realistic example — AlderGate Motion Products

AlderGate pilots a shared transport-event service with two third-party warehouses. It deliberately leaves safety-critical conveyor controls on site. The service is eligible only after IT tests role separation, record export, incident restoration and maximum delay from status capture to authorized planner response.

## Applied decision artifact or worked calculation

[Download the original fictional dataset](../../assets/data/module-8/section-c/cloud-comparison.csv)

Fictional SaaS recurring annual expense is **$123,000** ($96,000 subscription + $18,000 support + $9,000 connectivity) and one-time setup $36,000. The on-premises alternative is **$101,000 annually** plus $165,000 setup. Three-year **undiscounted** totals are **$405,000 SaaS** and **$468,000 on-premises**. This does not establish NPV or rank options before response-time and privacy gates.

## Decision logic

- Name the customer or plant outcome and its measurement period.
- Determine which observations or qualified input records enable the proposed technology.
- Preserve legal, safety, security and technical feasibility as separate approval gates.
- Compare eligible alternatives over a common horizon including ongoing costs and limits.
- Review actual outcomes against the baseline and retain independent acceptance evidence.

## Trade-offs

| Design question | Consideration |
| --- | --- |
| Fast deployment versus assurance | Integration and qualification may set a hard pace limit |
| Automatic decisions versus accountable review | A fast false conclusion can be more costly than a slow verified decision |
| New capabilities versus ongoing ownership | Future maintenance, vendor dependency and data governance must be funded |

## Commonly confused with

A technical demonstration is not a completed business case. A model prediction, verified physical measurement and permitted business action are different evidence types. No vendor claim replaces the specified operating test.

## Common mistakes

- Selecting technology by name before defining the constrained process.
- Assuming missing evidence implies a successful physical result.
- Ignoring integration, support, recovery or upgrade costs.
- Overriding mandatory qualifications using a weighted savings score.

## Original knowledge check

**Question.** What should AlderGate verify before placing warehouse control events in a cloud application?

A. Only the vendor's brochure and first-month bill

B. Response time, permissions, recovery, data portability and business fit

C. That all plants can eliminate local control logic

D. That every supplier can view all customers' prices

<details>
<summary>Answer and rationale</summary>

### Correct answer

**B. Response time, permissions, recovery, data portability and business fit**

### Why it is correct

Feasibility includes latency, authorized access, continuity and exit evidence before cost ranking.

### Why the other answers are wrong

- **A.** A brochure cannot validate production operation.
- **C.** Physical controls may require local response even with cloud reports.
- **D.** Visibility must respect contractual and privacy access boundaries.

</details>

## Practitioner perspective

Enterprise applications must preserve identity, event timing, permitted actions and error recovery. A solution architect should be able to explain where a pilot can fail safely and who is authorized to restart it.

## Related concepts

- [Previous learning step](../README.md)
- [Module 2 digital supply-chain design](../../02-network-design-digital-connectivity-performance/README.md)
- [Module 7 continuity governance](../../07-supply-chain-risk/README.md)

---

[Section C overview](./README.md) · [Previous learning step](../README.md)
