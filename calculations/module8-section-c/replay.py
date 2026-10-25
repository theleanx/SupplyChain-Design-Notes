#!/usr/bin/env python3
"""Independent Module 8 Section C replay from original, fictional lesson CSV inputs."""
from __future__ import annotations
import csv, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"assets/data/module-8/section-c"

def load(name):
    with (DATA/name).open(newline="",encoding="utf-8") as f:
        return list(csv.DictReader(f))

def check(label,actual,expected,tol=0.025):
    if not math.isclose(float(actual),float(expected),rel_tol=0,abs_tol=tol):
        raise AssertionError(f"{label}: actual={actual} expected={expected}")
    print(f"PASS {label} = {float(actual):.4f}")

def main():
    cloud={x["option"]:x for x in load("cloud-comparison.csv")}
    for key,result in [("SaaS",405000),("OnPrem",468000)]:
        r=cloud[key]
        recurring=sum(float(r[x]) for x in ("annual_subscription_usd","annual_internal_support_usd","annual_connectivity_usd"))
        check("3-year "+key,3*recurring+float(r["one_time_setup_usd"]),result)

    ai={(r["actual"],r["predicted"]):int(r["count"]) for r in load("ai-failure-detection.csv")}
    TP=ai["failure","alert"];FN=ai["failure","no_alert"];FP=ai["no_failure","alert"];TN=ai["no_failure","no_alert"]
    check("failure recall %",100*TP/(TP+FN),90)
    check("alert precision %",100*TP/(TP+FP),37.5)
    check("failure model accuracy %",100*(TP+TN)/(TP+TN+FP+FN),84)

    ev=load("tower-event-pilot.csv")
    for r,match,action in zip(ev,(70,94),(45,82)):
        check("tower linked %",100*int(r["events_linked_to_orders"])/int(r["events_received"]),match)
        check("tower actioned %",100*int(r["events_actioned_on_time"])/int(r["events_received"]),action)

    options={x["option"]:x for x in load("emerging-options.csv")}
    assert options["unqualified_print"]["qualified"]=="no"
    assert all(options[k]["qualified"]=="yes" for k in ("approved_supplier","stock_buffer"))
    check("stock buffer recurring USD",float(options["stock_buffer"]["annual_running_usd"]),59000)
    check("approved supplier response days",float(options["approved_supplier"]["response_days"]),4)

    assets=load("asset-condition.csv")
    for r,exp in zip(assets,(7,3.75)):
        check("unplanned downtime %",100*int(r["unplanned_down_hours"])/int(r["scheduled_hours"]),exp)
    check("connected asset %",100*int(assets[1]["connected_assets"])/int(assets[1]["total_assets"]),80)

    led=load("custody-events.csv")
    for r,rec in zip(led,(92,99)):
        check("custody captured %",100*int(r["events_recorded"])/int(r["events_expected"]),rec)
    check("pilot physically verified %",100*int(led[1]["physical_events_verified"])/int(led[1]["events_expected"]),96)

    road=load("technology-roadmap.csv")
    eligible=sum(float(r["modeled_annual_saving_usd"]) for r in road if r["prerequisite_verified"]=="yes")
    check("eligible roadmap yearly savings USD",eligible,64000)
    assert any(r["prerequisite_verified"]=="no" for r in road)

    audit=load("technology-audit.csv")
    check("audit closure %",100*sum(int(r["verified_closed"]) for r in audit)/sum(int(r["findings"]) for r in audit),75)
    assert sum(int(r["critical_open"]) for r in audit)==1

    req={r["requirement"]:r for r in load("requirement-results.csv")}
    for name,expected in (("priority_order_visibility",96),("supplier_confirmation",82)):
        r=req[name]
        check(name+" acceptance %",100*int(r["events_meeting_target"])/int(r["events"]),expected)
    assert 96>=int(req["priority_order_visibility"]["target_pct"])
    assert 82<int(req["supplier_confirmation"]["target_pct"])

    gaps={r["capability"]:r for r in load("technology-readiness-gaps.csv")}
    assert float(gaps["trained_user_access"]["pilot_score"])<float(gaps["trained_user_access"]["target_score"])
    assert all(float(gaps[k]["pilot_score"])>=float(gaps[k]["target_score"]) for k in ("material_identity","reporting_refresh"))
    print("PASS readiness gap: mandatory trained user access still failing")

    vendors={r["vendor"]:r for r in load("technology-selection.csv")}
    eligible_v=[r for r in vendors.values() if r["data_security_gate"]=="yes" and r["response_time_gate"]=="yes"]
    assert {r["vendor"] for r in eligible_v}=={"A","B"}
    assert max(eligible_v,key=lambda r:float(r["weighted_score"]))["vendor"]=="B"
    check("qualified vendor B annual cost USD",float(vendors["B"]["annual_cost_usd"]),84000)

    cutover=load("cutover-acceptance.csv")
    check("cutover test passed %",100*sum(int(r["passed"]) for r in cutover)/sum(int(r["tests"]) for r in cutover),95)
    assert sum(int(r["blocking_remaining"]) for r in cutover)==2
    print("PASS cutover critical gate: blocked until defects corrected")

    raci=load("raci-handoffs.csv")
    assert len(raci)==3 and all(int(r["accountable_people"])==1 for r in raci)
    print("PASS fictional RACI: one accountable owner for each of three deliverables")

    tasks={r["task"]:r for r in load("project-dependencies.csv")}
    check("critical project path days",sum(int(tasks[k]["duration_days"]) for k in ("identity_mapping","integration_test","operational_acceptance")),17)
    assert int(tasks["hardware_ready"]["duration_days"])==6

    iterations={r["release"]:r for r in load("iteration-readiness.csv")}
    for k,v in (("iteration_2",100*10/12),("iteration_3",90)):
        r=iterations[k]
        check("accepted features "+k,100*int(r["accepted_features"])/int(r["planned_features"]),v)
    assert int(iterations["iteration_3"]["critical_defects_open"])==1

    change=load("change-coalition.csv")
    population=sum(int(r["affected_workers"]) for r in change)
    check("change trained %",100*sum(int(r["trained_workers"]) for r in change)/population,90)
    check("change active users %",100*sum(int(r["active_process_users"]) for r in change)/population,67)

    adoption=load("adoption-outcomes.csv")
    for r,ad,correct in zip(adoption,(85,50),(82,44.5)):
        total=int(r["eligible_transactions"])
        check(r["site"]+" process adoption %",100*int(r["transactions_new_process"])/total,ad)
        check(r["site"]+" correct outcome %",100*int(r["transactions_with_correct_outcomes"])/total,correct)

    m=load("technology-maintenance.csv")
    before=sum(int(m[0][k]) for k in ("planned_maintenance_hours","unplanned_downtime_hours"))
    after=sum(int(m[1][k]) for k in ("planned_maintenance_hours","unplanned_downtime_hours"))
    check("maintenance and downtime before hours",before,135)
    check("maintenance and downtime after hours",after,103)
    check("modeled net hours reduction",before-after,32)
    print("MODULE 8 SECTION C INDEPENDENT CALCULATION REPLAY PASSED")

if __name__=="__main__":main()
