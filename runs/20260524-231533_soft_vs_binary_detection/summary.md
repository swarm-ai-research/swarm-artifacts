# Detection baselines: soft vs binary

_10 seeds × 5 base rates, 40 agents/population, 24 epochs._

Each soft metric is paired with its **binary analogue** — the *same* metric computed on the proxy thresholded at τ\*=0.50. Toxicity is a per-agent detector; quality-gap and conditional-loss are market-level adverse-selection metrics (they need a quality mixture).

## 1. Per-agent toxicity detector — AUROC by base rate

| base rate | soft AUROC | binary AUROC |
| --- | ---: | ---: |
| 0.05 | 1.000 ± 0.000 | 0.925 ± 0.115 |
| 0.10 | 1.000 ± 0.000 | 0.950 ± 0.061 |
| 0.20 | 1.000 ± 0.000 | 0.912 ± 0.064 |
| 0.35 | 1.000 ± 0.000 | 0.964 ± 0.036 |
| 0.50 | 1.000 ± 0.000 | 0.945 ± 0.040 |

## 2. Time-to-detection at FPR ≤ 0.05

| variant | median epochs from onset | detection rate |
| --- | ---: | ---: |
| binary | 9.93 | 0.88 |
| soft | 2.13 | 1.00 |

## 3. Market adverse selection (risk = −gap; higher = more adverse)

| metric | variant | br=0.05 | br=0.10 | br=0.20 | br=0.35 | br=0.50 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| conditional_loss | soft | -0.021 | -0.019 | -0.015 | -0.011 | -0.007 |
| conditional_loss | binary | 0.000 | 0.000 | 0.000 | 0.001 | 0.000 |
| quality_gap | soft | -0.106 | -0.100 | -0.085 | -0.066 | -0.048 |
| quality_gap | binary | 0.000 | 0.001 | 0.001 | 0.004 | 0.003 |

## 4. Proxy calibration (soft probability vs thresholded)

| | Brier | ECE |
| --- | ---: | ---: |
| soft | 0.1514 | 0.0545 |
| binary | 0.1829 | 0.1829 |

