# 6. Digital Requirements and Information Latency

## Learning objectives

After this topic, you should be able to:

- derive information requirements from business decisions;
- distinguish data freshness from end-to-end decision latency;
- select batch, event, or real-time exchange based on value; and
- explain why more data does not automatically create better visibility.

## Concept in plain English

A digital requirement should state **which decision must improve, which information is needed, how quickly it must arrive, how reliable it must be, and who acts on it**.

“We need real-time visibility” is incomplete. A stronger requirement is: “When a critical European shipment misses a carrier milestone by more than two hours, notify the order owner within fifteen minutes with the affected customer promise and approved recovery options.”

## Decision-to-data method

```mermaid
flowchart TD
    A[Business decision] --> B[Required facts]
    B --> C[Source and owner]
    C --> D[Freshness and quality]
    D --> E[Trigger and workflow]
    E --> F[Action and outcome]
```

## Four clocks

| Clock | Meaning | Example |
|---|---|---|
| Event time | when the physical event occurred | truck departed at 10:04 |
| Capture time | when the event was recorded | scan completed at 10:07 |
| Availability time | when the event reached the consuming system | message posted at 10:09 |
| Action time | when an accountable person or automation responded | recovery booked at 10:25 |

End-to-end decision latency is the time from event to useful action. Improving only message transmission may have little value if events are captured late or exceptions wait in an unowned queue.

## Choosing an update pattern

| Pattern | Best fit | Example |
|---|---|---|
| Scheduled batch | stable decisions with longer horizons | nightly supplier master synchronization |
| Frequent micro-batch | aggregated operational planning | inventory refresh every fifteen minutes |
| Event-driven | time-sensitive state change | shipment departure or quality hold |
| Request-response | information needed at a decision point | delivery-promise check during order entry |

Real time has cost: interfaces, monitoring, message volume, support, cybersecurity, and data-correction complexity. Use it where decision value decays quickly.

## AsterWorks example

AsterWorks initially asks for live inventory from every supplier. Analysis shows three different decisions:

- strategic capacity review needs a monthly certified view;
- replenishment planning needs daily available inventory;
- a production-stop component needs an event when supply falls below a protected threshold.

One universal frequency would either overspend on low-value data or under-serve a critical decision.

## Information requirement card

For each high-value decision, document:

- decision owner;
- business event or review cadence;
- required data elements and definitions;
- source and authoritative owner;
- maximum acceptable age;
- completeness and accuracy threshold;
- exception trigger;
- response deadline; and
- fallback when data are missing.

## Common mistakes

- Starting with a preferred technology rather than a decision.
- Treating a dashboard as visibility even when no action follows.
- Using “real time” without defining seconds, minutes, or hours.
- Ignoring event-time and time-zone semantics.
- Sharing all available data instead of the minimum useful and permitted data.

## Practitioner perspective

Design information around exceptions and decisions, not around every possible field. High-value visibility is selective: it makes the material change obvious, connects it to impact, and routes it to someone who can act.

## Original knowledge check

A carrier sends status messages within seconds, but warehouse departure scans are entered four hours late. Has real-time integration solved the visibility problem?

<details><summary>Answer</summary>

**No.** Transmission is fast, but capture latency keeps the information stale. End-to-end latency must be measured from the physical event to the decision or action.
</details>

## Related concepts

Continue to [technology business case and total cost](07-technology-business-case-and-tco.md).
