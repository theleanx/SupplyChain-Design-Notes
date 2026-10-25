#!/usr/bin/env python3
"""Independent AlderGate (fictional) Module 8 capstone replay from committed input CSVs.

Read existing Module 8 Sections A/B/C datasets alongside additional capstone policy,
sustainability and cost inputs. The input figures are teaching assumptions, not actual
measured company financials, supplier evidence, a legal determination, or certification.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "assets" / "data" / "module-8"


def read(subpath: str) -> list[dict[str, str]]:
    file = DATA / subpath
    with file.open(newline="", encoding="utf-8") as handle:
        result = list(csv.DictReader(handle))
    assert result, f"empty required input: {subpath}"
    return result


def expect(label: str, actual: float, target: float, tol: float = 0.035) -> None:
    if not math.isclose(float(actual), float(target), rel_tol=0, abs_tol=tol):
        raise AssertionError(f"{label}: actual={actual} expected={target}")
    print(f"PASS {label}: {actual:,.4f}")


def truth(value: str) -> bool:
    if value not in ("yes", "no"):
        raise AssertionError(f"Expected yes/no, got {value!r}")
    return value == "yes"


def main() -> None:
    policy = {r["parameter"]: r["value"] for r in read("capstone/executive-policy.csv")}
    weekly = int(policy["required_weekly_units"])
    stress = int(policy["demand_stress_weekly_units"])
    weeks = int(policy["weeks_per_year"])
    horizon = int(policy["evaluation_years"])
    discount = float(policy["annual_discount_rate"])
    target_co2 = float(policy["aspirational_emissions_target"])
    f_base = float(policy["benefit_realization_base"])
    expect("annual modeled units", weekly * weeks, 52000)
    assert (weekly, stress, horizon, discount) == (1000, 1200, 5, 0.10)

    networks = {r["option"]: r for r in read("section-a/location-design-alternatives.csv")}
    footprint = {r["option"]: r for r in read("capstone/network-sustainability.csv")}
    assert set(networks) == set(footprint) == {"central", "regional", "low-cost"}
    net_cost = {}
    pass_base = {}
    for key, r in networks.items():
        assert int(r["required_weekly_units"]) == weekly, f"{key}: distinct demand pool"
        net_cost[key] = sum(float(r[c]) for c in
                            ("facility_cost_usd", "transport_cost_usd", "inventory_cost_usd", "service_failure_cost_usd"))
        slack = int(r["weekly_capacity_units"]) - weekly
        f = footprint[key]
        pass_base[key] = slack >= 0 and truth(f["worker_safety_gate"]) and truth(f["destination_evidence_gate"])
        print(f"SCREEN {key}: annual network USD {net_cost[key]:,.0f}; slack {slack:+d} units/week; eligible {pass_base[key]}")
    for key, amount in (("central", 625000), ("regional", 575000), ("low-cost", 520000)):
        expect("network "+key, net_cost[key], amount)
    assert pass_base == {"central": True, "regional": True, "low-cost": False}
    selected = min((net_cost[k], k) for k in networks if pass_base[k])[1]
    assert selected == policy["target_network"] == "regional"
    network_avoided = net_cost[policy["baseline_network"]] - net_cost[selected]
    expect("eligible network annual saving USD", network_avoided, 50000)

    emissions = {}
    for key, f in footprint.items():
        emissions[key] = float(f["warehouse_energy_tco2e_year"]) + float(f["outbound_transport_tco2e_year"])
    for key, t in (("central", 139), ("regional", 109), ("low-cost", 101)):
        expect("scoped CO2e tonnes "+key, emissions[key], t)
    assert emissions[selected] <= target_co2 < emissions["central"]
    expect("scoped emissions reduction t", emissions["central"] - emissions[selected], 30)
    expect("scoped emissions reduction %", 100*(emissions["central"]-emissions[selected])/emissions["central"], 21.58273381295)

    waste = read("section-b/recycling-lineage.csv")
    assert {r["site"] for r in waste} == {"Plant_A", "Plant_B"}
    total_eligible = sum(float(r["eligible_kg"]) for r in waste)
    total_recycled = sum(float(r["verified_recycled_kg"]) for r in waste)
    for r in waste:
        expect("site recycling % "+r["site"],
               100*float(r["verified_recycled_kg"])/float(r["eligible_kg"]),
               {"Plant_A":70,"Plant_B":60}[r["site"]])
    expect("mass-weighted recycling %",100*total_recycled/total_eligible,66)
    assert sum(int(r["source_exceptions"]) for r in waste) == 2, "public claim evidence mismatch"

    vendors = {r["vendor"]: r for r in read("section-c/technology-selection.csv")}
    costs = read("capstone/program-costs.csv")
    upfront = sum(float(r["amount_usd"]) for r in costs if r["timing"] == "at_t0")
    new_support = sum(float(r["amount_usd"]) for r in costs if r["timing"] == "annual_years_1_to_5")
    assert len(costs) == 4 and len([r for r in costs if r["timing"] == "at_t0"]) == 3
    expect("t0 program capital USD", upfront, 185000)
    expect("annual incremental support USD", new_support, 24000)
    assert upfront <= float(policy["capital_limit"])
    eligible_vendors = {}
    for key, r in vendors.items():
        gates = truth(r["data_security_gate"]) and truth(r["response_time_gate"])
        added_annual = float(r["annual_cost_usd"]) + new_support
        eligible_vendors[key] = gates and added_annual <= float(policy["annual_incremental_technology_limit"])
        print(f"SCREEN vendor {key}: annual tech USD {added_annual:,.0f}, technical gates {gates}, eligible {eligible_vendors[key]}")
    assert eligible_vendors == {"A":False, "B":True, "C":False}
    selected_vendor = policy["preferred_technology_vendor"]
    assert selected_vendor == "B" and eligible_vendors[selected_vendor]
    new_tech_annual = float(vendors[selected_vendor]["annual_cost_usd"]) + new_support
    expect("chosen new annual technology USD",new_tech_annual,108000)
    assert new_tech_annual <= float(policy["annual_incremental_technology_limit"])

    benefit_rows = read("capstone/manual-work-benefits.csv")
    assert len(benefit_rows) == 2
    assert {r["overlap_rule"] for r in benefit_rows} == {"exclusive_event_population","exclusive_invoice_population"}
    assert all(r["confirmed_cash_avoidability"] == "pending_finance_verification" for r in benefit_rows)
    benefits = {r["workstream"]:float(r["annual_distinct_cases"])*float(r["hours_avoided_per_case"])*
                                float(r["avoidable_cash_cost_usd_per_hour"]) for r in benefit_rows}
    expect("manual event saving potential USD",benefits["order_event_reconciliation"],105000)
    expect("invoice saving potential USD",benefits["invoice_dispute_resolution"],50000)
    potential = sum(benefits.values())
    expect("maximum process potential USD",potential,155000)

    base_annual = net_cost[policy["baseline_network"]] + potential
    proposed_fixed_annual = net_cost[selected] + new_tech_annual
    expect("baseline combined annual USD",base_annual,780000)
    expect("proposed fixed annual before remaining manual expense USD",proposed_fixed_annual,683000)
    check_net = lambda fraction: network_avoided + potential*fraction - new_tech_annual
    expect("realization base fraction",f_base,0.75)
    expect("base fraction annual net saving USD",check_net(f_base),58250)
    proposed_annual = proposed_fixed_annual + potential*(1-f_base)
    expect("proposed annual USD at 75% cash realization",proposed_annual,721750)
    expect("accounting identity: delta vs baseline",base_annual-proposed_annual,check_net(f_base))

    factor = sum((1+discount)**(-year) for year in range(1,horizon+1))
    expect("five-year present value annuity factor",factor,3.7907867694084474,1e-8)
    NPV = lambda fraction: -upfront + check_net(fraction)*factor
    payback = upfront/check_net(f_base)
    expect("base 75% NPV USD",NPV(f_base),35813.32931804)
    expect("base undiscounted simple payback years",payback,3.17596566523605,1e-8)

    sensitivity = read("capstone/benefit-sensitivity.csv")
    expected = {
        "downside":(.60,35000,-52322.46307070),
        "observed_training_pilot_proxy":(.67,45850,-11192.42662262),
        "gated_minimum":(.75,58250,35813.32931804),
        "full_assumption":(1.00,97000,182706.31663262),
    }
    assert set(x["scenario"] for x in sensitivity) == set(expected)
    for scenario in sensitivity:
        title=scenario["scenario"]
        assumed, annual, npv=expected[title]
        fraction=float(scenario["benefit_realization_fraction"])
        expect(title+" benefit realization ratio",fraction,assumed,1e-8)
        expect(title+" annual benefit USD",check_net(fraction),annual)
        expect(title+" NPV USD",NPV(fraction),npv)
    crossover = (upfront/factor - network_avoided + new_tech_annual)/potential
    expect("financial break-even fraction",crossover,0.6890486061098574,1e-10)
    assert crossover < float(policy["minimum_active_adoption_ratio"])
    # Financial crossover is NOT a validated relationship from worker adoption to savings.

    change = read("section-c/change-coalition.csv")
    total_workers = sum(int(r["affected_workers"]) for r in change)
    trained = sum(int(r["trained_workers"]) for r in change)
    active = sum(int(r["active_process_users"]) for r in change)
    expect("change training %",100*trained/total_workers,90)
    expect("change actual active use %",100*active/total_workers,67)
    assert total_workers == 200 and trained/total_workers >= float(policy["minimum_worker_training_ratio"])
    assert active/total_workers < float(policy["minimum_active_adoption_ratio"])
    expect("additional active people to meet 75 percent",math.ceil(float(policy["minimum_active_adoption_ratio"])*total_workers)-active,16)
    cuts = read("section-c/cutover-acceptance.csv")
    expect("cutover total pass %",100*sum(int(r["passed"]) for r in cuts)/sum(int(r["tests"]) for r in cuts),95)
    remaining = sum(int(r["blocking_remaining"]) for r in cuts)
    assert remaining == 2 > int(policy["maximum_critical_cutover_failures"])
    print("HARD GATES: full automated cutover blocked; recycling public claim unverified; cash avoidability pending")

    # This is a separate stress. Current base annual cost/emissions cannot be carried forward.
    for key,r in networks.items():
        delta = int(r["weekly_capacity_units"])-stress
        expect("stress slack "+key,delta,{"central":0,"regional":-100,"low-cost":-350}[key])
    partial_stress_annual = potential*f_base-new_tech_annual # removes ONLY network saving
    partial_stress_npv = -upfront+partial_stress_annual*factor
    expect("partial loss-of-network-savings annual USD",partial_stress_annual,8250)
    expect("partial loss-of-network-savings NPV USD",partial_stress_npv,-153726.00915238)

    risks = read("capstone/governance-actions.csv")
    assert len(risks)==8 and len(set(r["risk_id"] for r in risks))==8
    assert set(r["review_by_day"] for r in risks) <= {"15","30","45","60","90"}
    print("PASS owner/action register: 8 unique risks, dated triggers and owners")
    print("MODULE 8 INTEGRATED ALDERGATE CAPSTONE REPLAY PASSED")
    print("DECISION: conditional design/read-only pilot ONLY; NOT full production cutover or verified sustainability disclosure")


if __name__ == "__main__":
    main()
