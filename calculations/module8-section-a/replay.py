#!/usr/bin/env python3
"""Reproduce fictional Module 8 Section A calculations using checked-in CSVs."""
import csv,math
from pathlib import Path
D=Path(__file__).resolve().parents[2]/"assets/data/module-8/section-a"
def read(s):
    with (D/s).open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def ck(name,result,expected):
    if not math.isclose(result,expected,rel_tol=0,abs_tol=0.011):raise AssertionError(f"{name}: {result} != {expected}")
    print(f"PASS {name} = {result:.3f}")
def main():
    z=read("service-promise.csv")
    for a,e in zip(z,[73,93]):ck("order service %",100*int(a["on_time_orders"])/int(a["total_orders"]),e)
    for a,e in zip(read("competitive-contribution.csv"),[222000,181500]):
        ck("monthly contribution",int(a["units"])*(float(a["unit_price_usd"])-float(a["unit_variable_cost_usd"])),e)
    for a,e in zip(read("segment-variability.csv"),[.075,.6]):
        ck("CV",float(a["weekly_stddev_units"])/float(a["weekly_mean_units"]),e)
    a=read("business-plan-economics.csv")[0]
    ck("annual business contribution",float(a["incremental_revenue_usd"])-sum(float(a[k]) for k in ["variable_expense_usd","engineering_fixed_usd","technology_fixed_usd"]),54000)
    net=read("location-design-alternatives.csv")
    totals={a["option"]:sum(float(a[k]) for k in ["facility_cost_usd","transport_cost_usd","inventory_cost_usd","service_failure_cost_usd"]) for a in net}
    for k,e in [("central",625000),("regional",575000),("low-cost",520000)]:ck("annual network "+k,totals[k],e)
    feasible={a["option"]:int(a["weekly_capacity_units"])>=int(a["required_weekly_units"]) for a in net}
    assert feasible=={"central":True,"regional":True,"low-cost":False}
    assert min((totals[n],n) for n in totals if feasible[n])[1]=="regional"
    z=read("three-v-measures.csv")
    for a,e in zip(z,[70,92.5]):ck("visibility %",100*int(a["valid_events"])/int(a["total_orders"]),e)
    ck("velocity improvement %",100*(1-float(z[1]["order_to_update_hours"])/float(z[0]["order_to_update_hours"])),25)
    ck("variability reduction %",100*(1-float(z[1]["demand_cv"])/float(z[0]["demand_cv"])),37.5)
    s=read("stakeholder-economic-boundaries.csv")
    assert s[0]["stakeholder"]=="customer" and s[1]["stakeholder"]=="AlderGate"
    ck("customer separate benefit",float(s[0]["modeled_benefit_usd"]),180000)
    ck("firm separate expense",float(s[1]["incremental_company_cost_usd"]),95000)
    z=read("partner-service-pilot.csv")
    for a,e in zip(z,[88,95.5]):ck("complete order %",100*int(a["complete_on_time_orders"])/int(a["total_orders"]),e)
    ck("partner incremental model",float(z[1]["incremental_modeled_contribution_usd"])-float(z[1]["incremental_cost_usd"]),-8000)
    for a,e in zip(read("strategic-gap-cases.csv"),[88,91.25]):
        ck("gap case complete %",100*int(a["complete_on_time_orders"])/int(a["observed_orders"]),e)
    a,b=read("production-mix.csv")
    cand=[]
    for x in range(int(a["max_weekly_demand_units"])+1):
        for y in range(int(b["max_weekly_demand_units"])+1):
            hr=x*float(a["finishing_hours_per_unit"])+y*float(b["finishing_hours_per_unit"])
            if hr<=120:cand.append((x*float(a["contribution_usd_per_unit"])+y*float(b["contribution_usd_per_unit"]),x,y,hr))
    best=max(cand);assert best==(2150,40,10,120);ck("OR max contribution",best[0],2150)
    z=read("capital-investment-cash-flows.csv");rate=float(z[0]["discount_rate_annual"]);invest=-float(z[0]["net_cash_flow_usd"])
    pv=[float(r["net_cash_flow_usd"])/(1+rate)**int(r["year"]) for r in z[1:]]
    ck("simple payback",invest/float(z[1]["net_cash_flow_usd"]),3.6)
    ck("5-year NPV",sum(pv)-invest,9539.33847042)
    ck("discounted payback",4+(invest-sum(pv[:4]))/pv[4],4.692736)
    print("SECTION A CALCULATION REPLAY PASSED")
if __name__=="__main__":main()
