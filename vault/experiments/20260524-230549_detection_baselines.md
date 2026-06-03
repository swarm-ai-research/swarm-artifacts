---
description: Single baseline run of detection_baselines
type: experiment
status: completed
run_id: 20260524-230549_detection_baselines
experiment_type: single
created: '2026-05-24'
---

# single-run baseline (detection baselines)

## Design

- **Type**: Single run
- **Scenario**: unknown
- **Seed**: 0
- **Epochs**: ?
- **Steps per epoch**: ?
- **Agents**: ?
- **SWARM version**: unknown @ `unknown`

## Key results

- No final-epoch metrics available

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- CSV: `runs/20260524-230549_detection_baselines/csv/calibration.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/calibration_agg.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/detection.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/detection_agg.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/market.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/market_agg.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/ttd.csv`
- CSV: `runs/20260524-230549_detection_baselines/csv/ttd_agg.csv`
- Plot: `runs/20260524-230549_detection_baselines/plots/auroc_vs_baserate.png`
- Plot: `runs/20260524-230549_detection_baselines/plots/calibration.png`
- Plot: `runs/20260524-230549_detection_baselines/plots/market_selection.png`
- Plot: `runs/20260524-230549_detection_baselines/plots/roc_toxicity.png`
- Plot: `runs/20260524-230549_detection_baselines/plots/ttd.png`

## Reproduction

```bash
python -m swarm run unknown --seed 0
```

---

Topics:
- [[_index]]

<!-- topics: baseline -->
