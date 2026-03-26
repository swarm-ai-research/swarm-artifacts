---
description: "Allocation loses 10% capability at tight governance while long_horizon loses 46%; governance cost scales with task coordination demands"
type: claim
status: active
confidence: high
domain: governance
evidence:
  supporting:
  - run: 20260304_212912_frontier_trace
    metric: "capability delta (oracle vs tight)"
    detail: "50 seeds. Allocation: 1.000→0.896 (delta=-10.4%, d=6.63). Long_horizon: 1.000→0.543 (delta=-45.7%, d=1.63). Routing: 1.000→0.628 (delta=-37.2%, d=1.34). Coordination: 1.000→0.710 (delta=-29.0%, d=6.08). All Bonferroni-significant."
  weakening: []
  boundary_conditions:
  - "10-agent, 20% adversarial, 4 task types tested"
  - "Allocation 100% completion even at tight governance, vs long_horizon 48% (majority failure)"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-governance-capability-cost-is-monotonic-and-task-universal
  relation: extends
- claim: claim-governance-cost-paradox
  relation: supports
created: 2026-03-25
updated: 2026-03-25
aliases:
- task-complexity-governance-cost-amplification
cssclasses:
- claim
- claim-high
tags:
- governance
- task-complexity
- coordination-demands
- capability-loss
graph-group: claim
---

# Task complexity amplifies governance capability cost, with allocation losing 10% and long-horizon losing 46% under tight governance

## Evidence summary

The same tight governance configuration produces dramatically different capability losses depending on task type:

| Task | Oracle | Tight | Delta | d |
|------|--------|-------|-------|-------|
| Allocation | 1.000 | 0.896 | -10.4% | 6.63 |
| Coordination | 1.000 | 0.710 | -29.0% | 6.08 |
| Routing | 1.000 | 0.628 | -37.2% | 1.34 |
| Long_horizon | 1.000 | 0.543 | -45.7% | 1.63 |

The 4.4× amplification factor between the most and least affected task types shows that governance cost is not a fixed overhead but scales with task coordination demands. Completion rate tells the same story: allocation 100% completion at tight governance vs long_horizon 48% (majority failure). All differences survive Bonferroni correction.

## Mechanism

Governance mechanisms constrain inter-agent communication bandwidth and action diversity. Tasks requiring multi-step coordination (long_horizon) are disproportionately affected because they require more communication rounds, each subject to governance overhead. Allocation tasks are inherently more parallelizable and require fewer coordination rounds.

The ordering of task complexity by governance sensitivity matches our expectation: allocation (independent decisions) < routing (single-hop coordination) < coordination (multi-hop messaging) < long_horizon (temporal dependency chains).

## Open questions

1. Where is the crossover point — at what task complexity level does governance become net-harmful?
2. Can governance be task-adaptive (tight for allocation, loose for long_horizon)?
3. Does the amplification factor grow with agent count (larger teams may require more coordination)?

---

Topics:
- [[_index]]
- [[governance-dashboard]]

<!-- topics: governance, task-complexity, coordination-demands, capability-loss -->
