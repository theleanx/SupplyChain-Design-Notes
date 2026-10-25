# AlderGate Integrated Module 8 — Finance, Eligibility and ESG Calculation Reference

> A worked educational model, **not** a business approval, reporting methodology, vendor endorsement or APICS-supplied formula sheet.

## Bases and source boundaries

The 1,000-unit/week requirement and three network rows come from [Section A's unchanged location study](../../assets/data/module-8/section-a/location-design-alternatives.csv). The [capstone policy](../../assets/data/module-8/capstone/executive-policy.csv) sets 52 weeks/year, a five-year future operating horizon, a 10% annual discount rate, independent capital/recurring limits and cutover/adoption gates. Benefits and new expenses are the [manual-work](../../assets/data/module-8/capstone/manual-work-benefits.csv) and [program-cost](../../assets/data/module-8/capstone/program-costs.csv) assumptions. Cloud/AI/asset examples elsewhere in Section C have different populations and must not be added.

## Financial reproduction

Define USD/year network cost `C_n = facility + transport + inventory + network_service_failure`.

- `C_central = $625,000`.
- `C_regional = $575,000`.
- `C_low_cost = $520,000`, but its 850 units/week are below the mandatory 1,000-unit/week requirement and it fails the fictional worker gate.
- `N = $625,000 - $575,000 = $50,000/year` is the **modeled network difference** among eligible alternatives.
- Labor potential `L = 15,000 × 0.35 × $20 + 5,000 × 0.50 × $20 = $155,000/year`. The workloads are **disjoint** and absent from the Section A cost columns. Finance has *not* established cash avoidability.
- Chosen eligible technology recurring service `V_B=$84,000/year`. Incremental support `S=$24,000/year`. `V_B + S = $108,000/year`.
- Certain time-zero costs `I=$110,000+$45,000+$30,000=$185,000`.
- Baseline annual full operating scope `C_base = $625,000 + $155,000 = $780,000`.
- With benefit fraction `f`, proposed full operating annual amount `C_prop(f)=$575,000+$84,000+$24,000+$155,000(1-f)`.
- Annual incremental net `D(f)=C_base-C_prop(f)=$50,000+$155,000f-$108,000=$155,000f-$58,000`.
- `PVA=SUM_{t=1..5}(1.10)^{-t}=3.7907867694`.
- `NPV(f) = -$185,000 + D(f)×PVA`.
- `NPV(0.75)=+$35,813.33`, with simple undiscounted payback `I/D(0.75)=3.176 operating years`.
- `f_break_even=[I/PVA +$58,000]/$155,000=68.90486%`, **not** the separate 75% operational adoption rule.

These are level annual cash-flow **scenarios after acceptance**, not reported financial results or claims about calendar dates. There is no modeled price or volume inflation, tax, debt interest, salvage, or terminal value.

## Eligibility and no-offset rules

Apply gates *before* annual cost and subjective vendor ranking:

- Capacity (weekly): candidate at least the documented required weekly customer volume. At 1,200/week stress, regional 1,100 is short and cannot keep the base modeled network-saving estimate without a redesigned service and economic case.
- Worker/safety and destination authorization: must pass for the selected physical network. A favorable modeled footprint does not overcome a failed worker gate.
- Vendor: both secure-access and response gates must pass, and annual vendor+incremental support must be <= $110,000. Vendor A is technically qualified but $116,000 exceeds the training budget; vendor C is excluded because access fails; B is the chosen eligible candidate.
- Funding: $185,000 t0 is <= $200,000 capital cap. No business authorization is implied.
- Quality: two critical failures remain versus permitted zero; **do not activate automatic release**.
- Change: 180/200 trained = 90% meets threshold but 134/200 active = 67% below 75%. At least 16 more users must demonstrate meaningful correct new-process use at the same sample size.
- Reporting: physical/site evidence is needed before asserting verified emissions or the aggregate 66% recycling claim while Plant B source exceptions remain.

**Environmental boundary:** modeled annual `tCO2e = warehouse-energy tonnes + outbound-transport tonnes`. Central 139, regional 109, low-cost 101 (ineligible for other reasons). The regional design's modeled decrease is 30/139 = 21.58%, **not** a whole-company or lifecycle reduction. A fictional 120-tonne aspiration is voluntary.

## Decision-sensitive outcomes

| Modeled benefit fraction | D(f), USD/year | NPV, USD |
| --- | ---: | ---: |
| 60% | 35,000 | -52,322.46 |
| 67% | 45,850 | -11,192.43 |
| 75% | 58,250 | +35,813.33 |
| 100% | 97,000 | +182,706.32 |

The 67% active-use observation is **not proof of 67% avoided cash**. Applying it as a proxy is an explicitly labeled sensitivity. Removing only the $50,000 network saving while holding everything else fixed at 75% gives annual `$8,250` and five-year `NPV=-$153,726.01`; this is **not** a complete 1,200-unit/week network economics model.

## Sources and replay

- [Assignment](../../08-optimization-sustainability-technology/capstone/README.md)
- [Fully worked solution](../../08-optimization-sustainability-technology/capstone/solution-guide.md)
- [Direct input catalog](../../assets/data/module-8/capstone/README.md)
- [Independent CSV replay](./replay.py)
