# AsterWorks Capstone Solution Guide

There is no single correct design. A strong answer makes assumptions explicit, connects recommendations to business outcomes, and treats network, technology, data, risk, and measurement as one operating system.

## Recommended direction

A defensible recommendation is a **phased European postponement model**:

- retain core assembly in the existing plant;
- establish a smaller European center for final configuration, regional inventory, and returns;
- segment stable replacement cartridges from configurable treatment skids;
- implement event-based partner connectivity and governed master data before advanced optimization;
- phase specialized planning and transportation capabilities after foundational data reaches an agreed quality threshold.

This design improves response time without duplicating the entire production network.

## Network decision

Use the weighted-score method from Section A. If service, resilience, and launch risk receive meaningful weights, the postponement-center option should outperform both the current-state and full-plant alternatives. A sensitivity test should still be performed because the decision can change if growth, tariffs, or volume assumptions move materially.

## Technology decision

The first release should prioritize:

1. common customer, item, location, and lane identifiers;
2. order, inventory, shipment, and delivery-event integration;
3. exception ownership and workflow;
4. warehouse and carrier execution connectivity; and
5. a limited executive dashboard.

Optimization, predictive alerts, and automated recommendations should follow once transaction completeness, latency, and master-data quality are stable.

## Data controls

| Data object | Primary owner | Critical rule | Control evidence |
|---|---|---|---|
| Item | Product data lead | configuration and handling attributes complete | completeness report |
| Customer | Commercial operations | ship-to, tax, and service segment valid | approval workflow |
| Location | Network operations | time zone, calendar, and capabilities current | quarterly owner attestation |
| Lane | Transportation | mode, lead time, cost, and emissions factor current | carrier review |
| Supplier | Procurement | identity, payment, risk, and capacity fields approved | supplier record audit |

## Monthly executive scorecard

A compact scorecard could include:

- perfect-order rate;
- customer-order cycle time;
- expedite rate;
- forecast-to-capacity variance;
- inventory days and cash-to-cash time;
- total delivered cost per order;
- critical master-data defect rate;
- high-severity exception closure time;
- supplier recovery readiness; and
- shipment emissions intensity.

Every measure needs an owner, target, data definition, drill-down path, and decision threshold.

## Roadmap

| Horizon | Priority |
|---|---|
| First 90 days | validate business case, appoint owners, baseline metrics, cleanse critical data, confirm legal and security requirements |
| Months 4–12 | launch postponement pilot, connect warehouse/carrier events, implement exception workflow, stabilize scorecard |
| Year 2 | scale the network, add scenario planning, improve predictive signals, automate selected low-risk decisions |

## What distinguishes an excellent answer

An excellent answer shows the economic mechanism: better regional response reduces expedites and lost sales, while postponement limits finished-goods proliferation. It also recognizes that technology benefits will not materialize if identifiers, timestamps, ownership, and exception-response processes remain weak.
