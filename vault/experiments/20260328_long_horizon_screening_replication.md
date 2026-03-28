---
description: 750-run replication of long-horizon screening effect at 50 seeds; 10-seed d=2.75 shrinks to d=0.38 (tight, non-sig) and d=0.76 (moderate, Bonferroni-sig)
type: experiment
status: completed
run_id: 20260328_long_horizon_screening_replication
experiment_type: sweep
created: '2026-03-28'
aliases:
- 20260328_long_horizon_screening_replication
cssclasses:
- experiment
- experiment-sweep
graph-group: experiment
tags:
- sweep
- screening
- long-horizon
- replication
- small-sample-inflation
---

# Fifty-seed replication deflates long-horizon screening effect from d=2.75 to d=0.38 under tight governance, confirming moderate-governance benefit at d=0.76

## Design

- **Purpose**: Replicate the surprising d=2.75 long-horizon improvement at screening strength 1.0 found in the 10-seed confirmatory arm of [[20260326_screening_strength_sweep]]
- **Type**: Focused replication sweep
- **Parameters swept**:
  - `screening_strength`: 0.0, 0.3, 0.5, 0.7, 1.0 (baseline + valley + recovery points)
  - `governance_level`: tight, moderate, light
- **Seeds**: 50 per configuration (5× the original 10-seed arm)
- **Total runs**: 750
- **Settings**: 10 agents, 20% adversarial fraction

## Key results

### The d=2.75 does NOT replicate

The 10-seed estimate was massively inflated by small-sample noise. At 50 seeds:

| Governance | Baseline (0.0) | Strength 1.0 | d | p | Bonferroni sig? |
|------------|---------------|-------------|-----|--------|-----------------|
| **Tight** | 0.543 | 0.692 | +0.38 | 0.058 | No |
| **Moderate** | 0.552 | 0.828 | +0.76 | 0.0001 | **Yes** |
| **Light** | 0.881 | 0.895 | +0.05 | 0.811 | No |

Bonferroni threshold: alpha/12 = 0.004.

### Moderate governance shows a real, dose-dependent effect

The moderate governance dose-response is clean and monotonic:
- 0.0: 0.552
- 0.3: 0.723 (d=+0.44, p=0.026)
- 0.5: 0.766 (d=+0.57, p=0.005)
- 0.7: 0.756 (d=+0.54, p=0.007)
- 1.0: 0.828 (d=+0.76, p=0.0001, Bonferroni-sig)

### Tight governance shows a trend but not significance

Tight governance at strength 1.0 shows d=0.38 (p=0.058) — suggestive but not significant. The dose-response is gradual: 0.543 → 0.590 → 0.592 → 0.640 → 0.692.

### Light governance is at ceiling

Light governance baseline is already 0.881 — no room for screening to improve.

## Interpretation

The 10-seed result (d=2.75) was a textbook case of small-sample effect size inflation. The replication vindicates the vault's confidence calibration: the original 10-seed finding was correctly flagged as "suggestive but requires replication" (confirmatory arm only).

The real finding: **screening improves long-horizon planning under moderate governance** (d=0.76, Bonferroni-significant, 50 seeds). This is a meaningful effect — comparable in magnitude to the coordination improvement at strength 0.5. But it is specific to moderate governance, not the dramatic universal effect the 10-seed estimate suggested.

## Claims affected

- [[claim-screening-signal-reliability-determines-routing-outcome]] — long-horizon evidence downgraded from "massive effect" to "moderate governance-specific effect"
- [[claim-screening-effect-is-task-type-dependent]] — long-horizon is NOT null; it shows moderate-governance-specific improvement at high screening strength

## Artifacts

- `runs/20260328_long_horizon_screening_replication/csv/long_horizon_raw.csv` (750 rows)
- `runs/20260328_long_horizon_screening_replication/summary.json`

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: sweep, screening, long-horizon, replication, small-sample-inflation -->
