---
description: 2640-run screening strength dose-response reveals U-shaped routing curve falsifying diversity-consensus mechanism; coordination monotonically improves (rho=0.97)
type: experiment
status: completed
run_id: 20260326_screening_strength_sweep
experiment_type: sweep
created: '2026-03-26'
aliases:
- 20260326_screening_strength_sweep
cssclasses:
- experiment
- experiment-sweep
graph-group: experiment
tags:
- sweep
- screening
- dose-response
- falsification
- mechanism-revision
---

# Screening strength dose-response falsifies diversity-consensus mechanism and reveals U-shaped routing curve driven by signal reliability

## Design

- **Hypothesis**: The diversity-consensus mechanism predicts that screening reduces agent belief variance, producing monotonic coordination improvement and inverted-U routing response (crossover at strength 0.2-0.3 for tight governance). This sweep tests the prediction with 11 screening strengths.
- **Type**: Full factorial sweep with confirmatory arm
- **Parameters swept**:
  - `screening_strength`: 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0
  - `governance_level`: tight, moderate, light
  - `task_type`: routing, coordination (primary, 30 seeds); allocation, long_horizon (confirmatory, 10 seeds)
- **Settings**: 10 agents, 20% adversarial fraction
- **Total runs**: 2,640 (1,980 primary + 660 confirmatory)

## Key results

### Prediction 1 CONFIRMED: Coordination improves monotonically

All three governance levels show near-perfect monotonic increase with screening strength:
- Tight: rho = +0.964, range 0.730 → 0.856 (d = 2.57 at strength 1.0 vs baseline)
- Moderate: rho = +0.973, range 0.788 → 0.874 (d = 2.54)
- Light: rho = +0.982, range 0.966 → 0.989 (d = 2.59)

Effect sizes grow continuously without plateau. The consensus arm of the mechanism is validated.

### Prediction 2 FALSIFIED: Routing × tight shows U-shape, not inverted-U

The routing dose-response under tight governance is **U-shaped** — the opposite of predicted:
- Baseline (0.0): capability = 0.623
- Minimum at strength 0.4: capability = 0.368 (d = -0.66 vs baseline)
- Recovery at strength 1.0: capability = 0.778 (d = +0.41 vs baseline, EXCEEDS baseline)

The diversity-consensus mechanism predicted an inverted-U with harm at high strength. Instead, harm peaks at intermediate strength (0.1-0.4) and reverses at high strength (0.7-1.0). This falsifies the proposed mechanism.

### Prediction 3 MIXED: Routing × light shows high variance

Routing under light governance shows no clear monotonic trend. Strengths 0.5 and 0.8 achieve perfect 1.000 capability, but 0.2 drops to 0.811. Variance too high for confident trend detection at N=30.

### Prediction 4 FALSIFIED: Long horizon shows large effects at high screening

Long horizon × tight shows massive improvement at high screening strength:
- Baseline (0.0): capability = 0.319
- Strength 1.0: capability = 0.971 (d = 2.75)

This contradicts the null prediction. However, variance is very high (SD = 0.33-0.45) across most strengths, and this is the confirmatory arm (10 seeds only). The effect is suggestive but requires replication at 30+ seeds.

### Revised mechanism: Screening as selective relaxation

The U-shaped routing curve suggests a signal-reliability mechanism, not a diversity-consensus mechanism:

1. **Low screening strength (0.1-0.4)**: Trust signal is noisy. Governance is applied inconsistently — some honest agents get spurious penalties, some adversarial agents get spurious relaxation. Net effect is HARMFUL because inconsistency degrades routing more than uniform governance does.

2. **Medium screening strength (0.5)**: Trust signal is partially reliable. Some honest agents benefit, but noise remains. This is the "valley" where the prior study (20260304_213700_screening) measured screening at strength 0.5 and found harm.

3. **High screening strength (0.7-1.0)**: Trust signal is clean. Honest agents get genuine governance relaxation, restoring path diversity specifically for them. Adversarial agents remain constrained. Net effect is BENEFICIAL — selective relaxation outperforms uniform governance.

This mechanism is mechanistically grounded in the `_differentiated_friction` function: `friction_effective = base_friction * (1 - trust_discount)` where `trust_discount = agent_trust * screening_strength`. At low screening_strength, trust_discount is small and noisy relative to the governance baseline. At high screening_strength, trust_discount cleanly separates honest (trust 0.7-1.0) from adversarial (trust 0.0-0.3) agents.

## Summary table

| Task × Gov | Pattern | d(max) | Supports mechanism? |
|------------|---------|--------|-------------------|
| Coordination × tight | Monotonic up | +2.57 | Yes (consensus benefit) |
| Coordination × moderate | Monotonic up | +2.54 | Yes |
| Coordination × light | Monotonic up | +2.59 | Yes |
| Routing × tight | U-shaped | +0.41 (at 1.0) | No (falsifies diversity-consensus, supports selective-relaxation) |
| Routing × moderate | Non-monotonic | +0.34 | Ambiguous |
| Routing × light | Non-monotonic | +0.49 | Ambiguous |
| Allocation × all | Gradual increase | +0.72-1.65 | Consistent with both |
| Long horizon × tight | Large increase (noisy) | +2.75 | Falsifies null prediction (10 seeds, needs replication) |

## Claims affected

### New claims

- [[claim-coordination-capability-increases-monotonically-with-screening-strength]] (high) — rho=0.96-0.98 across all 3 governance levels, 30 seeds, d up to 2.59
- [[claim-routing-screening-dose-response-is-u-shaped-under-tight-governance]] (medium) — U-shape from 0.623 baseline to 0.368 minimum at 0.4, recovering to 0.778 at 1.0. 30 seeds.
- [[claim-screening-signal-reliability-determines-routing-outcome]] (medium) — noisy trust signal at low strength harms; clean signal at high strength benefits

### Existing claims weakened

- [[claim-screening-harms-routing-under-tight-governance]] — **WEAKENED**: the harm is specific to intermediate screening strength (0.1-0.5). At high strength (0.7-1.0), screening HELPS routing under tight governance.
- [[claim-screening-effect-is-task-type-dependent]] — **REFINED**: the task-type dependence is real but the mechanism is wrong. Routing harm is dose-dependent, not categorical.

### Existing claims confirmed with new evidence

- [[claim-screening-improves-coordination-capability-universally]] — **STRENGTHENED**: dose-response confirms monotonic improvement across full 0.0-1.0 range

## Artifacts

- `runs/20260326_screening_strength_sweep/csv/routing_raw.csv` (990 rows)
- `runs/20260326_screening_strength_sweep/csv/coordination_raw.csv` (990 rows)
- `runs/20260326_screening_strength_sweep/csv/allocation_raw.csv` (330 rows)
- `runs/20260326_screening_strength_sweep/csv/long_horizon_raw.csv` (330 rows)
- `runs/20260326_screening_strength_sweep/summary.json`

## Reproduction

```bash
cd /Users/raelisavitt/distributional-agi-safety && python /path/to/runs/20260326_screening_strength_sweep/run_sweep.py
```

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: sweep, screening, dose-response, falsification, mechanism-revision -->
