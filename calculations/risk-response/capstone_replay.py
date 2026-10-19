#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reproduce Stonebridge Module 7 capstone arithmetic from fictional CSV inputs.

Training-only validation: does not measure actual event probabilities or prove readiness.
Usage: python3 calculations/risk-response/capstone_replay.py
"""
from __future__ import annotations

import csv
import json
import random
import statistics
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "assets" / "data" / "module-7"


def rows(filename: str) -> list[dict[str, str]]:
    with (DATA / filename).open(encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def dec(x: str | int | float) -> Decimal:
    return Decimal(str(x))


def assert_eq(observed, expected, label: str) -> None:
    if observed != expected:
        raise AssertionError(f"{label}: observed={observed}, expected={expected}")


def main() -> None:
    result: dict[str, object] = {"case": "Stonebridge Module 7 fictional integrated capstone"}

    ratings = rows("qualitative-risk-ratings.csv")
    scores = {r["risk_id"]: int(r["likelihood_1_to_5"]) * int(r["consequence_1_to_5"]) for r in ratings}
    for r in ratings:
        assert_eq(scores[r["risk_id"]], int(r["product_score"]), "qualitative source score")
    assert_eq(scores, {"R7-11": 16, "R7-12": 15, "R7-13": 10, "R7-14": 12}, "all risk scores")
    result["qualitative_scores"] = scores

    lane = rows("emv-outcome-scenarios.csv")
    assert all(r["analysis_horizon"] == "1 year" for r in lane)
    probability_sum = sum((dec(r["probability"]) for r in lane), Decimal(0))
    assert_eq(probability_sum, Decimal("1.00"), "mutually exclusive lane probability sum")
    signed_emv = sum((dec(r["probability"]) * dec(r["conditional_operating_impact_usd"]) for r in lane), Decimal(0))
    assert_eq(signed_emv, Decimal(-45000), "lane signed EMV")
    result["lane_signed_emv_usd"] = int(signed_emv)
    result["lane_positive_expected_loss_usd"] = int(-signed_emv)

    opts = rows("emv-response-options.csv")
    control_costs = {r["option_id"]: dec(r["certain_annual_cost_usd"]) + dec(r["annual_probability"]) * dec(r["conditional_loss_usd"]) for r in opts}
    assert_eq(control_costs, {"BASE": 46800, "PATCH": 28600, "FAILOVER": 37700, "INSURE": 23400}, "base access-control arithmetic")
    eligible = [r for r in opts if r["security_gate_pass"] == "yes" and r["insurance_coverage_gate_pass"] == "yes" and dec(r["annual_probability"]) <= Decimal("0.10")]
    assert_eq({r["option_id"] for r in eligible}, {"PATCH", "FAILOVER"}, "technical eligibility")
    recommended = min(eligible, key=lambda r: control_costs[r["option_id"]])["option_id"]
    assert_eq(recommended, "PATCH", "lowest gated option")
    result["access_control_cost_usd_per_year"] = {k: int(v) for k, v in control_costs.items()}
    result["technically_eligible_access_options"] = sorted(r["option_id"] for r in eligible)
    result["preferred_gated_annual_option"] = recommended
    result["patch_difference_vs_ineligible_base_usd"] = int(control_costs["BASE"]-control_costs["PATCH"])
    result["patch_difference_vs_failover_usd"] = int(control_costs["FAILOVER"]-control_costs["PATCH"])

    sensitivity = rows("risk-sensitivity-cases.csv")
    stress = next(r for r in sensitivity if r["option"] == "Monitored_hardening_degraded")
    stress_cost = dec(stress["annual_certain_cost_usd"]) + dec(stress["assumed_event_probability"]) * dec(stress["conditional_loss_usd"])
    assert_eq(stress_cost, Decimal(48400), "hardening stress annual cost")
    assert_eq(dec(stress["expected_annual_cost_usd"]), stress_cost, "hardening source stress arithmetic")
    assert_eq(stress["hard_gate"], "fail", "hardening degraded hard gate consistency")
    crossover = (control_costs["FAILOVER"] - dec(next(r for r in opts if r["option_id"] == "PATCH")["certain_annual_cost_usd"])) / dec(next(r for r in opts if r["option_id"] == "PATCH")["conditional_loss_usd"])
    assert_eq(crossover, Decimal(26700)/Decimal(220000), "cost crossover")
    result["hardening_stress_expected_annual_cost_usd"] = int(stress_cost)
    result["hardening_cost_indifference_probability"] = round(float(crossover), 8)
    result["binding_probability_security_gate"] = 0.10

    sim = rows("risk-simulation-spec.csv")[0]
    rng = random.Random(int(sim["seed"]))
    counts = {0: 0, int(sim["moderate_loss_usd"]): 0, int(sim["severe_loss_usd"]): 0}
    sample = []
    n1 = float(sim["p_no_disruption"])
    n2 = n1 + float(sim["p_moderate"])
    for _ in range(int(sim["draws"])):
        u = rng.random()
        loss = 0 if u < n1 else int(sim["moderate_loss_usd"]) if u < n2 else int(sim["severe_loss_usd"])
        counts[loss] += 1
        sample.append(loss)
    assert_eq(counts, {0: 6540, 80000: 2467, 250000: 993}, "simulation counts")
    assert_eq(statistics.mean(sample), 44561, "simulation mean")
    result["simulation_draws_and_mean"] = {"draws":len(sample), "counts":{str(k):v for k,v in counts.items()},"mean_loss_usd":statistics.mean(sample)}

    suppliers = rows("supply-continuity.csv")
    apex = next(r for r in suppliers if r["supplier"] == "Apex_Micro")
    nova = next(r for r in suppliers if r["supplier"] == "Nova_Circuits")
    qty = int(apex["weekly_demand_units"])
    opening = int(apex["available_usable_stock_units"])
    weeks_cover = dec(opening)/dec(qty)
    assert_eq(weeks_cover, Decimal(2), "usable stock cover")
    assert_eq(int(nova["qualification_days"]), 14, "conditional qualification lead")
    total_short_approved=total_short_rejected=0
    inventory=opening
    schedule=[]
    for week in range(1,5):
        used=min(inventory,qty)
        inventory-=used
        conditional_supply=int(nova["alternative_units_week"]) if week>=3 else 0
        gap_if_approved=max(0,qty-used-conditional_supply)
        gap_if_rejected=max(0,qty-used)
        total_short_approved+=gap_if_approved
        total_short_rejected+=gap_if_rejected
        schedule.append({"week":week,"demand":qty,"approved_stock_used":used,"conditional_nova":conditional_supply,"gap_if_quality_pass":gap_if_approved,"gap_if_no_pass":gap_if_rejected})
    assert_eq((total_short_approved,total_short_rejected),(80,240),"four-week CT7 alternate scenario")
    result["ct7_weeks_of_approved_cover"] = int(weeks_cover)
    result["ct7_four_week_supply_stress"] = schedule
    result["ct7_shortfall_with_day14_nova_approval"] = total_short_approved
    result["ct7_shortfall_without_nova_approval"] = total_short_rejected

    routes = rows("environmental-route-continuity.csv")
    nodes = rows("network-exposure.csv")
    primary = next(r for r in routes if r["lane"] == "Primary_River_Road")
    alternate = next(r for r in routes if r["lane"] == "Eastgate_Alternate")
    eastgate = next(r for r in nodes if r["node"] == "Eastgate_Hub")
    primary_units=int(primary["potential_capacity_week"])
    nominated_alternate=int(alternate["potential_capacity_week"])
    site_cap=int(eastgate["alternate_capacity_units_week"])
    assert_eq((primary_units,site_cap,nominated_alternate),(800,450,400),"site vs lane capacity")
    result["outbound_gap_without_carrier_approval_units_week"] = primary_units
    result["outbound_gap_after_carrier_approval_units_week"] = primary_units-min(site_cap,nominated_alternate)
    assert_eq(result["outbound_gap_after_carrier_approval_units_week"],400,"lane gap")

    demand=next(r for r in rows("demand-risk-scenarios.csv") if r["case"]=="Upside")
    short=max(0,int(demand["confirmed_demand_units"])-int(demand["available_weekly_capacity_units"])-int(demand["reliable_substitute_units"]))
    assert_eq(short,int(demand["shortfall_units"]),"OEM upside gap")
    assert_eq(short,100,"OEM upside exact gap")
    result["separate_oem_weekly_gap_units"] = short

    policy=next(r for r in rows("risk-appetite-policy.csv") if r["exposure_id"]=="SB-P03")
    cap=int(policy["hard_threshold"].replace("USD","").strip())
    planned=rows("risk-funding-plan.csv")
    planned_fixed=sum(int(r["amount_usd"]) for r in planned if r["type"]=="planned preventive")
    reserve=sum(int(r["amount_usd"]) for r in planned if "reserve" in r["type"])
    patch=int(next(r for r in opts if r["option_id"]=="PATCH")["certain_annual_cost_usd"])
    full=planned_fixed+patch
    staged=patch+7500
    assert_eq((cap,planned_fixed,reserve,full,staged,full-cap,cap-staged), (25000,25500,40000,36500,18500,11500,6500), "portfolio funding gate")
    result["budget_and_reserve_usd"] = {"combined_cap":cap,"portfolio_requested":full,"excess_requires_exception":full-cap,"stage_one_requested":staged,"unused_cap_after_stage_one":cap-staged,"incident_reserve_not_general_funding":reserve}

    fx=next(r for r in rows("financial-risk-controls.csv") if r["case"]=="FX_payable")
    metal=next(r for r in rows("financial-risk-controls.csv") if r["case"]=="Commodity_contract")
    fx_diff=dec(fx["exposure"])*(dec(fx["stress_value"])-dec(fx["base_value"]))
    material_diff=dec(metal["exposure"])*(dec(metal["stress_value"])-dec(metal["base_value"]))
    assert_eq((fx_diff,material_diff),(Decimal(56000),Decimal(25000)),"financial stress")
    result["financial_stress_usd_not_annual_emv"]={"fx_payable":int(fx_diff),"material_lot":int(material_diff)}

    bcms=rows("business-continuity-dependencies.csv")
    assert_eq(len(bcms),5,"five continuity recovery paths")
    assert all(int(r["estimated_recovery_hours"])<=int(r["recovery_target_hours"]) for r in bcms)
    dr=rows("crisis-exercise-actions.csv")
    failures=[r for r in dr if int(r["observed_minutes"])>int(r["target_minutes"])]
    assert_eq((len(failures),len(dr)),(2,3),"exercise failure count")
    assert_eq(sorted(int(r["observed_minutes"])-int(r["target_minutes"]) for r in failures),[4,40],"exercise gap")
    assert all(r["next_test"]=="2026-11-15" for r in failures)
    result["bcms_estimated_target_rows_within_limits"] = len(bcms)
    result["observed_exercise_failure_minutes"]={r["inject"]:int(r["observed_minutes"])-int(r["target_minutes"]) for r in failures}
    result["verified_end_to_end_continuity"] = False
    result["calculation_assertions"] = "PASS"
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__ == "__main__":
    main()
