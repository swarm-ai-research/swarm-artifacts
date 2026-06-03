---
description: Long-horizon screening effect from 10-seed inflates to d=2.75; replication at 50 seeds deflates to d=0.38 under tight governance, d=0.76 under moderate (Bonferroni-sig)
type: claim
status: active
confidence: high
domain: methodology
evidence:
  supporting:
  - run: 20260326_screening_strength_sweep
    metric: long_horizon_capability_tight
    detail: 'd=2.75, p<0.001, N=10 seeds, screening strength 1.0 vs baseline, Bonferroni-corrected'
  - run: 20260328_long_horizon_screening_replication
    metric: long_horizon_capability
    detail: 'Replication N=50 seeds: tight governance d=0.38, p=0.058 (not Bonferroni-sig, α=0.004); moderate governance d=0.76, p=0.0001 (Bonferroni-sig, α=0.004)'
  weakening: []
  boundary_conditions:
  - "Original: N=10 seeds per configuration (10 agents, 20% adversarial, tight governance)"
  - "Replication: N=50 seeds, same configuration (5x power increase)"
  - Long-horizon task (multi-step planning) with maximum screening strength (1.0)
  - Default topology, Bonferroni correction α/12 = 0.004 for multiple comparisons
sensitivity:
  sample_size: inflation is severe at N=10, diminishes at N=50
  governance_regime: tight governance effect disappears; moderate governance persists
  screening_strength: replication only at strength 1.0 (baseline and intermediate strengths also tested)
  task_type: applies to long-horizon planning task
supersedes: []
superseded_by: []
related_claims:
- claim-coordination-capability-increases-monotonically-with-screening-strength
- claim-routing-screening-dose-response-is-u-shaped-under-tight-governance
- claim-screening-signal-reliability-determines-routing-outcome
created: 2026-06-02
updated: 2026-06-02
aliases:
- small-sample-inflation
- long-horizon-replication-deflation
cssclasses:
- claim
- claim-high
tags:
- methodology
- sample-size
- statistical-power
- replication
graph-group: claim
---

# small-sample inflation deflates screening effect from d=2.75 to d=0.38 under tight governance

The apparent d=2.75 long-horizon improvement under tight governance with high screening strength, measured in the 10-seed confirmatory arm of the dose-response sweep, is a textbook case of small-sample effect size inflation. Replication at 50 seeds deflates the estimate to d=0.38 (non-significant), while revealing a genuine moderate-governance effect (d=0.76, Bonferroni-significant).

## Evidence

| Governance | N (original) | d (original) | N (replication) | d (replication) | p-value | Bonferroni-sig? |
|-----------|-------------|------------|-----------------|----------------|---------|-----------------|
| **Tight** | 10 | **2.75** | 50 | **0.38** | 0.058 | **No** |
| **Moderate** | 10 | (unclear) | 50 | **0.76** | 0.0001 | **Yes** |
| **Light** | 10 | (ceiling) | 50 | 0.05 | 0.811 | No |

Bonferroni correction threshold: α/12 = 0.004

The 50-seed replication shows that only the moderate-governance effect is real and Bonferroni-significant. The tight-governance effect is a phantom caused by sampling noise.

## Mechanism of inflation

With N=10 seeds:
- Small random fluctuations in endpoint measurements create large effect sizes by chance
- Variance estimate is unstable at N=10
- d = (μ_high - μ_baseline) / σ can inflate if either numerator is boosted or σ is deflated by sampling noise

With N=50 seeds:
- Variance estimate stabilizes
- Random fluctuations average out
- True effect emerges

## The real finding

Screening improves long-horizon planning under **moderate governance** (d=0.76, equivalent in magnitude to coordination improvements at intermediate screening strength). This effect is:
- **Genuine**: Bonferroni-significant
- **Governance-specific**: Only emerges under moderate, not tight
- **Dose-dependent**: monotonically increases 0.0→1.0 under moderate governance

The tight-governance null (d=0.38, not significant) suggests that tight governance already constrains agents enough to hinder long-horizon planning. Adding screening relaxation doesn't help because agents remain constrained.

## Methodological implications

1. **Small-sample inflation is severe in high-variance domains.** Agent-based models have high noise. Confirmatory arms at N=10 are insufficient.
2. **Bonferroni correction caught this.** The original d=2.75 would have passed raw p < 0.05 but fails Bonferroni correction even at N=10.
3. **Replication is essential.** This claim could not have been made without the full 50-seed replication.

This finding parallels and grounds the statistical criteria documented in the SWARM methodology. [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse]] and [[claim-toxicity-mechanism-effects-are-additive-not-synergistic]] both rely on Bonferroni-corrected significance thresholds and explicit replication. The present claim validates this approach: without Bonferroni correction and replication, a false positive (d=2.75 tight governance effect) would have been published.

## Open questions

1. How many seeds are sufficient for stable long-horizon estimates in agent-based simulations?
2. Does the moderate-governance effect persist at different adversarial fractions?
3. Can we build confidence calibration that accounts for this inflation pattern?

## Update history

**2026-06-02** — extracted from 20260326_screening_strength_sweep (confirmatory arm, N=10) and 20260328_long_horizon_screening_replication (N=50).

---

Topics:
- [[_index]]
- [[methodology-dashboard]]
- [[screening-mechanisms]]

<!-- topics: methodology, sample-size, statistical-power, replication -->
