---
description: "Loose governance achieves >99.7% capability across all task types while providing safety_proxy ≈ 0.015; near-zero cost for initial safety signal"
type: claim
status: active
confidence: medium
domain: governance
evidence:
  supporting:
  - run: 20260304_212912_frontier_trace
    metric: "capability ratio (loose/oracle)"
    detail: "50 seeds × 4 tasks. Loose capability: routing 1.000, coordination 0.997, allocation 1.000, long_horizon 1.000. Safety_proxy: 0.015 across all tasks. Capability loss <0.3% mean."
  weakening: []
  boundary_conditions:
  - "10-agent, 20% adversarial, single adversarial fraction tested"
  - "Loose config: audit_rate=0.05, no CB, no staking, no confirmation gates, bandwidth_cap=100"
  - "Safety_proxy value of 0.015 is very small — safety benefit may be negligible against sophisticated adversaries"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-governance-capability-cost-is-monotonic-and-task-universal
  relation: supports
- claim: claim-optimal-tax-range-0-to-5pct
  relation: supports
created: 2026-03-25
updated: 2026-03-25
aliases:
- loose-governance-costless-entry-point
cssclasses:
- claim
- claim-medium
tags:
- governance
- safety-proxy
- capability-preservation
- pareto-frontier
graph-group: claim
---

# Loose governance provides near-zero capability cost while establishing initial safety monitoring signal

## Evidence summary

At the loosest governance config (audit_rate=0.05, no CB, no staking, no confirmation gates, bandwidth_cap=100), capability remains >99.7% of oracle across all 4 task types:

| Task | Loose (% of oracle) | Safety_proxy |
|------|---------------------|--------------|
| Routing | 1.000 | 0.015 |
| Coordination | 0.997 | 0.015 |
| Allocation | 1.000 | 0.015 |
| Long_horizon | 1.000 | 0.015 |

This represents the "first rung" of the safety-capability Pareto frontier — a near-free entry point. Capability loss is <0.3% on average, with no task type exceeding 0.3% degradation. Safety_proxy is uniform at 0.015 across all tasks (vs 0.0 for oracle).

## Mechanism

Minimal audit (5%) and no active enforcement means agents are barely constrained. The safety signal comes from passive monitoring rather than active intervention. The low safety_proxy value suggests loose governance detects anomalies through audit sampling but does not meaningfully restrict adversarial behavior.

## Boundary & sensitivity

Only tested at 20% adversarial fraction. Loose governance may be insufficient at higher adversarial fractions. The safety_proxy value of 0.015 is on the edge of statistical noise — the actual defensive value against sophisticated adversaries is unclear.

## Open questions

1. Is the 0.015 safety_proxy meaningful for defense against adaptive adversaries?
2. At what adversarial fraction does loose governance fail to provide adequate safety?
3. Is there a "steeper" entry point (e.g., light governance) that provides substantially more safety (0.05+) for only 3-5% capability cost?
4. How does safety_proxy scale with adversarial fraction across the loose→light→moderate spectrum?

---

Topics:
- [[_index]]
- [[governance-dashboard]]

<!-- topics: governance, safety-proxy, capability-preservation, pareto-frontier -->
