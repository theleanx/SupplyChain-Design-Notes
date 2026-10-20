# Module 7 fictional data register

All cases and figures are invented; they are not observed industry statistics or official thresholds. The training worksheets separate annual costs from conditional losses, constrain operational alternatives through mandatory gates and preserve common horizons.

## Available datasets

- [`asset-loss-control-record.csv`](./asset-loss-control-record.csv)
- [`business-continuity-dependencies.csv`](./business-continuity-dependencies.csv)
- [`crisis-exercise-actions.csv`](./crisis-exercise-actions.csv)
- [`demand-risk-scenarios.csv`](./demand-risk-scenarios.csv)
- [`emv-outcome-scenarios.csv`](./emv-outcome-scenarios.csv)
- [`emv-response-options.csv`](./emv-response-options.csv)
- [`environmental-route-continuity.csv`](./environmental-route-continuity.csv)
- [`financial-risk-controls.csv`](./financial-risk-controls.csv)
- [`grc-control-map.csv`](./grc-control-map.csv)
- [`ip-and-reputation-register.csv`](./ip-and-reputation-register.csv)
- [`network-exposure.csv`](./network-exposure.csv)
- [`people-security-gates.csv`](./people-security-gates.csv)
- [`preventive-contingency-model.csv`](./preventive-contingency-model.csv)
- [`process-failure-paths.csv`](./process-failure-paths.csv)
- [`qualitative-risk-ratings.csv`](./qualitative-risk-ratings.csv)
- [`risk-appetite-policy.csv`](./risk-appetite-policy.csv)
- [`risk-category-cases.csv`](./risk-category-cases.csv)
- [`risk-classification-sample.csv`](./risk-classification-sample.csv)
- [`risk-evidence-quality.csv`](./risk-evidence-quality.csv)
- [`risk-funding-plan.csv`](./risk-funding-plan.csv)
- [`risk-identification-workshop.csv`](./risk-identification-workshop.csv)
- [`risk-lifecycle-events.csv`](./risk-lifecycle-events.csv)
- [`risk-owner-coordination.csv`](./risk-owner-coordination.csv)
- [`risk-probability-distributions.csv`](./risk-probability-distributions.csv)
- [`risk-register-sample.csv`](./risk-register-sample.csv)
- [`risk-response-methods.csv`](./risk-response-methods.csv)
- [`risk-response-plan.csv`](./risk-response-plan.csv)
- [`risk-sensitivity-cases.csv`](./risk-sensitivity-cases.csv)
- [`risk-simulation-spec.csv`](./risk-simulation-spec.csv)
- [`risk-standard-use-ledger.csv`](./risk-standard-use-ledger.csv)
- [`simulation-reproducibility.json`](./simulation-reproducibility.json)
- [`supply-continuity.csv`](./supply-continuity.csv)
- [`unknown-risk-signals.csv`](./unknown-risk-signals.csv)

## Integrated capstone reuse

The [Stonebridge capstone assignment](../../../07-supply-chain-risk/capstone/README.md) and [solution](../../../07-supply-chain-risk/capstone/solution-guide.md) reuse existing risk, mitigation, supplier, route, demand and recovery datasets. No private APICS source files are republished. During capstone integration, the 17% degraded-hardening sensitivity row was corrected to `fail` (modeled 17% residual probability exceeds the stated fictional 10% mandatory security gate) to match the pre-existing mandatory security policy in the related lessons; the arithmetic values were not changed.
