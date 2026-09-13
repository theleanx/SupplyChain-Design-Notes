# 8. Product Lifecycle Management and New-Product Introduction

## Learning objectives

You should be able to:

- explain PLM in supply-chain terms;
- describe beginning-, middle-, and end-of-life concerns;
- connect PLM to versioning, effectivity, traceability, recalls, and reverse logistics;
- describe a practical NPI sequence;
- explain why supply-chain involvement must begin before launch.

## PLM in plain English

Product lifecycle management (PLM) is the discipline of managing the product and its information **from idea through use, support, and retirement**.

It is broader than an engineering document repository.

PLM can help manage:

- product and component versions;
- bills of material;
- effectivity dates;
- technical documents;
- serial or lot traceability;
- engineering changes;
- upgrades;
- recalls;
- end-of-life support.

## Original visualization — beginning, middle, end

![Product lifecycle management](../../assets/diagrams/module-1/section-c/plm-lifecycle.svg)

### Beginning of life

Focus:

- customer need;
- research and concept;
- product design;
- prototypes;
- suppliers;
- process capability;
- launch readiness.

### Middle of life

Focus:

- scaling production and distribution;
- use and performance;
- engineering changes;
- service feedback;
- configuration control;
- traceability.

### End of life

Focus:

- phase-out;
- final production or last-time buys;
- service and warranty obligations;
- returns;
- recycling or remanufacturing;
- supplier and asset exit decisions.

## Effectivity and traceability

Imagine a medical device with three hardware revisions.

A PLM discipline should answer:

- Which BOM revision was valid on March 1?
- Which serial numbers received the revised component?
- Which customers own those serial numbers?
- Which service instruction applies?
- If a recall occurs, which units are affected?

This is why PLM has direct supply-chain value.

## New-product introduction process

A practical NPI/development-chain sequence can be expressed as:

```mermaid
flowchart LR
    A[Innovation<br/>research and market insight] --> B[Concept<br/>customer and financial promise]
    B --> C[Development<br/>cross-functional design]
    C --> D[Prototype<br/>test feasibility and feedback]
    D --> E[Engineering<br/>structure, BOM, specifications]
    E --> F[Supply<br/>supplier readiness and footprint]
    F --> G[Manufacturing<br/>capability and capacity]
    G --> H[Launch<br/>commercial release]
```

These phases can overlap. Good NPI is cross-functional rather than a baton pass.

## Supply-chain involvement before launch

Late supply-chain involvement causes avoidable problems:

- component cannot be sourced at scale;
- supplier lead time misses market window;
- logistics cost destroys margin;
- design is difficult to manufacture;
- capacity is insufficient;
- packaging creates transport damage;
- spare-parts/service model is ignored.

## Innovative vs. functional product emphasis

An innovative product often prioritizes:

- speed;
- time to market;
- responsiveness;
- flexible capacity.

A functional product with predictable demand and low margins often prioritizes:

- cost;
- scale;
- efficiency;
- repeatability.

## Realistic example — smart industrial pump launch

NorthStar is launching the NS-900 smart pump.

During prototype review, engineering wants a custom communications module. Procurement finds that its supplier lead time is 22 weeks and minimum order quantity is 5,000 units.

The forecast for launch year is only 2,400 units with high uncertainty.

Because sourcing is involved before design freeze, NorthStar can compare:

- custom module;
- standard industrial module;
- redesign for modular interchangeability.

That decision can materially reduce launch risk.

## Practitioner perspective

In an enterprise environment, PLM and ERP often intersect around:

- material master creation;
- BOMs;
- engineering change management;
- document management;
- production versions;
- effectivity;
- serialization/batch traceability.

The business principle remains the same even when system names differ: **the right product definition must be valid at the right time for the right unit or batch**.

## Common confusion

**NPI schedule vs. product life cycle:** NPI manages the development and launch process. The product life cycle continues long after launch.

## Related concepts

- [Product life cycle](07-product-life-cycle.md)
- [NPI frequency and demand uncertainty](09-npi-frequency-and-demand-uncertainty.md)

## Related concepts

Module 1 → Section C → Product Life Cycle Management; New Product Introduction Schedules.
