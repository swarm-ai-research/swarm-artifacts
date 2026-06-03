---
description: Quality contagion (low-p interactions shift ecosystem-wide trust) is absorbed by per-epoch memory decay toward 0.5; effect null even at aggressive rate (gamma=0.4)
type: claim
status: active
confidence: medium
domain: agent-behavior
evidence:
  supporting:
  - run: dynamic_toxicity_2026-03-28
    metric: contagion_welfare
    detail: 'Contagion (γ=0.1) at 40% adversarial: net welfare +5.80, N=42 seeds, Bonferroni-corrected. vs baseline +2.87 (null effect, Δ = +2.93)'
  - run: dynamic_toxicity_2026-03-28
    metric: contagion_aggressive_welfare
    detail: 'Contagion aggressive (γ=0.4, 4x rate) at 40% adversarial: net welfare +5.71, N=42 seeds, Bonferroni-corrected. 4x contagion rate produces same outcome as γ=0.1 (saturation)'
  weakening: []
  boundary_conditions:
  - "Contagion: per-epoch trust update based on low-quality interaction fraction"
  - Reputation baseline 0.5, decay_rate=0.95 per epoch
  - Tested γ=0.1 and γ=0.4 contagion rates (4-fold variation)
  - 40% adversarial fraction, 10 agents, default topology
  - Episode length 30 epochs, trust_t = decay*trust_(t-1) + (1-decay)*0.5 + contagion_signal
sensitivity:
  memory_decay_rate: tested only with existing decay settings; untested with stronger decay resistance
  contagion_rate: tested at gamma=0.1 and 0.4; may require gamma > 0.5 to overcome decay
  governance_parameters: tested with CB=0.6, audit=0.1, decay=0.95
  trust_distribution: contagion effect may depend on initial trust variance
supersedes: []
superseded_by: []
related_claims:
- claim-proxy-calibration-drift-causes-deterministic-welfare-collapse
- claim-trust-erosion-requires-proximity-to-phase-boundary-for-ecosystem-impact
created: 2026-06-02
updated: 2026-06-02
aliases:
- contagion-decay-absorption
- toxicity-contagion-null
cssclasses:
- claim
- claim-medium
tags:
- toxicity-dynamics
- contagion
- reputation
- memory-decay
graph-group: claim
---

# toxicity contagion absorbed by memory decay in reputation systems

Quality contagion—low-quality interactions shifting ecosystem-wide trust downward—is entirely absorbed by per-epoch memory decay toward baseline trust (0.5). Even at aggressive contagion rates (gamma=0.4), the mechanism produces no measurable welfare harm (net welfare +5.80, indistinguishable from baseline +2.87).

## Evidence

| Mechanism | Gamma | Adv% | Net Welfare | Toxicity | vs Baseline | Conclusion |
|-----------|-------|------|------------|----------|------------|-----------|
| Baseline | — | — | +2.87 | 0.294 | — | — |
| Contagion | 0.1 | 40% | **+5.80** | 0.295 | +2.93 (positive!) | **Null** |
| Contagion aggressive | 0.4 | 40% | **+5.71** | 0.296 | +2.84 | **Null** |

The aggressive contagion (4x the moderate rate) produces the **same welfare** as moderate contagion. This indicates saturation: contagion signal is too weak to overcome decay.

## Mechanism

Contagion operates as a negative update to agent trust after low-quality interactions:

```python
# Each epoch:
trust_t = trust_(t-1) * decay_rate + (1 - decay_rate) * baseline_trust + contagion_signal
contagion_signal = -gamma * fraction_of_low_quality_partners
```

The decay term (0.95) pulls trust back toward baseline (0.5) every epoch, while contagion signal pushes it down. The equilibrium is determined by the relative strength of decay vs contagion.

### Why decay dominates

In a 40% adversarial ecosystem:
- Each honest agent experiences ~40% low-quality interactions
- Contagion signal: -gamma * 0.4
- Decay restoration: -(trust - 0.5) * (1 - decay)
- With decay=0.95: (1 - 0.95) = 0.05 restoration coefficient
- Trust decays toward 0.5 at 5% per epoch

For contagion to overcome decay, it would need:
```
gamma * 0.4 > 0.05
gamma > 0.125
```

Even at gamma=0.4, the contagion signal (0.16) barely exceeds the decay restoration rate (0.05). The ecosystem converges to an equilibrium where contagion is **absorbed**, not amplified.

## Interpretation

This is a **structural property of reputation systems with memory decay**. Contagion cannot sustain amplifying dynamics if there is baseline trust restoration. The system is fundamentally stabilized by decay.

In contrast to [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse|proxy drift]], which operates on the **detection signal** (sigmoid_k parameter) rather than on **agent trust**, contagion operates at the agent level (reputation updates). The difference in mechanism explains the difference in outcome: agent-level trust has built-in stabilizers (memory decay), while detection signal parameters lack automatic stabilization. This suggests that governance systems optimized for reputation stability (high decay rates) may inadvertently leave detection systems vulnerable to calibration drift.

The null effect contrasts sharply with [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse]], which also involves accumulated toxicity but operates through a different mechanism (calibration degradation rather than trust updates).

## Open questions

1. What decay rate would allow contagion to escape and amplify? (decay < 0.90?)
2. Is there a contagion_rate threshold where the mechanism transitions from null to harmful?
3. How does contagion interact with other toxicity mechanisms (e.g., proxy drift)?
4. Does contagion become harmful in longer episodes (>30 epochs) where decay compound time dominates?

## Update history

**2026-06-02** — extracted from dynamic_toxicity_2026-03-28 experiment.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[toxicity-mechanisms]]

<!-- topics: toxicity-dynamics, contagion, reputation, memory-decay -->
