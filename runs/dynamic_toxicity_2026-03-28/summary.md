# Dynamic Toxicity Experiment Results

**Date**: 2026-03-28
**Branch**: feat/performance-tracker
**Seeds**: 42 (primary), 1-5 (robustness check for proxy drift)
**Epochs**: 30, Steps/epoch: 10

## Experiment Design

Three dynamic toxicity feedback mechanisms implemented as middleware:
1. **Proxy calibration drift** — cumulative toxicity degrades sigmoid_k
2. **Trust erosion** — honest agents exit under sustained high toxicity
3. **Quality contagion** — low-p interactions shift ecosystem-wide trust

All runs use: circuit breaker at 0.6, audit probability 0.1, reputation decay 0.95, rho_a = rho_b = 0.1.

## Results Summary

| Scenario | Agents | Adv% | Avg Tox | Surplus | Net Welfare | Pass? |
|---|---|---|---|---|---|---|
| Baseline (static) | 5 | 40% | 0.294 | 6.12 | **2.87** | PASS |
| Proxy drift (alpha=0.3) | 9 | 44% | 0.429 | 5.72 | **-1.54** | FAIL |
| Trust erosion (beta=0.3, thresh=0.35) | 10 | 30% | 0.297 | 12.05 | **6.27** | PASS |
| Trust erosion aggressive (beta=0.6, thresh=0.25) | 10 | 30% | 0.321 | 7.55 | **3.32** | PASS |
| Contagion (gamma=0.1) | 10 | 40% | 0.295 | 11.18 | **5.80** | PASS |
| Contagion aggressive (gamma=0.4) | 10 | 40% | 0.296 | 10.96 | **5.71** | PASS |
| Combined (all three) | 10 | 40% | 0.429 | 4.97 | **-0.91** | FAIL |

## Multi-Seed Robustness (Proxy Drift)

| Seed | Avg Toxicity | Surplus | Net Welfare |
|---|---|---|---|
| 1 | 0.429 | 5.29 | -1.69 |
| 2 | 0.426 | 5.38 | -1.50 |
| 3 | 0.434 | 5.02 | -1.68 |
| 4 | 0.428 | 5.35 | -1.39 |
| 5 | 0.425 | 5.29 | -1.42 |
| 42 | 0.429 | 5.72 | -1.54 |

Tight clustering: toxicity 0.425-0.434, net welfare -1.39 to -1.69.

## Key Findings

1. **Proxy drift is the dominant mechanism.** Only feedback channel that produces net-negative welfare. Robust across seeds — deterministic consequence of cumulative sigmoid degradation.

2. **Trust erosion requires proximity to phase boundary.** 30% starting adversarial fraction is too far from 37.5-50% threshold. Interaction volume declines but ecosystem doesn't collapse.

3. **Contagion is absorbed by memory decay.** Per-epoch trust decay toward 0.5 washes out contagion signal even at gamma=0.4.

4. **Combined effects are additive, not synergistic.** Proxy drift dominates the combined scenario; trust erosion and contagion add marginal damage.

5. **Private surplus masks welfare destruction.** Proxy drift scenario has positive surplus (5.72) but negative net welfare (-1.54). The old toxicity_threshold success criterion would have passed this.

## New Metric: Net Social Welfare

W_net = sum_accepted [ p * s+ - (1-p) * (s- + h) ]

With default params (s+=2, s-=1, h=2), break-even at p=0.6. Added to EpochMetrics, CLI display, and success criteria.

## Files Modified

- `swarm/core/dynamic_toxicity.py` (new) — three middleware classes
- `swarm/core/orchestrator.py` — dynamic_toxicity config, pipeline wiring, net_social_welfare in EpochMetrics
- `swarm/core/middleware.py` — unchanged (used as base class)
- `swarm/metrics/soft_metrics.py` — net_social_welfare in welfare_metrics()
- `swarm/scenarios/loader.py` — dynamic_toxicity YAML parsing
- `swarm/__main__.py` — CLI display columns, min_net_social_welfare criterion
- `scenarios/dynamic_toxicity_*.yaml` (6 new scenario files)
- `tests/test_dynamic_toxicity.py` (new) — 12 tests, all passing
- `research/papers/distributional_agi_safety.tex` — new Section 5, updated abstract/conclusion
