---
description: Soft detection maintains negative quality gap across base rates (−0.048 to −0.106), indicating sustained adverse selection control; binary achieves ~0 gap
type: claim
status: active
confidence: medium
domain: detection
evidence:
  supporting:
  - run: 20260524-230549_detection_baselines
    metric: quality_gap
    detail: 'Soft quality gap ranges −0.048 to −0.106 across base rates. Binary gap ≈0 (−0.001 to +0.004). Gap indicates how much honest agents outperform adversarial on quality. 10 seeds'
  - run: 20260524-231533_soft_vs_binary_detection
    metric: quality_gap
    detail: 'Soft quality gap ranges −0.048 to −0.106. Binary ≈0. Consistent pattern. 10 seeds'
  weakening: []
  boundary_conditions:
  - Quality gap defined as (honest_quality - adversarial_quality) in accepted transactions
  - Requires sufficient quality mixture for reliable measurement
  - Tested at 5 base rates from 5% to 50% adversarial fraction
  - Gap magnitude varies with base rate but direction (negative) is consistent
sensitivity:
  quality_metric: gap definition depends on underlying quality model
  adverse_selection_strength: untested at higher adversarial fractions
  governance_regime: tested with soft detection only
supersedes: []
superseded_by: []
related_claims:
- claim-soft-toxicity-detection-achieves-perfect-auroc-across-all-base-rates
- claim-soft-detection-reduces-time-to-detection-35x-vs-binary-threshold
- claim-soft-proxy-calibration-superior-to-binary-threshold
created: 2026-06-02
updated: 2026-06-02
aliases:
- soft-detection-quality-gap-control
cssclasses:
- claim
- claim-medium
tags:
- detection
- quality-gap
- adverse-selection
- soft-metrics
graph-group: claim
---

# soft detection maintains negative quality gap indicating adverse selection control

Soft toxicity detection sustains a negative quality gap of −0.048 to −0.106 (honest agents outperform adversarial on quality), indicating that soft detection successfully controls adverse selection. Binary thresholding eliminates this gap (approaches 0), suggesting loss of quality differentiation.

## Evidence summary

| Base Rate | Soft Quality Gap | Binary Quality Gap | Gap differential |
|-----------|-----------------|------------------|-----------------|
| 0.05 | −0.106 | 0.000 | −0.106 |
| 0.10 | −0.100 | 0.001 | −0.101 |
| 0.20 | −0.085 | 0.001 | −0.086 |
| 0.35 | −0.066 | 0.004 | −0.070 |
| 0.50 | −0.048 | 0.003 | −0.051 |

Soft detection consistently separates honest quality from adversarial quality. Binary thresholding loses this separation entirely.

## Mechanism

Soft detection continuously monitors agent behavior quality. Adversarial agents who slip through are caught early before accumulating enough quality-damaging transactions to reverse the gap. Binary thresholds accept the first agent to cross τ*=0.50, regardless of subsequent behavior quality.

## Interpretation

The persistent negative gap under soft detection indicates the system is not just detecting adversaries faster (as per [[claim-soft-detection-reduces-time-to-detection-35x-vs-binary-threshold]]), but is also preventing contamination of the quality distribution. Binary thresholding's ~0 gap suggests adversarial contamination.

## Open questions

1. Does the gap remain negative at higher adversarial fractions (>50%)?
2. How does gap vary with the underlying quality definition?
3. Is there a causal connection between fast detection and quality gap maintenance?
4. Can adversaries strategically perform high-quality transactions to obscure toxicity signal?

## Update history

**2026-06-02** — initial extraction from 20260524 detection runs.

---

Topics:
- [[_index]]
- [[detection-dashboard]]

<!-- topics: detection, quality-gap, adverse-selection, soft-metrics -->
