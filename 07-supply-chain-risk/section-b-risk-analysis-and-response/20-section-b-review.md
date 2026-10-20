# 20. Section B Review — Analysis, Response, and Continuity

> **Independent learning assessment.** The questions below were authored for this repository and do not reproduce APICS examination or workbook questions. All cases and numerical assumptions are fictional.

## Learning outcomes

- Categorize event paths and rate their qualitative severity without false numerical precision.
- Calculate valid scenario EMV, prevention economics, sensitivity thresholds and shortfalls.
- Choose feasible responses under safety, security, quality, insurance and legal gates.
- Confirm recovery through tested process, information, supplier and logistics dependencies.

## Review questions

Study each situation and choose the **best** answer. Open the rationale only after recording your choice.

### Question 1 — Qualitative risk and models

**Question.** Two independent suppliers both use one inland freight bridge. A storm closes the bridge and delays the same customer order. Which analysis avoids double counting?

A. Register two independent customer-penalty losses for one delayed order

B. Ignore supplier risks because the event is external

C. Model one bridge shock with multiple dependent consequences and one consolidated service loss

D. Move every effect into a financial-risk category

<details>
<summary>Answer and rationale</summary>

**Correct answer: C — Model one bridge shock with multiple dependent consequences and one consolidated service loss.**

A common bridge interruption is one shared initiating event; model each distinct consequence and count the delayed order loss once.

**Why the alternatives do not prevail:**

- **A.** A second reported impact on the same customer penalty would duplicate loss.
- **B.** External origins still create supply-chain exposure and ownership.
- **D.** Changing a category does not identify shared dependencies.

</details>

### Question 2 — Qualitative risk and models

**Question.** A supplier interruption rates 4 likelihood and 3 consequence; a plant safety exposure rates 2 and 5 and requires immediate inspection. Which conclusion is justified?

A. Supplier score is 12, but the safety inspection gate must still be met

B. Plant score is 25 because safety is always scored highest

C. Supplier has 12% probability and safety has 10% probability

D. Neither can be acted on until a cash flow is estimated

<details>
<summary>Answer and rationale</summary>

**Correct answer: A — Supplier score is 12, but the safety inspection gate must still be met.**

The supplier scores 4×3=12, but the independent safety inspection is a hard gate and cannot wait for ranking.

**Why the alternatives do not prevail:**

- **B.** The second score is 2×5=10, not 25.
- **C.** Ordinal scores do not equal percentages.
- **D.** Mandatory inspection should not wait for EMV.

</details>

### Question 3 — Qualitative risk and models

**Question.** Two analysts report the same estimated loss as $22,000 and $22,000.005, both using incomplete incident logs. What is the best inference?

A. Six decimal places prove a better probability model

B. Precision of formatting does not fix incomplete or biased evidence

C. The more precise entry necessarily has lower uncertainty

D. An event with incomplete logs has zero loss

<details>
<summary>Answer and rationale</summary>

**Correct answer: B — Precision of formatting does not fix incomplete or biased evidence.**

Accuracy, data integrity and representative records determine evidentiary quality; extra decimal places do not repair weak inputs.

**Why the alternatives do not prevail:**

- **A.** Formatting is not evidence of input accuracy.
- **C.** More decimal places do not quantify underlying uncertainty.
- **D.** Missing logs cannot imply zero loss.

</details>

### Question 4 — Qualitative risk and models

**Question.** Three conditional cost estimates are $10k, $20k most likely and $50k. What is the weighted PERT-style mean?

A. $20,000

B. $26,667

C. $23,333

D. $33,333

<details>
<summary>Answer and rationale</summary>

**Correct answer: C — $23,333.**

(10+4×20+50)/6 = 140/6 ≈ $23,333; it is an estimated conditional loss, not annual event EMV.

**Why the alternatives do not prevail:**

- **A.** This uses the mode alone.
- **B.** This figure is not the stipulated weighted PERT mean.
- **D.** This amount is not implied by the estimates.

</details>

### Question 5 — Quantitative risk and economics

**Question.** Annual mutually exclusive outcomes are 75% no loss, 15% of a $60k loss, and 10% of a $120k loss. What is the expected annual loss?

A. $180,000

B. $15,000

C. $9,000

D. $21,000

<details>
<summary>Answer and rationale</summary>

**Correct answer: D — $21,000.**

Expected annual loss is 0.75×0 + 0.15×$60,000 + 0.10×$120,000 = $21,000.

**Why the alternatives do not prevail:**

- **A.** This adds unweighted conditional outcomes.
- **B.** This omits the severe outcome.
- **C.** This omits the moderate outcome.

</details>

### Question 6 — Quantitative risk and economics

**Question.** A protection program costs a certain $14k yearly. Following implementation, interruption likelihood is 10% with $80k conditional loss. Which expected annual total is correct?

A. $22,000

B. $8,000

C. $14,800

D. $15,000

<details>
<summary>Answer and rationale</summary>

**Correct answer: A — $22,000.**

Pay the certain $14,000 every year, then add 10% of the $80,000 conditional event cost: $22,000.

**Why the alternatives do not prevail:**

- **B.** This ignores the certain control fee.
- **C.** The calculation incorrectly weights the certain expense.
- **D.** The total lacks one or more cost components.

</details>

### Question 7 — Quantitative risk and economics

**Question.** A response option costs $5k annually plus probability p times $150k conditional loss. An eligible alternative costs $25k annually. At approximately which probability do costs match?

A. 5.00%

B. 13.33%

C. 20.00%

D. 25.00%

<details>
<summary>Answer and rationale</summary>

**Correct answer: B — 13.33%.**

Equate $5,000 + 150,000p to $25,000: p = 20,000/150,000 ≈ 13.33%.

**Why the alternatives do not prevail:**

- **A.** 5% does not balance $20k excess cost.
- **C.** 20% is higher than the switching value.
- **D.** 25% makes the variable-cost option substantially more expensive.

</details>

### Question 8 — Quantitative risk and economics

**Question.** A Monte Carlo analyst increases runs from 10,000 to 1 million without changing a questionable event probability. What does this improve?

A. The truth of the assumed probability

B. Independence between correlated supply-chain hazards

C. Numerical sampling stability, not input-model correctness

D. Evidence that the events have actually occurred

<details>
<summary>Answer and rationale</summary>

**Correct answer: C — Numerical sampling stability, not input-model correctness.**

Additional draws reduce finite-sample noise conditional on the assumed model, but do not correct a wrong event probability.

**Why the alternatives do not prevail:**

- **A.** More draws cannot validate event probability.
- **B.** Sampling method does not eliminate underlying correlated hazards.
- **D.** Simulated values are not actual recorded incidents.

</details>

### Question 9 — Responses and risk controls

**Question.** An insurance policy covers some direct property loss but excludes production stoppage after a supplier cyber incident. How should the risk owner classify this?

A. Total avoidance

B. Complete reduction in cyber-event likelihood

C. Full transfer of every operational consequence

D. Partial transfer of specified financial effects with uncovered downtime

<details>
<summary>Answer and rationale</summary>

**Correct answer: D — Partial transfer of specified financial effects with uncovered downtime.**

Specified covered financial losses may transfer; supplier cyber downtime expressly excluded under the hypothetical contract remains.

**Why the alternatives do not prevail:**

- **A.** An insured loss is not the removal of the exposure.
- **B.** Policy coverage does not change the cyber event frequency.
- **C.** The express exclusion invalidates full transfer.

</details>

### Question 10 — Responses and risk controls

**Question.** An alternate component plan has an owner and a supplier quote but lacks required engineering signoff. How should the plan be shown?

A. Not executable until qualification/release criteria are verified

B. Fully ready because commercial sourcing is complete

C. Closed because it has a response owner

D. Accepted permanently regardless of product approval

<details>
<summary>Answer and rationale</summary>

**Correct answer: A — Not executable until qualification/release criteria are verified.**

Supplier quotes and assigned owners are insufficient where an engineering/quality release gate has not passed.

**Why the alternatives do not prevail:**

- **B.** Commercial readiness does not establish technical release.
- **C.** The owner has not completed the approval gate.
- **D.** Acceptance cannot override the unpassed product requirement.

</details>

### Question 11 — Responses and risk controls

**Question.** A recovery vendor charges an $8k annual standby retainer and an additional $50k only if an event occurs. Event probability is 10%. Expected annual payment is:

A. $5,000

B. $13,000

C. $8,000

D. $58,000

<details>
<summary>Answer and rationale</summary>

**Correct answer: B — $13,000.**

Standing retainer $8,000 + 0.10×$50,000 expected activation fee = $13,000 per year.

**Why the alternatives do not prevail:**

- **A.** This omits the annual retainer.
- **C.** This ignores incident-triggered vendor fees.
- **D.** This charges the incident-only fee in every year.

</details>

### Question 12 — Responses and risk controls

**Question.** An alternate network path has a separate carrier but uses the same electrical substation as the primary hub. What must the strategic risk review do?

A. Declare geographic redundancy sufficient

B. Use average cost alone to select one path

C. Test correlated outage exposure and effective alternate throughput

D. Exclude the substation because it is not owned by the manufacturer

<details>
<summary>Answer and rationale</summary>

**Correct answer: C — Test correlated outage exposure and effective alternate throughput.**

Two carriers can share power infrastructure; apparent redundancy fails unless the common-cause hazard is examined.

**Why the alternatives do not prevail:**

- **A.** Geographic or carrier diversity is not proven independent.
- **B.** A shared substation can defeat a low-cost backup.
- **D.** Critical infrastructure is relevant even when outsourced.

</details>

### Question 13 — Responses and risk controls

**Question.** Usable material is 300 units at 150 units/week and a proposed alternative needs three weeks to qualify. What is the crucial conclusion?

A. The firm has three weeks of assured cover

B. The alternate can be released immediately to match consumption

C. The gap is eliminated because average stock is positive

D. The two-week cover is shorter than qualification time and requires a bridge plan

<details>
<summary>Answer and rationale</summary>

**Correct answer: D — The two-week cover is shorter than qualification time and requires a bridge plan.**

300/150 gives two weeks of usable cover, below the three-week qualification time. An approved bridge is necessary.

**Why the alternatives do not prevail:**

- **A.** Inventory provides two, not three, weeks of cover.
- **B.** The alternate qualification remains pending.
- **C.** Positive stock is insufficient to bridge the full lead time.

</details>

### Question 14 — Responses and risk controls

**Question.** A confirmed customer surge demands 600 units; the plant can make 520 plus 40 fully approved substitutes. What minimum shortfall needs allocation?

A. 40 units

B. 80 units

C. 0 units

D. 120 units

<details>
<summary>Answer and rationale</summary>

**Correct answer: A — 40 units.**

Production and substitutes provide 520+40=560 approved units, leaving 600−560=40 to allocate.

**Why the alternatives do not prevail:**

- **B.** This counts only the shortfall above ordinary production, ignoring approved substitutes.
- **C.** The demand still exceeds approved output.
- **D.** No data supports this larger shortfall.

</details>

### Question 15 — Continuity and recovery

**Question.** A line restart is technically possible but the affected quality-hold lots have not passed release testing. What governs the next step?

A. A sales target for the month

B. Validated quality and safety signoff before customer release

C. The size of last month’s overtime budget

D. Whether the IT help desk ticket is closed

<details>
<summary>Answer and rationale</summary>

**Correct answer: B — Validated quality and safety signoff before customer release.**

Product release remains subject to validated safety and quality authorization even if equipment can restart.

**Why the alternatives do not prevail:**

- **A.** Sales targets do not authorize quality-hold release.
- **C.** Opex budget does not establish product conformity.
- **D.** A closed help desk incident does not release quarantined goods.

</details>

### Question 16 — Continuity and recovery

**Question.** A primary route moves 900 weekly units and a flood-safe alternate has verified space for 500. No buffer is available. What does the continuity plan need to allocate?

A. 500 units

B. 900 units

C. 400 units

D. Zero because the lane is independent

<details>
<summary>Answer and rationale</summary>

**Correct answer: C — 400 units.**

900 weekly units minus verified 500-unit alternate capacity leaves 400 weekly units uncovered.

**Why the alternatives do not prevail:**

- **A.** 500 is protected capacity, not the missing amount.
- **B.** 900 is total demand, not the uncovered portion.
- **D.** An alternate lane does not automatically cover the entire original flow.

</details>

### Question 17 — Continuity and recovery

**Question.** During a hazardous vapor incident, a supervisor suggests waiting for a full EMV study before evacuation. The strongest risk response is:

A. Reduce the impact category because the event is uncertain

B. Transfer the risk to the cleaning contractor immediately

C. Continue production until a customer complaint arrives

D. Follow authorized immediate safety procedures and assess economics only afterward

<details>
<summary>Answer and rationale</summary>

**Correct answer: D — Follow authorized immediate safety procedures and assess economics only afterward.**

Immediate credible exposure triggers authorized life-safety response before economic loss comparison.

**Why the alternatives do not prevail:**

- **A.** Lower scores do not cancel emergency safety gates.
- **B.** A financial transfer cannot replace immediate protection.
- **C.** Waiting for harm to materialize would be unsafe.

</details>

### Question 18 — Continuity and recovery

**Question.** A €1 million payable is exposed to a rise in USD/EUR from 1.08 to 1.17, without a hedge. What is the incremental dollar cost?

A. $90,000

B. $1,170,000

C. $9,000

D. $1,080,000

<details>
<summary>Answer and rationale</summary>

**Correct answer: A — $90,000.**

€1,000,000×(1.17−1.08) USD per EUR equals $90,000 incremental payable before hedge effects.

**Why the alternatives do not prevail:**

- **B.** This is the stressed total invoice, not incremental cost.
- **C.** The calculation uses a tenth of the true exposure.
- **D.** This is the original rate amount, not the incremental shock.

</details>

### Question 19 — Continuity and recovery

**Question.** The order system is recovered inside four hours, but batch validation and critical transport have not been restored. Which business continuity claim is supportable?

A. The full end-to-end supply chain has recovered

B. An IT dependency is restored, while minimum customer service is still unverified

C. All recovery targets are met because the earliest target passed

D. The business continuity plan is no longer needed

<details>
<summary>Answer and rationale</summary>

**Correct answer: B — An IT dependency is restored, while minimum customer service is still unverified.**

Restoring order data fulfills only an IT dependency; production, batch clearance and physical dispatch remain unverified.

**Why the alternatives do not prevail:**

- **A.** System recovery is not end-to-end operational recovery.
- **C.** Other dependencies and targets remain open.
- **D.** A completed IT activity does not retire continuity governance.

</details>

## Completion and readiness checkpoint

**Readiness is demonstrated, not assumed.** A learner completing this section should independently:

- Reproduce the $45,000 analytical scenario EMV and explain its difference from the $44,561 seeded Monte Carlo sample mean.
- Reproduce the eligible hardening $28,600 and failover $37,700 annual comparisons, with a 12.14% switching probability.
- Distinguish approved operational capacity from quoted or conditional alternatives.
- Show at least one safety/quality/security hard gate that blocks a nominally cheaper response.
- Build an executable response record with event trigger, owners, evidence, RTO and dated retest.
- Explain how a supply-chain continuity program uses minimum service and dependencies rather than IT restoration alone.

**If any check fails:** revisit the linked detailed lessons, record what evidence is missing, and repeat the relevant calculation or response drill before attempting the integrated two-section capstone.

---

[Previous: Business Continuity and Partner Coordination](./19-business-continuity-management-recovery-and-partner-coordination.md) · [Section overview](./README.md) · [Module 7 overview](../README.md)
