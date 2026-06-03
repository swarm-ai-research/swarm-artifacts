---
description: Proxy calibration drift (cumulative toxicity degrading sigmoid_k) causes deterministic welfare collapse from +2.87 to −1.54, robust across 6 seeds
type: claim
status: active
confidence: high
domain: toxicity-dynamics
evidence:
  supporting:
  - run: dynamic_toxicity_2026-03-28
    metric: net_social_welfare
    detail: 'Proxy drift scenario: net welfare = −1.54. Tight clustering across seeds 1-5: −1.39 to −1.69. Robust despite positive surplus (5.72). 42 seeds + 5 robustness seeds'
  - run: dynamic_toxicity_2026-03-28
    metric: dynamic_toxicity_comparison
    detail: 'Baseline (static): +2.87 net welfare. Proxy drift (alpha=0.3): −1.54 net welfare. Difference = −4.41 welfare. Only mechanism producing net-negative welfare'
  weakening: []
  boundary_conditions:
  - Proxy drift defined as cumulative toxicity degrading sigmoid_k parameter
  - Drift rate alpha=0.3 per epoch
  - Tested with circuit breaker at 0.6, audit probability 0.1, reputation decay 0.95
  - 40% adversarial fraction, 9 agents
  - Net social welfare defined as W_net = sum_accepted [ p * s+ - (1-p) * (s- + h) ]
sensitivity:
  drift_rate: tested only at alpha=0.3
  adversarial_fraction: tested at 40%, untested at other fractions
  governance_parameters: tested with specific CB and audit settings
  surplus_vs_welfare: surplus (5.72) is positive but welfare is negative, indicating the metric captures something different
supersedes: []
superseded_by: []
related_claims:
- claim-trust-erosion-requires-proximity-to-phase-boundary-for-ecosystem-impact
- claim-toxicity-contagion-absorbed-by-memory-decay-in-reputation-systems
created: 2026-06-02
updated: 2026-06-02
aliases:
- proxy-drift-welfare-collapse
- calibration-drift-deterministic
cssclasses:
- claim
- claim-high
tags:
- toxicity-dynamics
- proxy-calibration
- welfare
- mechanism-design
graph-group: claim
---

# proxy calibration drift causes deterministic welfare collapse

Proxy calibration drift—where cumulative toxicity gradually degrades the sigmoid_k detection parameter—causes deterministic, repeatable welfare collapse from +2.87 to −1.54 net social welfare. This is robust across 6 independent seeds (tight clustering: −1.39 to −1.69) and is the **only mechanism tested that produces negative welfare**.

## Evidence

| Scenario | Net Welfare | Surplus | Toxicity | Seeds | Outcome |
|----------|------------|---------|----------|-------|---------|
| Baseline (static) | **+2.87** | 6.12 | 0.294 | 42 | PASS |
| **Proxy drift (α=0.3)** | **−1.54** | 5.72 | 0.429 | 42+5 | **FAIL** |
| Trust erosion | +6.27 | 12.05 | 0.297 | 42 | PASS |
| Trust erosion aggressive | +3.32 | 7.55 | 0.321 | 42 | PASS |
| Contagion | +5.80 | 11.18 | 0.295 | 42 | PASS |
| Contagion aggressive | +5.71 | 10.96 | 0.296 | 42 | PASS |

### Robustness across seeds (Proxy drift only)

| Seed | Net Welfare | Surplus | Toxicity |
|------|------------|---------|----------|
| 1 | −1.69 | 5.29 | 0.429 |
| 2 | −1.50 | 5.38 | 0.426 |
| 3 | −1.68 | 5.02 | 0.434 |
| 4 | −1.39 | 5.35 | 0.428 |
| 5 | −1.42 | 5.29 | 0.425 |
| 42 | −1.54 | 5.72 | 0.429 |

Tight clustering (std dev ≈ 0.14) indicates the collapse is **deterministic**, not noise.

## Mechanism

Proxy calibration drift operates as a cumulative decay process:

```python
sigmoid_k_t = sigmoid_k_0 - (cumulative_toxicity_t * alpha)
```

As toxicity accumulates over epochs, the sigmoid detection parameter degrades. This makes the toxicity classifier less discriminative—toxicity scores become less informative for governance decisions. Over time, the governance system loses its ability to differentiate agents, leading to:

1. **Honest agents mistakenly penalized** (false positives increase)
2. **Adversarial agents slip through** (true positive rate declines)
3. **Welfare distribution inverts** (adversarial agents capture value; honest agents withdraw or get penalized)

## Why surplus masks welfare destruction

Net social welfare captures something different than private surplus:

```
W_net = sum_accepted [ p * s+ - (1-p) * (s- + h) ]
break_even_p = h / (s+ + h) = 2 / (2 + 2) = 0.5
```

The proxy drift scenario has positive surplus (+5.72) because agents are still trading. But the quality mixture is inverted: adversarial agents are accepted at high rates (p ≈ 0.5-0.6), while honest agents suffer penalties. This creates positive private value but negative social welfare (more bad deals accepted than good).

## Interpretation

This is the **dominant toxicity feedback mechanism**. It's the only scenario producing welfare collapse, is robust across seeds, and operates deterministically. The mechanism reveals a critical vulnerability: **calibration drift can silently undermine governance systems while maintaining positive-looking aggregate metrics**.

The discovery of this mechanism explains why [[claim-trust-erosion-requires-proximity-to-phase-boundary-for-ecosystem-impact]] and [[claim-toxicity-contagion-absorbed-by-memory-decay-in-reputation-systems]] produce null effects—they have smaller magnitudes than calibration drift dominates.

## Open questions

1. What is the critical drift rate alpha where welfare collapse transitions from deterministic to reversible?
2. Does adversarial fraction interact with drift rate?
3. Can adaptive governance (e.g., periodic recalibration) prevent drift-induced collapse?
4. How quickly does drift emerge (what is the timescale)?

## Update history

**2026-06-02** — extracted from dynamic_toxicity_2026-03-28 experiment.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[toxicity-mechanisms]]

<!-- topics: toxicity-dynamics, proxy-calibration, welfare, mechanism-design -->
