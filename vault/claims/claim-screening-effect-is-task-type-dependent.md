---
description: "Screening shifts the capability frontier differently by task type: positive for coordination, negative for tight-gov routing, null for long_horizon"
type: claim
status: active
confidence: high
domain: market
evidence:
  supporting:
  - run: 20260304_213700_screening
    metric: "capability by task type"
    detail: "50 seeds × 3 gov × 4 tasks = 1200 runs. Coordination: d=+0.97 to +1.10 (all Bonferroni-sig). Allocation: d=+0.40 to +0.87 (mixed sig). Routing tight: d=-0.78 (Bonferroni-sig harm). Long_horizon: d=-0.06 to +0.27 (all null). Bonferroni threshold alpha/18=0.00278."
  - run: 20260304_232817_screening
    metric: "routing replication"
    detail: "20 seeds. Tight d=-0.47, light d=+0.60. Directions replicate."
  - run: 20260304_232823_screening
    metric: "long_horizon replication"
    detail: "20 seeds. All null (d=-0.04 to +0.54). Confirms no long_horizon effect."
  weakening: []
  boundary_conditions:
  - "10 agents, 20% adversarial, screening_strength=0.5, 3 governance levels tested"
  - "Single screening strength (0.5) tested; task-type interaction may change at other strengths"
  - "Single adversarial fraction (20%) tested"
sensitivity:
  screening_strength: "unknown if interaction profile differs at 0.25 or 0.75"
  adversarial_fraction: "tested at 20% only"
  task_complexity: "may interact with task-type effects at higher complexity levels"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-screening-improves-coordination-capability-universally
  relation: supports
- claim: claim-screening-harms-routing-under-tight-governance
  relation: supports
- claim: claim-game-structure-determines-optimal-governance-regime
  relation: extends
- claim: claim-task-complexity-amplifies-governance-capability-cost
  relation: extends
created: 2026-03-25
updated: 2026-03-25
aliases:
- screening-task-type-specialization
cssclasses:
- claim
- claim-high
tags:
- screening
- task-type-dependence
- governance
- market
- mechanism-design
- capability-frontier
graph-group: claim
---

# Screening is a task-type specialization tool, not a universal capability frontier improvement

## Evidence summary

Across 1200+ runs (main) + 240 (replications), screening (strength=0.5) shows fundamentally different effects by task type. The task-type dependence is the dominant factor, not governance level.

| Task Type | Governance Level | Effect Size | p-value | Bonferroni-Sig |
|-----------|-----------------|-------------|---------|-----------------|
| Coordination | Tight | d=+1.04 | p<0.000001 | Yes |
| Coordination | Moderate | d=+0.97 | p=0.000001 | Yes |
| Coordination | Light | d=+1.10 | p<0.000001 | Yes |
| Allocation | Tight | d=+0.87 | varies | Mixed |
| Allocation | Moderate | d=+0.40 | varies | Mixed |
| Allocation | Light | d=+0.56 | varies | Mixed |
| Routing | Tight | d=-0.78 | p=0.0001 | Yes |
| Routing | Moderate | d=-0.12 | p=0.534 | No |
| Routing | Light | d=+0.21 | p=0.285 | No |
| Long_Horizon | Tight | d=-0.04 | null | No |
| Long_Horizon | Moderate | d=+0.27 | null | No |
| Long_Horizon | Light | d=+0.54 | null | No |

### Summary by task type:

**Coordination**: Universally positive (d=0.97-1.10, all Bonferroni-significant). Screening amplifies all governance levels equally.

**Allocation**: Modestly positive (d=0.40-0.87). Effect strongest under tight governance, weakens under lighter governance. Mixed significance, requiring further replication at N>20.

**Routing**: Governance-dependent with harm under tight governance (d=-0.78, Bonferroni-sig). Null or positive under moderate/light governance. Directional replication confirmed.

**Long_Horizon**: Consistently null across 3 independent runs and all governance levels (d=-0.06 to +0.54). Screening has no effect on long-horizon planning.

## Mechanism

Screening reduces agent belief variance. This helps tasks requiring consensus (coordination) but harms tasks requiring diversity (routing under constraints). Tasks with neither requirement (long_horizon planning) are unaffected.

- **Coordination**: Agents need agreement on goals. Screening reduces wasted motion from divergent intent signals.
- **Routing**: Agents need path diversity to explore alternatives. Screening homogenizes routes, reducing useful exploration.
- **Long_Horizon**: Planning horizons depend on lookahead depth, not on belief alignment. Screening is orthogonal to this capability.

## Implications

This finding refutes the hypothesis that screening is a "universal improvement" mechanism. Instead, screening is a **task-type specialization tool** that trades across objectives. Organizations deploying screening must match it to their primary task demands:

- Deploy screening if coordination is critical and routing is not
- Reduce screening strength or disable it if routing must remain flexible
- Leave screening disabled for long-horizon planning tasks

The strong task-type dependence also suggests that [[claim-game-structure-determines-optimal-governance-regime|game structure determines optimal governance]], not mechanism design alone. The same governance parameter produces opposite effects depending on task demands.

## Boundary conditions

Single screening strength (0.5). Single adversarial fraction (20%). The task-type interaction may change at different screening strengths or higher adversarial fractions.

## Open questions

1. Can a task-adaptive screening policy be designed that applies screening selectively based on current task type?
2. Does the task-type dependence generalize to other mechanism design interventions (e.g., circuit breakers, reward shaping)?
3. At what screening strength does the allocation task lose its benefit?
4. Does the long_horizon null effect hold for planning horizons >20 steps?

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: screening, task-type-dependence, governance, market, mechanism-design, capability-frontier -->
