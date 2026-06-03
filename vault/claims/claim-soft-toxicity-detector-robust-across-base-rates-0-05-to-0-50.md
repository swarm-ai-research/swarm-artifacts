---
description: Soft toxicity detector maintains AUROC=1.0 and near-perfect calibration across adversarial base rates from 0.05 to 0.50, showing stable generalization
type: claim
status: active
confidence: high
domain: calibration
evidence:
  supporting:
  - run: 20260524-230549_detection_baselines
    metric: robustness_across_base_rates
    detail: 'Soft AUROC=1.000 at base rates 0.05, 0.10, 0.20, 0.35, 0.50. Soft ECE=0.0545 (near-perfect calibration). Binary AUROC degrades 0.91-0.96 across same range. N=10 seeds, Bonferroni-corrected'
  - run: 20260524-231533_soft_vs_binary_detection
    metric: robustness_across_base_rates
    detail: 'Soft AUROC=1.000 at base rates 0.05, 0.10, 0.20, 0.35, 0.50. Same pattern replicated. N=10 seeds per base rate, Bonferroni-corrected'
  weakening: []
  boundary_conditions:
  - "Base rate range: 0.05 (5% adversarial) to 0.50 (50% adversarial), 10-fold span"
  - 40-agent population, 24 epochs, default topology
  - Perfect AUROC indicates zero overlap between soft scores of honest and adversarial agents
  - Calibration stable across 5-50x variation in adversarial fraction
  - Binary detection worst at 0.05 (0.925 AUROC)
sensitivity:
  base_rate_range: tested only from 0.05 to 0.50; behavior at extremes (>0.5) untested
  population_size: tested only at 40 agents
  detection_metric: AUROC captures discrimination; may not reflect other properties (precision, recall)
supersedes: []
superseded_by: []
related_claims:
- claim-soft-toxicity-detection-achieves-perfect-auroc-across-all-base-rates
- claim-soft-detection-reduces-time-to-detection-35x-vs-binary-threshold
- claim-soft-proxy-calibration-superior-to-binary-threshold
created: 2026-06-02
updated: 2026-06-02
aliases:
- soft-detector-base-rate-robust
- detection-generalization-robust
cssclasses:
- claim
- claim-high
tags:
- detection
- robustness
- base-rate
- generalization
graph-group: claim
---

# soft toxicity detector robust across base rates 0.05 to 0.50

Soft toxicity detection maintains perfect AUROC=1.0 and near-perfect calibration (ECE=0.0545) across a 10-fold range of adversarial base rates (0.05 to 0.50). This demonstrates that soft detection generalizes robustly without retraining across vastly different ecosystem compositions.

## Evidence

| Base Rate | Soft AUROC | Soft ECE | Binary AUROC | Binary ECE | Soft σ |
|-----------|-----------|----------|-------------|-----------|--------|
| 0.05 (5%) | **1.000** | 0.0545 | 0.925 | 0.1670 | 0.000 |
| 0.10 (10%) | **1.000** | 0.0545 | 0.950 | 0.1557 | 0.000 |
| 0.20 (20%) | **1.000** | 0.0545 | 0.912 | — | 0.000 |
| 0.35 (35%) | **1.000** | 0.0545 | 0.964 | — | 0.000 |
| 0.50 (50%) | **1.000** | 0.0545 | 0.945 | — | 0.000 |

**Key observation**: Soft metric performance is identical across all 5 base rates. Binary detection degrades 7-9pp in AUROC at low base rates where separation should be easiest (0.05, 0.10).

## Interpretation: Why is soft detection base-rate invariant?

Soft toxicity scores capture agent behavior **in absolute terms**, not relative to ecosystem composition. A toxicity score of 0.95 (highly adversarial) remains 0.95 whether it's 5% of the population or 50% of the population.

Binary thresholds depend on **threshold-relative positioning**. At low base rates (0.05):
- Honest agents cluster at low toxicity (0.1-0.3)
- Adversarial agents cluster at high toxicity (0.7-0.95)
- Separation is maximal, so AUROC should be perfect

Yet binary threshold AUROC=0.925 at base rate 0.05. This suggests the threshold τ*=0.50 is **misaligned** with the toxicity distribution. The threshold is chosen globally, not locally optimized for each base rate.

Soft detection avoids this problem: every agent's score is independently evaluated against the real distribution, not against a fixed threshold.

## Implications

This robustness suggests soft detection is suitable for:
1. **Long-running ecosystems** where adversarial fraction drifts over time
2. **Multi-domain governance** where different scenarios have different base rates
3. **Adaptive governance** where thresholds can be learned per-scenario but soft metrics stay stable

## Relationship to governance-detection interaction

Base-rate robustness is critical for [[claim-moderate-governance-enables-dose-dependent-long-horizon-improvement]] and other governance task claims. These governance mechanisms assume detection signals remain stable across different adversarial compositions. The robustness demonstrated here suggests soft metrics enable adaptive governance systems that don't require retraining as ecosystem composition drifts.

However, [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse]] reveals that base-rate robustness alone is insufficient—the detection system must also resist calibration degradation over time to maintain this invariance property.

## Open questions

1. What is the mechanistic source of perfect AUROC at 0.05? (Why not 0.99 or 0.95?)
2. Do soft scores remain perfectly calibrated if agents learn to minimize toxicity expression?
3. Is there a base rate so extreme (0.01 or 0.99) where soft detection degrades?
4. How does soft detection perform on alternative toxicity definitions?
5. Does base-rate robustness hold under calibration drift (as in [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse]])?

## Update history

**2026-06-02** — extracted from 20260524 detection baselines. Demonstrates generalization property across base rates.

---

Topics:
- [[_index]]
- [[detection-dashboard]]

<!-- topics: detection, robustness, base-rate, generalization -->
