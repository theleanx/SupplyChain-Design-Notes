#!/usr/bin/env python3
"""Independently replay fictional CSCP Module 8 Section B sustainability examples."""
from pathlib import Path
import csv, math

D=Path(__file__).resolve().parents[2]/"assets/data/module-8/section-b"

def rows(filename):
    with (D/filename).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def check(label,actual,expected,tol=0.02):
    if not math.isclose(float(actual),float(expected),abs_tol=tol,rel_tol=0):
        raise AssertionError(f"{label}: actual={actual} expected={expected}")
    print(f"PASS {label}: {actual:.4f}")

def main():
    tbl={r["measure"]:float(r["value"]) for r in rows("tbl-baseline.csv")}
    check("TBL operating contribution USD",tbl["operating_revenue"]-tbl["operating_expense"],400000)
    assert tbl["electricity"]==1200 and tbl["recorded_safety_events"]==6

    horizon=rows("horizon-economics.csv")[0]
    gross=float(horizon["annual_net_benefit_usd"])*int(horizon["years"])
    check("nominal lifetime delta USD",gross-float(horizon["upfront_program_cost_usd"]),175000)

    freight=rows("freight-environment.csv")
    values=[]
    for r in freight:
        co2e=float(r["shipments"])*float(r["tonnes_per_shipment"])*float(r["km_per_shipment"])*float(r["fictional_kg_co2e_per_tonne_km"])
        values.append(co2e)
    check("baseline freight kg CO2e",values[0],1860)
    check("alternative freight kg CO2e",values[1],1200)
    check("modeled freight reduction kg CO2e",values[0]-values[1],660)
    check("cost per kg avoided USD",float(freight[1]["incremental_transport_cost_usd"])/(values[0]-values[1]),11.363636)

    labor=rows("social-remediation.csv")
    for r,expect in zip(labor,[8/12*100,90]):
        check("closed cohort fraction percent",100*float(r["issues_verified_closed"])/float(r["issues_reported"]),expect)

    lanes=rows("compliance-gate-register.csv")
    check("fictional eligible lanes pct",100*sum(r["shipment_eligible"]=="yes" for r in lanes)/len(lanes),75)
    assert next(r for r in lanes if r["route"]=="L2")["shipment_eligible"]=="no"

    mineral=rows("responsible-minerals-screen.csv")[0]
    check("parts with sufficient documentation pct",100*int(mineral["parts_with_sufficient_documentation"])/int(mineral["parts_screened"]),91.6666667)
    assert int(mineral["parts_pending"])==10

    ungc=rows("ungc-principles.csv")
    assert sum(int(r["principles"]) for r in ungc)==10
    check("UNGC internal evidence coverage pct",100*sum(int(r["evidenced_controls"]) for r in ungc)/sum(int(r["expected_controls"]) for r in ungc),80)

    oecd=rows("oecd-diligence.csv")[0]
    check("fictional adverse-impact signals pct",100*int(oecd["adverse_impact_signals"])/int(oecd["reviewed_suppliers"]),24)
    assert int(oecd["corrective_actions_open"])==5

    gri=rows("gri-disclosure-evidence.csv")
    check("GRI-related internal records coverage pct",100*sum(int(r["verified_records"]) for r in gri)/sum(int(r["required_records"]) for r in gri),85.7142857)

    iso=rows("iso-scope-example.csv")
    ready=[r for r in iso if r["site_in_scope"]=="yes" and r["qualification_status"]=="valid_illustrative"]
    check("fictional ISO claim immediately usable pct",100*len(ready)/len(iso),33.3333333)

    claims=rows("assurance-claims.csv")
    assert len(claims)==3
    assert all(r["review_state"] not in ("valid","approved") for r in claims)
    print("PASS assurance claims: zero accepted without review")

    recycling=rows("recycling-lineage.csv")
    for r,expected in zip(recycling,[70,60]):
        check("site recycling percent",100*float(r["verified_recycled_kg"])/float(r["eligible_kg"]),expected)
    network=100*sum(float(r["verified_recycled_kg"]) for r in recycling)/sum(float(r["eligible_kg"]) for r in recycling)
    check("weighted network recycling percent",network,66)
    assert sum(int(r["source_exceptions"]) for r in recycling)==2
    print("MODULE 8 SECTION B INDEPENDENT REPLAY PASSED")

if __name__=="__main__":
    main()
