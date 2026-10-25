# Module 8 Integrated Capstone — Fictional AlderGate Inputs

All six CSVs are original, synthetic training inputs. They are **not ASCM/APICS source datasets**, actual operational facts, verified emissions, publicly reportable sustainability figures, vendor evaluations or externally binding policies.

| CSV | Contents | Used by |
| --- | --- | --- |
| [executive-policy.csv](./executive-policy.csv) | Five-year 10% modeling policy, base/stress volume, finance and rollout gates | [Assignment](../../../../08-optimization-sustainability-technology/capstone/README.md), [worked solution](../../../../08-optimization-sustainability-technology/capstone/solution-guide.md) |
| [network-sustainability.csv](./network-sustainability.csv) | Annual energy/outbound emission components and labor/destination gates | [Assignment](../../../../08-optimization-sustainability-technology/capstone/README.md) |
| [manual-work-benefits.csv](./manual-work-benefits.csv) | Disjoint event and invoice process pools, time assumptions and open cash verification | [Worked solution](../../../../08-optimization-sustainability-technology/capstone/solution-guide.md) |
| [program-costs.csv](./program-costs.csv) | New t0 investments and ongoing support, separately from external vendor fee | [Worked solution](../../../../08-optimization-sustainability-technology/capstone/solution-guide.md) |
| [benefit-sensitivity.csv](./benefit-sensitivity.csv) | Four cash-realization assumptions, not actual adoption-to-benefit relationships | [Worked solution](../../../../08-optimization-sustainability-technology/capstone/solution-guide.md) |
| [governance-actions.csv](./governance-actions.csv) | Eight initial open controls with triggers, owners and day-specific reviews | [Worked solution](../../../../08-optimization-sustainability-technology/capstone/solution-guide.md) |

The integrated case *also* links the previously authored, unchanged [Section A network data](../section-a/location-design-alternatives.csv), [Section B recycling data](../section-b/recycling-lineage.csv), and [Section C vendor](../section-c/technology-selection.csv), [change pilot](../section-c/change-coalition.csv) and [cutover](../section-c/cutover-acceptance.csv) datasets.

**Financial boundaries:** Section A network costs exclude the two new disjoint manual activities; the Section C software fee and new support are not already included. Otherwise the incremental cash model would double count the same saving or expense. Values and eligibility flags are fictional; specific regulatory obligations and supplier certificates must be independently verified.

Run [the replay](../../../../calculations/module8-capstone/replay.py) and [the capstone validator](../../../../scripts/validate_module8_capstone.py) to validate source consistency and calculations.
