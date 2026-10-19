# Supply Chain Risk Analysis — Calculation and Decision-Control Reference

> **Scope:** Module 7 Section B. Stonebridge examples and data are fictional training cases, not measured risk rates or official performance standards. Financial and operational alternatives must pass mandatory eligibility gates before ranking.

## 1. Define the event, outcome and horizon

A probability is only interpretable with a stated event and period. For one complete, mutually exclusive outcome set, the probabilities must sum to **1.00**. Conditional loss refers to the magnitude **if** the event or outcome occurs. Probability-weighted losses are expected values, not guaranteed annual charges.

If losses are shown as positive magnitudes, annual **expected loss** is

`E[L] = Σ P(outcome i) × Loss_if_outcome_i`, in USD per year when the inputs refer to one year.

For the three exclusive Stonebridge shipping outcomes in [`emv-outcome-scenarios.csv`](../../assets/data/module-7/emv-outcome-scenarios.csv), 65% probability of no loss, 25% of an $80,000 loss and 10% of a $250,000 loss result in **$45,000** expected annual loss. A signed operating-result EMV uses negative signs for losses; here it is **−$45,000**. The most severe modeled consequence remains $250,000, not $45,000.

## 2. Three-point conditional estimates

Given optimistic cost `a`, most likely cost `m` and pessimistic cost `b`, where `a ≤ m ≤ b`:

- Equal-weight three-point mean = `(a + m + b)/3`.
- PERT-style weighted mean = `(a + 4m + b)/6`.

For invented recovery outcomes of $25,000, $40,000 and $100,000, the results are **$55,000** and **$47,500** respectively. These are summaries of *conditional event severity* under alternate estimation conventions, not annual EMVs and not an automatically validated probability distribution.

## 3. Certain expenses versus event-only consequences

For a control paid annually regardless of disruption with one relevant event at most per year:

`Expected annual total cost = certain annual control cost + P(event after control) × loss_if_event_after_control`.

The [`emv-response-options.csv`](../../assets/data/module-7/emv-response-options.csv) example compares eligible monitored hardening and isolated failover:

| Response | Certain annual cost | Residual event probability | Conditional loss | Expected annual cost | Feasible gate |
| --- | ---: | ---: | ---: | ---: | --- |
| Monitored hardening | $11,000 | 8% | $220,000 | **$28,600** | Pass |
| Isolated failover | $29,000 | 6% | $145,000 | **$37,700** | Pass |

The insurance-only illustration is **not eligible** for ranking: modeled losses omit a material coverage exclusion, and a mandatory security requirement fails. Its nominal arithmetic is not an insured outcome prediction. The baseline untreated $46,800 expected annual loss is also ineligible under the fictional security gate.

A multi-year investment needs a consistent treatment of initial investment, operating costs, terminal value and discounting rather than plugging all cash flows into the one-year formula. Incident-only vendor fees are conditional; annual vendor retainers are certain.

## 4. Sensitivity and switching value

Set two eligible alternative costs equal, holding other inputs unchanged:

`11,000 + 220,000 × p_hardening = 37,700`.

So `p_hardening = 26,700/220,000 = 0.1213636364`, or **12.14%** when rounded. At 17% hardening probability, the modeled annual hardening cost is **$48,400**, above failover at $37,700. **The fictional 10% security gate binds first**: hardening becomes ineligible above 10%, before the hypothetical 12.14% cost-indifference point. Changing a model input does **not** establish that the new probability is empirically credible.

## 5. Monte Carlo: a reproducible teaching simulation

[`risk-simulation-spec.csv`](../../assets/data/module-7/risk-simulation-spec.csv) fixes the model, number of draws and random seed; [`simulation-reproducibility.json`](../../assets/data/module-7/simulation-reproducibility.json) preserves the resulting statistics.

```python
import random
import statistics

rng = random.Random(20261019)
losses = []
for _ in range(10_000):
    u = rng.random()
    loss = 0 if u < 0.65 else 80_000 if u < 0.90 else 250_000
    losses.append(loss)

print({amount: losses.count(amount) for amount in (0, 80_000, 250_000)})
print(statistics.mean(losses))
```

Using Python's seeded default random-number algorithm in this example, the output is **6,540**, **2,467**, **993** simulated outcomes and a mean of **$44,561**. The analytic mean remains **$45,000**. Simulated draws do not become real-world observed incidents. Dependencies and tail-loss assumptions must be justified in any practical model.

## 6. Operational coverage and capacity

- Material **weeks of usable cover** = `unrestricted approved units / expected units consumed each week`. For 240 usable controller components and 120/week, cover is **2 weeks**. An unqualified alternate does not increase approved cover.
- Weekly surge **uncovered units** = `max(0, confirmed demand − (qualified normal capacity + approved additional supply))`. For 650 demand, 500 normal and 50 substitute, uncovered = **100/week**.
- Emergency lane coverage: 800 primary and **verified** 400 backup gives **400 units/week uncovered**. A weather-affected or unconfirmed 100-unit air backup must be excluded until approved and viable.

## 7. Financial stress and expert review

- FX incremental USD payable on a fixed EUR amount = `EUR exposure × (stress USD/EUR − baseline USD/EUR)`. For €800,000 from 1.10 to 1.17 the incremental amount is **$56,000** unhedged.
- Commodity cost increment = `affected quantity × (stress price − baseline price)`. For 50,000 kg at +$0.50/kg it is **$25,000**.

Neither amount is an annual risk expected loss absent a separate probability scenario. Currency hedging, commercial claims, sanctions, product liability, and litigation reserves require specialist approvals. Hard legal and life-safety requirements are never made optional by favorable EMV.

## 8. Continuity tests and gates

The **recovery time objective (RTO)** is a planned maximum period for restoring a specified activity to an acceptable level. Exercise actual durations are measured observations. Restoring order-system access in four hours does not guarantee finished-goods release when quality validation, supplier confirmation or physical dispatch is unavailable. Test business process dependencies end to end. A failed tabletop activation time must generate corrective action and a dated retest.

## 9. Anti-patterns to reject

1. Multiplying certain annual mitigation expenses by incident probability.
2. Combining signed profits with positive loss magnitudes without explicit sign policy.
3. Ranking an option that fails a mandatory coverage, safety, quality or cybersecurity gate.
4. Adding correlated incident consequences as if they were independent events.
5. Treating qualitative 1–5 ratings as empirical probabilities or multiplying them into dollar EMV.
6. Reporting simulation results as real observed frequencies.
7. Counting conditional supplier/transport capacity before qualification, confirmation, or safe authorization.
8. Declaring the supply chain recovered solely because the IT system is back online.

---

[Module 7 Section B overview](../../07-supply-chain-risk/section-b-risk-analysis-and-response/README.md) · [Module 7 overview](../../07-supply-chain-risk/README.md)
