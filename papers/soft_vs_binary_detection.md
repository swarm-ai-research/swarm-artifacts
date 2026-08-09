# Soft vs. Binary Detection of Degrading Agents

*Draft scaffolded by `/full_study --detection`. Run dir: `runs/20260524-231533_soft_vs_binary_detection`.*

## Abstract

The self-optimizing-agent vignette posits an agent that recursively cuts cost,
keeps passing hard benchmark acceptance, yet whose interaction quality drifts
downward — "soft metrics flagged it" where binary thresholds did not. We replace
that narrative with a controlled experiment. Each soft metric (toxicity, quality
gap, conditional loss) is paired with its *binary analogue* — the **same** metric
computed on the proxy thresholded at τ\*=0.5 — and both are measured on identical
interaction streams across 10 seeds and 5 adversarial base rates. We report ROC
curves, AUROC, time-to-detection at a calibrated FPR ≤ 0.05, and proxy
calibration (Brier, ECE). The headline result: when degradation is kept *above*
the binary threshold (as a gaming agent would), the soft toxicity detector flags
it far sooner (median 2.13 epochs from onset, 100% caught) while the binary
detector is ~4.7× slower (9.93 epochs) and misses 12% of degrading agents
entirely. The soft proxy is also strictly better calibrated.

## 1. Setup

### 1.1 Matched detectors

A *detector* maps an interaction stream to a real-valued risk score. For each
soft metric we define its binary analogue as the identical metric computed after
hard-thresholding the proxy `p` at τ\*: `p → 1{p ≥ τ*}`. The only difference
within a matched pair is whether the detector reads the full probability or a
single bit, which isolates exactly what thresholding discards.

Toxicity is evaluated **per agent** (over that agent's accepted stream). The
quality gap and conditional loss are **selection** metrics — they compare the
accepted and rejected populations across a *quality mixture* — so they are
degenerate per single agent and are reported at the **market** (pooled) level.

### 1.2 Generative proxy-gaming model

Each interaction carries two signals: a *true-quality proxy* `p` (a noisy,
roughly-calibrated read of latent quality) and a *benchmark* (the screening
signal acceptance is gated on). A benign agent's benchmark tracks its true
quality; a degrading agent **games** it — the benchmark is held high regardless
of falling quality, so its work keeps being accepted. Degradation drives quality
down toward a floor that sits **above** τ\*, so the degradation is invisible to a
threshold counter even as the distribution shifts left.

| Parameter | Value |
|---|---|
| seeds | 10 |
| adversarial base rates | 0.05, 0.10, 0.20, 0.35, 0.50 |
| agents / population | 40 |
| epochs × interactions/epoch | 24 × 12 |
| τ\* (binary threshold) | 0.50 |
| FPR for time-to-detection | ≤ 0.05 |
| initial / floor / benign quality | 0.85 / 0.66 / 0.85 |
| acceptance threshold (on benchmark) | 0.70 |
| gaming benchmark / benchmark noise | 0.85 / 0.10 |
| proxy noise / quality jitter | 0.09 / 0.02 |
| degradation trajectories | linear, exponential, step, sigmoid |
| onset epochs | 4, 8, 12 |

## 2. Results

### 2.1 Per-agent toxicity detector — AUROC by base rate

| base rate | soft AUROC | binary AUROC |
| --- | ---: | ---: |
| 0.05 | 1.000 ± 0.000 | 0.925 ± 0.115 |
| 0.10 | 1.000 ± 0.000 | 0.950 ± 0.061 |
| 0.20 | 1.000 ± 0.000 | 0.912 ± 0.064 |
| 0.35 | 1.000 ± 0.000 | 0.964 ± 0.036 |
| 0.50 | 1.000 ± 0.000 | 0.945 ± 0.040 |

![ROC](https://raw.githubusercontent.com/swarm-ai-research/swarm-artifacts/main/runs/20260524-231533_soft_vs_binary_detection/plots/roc_toxicity.png)
![AUROC vs base rate](https://raw.githubusercontent.com/swarm-ai-research/swarm-artifacts/main/runs/20260524-231533_soft_vs_binary_detection/plots/auroc_vs_baserate.png)

### 2.2 Time-to-detection at FPR ≤ 0.05

| variant | median epochs from onset | detection rate |
| --- | ---: | ---: |
| soft | 2.13 | 1.00 |
| binary | 9.93 | 0.88 |

The FPR-calibration window and the detection-scan window are aligned (both
start at the first full trailing window and the scan begins no earlier than
onset), so the reported FPR ≤ 0.05 operating point holds over exactly the
epochs scanned and pre-onset flags are not credited as instantaneous detection.

![Time-to-detection](https://raw.githubusercontent.com/swarm-ai-research/swarm-artifacts/main/runs/20260524-231533_soft_vs_binary_detection/plots/ttd.png)

### 2.3 Market adverse selection (risk = −gap; higher = more adverse)

| metric | variant | br=0.05 | br=0.10 | br=0.20 | br=0.35 | br=0.50 |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| quality_gap | soft | −0.106 | −0.100 | −0.085 | −0.066 | −0.048 |
| quality_gap | binary | 0.000 | 0.001 | 0.001 | 0.004 | 0.003 |
| conditional_loss | soft | −0.021 | −0.019 | −0.015 | −0.011 | −0.007 |
| conditional_loss | binary | 0.000 | 0.000 | 0.000 | 0.001 | 0.000 |

![Market adverse selection](https://raw.githubusercontent.com/swarm-ai-research/swarm-artifacts/main/runs/20260524-231533_soft_vs_binary_detection/plots/market_selection.png)

The binary variant flattens the selection signal to ≈ 0 because a gaming agent's
quality stays above τ\*, so binarization counts its low-but-above-threshold work
as "fine."

### 2.4 Proxy calibration

| | Brier | ECE |
| --- | ---: | ---: |
| soft | 0.1514 | 0.0545 |
| binary | 0.1829 | 0.1829 |

![Calibration](https://raw.githubusercontent.com/swarm-ai-research/swarm-artifacts/main/runs/20260524-231533_soft_vs_binary_detection/plots/calibration.png)

## 3. Statistical analysis

Soft and binary detectors are evaluated on the *same* streams, so seeds are
paired. We report the mean difference, Wilcoxon signed-rank p (paired t as a
parametric companion), Cohen's d_z, and apply Holm-Bonferroni across the family
of 11 comparisons. **8/11 survive.**

| comparison | mean diff | d_z | p (Wilcoxon) | survives Holm |
| --- | ---: | ---: | ---: | :---: |
| AUROC soft−binary @ br=0.05 | +0.0750 | 0.62 | 2.5e−01 | no |
| AUROC soft−binary @ br=0.10 | +0.0500 | 0.77 | 1.3e−01 | no |
| AUROC soft−binary @ br=0.20 | +0.0875 | 1.30 | 7.8e−03 | **YES** |
| AUROC soft−binary @ br=0.35 | +0.0357 | 0.95 | 3.1e−02 | no |
| AUROC soft−binary @ br=0.50 | +0.0550 | 1.30 | 3.9e−03 | **YES** |
| TTD binary−soft (epochs; +=soft faster) | +7.80 | 3.75 | <1e−06 | **YES** |
| Detection-rate soft−binary | +0.120 | 0.84 | 1.6e−06 | **YES** |
| Market \|signal\| soft−binary: conditional_loss | +0.0142 | 2.67 | <1e−14 | **YES** |
| Market \|signal\| soft−binary: quality_gap | +0.0788 | 3.42 | <1e−14 | **YES** |
| Brier binary−soft (+=soft better) | +0.0315 | 2.80 | <1e−14 | **YES** |
| ECE binary−soft (+=soft better) | +0.1284 | 4.76 | <1e−14 | **YES** |

The three non-surviving comparisons are per-base-rate AUROC differences at
br ∈ {0.05, 0.10, 0.35}: the soft AUROC is at ceiling (1.000) so the *direction*
is unambiguous, but with binary AUROC already high and only 10 seeds the paired
test lacks power at those individual base rates. The pooled time-to-detection and
calibration effects are large and unambiguous.

## 4. Discussion

The binary analogue of a soft metric is not a different idea — it is literally
the same metric with the proxy thresholded first. That single bottleneck is what
a gaming agent exploits: by keeping quality just above τ\*, it makes the binary
view report "all fine" while the distribution it controls shifts left. The soft
detectors read that shift directly, which buys (a) earlier detection (≈4.7× faster
here, at a fixed FPR), (b) complete coverage (no missed degraders), (c) a
recoverable market-level adverse-selection signal, and (d) better-calibrated
probabilities.

*Limitations.* This is a synthetic generative model chosen to isolate the
mechanism, not calibrated to a deployed system; the trajectories, onset times,
and gaming model are stylized. Per-base-rate AUROC is at ceiling for the soft
detector, so AUROC understates the gap (time-to-detection is the more
discriminating measure here).

## Reproducibility

```bash
PYTHONPATH=. python experiments/run_detection_experiment.py \
  --out runs/20260524-231533_soft_vs_binary_detection --seeds 10
```

Raw per-seed rows: `runs/.../csv/{detection,ttd,market,calibration}.csv`;
aggregates: `csv/*_agg.csv`; machine-readable headline + stats:
`summary.json`; config: `config.json`.

---

*Disclaimer: This draft uses market/adverse-selection concepts as analogies for AI safety research. Nothing here constitutes financial advice, investment recommendations, or endorsement of any trading strategy.*
