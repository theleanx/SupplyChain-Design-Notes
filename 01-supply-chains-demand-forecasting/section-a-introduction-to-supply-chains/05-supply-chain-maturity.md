# 5. Supply Chain Maturity

## The five-stage progression

Supply-chain evolution can be understood through five maturity stages. The important idea is not memorizing labels alone; it is understanding how **coordination, information, technology, planning, and external collaboration** mature over time.

```mermaid
flowchart LR
    S1[1. Multiple dysfunction
Reactive] --> S2[2. Semifunctional enterprise
Reactive efficient]
    S2 --> S3[3. Integrated enterprise
Proactive efficient]
    S3 --> S4[4. Extended enterprise
Strategic driver]
    S4 --> S5[5. Orchestrated supply chain
Consistent & systematic]
```

## Stage 1 - Multiple dysfunction

Functions operate largely in silos. Information is fragmented, planning is weak, purchasing can be transactional, and the supply chain primarily reacts to demand.

```mermaid
flowchart LR
    S[Sales] -. limited coordination .- P[Production]
    P -. limited coordination .- B[Buying]
    B -. limited coordination .- W[Warehouse]
    X[External partners] -->|transactional only| B
```

### NorthStar example

Sales promises delivery without checking production. Purchasing buys based on urgent requests. Warehousing receives trucks without coordinated appointments. Forecasting is mostly judgmental. Each function can appear busy while total performance remains poor.

## Stage 2 - Semifunctional enterprise

Individual functions improve their own efficiency. Better tools and practices appear, but coordination across functions is still limited.

```mermaid
flowchart LR
    S[Sales improved] --> H[Sequential handoffs]
    P[Production improved] --> H
    B[Procurement improved] --> H
    L[Logistics improved] --> H
    H --> C[Better local efficiency, weak enterprise optimization]
```

### NorthStar example

Purchasing introduces preferred suppliers and logistics negotiates better carrier contracts, while inventory management reduces stock. Each initiative helps locally, but decisions are not yet driven by one enterprise plan.

## Stage 3 - Integrated enterprise

The organization integrates processes and information internally. Cross-functional planning, enterprise systems, and coordinated business processes replace many functional silos.

```mermaid
flowchart TB
    D[Shared enterprise data / planning] --> S[Sales]
    D --> O[Operations]
    D --> P[Procurement]
    D --> L[Logistics]
    S <--> O
    O <--> P
    O <--> L
```

### NorthStar example

Sales, operations, procurement, logistics, and finance use common planning data. Product-development decisions include manufacturing and supply-chain input earlier in the design process.

## Stage 4 - Extended enterprise

Integration expands outside the organization to selected suppliers and customers. Planning and information sharing become collaborative across company boundaries.

```mermaid
flowchart LR
    SUP[Strategic supplier] <--> N[Nucleus company
shared plans & processes]
    N <--> CUST[Strategic customer]
    SUP -. synchronized data .-> N
    CUST -. demand / usage data .-> N
```

### NorthStar example

A strategic motor supplier receives forecast and capacity signals. NorthStar's largest distributor shares sell-through data. Both parties jointly resolve demand/supply mismatches.

## Stage 5 - Orchestrated supply chain

The network operates in a more systematic, data-driven, resilient, and change-ready way. Information integrity, end-to-end visibility, process automation, and shared improvement capabilities become important characteristics.

```mermaid
flowchart TB
    C[Customer / market signals] --> V[Shared end-to-end visibility]
    S[Supplier constraints] --> V
    V --> A[Analytics / exception detection]
    A --> W[Coordinated workflows]
    W --> R[Resilient response & continuous improvement]
    R -. learning .-> V
```

### NorthStar example

Customer usage signals update demand sensing; strategic suppliers provide near-real-time constraints; automated workflows highlight exceptions; cross-company teams manage disruptions and continuous improvement using common data.



## Process interdependencies and bottlenecks

As maturity improves, managers increasingly look at an end-to-end process instead of optimizing isolated departments. Mapping who owns each step, how one step depends on another, and where bottlenecks occur helps the organization streamline flow and remove delays that would be invisible inside a single functional silo.

## Maturity as an input to strategy

Maturity is not a trophy; it is a **gap-assessment tool**. A company should compare the capabilities its strategy requires with the capabilities the current supply chain actually has. Gaps in visibility, connectivity, process discipline, partner collaboration, data quality, resilience, or change readiness become improvement priorities.

Reassessment should continue over time because acquisitions, reorganizations, new technologies, new competitors, and major disruptions can change the maturity of the network. A business can also be at different maturity levels in different processes at the same time.

### Detailed comparison

| Stage | Typical planning / technology | Relationship pattern | Main management concern |
|---|---|---|---|
| 1 | Basic, fragmented, heavily manual | Mostly transactional | Respond somehow to demand |
| 2 | Better functional tools; local automation | External ties remain limited | Reduce cost inside each function |
| 3 | Shared enterprise systems and cross-functional planning | Internal integration is strong | Optimize the enterprise as one system |
| 4 | Shared data and synchronized processes with selected partners | Collaborative external processes | Compete as an extended network |
| 5 | Real-time data, analytics, automation, stronger security and resilience | Broad orchestration and rapid adaptation | Create sustained network advantage |

## Comparison

| Stage | Primary behavior | Integration scope | Planning character |
|---|---|---|---|
| 1 | Reactive | Siloed functions | Ad hoc |
| 2 | Reactive efficient | Functional | Local optimization |
| 3 | Proactive efficient | Enterprise | Cross-functional |
| 4 | Strategic driver | Selected external partners | Collaborative |
| 5 | Consistent/systematic | End-to-end network | Orchestrated and adaptive |

## Important nuance

Organizations do not always progress neatly. Different business units or processes can operate at different maturity levels at the same time.

## Common mistake

A company that has excellent ERP technology is not automatically at Stage 5. Higher maturity also requires process integration, collaboration, information quality, organizational capability, and effective use of technology.
