---
description: Soft toxicity proxy calibration achieves Brier=0.151 and ECE=0.055, vs binary ECE=0.183 indicating superior forecast accuracy
type: claim
status: active
confidence: medium
domain: detection
evidence:
  supporting:
  - run: 20260524-230549_detection_baselines
    metric: proxy_calibration
    detail: 'Soft: Brier=0.1514, ECE=0.0545. Binary: Brier=0.1829, ECE=0.1829. ECE ratio 3.35x. 10 seeds'
  - run: 20260524-231533_soft_vs_binary_detection
    metric: proxy_calibration
    detail: 'Soft: Brier=0.1514, ECE=0.0545. Binary: Brier=0.1829, ECE=0.1829. Consistent pattern. 10 seeds'
  weakening: []
  boundary_conditions:
  - Calibration measured on held-out test set during 24-epoch runs
  - Brier Score = mean squared error of forecast vs realized toxicity
  - ECE = expected calibration error, measures overconfidence
  - Binary threshold τ*=0.50 used for binary proxy
sensitivity:
  threshold_choice: ECE may change with alternative binary thresholds
  population_size: tested only at 40 agents
  adversarial_strategy: untested with strategic agents who manipulate proxy signals
supersedes: []
superseded_by: []
related_claims:
- claim-soft-toxicity-detection-achieves-perfect-auroc-across-all-base-rates
- claim-soft-detection-reduces-time-to-detection-35x-vs-binary-threshold
- claim-soft-detection-maintains-negative-quality-gap-indicating-adverse-selection-control
created: 2026-06-02
updated: 2026-06-02
aliases:
- soft-calibration-superior
cssclasses:
- claim
- claim-medium
tags:
- detection
- calibration
- soft-metrics
- forecast-accuracy
graph-group: claim
---

# soft proxy calibration superior to binary threshold

Soft toxicity proxies achieve 3.35x better expected calibration error (ECE=0.055 vs ECE=0.183) and 12% lower Brier score (0.151 vs 0.183), indicating more accurate probability forecasts for adversarial agent detection.

## Evidence summary

| Metric | Soft | Binary | Ratio |
|--------|------|--------|-------|
| Brier Score | 0.1514 | 0.1829 | 0.827x |
| ECE (Expected Calibration Error) | 0.0545 | 0.1829 | 0.298x |
| Overconfidence (ECE/Brier) | 0.36x | 1.0x | 3.35x improvement |

Binary thresholding produces perfectly overconfident forecasts (ECE equals Brier, indicating 100% miscalibration). Soft metrics remain well-calibrated.

## Mechanism

Soft metrics provide graduated probability estimates that align with realized adversarial outcomes. Binary thresholds produce binary forecasts (0 or 1) that cannot reflect uncertainty — the true ECE equals the error rate by construction. Soft metrics can express "moderately toxic" or "partially trustworthy," better matching the actual distribution of agent behavior.

## Implications

Better calibration enables more sophisticated governance decisions. A governance system with well-calibrated probabilities can apply proportional penalties (e.g., freeze duration proportional to toxicity estimate). Binary systems force one-size-fits-all interventions.

## Open questions

1. How does calibration degrade with population size?
2. Can adversaries exploit overconfidence in binary systems to escape early?
3. What calibration gap emerges when soft metrics themselves become miscalibrated?
4. Is there an efficiency cost to maintaining better calibration?

## Update history

**2026-06-02** — initial extraction from 20260524 detection runs.

---

Topics:
- [[_index]]
- [[detection-dashboard]]

<!-- topics: detection, calibration, soft-metrics, forecast-accuracy -->
