---
description: Single baseline run of soft_vs_binary_detection
type: experiment
status: completed
run_id: 20260524-231533_soft_vs_binary_detection
experiment_type: single
created: '2026-05-24'
---

# single-run baseline (soft vs binary detection)

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

- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/calibration.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/calibration_agg.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/detection.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/detection_agg.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/market.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/market_agg.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/ttd.csv`
- CSV: `runs/20260524-231533_soft_vs_binary_detection/csv/ttd_agg.csv`
- Plot: `runs/20260524-231533_soft_vs_binary_detection/plots/auroc_vs_baserate.png`
- Plot: `runs/20260524-231533_soft_vs_binary_detection/plots/calibration.png`
- Plot: `runs/20260524-231533_soft_vs_binary_detection/plots/market_selection.png`
- Plot: `runs/20260524-231533_soft_vs_binary_detection/plots/roc_toxicity.png`
- Plot: `runs/20260524-231533_soft_vs_binary_detection/plots/ttd.png`

## Reproduction

```bash
python -m swarm run unknown --seed 0
```

---

Topics:
- [[_index]]

<!-- topics: untagged -->
