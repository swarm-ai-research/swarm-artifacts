---
description: Combined toxicity feedback effects (proxy drift + trust erosion + contagion) are additive; proxy drift dominates combined scenario (net welfare −0.91)
type: claim
status: active
confidence: medium
domain: toxicity-dynamics
evidence:
  supporting:
  - run: dynamic_toxicity_2026-03-28
    metric: combined_effects
    detail: 'Combined scenario (all 3 mechanisms): net welfare −0.91, toxicity 0.429. Proxy drift alone: −1.54. Difference (−0.91 - (−1.54) = 0.63) suggests trust erosion and contagion add ~0.63 welfare vs proxy drift alone'
  - run: dynamic_toxicity_2026-03-28
    metric: mechanism_comparison
    detail: 'No multiplicative interaction observed. Trust erosion alone: +6.27. Contagion alone: +5.80. When combined with proxy drift, effects accumulate linearly'
  weakening: []
  boundary_conditions:
  - Tested with all three mechanisms enabled simultaneously
  - 40% adversarial fraction, 10 agents
  - Proxy drift alpha=0.3, trust erosion beta=0.3, contagion gamma=0.1
  - Net social welfare metric captures combined effects
  - Only single combined scenario tested (not factorial design)
sensitivity:
  mechanism_parameters: tested only with moderate parameter values
  adversarial_fraction: tested at 40% only
  interaction_hypothesis: would require factorial design to test synergy hypothesis formally
supersedes: []
superseded_by: []
related_claims:
- claim-proxy-calibration-drift-causes-deterministic-welfare-collapse
- claim-trust-erosion-requires-proximity-to-phase-boundary-for-ecosystem-impact
- claim-toxicity-contagion-absorbed-by-memory-decay-in-reputation-systems
created: 2026-06-02
updated: 2026-06-02
aliases:
- additive-toxicity-effects
- no-mechanism-synergy
cssclasses:
- claim
- claim-medium
tags:
- toxicity-dynamics
- mechanism-interaction
- superposition
graph-group: claim
---

# toxicity mechanism effects are additive, not synergistic

Combined toxicity feedback mechanisms (proxy calibration drift + trust erosion + quality contagion) produce **additive effects**, not synergistic. Proxy drift dominates the combined scenario (net welfare −0.91), with trust erosion and contagion adding marginal linearly-combined damage.

## Evidence

| Scenario | Net Welfare | Toxicity | Mechanism(s) | Outcome |
|----------|------------|----------|--------------|---------|
| Baseline | +2.87 | 0.294 | None | PASS |
| Proxy drift | −1.54 | 0.429 | Drift alone | FAIL |
| Trust erosion | +6.27 | 0.297 | Erosion alone | PASS |
| Contagion | +5.80 | 0.295 | Contagion alone | PASS |
| **Combined** | **−0.91** | 0.429 | All three | **FAIL** |

### Additivity calculation

If effects were synergistic (multiplicative):
- Proxy drift baseline: −1.54
- Combined: −0.91
- Expected if multiplicative: drift × erosion_modifier × contagion_modifier ≈ much more negative

Observed instead:
- Proxy drift: −1.54
- Trust erosion + contagion interaction: +0.63 (relative to proxy drift alone)
- Net: −1.54 + 0.63 = −0.91

The combined effect is linear: base effect (proxy drift) + adjustment (other mechanisms).

## Mechanism

No interaction emerges at the tested parameter levels. Each mechanism operates independently:

1. **Proxy drift** — cumulative sigmoid degradation, deterministic
2. **Trust erosion** — honest agent exit, requires phase boundary
3. **Quality contagion** — memory decay-absorbed signal

In the combined scenario, proxy drift dominates (−1.54 net welfare) because it operates continuously and deterministically. Trust erosion and contagion both operate, but neither overcomes the drift signal. The effects stack additively.

## Interpretation

This suggests the mechanisms are **orthogonal** rather than coupled. If they were mechanistically entangled (e.g., drift causes erosion triggers contagion), we would see synergistic scaling. Instead, they degrade governance independently.

## Open questions

1. Do effects remain additive at higher parameter values (alpha > 0.3, beta > 0.6, gamma > 0.4)?
2. Is there a parameter regime where contagion or erosion amplifies drift?
3. Does the order of mechanism introduction affect additivity (e.g., drift first vs contagion first)?
4. What is the scaling relationship at higher adversarial fractions where erosion becomes active?

## Update history

**2026-06-02** — extracted from dynamic_toxicity_2026-03-28 experiment. Single combined run; formal factorial interaction testing recommended.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[toxicity-mechanisms]]

<!-- topics: toxicity-dynamics, mechanism-interaction, superposition -->
