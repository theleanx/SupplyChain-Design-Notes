# Logistics, Trade, and Reverse-Flow Formula & Control Sheet

This sheet supports Module 5 worked examples. All numbers used in the repository datasets are fictional.

## Warehouse capacity

**Pallet cube**

`pallet cube = pallet length × pallet width × loaded height`

**Base storage bays**

`base bays = forecast aggregate inventory cube ÷ pallet cube`

**Partial-pallet adjustment**

`adjusted bays = base bays × partial-pallet factor`

**Raw inventory footprint**

`raw footprint = adjusted bays × pallet floor footprint`

**Movement and aisle allowance**

`handling-adjusted footprint = raw footprint × movement/aisle factor`

**Vertical-space adjustment**

`vertical-adjusted area = handling-adjusted footprint ÷ usable storage levels`

**Target-utilization allowance**

`required core warehouse area = vertical-adjusted area ÷ target utilization`

If the scenario has a separate bulk-storage requirement:

`total required area = required core warehouse area + separate bulk-storage allowance`

## Product and shipment density

**Value density**

`value density = shipment value ÷ occupied shipment volume`

**Packaging density**

`packaging density = packed unit quantity ÷ occupied shipment volume`

Neither measure is a stand-alone mode-selection rule.

## Illustrative import-cost arithmetic

Customs valuation, tariff bases, taxes, exemptions, and drawback rules vary by jurisdiction. The equations below are training mechanics only.

**Import duty**

`duty = stated customs-assessment value × stated tariff rate`

**Illustrative VAT/GST-style calculation**

When the training scenario explicitly states that tax is assessed on customs value plus duty:

`tax base = customs value + duty`

`import tax = tax base × stated tax rate`

**Illustrative border-charge effect**

`border-charge effect = duty + modeled import tax − modeled duty drawback`

Do not apply these assumptions to a real shipment without current jurisdiction-specific verification.

## Reverse-logistics economics

For the HarborPeak learning cases:

`economic result = recovery revenue + restocking revenue + tax/incentive benefit + service benefit − processing cost − transport cost − repair/parts cost − credit/warranty cost`

A positive economic result never overrides a safety, regulatory, product-integrity, or chain-of-custody hold.

## Decision and control gates

1. **Total logistics cost / service gate** — compare cost alternatives only at an approved service level.
2. **3PL/4PL gate** — capability, control, reliability, metrics, subcontracting, remedies, and exit provisions must pass before price ranking.
3. **Warehouse network gate** — evaluate service, transportation, inventory, overhead, labor, infrastructure, and regulatory constraints together.
4. **Materials-handling gate** — safety and load/capability fit precede economic ranking.
5. **Transportation-capacity gate** — plan by lane/mode using forward-looking demand and preserve procurement lead time.
6. **Fulfillment/channel gate** — match service outputs, inventory position, handling, order channel, and capital before ranking architectures.
7. **Carrier-class gate** — choose the structural carrier model before scoring specific providers.
8. **Trade-compliance gate** — mandatory legal/security requirements cannot be offset by a weighted score.
9. **Trade-term responsibility gate** — record named place, rule/year, responsibilities, delivery/risk point, and insurance obligations as applicable.
10. **Document-completeness gate** — mandatory export/transport/import documents must be complete and mutually consistent before release.
11. **FTZ/trade-bloc strategy gate** — verify current eligibility and jurisdictional effects before applying a modeled benefit.
12. **Reverse-network gate** — stakeholder requirements, compliance, service, speed, return forecast, and life-cycle support precede make/buy ranking.
13. **Waste/hazardous-material gate** — safety, legal handling, approved-facility, and chain-of-custody requirements override recovery economics.

## Calculation discipline

Every quantitative lesson should state units and time horizon, assumptions, the dataset used, the calculation, the operational interpretation, and the decision or control action supported by the result.