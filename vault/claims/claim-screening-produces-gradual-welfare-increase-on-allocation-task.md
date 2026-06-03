---
description: Allocation task shows gradual welfare increase with screening strength across all governance levels (d=0.72-1.65), consistent with both diversity-consensus and signal-reliability mechanisms
type: claim
status: active
confidence: medium
domain: governance
evidence:
  supporting:
  - run: 20260326_screening_strength_sweep
    metric: allocation_capability
    detail: 'Allocation task confirmatory arm: tight d=0.72 p<0.05, moderate d=1.31 p<0.01, light d=1.65 p<0.001, N=10 seeds per governance level, screening strength 0.0→1.0, Bonferroni-corrected'
  weakening: []
  boundary_conditions:
  - 10 agents, 20% adversarial fraction, default topology
  - N=10 seeds per configuration (confirmatory arm)
  - "Screening strength range 0.0 to 1.0 (5 levels tested: 0.0, 0.3, 0.5, 0.7, 1.0)"
  - Three governance regimes (tight, moderate, light)
sensitivity:
  task_type: allocation task may differ in complexity from routing and coordination
  adversarial_strategy: untested with agents adapting to screening strength
  population_size: tested only at 10 agents
  adversarial_fraction: tested only at 20%
supersedes: []
superseded_by: []
related_claims:
- claim-coordination-capability-increases-monotonically-with-screening-strength
- claim-routing-screening-dose-response-is-u-shaped-under-tight-governance
- claim-screening-signal-reliability-determines-routing-outcome
created: 2026-06-02
updated: 2026-06-02
aliases:
- allocation-screening-gradual-increase
- screening-allocation-monotonic
cssclasses:
- claim
- claim-medium
tags:
- governance
- screening
- allocation
- dose-response
graph-group: claim
---

# screening produces gradual welfare increase on allocation task

The allocation task shows a **gradual (monotonic-like) welfare increase** with screening strength across all governance levels, with effect sizes ranging from d=0.72 to d=1.65. This pattern is consistent with both the diversity-consensus and signal-reliability mechanism explanations.

## Evidence summary

| Governance Level | Screening 0.0 | Screening 1.0 | Δ Welfare | d | N |
|-----------------|--------------|--------------|----------|---|---|
| Tight | — | — | — | 0.72 | 10 |
| Moderate | — | — | — | 1.31 | 10 |
| Light | — | — | — | 1.65 | 10 |

The effect size increases with lighter governance (d=1.65 at light > d=1.31 at moderate > d=0.72 at tight).

## Comparison to routing, coordination, and long-horizon planning

| Task | Pattern | Mechanism support | Governance interaction |
|------|---------|-------------------|------------------------|
| Coordination | Monotonic increase | Diversity-consensus confirmed | Universal across all levels |
| Routing | U-shape (tight only) | Signal-reliability confirmed | Tight governance only |
| **Allocation** | **Gradual increase** | **Ambiguous** | Increases with lighter governance |
| Long-horizon | Monotonic (moderate) | Signal-reliability (screening relaxation) | **Moderate governance only** |

The long-horizon task (from [[claim-moderate-governance-enables-dose-dependent-long-horizon-improvement]]) exhibits similar governance-specificity to routing: maximum benefit emerges at a particular governance intensity (moderate, rather than tight). This suggests that [[claim-screening-signal-reliability-determines-routing-outcome|signal reliability mechanism]] extends beyond routing to long-horizon planning — honest agents benefit most from selective governance relaxation (high screening strength) when governance is neither too tight nor too loose.

Allocation differs from both routing (non-U-shaped) and coordination (monotonic but with larger effect sizes). The pattern suggests screening benefits allocation through a different mechanism than either pure diversity consensus or pure signal reliability.

## Possible mechanism

Allocation tasks may require:
1. **Agent diversity** (coordination benefit) — honest and adversarial agents can contribute different allocation strategies
2. **Signal reliability** (routing benefit, weaker) — high screening strength does not harm allocation via noisy constraints
3. **Task-specific factors** — allocation may tolerate intermediate screening strength unlike routing

The gradual increase (rather than U-shape) suggests allocation tasks are more robust to noisy governance signals than routing tasks.

## Open questions

1. Why do effect sizes increase with lighter governance (d=1.65 > d=0.72)?
2. Does allocation truly require both diversity AND signal reliability, or just one?
3. How does the gradual increase curve compare quantitatively to monotonic (coordination) vs U-shaped (routing)?
4. Are there sub-task types within allocation that show different dose-response patterns?

## Update history

**2026-06-02** — extracted from 20260326_screening_strength_sweep confirmatory arm (allocation, 10 seeds).

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: governance, screening, allocation, dose-response -->
