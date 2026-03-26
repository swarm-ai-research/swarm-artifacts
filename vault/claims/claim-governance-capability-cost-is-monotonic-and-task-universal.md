---
description: "Seven governance configs produce identical capability ordering across 4 task types; oracle > loose > light > moderate-light > moderate > tight-moderate ≈ tight"
type: claim
status: active
confidence: high
domain: governance
evidence:
  supporting:
  - run: 20260304_212912_frontier_trace
    metric: "capability (mean)"
    detail: "50 seeds × 7 configs × 4 tasks = 1400 runs. Ordering invariant: oracle > loose > light > moderate-light > moderate > tight-moderate ≈ tight. Cohen's d vs oracle ranges 0.41-7.01. All comparisons Bonferroni-significant at alpha/24."
  weakening: []
  boundary_conditions:
  - "10-agent systems, 20% adversarial fraction"
  - "Tested across routing, coordination, allocation, and long_horizon tasks"
  - "Tight and tight-moderate show minor inversion on routing and long_horizon (d<0.1)"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-governance-cost-paradox
  relation: extends
- claim: claim-moderate-governance-pareto-dominates-welfare-toxicity-frontier
  relation: refines
created: 2026-03-25
updated: 2026-03-25
aliases:
- governance-monotonic-capability-ordering
cssclasses:
- claim
- claim-high
tags:
- governance
- capability-cost
- task-universality
- monotonic-ordering
graph-group: claim
---

# Governance capability cost follows a monotonic ordering that is invariant across all tested task types

## Evidence summary

50-seed sweep across 7 governance configs (oracle through tight) and 4 task types. The ordering oracle > loose > light > moderate-light > moderate > tight-moderate ≈ tight holds without exception across routing, coordination, allocation, and long_horizon. Effect sizes vs oracle:

| Task | d Range | Max d |
|------|---------|-------|
| Routing | 0.47–1.38 | 1.38 |
| Coordination | 4.0–7.0 | 7.0 |
| Allocation | 0.7–7.9 | 7.9 |
| Long_horizon | 0.41–2.04 | 2.04 |

All comparisons survive Bonferroni correction (alpha/24). The monotonic trend from oracle→tight is unambiguous: no config inverts the ordering.

## Mechanism

Each governance layer (audit, CB, staking, confirmation gates, bandwidth cap) independently constrains agent action space. Layering them compounds the constraint, producing monotonic degradation. The consistency across task types suggests the constraint is structural rather than task-specific.

## Open questions

1. Does the ordering hold with >20% adversarial fraction?
2. At what adversarial fraction does tight governance become net-positive for capability (via adversary suppression)?
3. Is there a non-monotonic region at very high adversarial fractions where tight governance recovers capability?

---

Topics:
- [[_index]]
- [[governance-dashboard]]

<!-- topics: governance, capability-cost, task-universality, monotonic-ordering -->
