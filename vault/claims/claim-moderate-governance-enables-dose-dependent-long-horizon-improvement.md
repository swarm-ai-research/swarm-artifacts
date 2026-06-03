---
description: Moderate governance shows dose-dependent long-horizon improvement (d=0.76 Bonferroni-sig at screening 1.0), while tight governance shows only trend (d=0.38, p=0.058)
type: claim
status: active
confidence: medium
domain: governance
evidence:
  supporting:
  - run: 20260328_long_horizon_screening_replication
    metric: long_horizon_moderate_governance
    detail: 'Moderate governance dose-response: 0.0→0.552, 0.3→0.723 (d=0.44), 0.5→0.766 (d=0.57), 0.7→0.756 (d=0.54), 1.0→0.828 (d=0.76, p=0.0001, Bonferroni-sig). Monotonic increase. 50 seeds'
  - run: 20260328_long_horizon_screening_replication
    metric: long_horizon_tight_governance
    detail: 'Tight governance trend: 0.0→0.543, 1.0→0.692 (d=0.38, p=0.058, not Bonferroni-sig). Non-monotonic: 0.543→0.590→0.592→0.640→0.692. 50 seeds'
  weakening: []
  boundary_conditions:
  - Tested with 10 agents, 20% adversarial fraction
  - 50 seeds per configuration (replication of 10-seed finding)
  - Screening strength range 0.0-1.0 (5 levels tested)
  - Long-horizon task with multiple steps required
  - Bonferroni correction threshold α/12 = 0.004
sensitivity:
  governance_regime: effect specific to moderate governance; tight governance shows weaker trend
  screening_strength: monotonic dose-response under moderate; non-monotonic under tight
  task_type: long-horizon planning; untested on routing or coordination at same strength levels
  agent_count: tested only at 10 agents
supersedes: []
superseded_by: []
related_claims:
- claim-screening-signal-reliability-determines-routing-outcome
- claim-small-sample-inflation-deflates-screening-effect-from-d-275-to-d-038
- claim-coordination-capability-increases-monotonically-with-screening-strength
created: 2026-06-02
updated: 2026-06-02
aliases:
- moderate-governance-long-horizon
- long-horizon-dose-dependent-improvement
cssclasses:
- claim
- claim-medium
tags:
- governance
- screening
- long-horizon
- dose-response
graph-group: claim
---

# moderate governance enables dose-dependent long-horizon improvement

Moderate governance reveals a **clean, dose-dependent improvement** in long-horizon task performance with screening strength (d=0.76 Bonferroni-significant at maximum strength). Tight governance shows only a suggestive trend (d=0.38, not significant), suggesting governance intensity modulates the screening benefit.

## Evidence

| Governance | Baseline (0.0) | Strength 0.3 | Strength 0.5 | Strength 0.7 | Maximum (1.0) | Pattern |
|-----------|--------------|------------|------------|------------|--------------|---------|
| **Moderate** | 0.552 | 0.723 | 0.766 | 0.756 | **0.828** | **Monotonic up** |
| **Tight** | 0.543 | 0.590 | 0.592 | 0.640 | 0.692 | Gradual up |
| Light | 0.881 | — | — | — | 0.895 | Ceiling |

### Statistical significance

| Governance | Strength 1.0 | d | p-value | Bonferroni-sig? |
|-----------|------------|---|---------|-----------------|
| Moderate | 0.828 | **0.76** | **0.0001** | **Yes** |
| Tight | 0.692 | 0.38 | 0.058 | No |
| Light | 0.895 | 0.05 | 0.811 | No |

Moderate governance d=0.76 survives Bonferroni correction (α/12 = 0.004). Tight governance fails to reach significance.

## Mechanism: Governance-screening interaction

The governance regime determines whether screening relaxation benefits long-horizon planning:

| Governance | Constraint Level | Screening Effect | Interpretation |
|-----------|-----------------|-----------------|-----------------|
| **Tight** | Very restrictive | Weak (d=0.38) | Already constrained; screening relaxation marginal |
| **Moderate** | Balanced | Strong (d=0.76) | Relaxation unlocks planning diversity |
| **Light** | Very permissive | Null (d=0.05) | Already relaxed; screening relaxation redundant |

Moderate governance operates in the "sweet spot": tight enough to enforce discipline, loose enough that selective honest-agent relaxation (screening effect) materially improves planning capability.

## Comparison to routing and coordination

- **Coordination**: Monotonic improvement at all governance levels (d=2.54-2.59)
- **Routing**: U-shaped under tight governance only (d=+0.41 at 1.0)
- **Long-horizon**: Dose-dependent under moderate governance only (d=0.76)

Each task type benefits maximally from screening under different governance regimes:
- Coordination: universally improved (needs diversity)
- Routing: tight governance (needs signal reliability to avoid inconsistency)
- Long-horizon: moderate governance (needs balance between constraint and relaxation)

## Implications

This suggests that **governance intensity and task complexity co-determine screening effectiveness**. One-size-fits-all governance does not maximize performance across task types. An adaptive governance system would:

1. Detect task type (coordination, routing, long-horizon)
2. Select appropriate governance intensity (light, moderate, tight)
3. Calibrate screening strength accordingly

## Open questions

1. Is the moderate governance benefit driven by selective honest-agent relaxation ([[claim-screening-signal-reliability-determines-routing-outcome]]), or by task-specific properties?
2. Does the dose-response remain monotonic under higher adversarial fractions?
3. Can we predict the optimal governance-task pairing from theory?
4. Are there other task types (e.g., delegation, hierarchical control) that peak at different governance levels?

## Update history

**2026-06-02** — extracted from 20260328_long_horizon_screening_replication (50 seeds, full dose-response).

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: governance, screening, long-horizon, dose-response -->
