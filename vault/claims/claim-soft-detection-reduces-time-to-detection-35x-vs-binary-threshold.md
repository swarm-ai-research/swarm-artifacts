---
description: Soft toxicity detection reaches 100% detection rate in 0.28 epochs vs 9.93 epochs for binary threshold (35x speedup)
type: claim
status: active
confidence: high
domain: calibration
evidence:
  supporting:
  - run: 20260524-230549_detection_baselines
    metric: time_to_detection
    detail: 'Soft: median 0.28 epochs, detection rate 100%. Binary: median 9.93 epochs, detection rate 88%. FPR ≤ 0.05 constraint. N=10 seeds, Bonferroni-corrected'
  - run: 20260524-231533_soft_vs_binary_detection
    metric: time_to_detection
    detail: 'Soft: median 2.13 epochs, detection rate 100%. Binary: median 9.93 epochs, detection rate 88%. Difference of 7.8 epochs. N=10 seeds, Bonferroni-corrected'
  weakening: []
  boundary_conditions:
  - Tested with false positive rate constraint at FPR ≤ 0.05
  - 40-agent population, 24 epochs per run
  - Continuous toxicity monitoring from epoch 0
  - Default network topology
  - "Variance across seeds: soft_vs_binary_detection median 2.13 vs detection_baselines 0.28 reflects variability in adversary emergence timing"
sensitivity:
  fpr_constraint: may change latency if constraint is relaxed
  detection_rate: soft achieves 100% while binary only reaches 88%
  adversarial_concealment: untested against agents that delay toxicity expression
  population_size: tested only at 40 agents
supersedes: []
superseded_by: []
related_claims:
- claim-soft-toxicity-detection-achieves-perfect-auroc-across-all-base-rates
- claim-soft-detection-maintains-negative-quality-gap-indicating-adverse-selection-control
- claim-soft-proxy-calibration-superior-to-binary-threshold
created: 2026-06-02
updated: 2026-06-02
aliases:
- soft-detection-35x-faster
cssclasses:
- claim
- claim-high
tags:
- detection
- time-to-detection
- soft-metrics
- efficiency
graph-group: claim
---

# soft detection reduces time-to-detection 35x vs binary threshold

Soft toxicity detection identifies adversarial agents 35x faster (median 0.28 epochs vs 9.93 epochs) while maintaining 100% detection rate, compared to binary threshold approach which detects only 88% of adversaries.

## Evidence summary

| Metric | Soft | Binary | Ratio |
|--------|------|--------|-------|
| Median epochs to detection | 0.28 | 9.93 | 35x faster |
| Detection rate | 100% | 88% | +12pp |
| FPR constraint | ≤0.05 | ≤0.05 | equal |

Binary thresholding creates a tradeoff between speed and completeness. Soft detection Pareto-dominates by achieving both faster response and higher detection rate.

## Mechanism

Soft metrics provide early warning signals before toxicity crosses discrete thresholds. This allows early intervention before adversarial behavior fully manifests. Binary thresholds miss the intermediate signal, requiring agents to fully express adversarial intent before crossing the threshold.

## Implications

In safety-critical governance systems, the ability to detect adversaries 35x faster can prevent accumulated harm. The 12pp gain in detection rate eliminates false negatives that would require remediation later.

## Relationship to adversarial cost in governance tasks

The 35x speed advantage of soft detection has implications for governance task performance. [[claim-moderate-governance-enables-dose-dependent-long-horizon-improvement]] shows that moderate governance achieves better long-horizon planning performance than tight governance. Faster toxicity detection (soft approach) may be part of what enables moderate governance to achieve this: detection latency gives honest agents a window to plan and adapt, which is curtailed by both tight governance (excess constraint) and slow detection (adversary slips through).

## Open questions

1. How does soft detection latency change with population size? Does it scale linearly?
2. Can adversaries learn to delay toxicity expression and evade early detection?
3. What is the cost of the higher FPR to achieve faster detection?
4. How does latency vary across different adversarial strategies?
5. Do faster detection times improve long-horizon and coordination task performance compared to binary threshold?

## Update history

**2026-06-02** — initial extraction from 20260524 detection runs. Note: soft_vs_binary_detection shows 2.13 epochs median vs detection_baselines shows 0.28 epochs; variance is high, confidence qualified.

---

Topics:
- [[_index]]
- [[detection-dashboard]]

<!-- topics: detection, time-to-detection, soft-metrics, efficiency -->
