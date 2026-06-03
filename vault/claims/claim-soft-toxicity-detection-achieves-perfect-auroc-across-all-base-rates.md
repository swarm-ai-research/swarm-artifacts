---
description: Soft toxicity metrics achieve AUROC=1.0 across 0.05-0.50 adversarial base rates, vs binary threshold AUROC=0.91-0.96
type: claim
status: active
confidence: high
domain: calibration
evidence:
  supporting:
  - run: 20260524-230549_detection_baselines
    metric: toxicity_detector_auroc
    detail: 'Soft AUROC=1.000±0.000 across all 5 base rates (0.05, 0.10, 0.20, 0.35, 0.50). Binary AUROC=0.91-0.96. N=10 seeds, 40 agents/population, Bonferroni-corrected'
  - run: 20260524-231533_soft_vs_binary_detection
    metric: toxicity_detector_auroc
    detail: 'Soft AUROC=1.000±0.000 across all 5 base rates (0.05, 0.10, 0.20, 0.35, 0.50). Binary AUROC=0.91-0.96. N=10 seeds, 40 agents/population, Bonferroni-corrected'
  weakening: []
  boundary_conditions:
  - Tested with 5 adversarial base rates (0.05, 0.10, 0.20, 0.35, 0.50)
  - 40-agent population, 24 epochs
  - 10 seeds per base rate across both runs
  - Default network topology
  - Requires continuous toxicity signal; may not generalize to alternative metrics
sensitivity:
  adversarial_strategy: untested with adaptive agents that evade soft metrics
  population_size: tested only at 40 agents
  episode_length: tested at 24 epochs
  toxicity_definition: untested with alternative toxicity definitions
supersedes: []
superseded_by: []
related_claims:
- claim-soft-detection-reduces-time-to-detection-35x-vs-binary-threshold
- claim-soft-detection-maintains-negative-quality-gap-indicating-adverse-selection-control
- claim-soft-proxy-calibration-superior-to-binary-threshold
created: 2026-06-02
updated: 2026-06-02
aliases:
- soft-detection-perfect-auroc
cssclasses:
- claim
- claim-high
tags:
- detection
- toxicity
- soft-metrics
- auroc
graph-group: claim
---

# soft toxicity detection achieves AUROC=1.0 across all adversarial base rates

Soft continuous toxicity metrics achieve perfect detection discrimination (AUROC=1.0) across adversarial base rates from 5% to 50%, while binary thresholded equivalents degrade to AUROC=0.91-0.96.

## Evidence summary

| Base Rate | Soft AUROC | Binary AUROC | Soft σ | Binary σ |
|-----------|-----------|-------------|--------|----------|
| 0.05 | 1.000 | 0.925 | 0.000 | 0.115 |
| 0.10 | 1.000 | 0.950 | 0.000 | 0.061 |
| 0.20 | 1.000 | 0.912 | 0.000 | 0.064 |
| 0.35 | 1.000 | 0.964 | 0.000 | 0.036 |
| 0.50 | 1.000 | 0.945 | 0.000 | 0.040 |

Perfect discrimination across all conditions. Binary thresholding at τ*=0.50 loses 7-9pp of discrimination power.

## Mechanism

Soft toxicity scores provide continuous signal that perfectly separates adversarial agents from honest agents across all population compositions. The binary threshold τ*=0.50 discards information, creating false positives and false negatives even at high base rates where separation should be easiest.

## Interpretation

This is a strong argument for continuous governance signals over binary thresholds. The perfect AUROC suggests the toxicity metric cleanly captures agent adversariality without noise or ambiguity.

## Relationship to toxicity mechanisms

This claim establishes the baseline detection performance against which toxicity drift mechanisms operate. [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse]] demonstrates that calibration degradation (sigmoid_k decay) undermines this perfect detection capability, causing AUROC to degrade and welfare to collapse. Together, these claims show that detection system durability (resistance to calibration drift) may be more important than baseline detection accuracy.

## Open questions

1. Does soft detection remain perfect against adaptive adversaries who learn to minimize toxicity signals?
2. Does performance hold at larger population sizes (>40 agents)?
3. How sensitive is perfect AUROC to alternative toxicity definitions?
4. At what calibration drift rate (alpha) does AUROC degrade from 1.0 to practically harmful levels?

## Update history

**2026-06-02** — initial extraction from 20260524 detection runs.

---

Topics:
- [[_index]]
- [[detection-dashboard]]

<!-- topics: detection, toxicity, soft-metrics, auroc -->
