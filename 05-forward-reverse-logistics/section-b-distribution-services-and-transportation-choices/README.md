# Section B: Distribution Services and Transportation Choices

Section B moves from the logistics-capacity foundation in Section A into distribution services, fulfillment channels, transportation modes, intermodal routes, and carrier structures.

This section follows fictional **HarborPeak Equipment Systems**. All examples, shipment records, costs, service scores, diagrams, datasets, and assessment questions are independently created for this repository.

## Learning outcomes

After completing Section B, you should be able to:

- trace receiving, put-away, storage, picking, movement, packing/marking, and shipping as one controlled warehouse execution flow;
- distinguish consolidation, break-bulk, cross-docking, postponement, stockpiling, spot stocking, assortment, and mixing;
- translate customer requirements into channel service outputs and fulfillment architectures;
- compare integrated, dedicated, pooled, direct-store, store, flow-through, drop-ship, and direct-delivery models;
- distinguish a distribution network from an individual order-fulfillment route;
- select transportation modes using service, access, value/packaging density, damage, security, reliability, and economics;
- compare rail, motor, water, pipeline, air, and intermodal capabilities without relying on simplistic mode stereotypes; and
- separate carrier classification/structure from transportation mode and apply eligibility gates before price ranking.

## Learning path

1. [Warehouse Execution Activities: Receive, Put Away, Pick, Pack, Move, and Ship](./01-warehouse-execution-activities-receive-put-away-pick-pack-move-and-ship.md)
2. [Value-Added Distribution Services: Consolidation, Break-Bulk, Cross-Dock, and Postponement](./02-value-added-distribution-services-consolidation-break-bulk-cross-dock-and-postponement.md)
3. [Stockpiling, Spot Stocking, Assortment, and Mixing](./03-stockpiling-spot-stocking-assortment-and-mixing.md)
4. [Channel Design, Supply and Distribution Channels, and Service Outputs](./04-channel-design-supply-and-distribution-channels-and-service-outputs.md)
5. [Order Channels and Fulfillment Strategy Design](./05-order-channels-and-fulfillment-strategy-design.md)
6. [Integrated and Dedicated Fulfillment](./06-integrated-and-dedicated-fulfillment.md)
7. [Pool, Direct-Store, Store, and Flow-Through Fulfillment](./07-pool-direct-store-store-and-flow-through-fulfillment.md)
8. [Comparing Distribution Strategies](./08-comparing-distribution-strategies.md)
9. [Distribution Network Architectures: Manufacturer, Distributor, and Aggregator Models](./09-distribution-network-architectures-manufacturer-distributor-and-aggregator-models.md)
10. [Drop Ship, Direct Delivery, and Order-Fulfillment Channel Comparison](./10-drop-ship-direct-delivery-and-order-fulfillment-channel-comparison.md)
11. [Transportation Mode Selection and Value/Packaging Density](./11-transportation-mode-selection-and-value-packaging-density.md)
12. [Rail and Motor Carrier Transport](./12-rail-and-motor-carrier-transport.md)
13. [Water, Pipeline, and Air Transport](./13-water-pipeline-and-air-transport.md)
14. [Intermodal, Package Delivery, and Container Services](./14-intermodal-package-delivery-and-container-services.md)
15. [Carrier Classifications and Carrier Selection](./15-carrier-classifications-and-carrier-selection.md)
16. [Section B Review](./16-section-b-review.md)

## Working data and visuals

- [`warehouse-operations.csv`](../../assets/data/module-5/warehouse-operations.csv) — receiving, put-away, picking, packing, cross-dock, postponement, and kitting activity data
- [`fulfillment-strategies.csv`](../../assets/data/module-5/fulfillment-strategies.csv) — integrated, dedicated, pooled, local, and drop-ship strategy comparison
- [`distribution-networks.csv`](../../assets/data/module-5/distribution-networks.csv) — network ownership, inventory, transport, response, and scalability scenarios
- [`transport-mode-selection.csv`](../../assets/data/module-5/transport-mode-selection.csv) — shipment, value/packaging density, mode, service, and line-haul comparison
- [`carrier-options.csv`](../../assets/data/module-5/carrier-options.csv) — common, private, contract, and exempt training scenarios
- [Logistics, Trade, and Reverse-Flow formula/control sheet](../../calculations/logistics-trade-reverse/formula-sheet.md)

Each topic also includes an original decision visual; process-oriented lessons use operational flows to separate sequence from conceptual comparison.

## How to study the section

Follow one customer order through the warehouse, then ask how the network changes when that order is consolidated, postponed, routed through a different fulfillment model, or assigned a different transportation mode. For every transportation decision, use the same sequence:

**define the requirement → eliminate infeasible choices → compare total-route/service economics → retain evidence**

Carrier classifications are presented as a curriculum framework. Real carrier authority, exemptions, safety requirements, and legal obligations vary by jurisdiction and must be verified against current official sources before operational use.