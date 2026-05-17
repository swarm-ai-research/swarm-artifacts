# MiroShark amplification / adverse-selection — raw runs

Supplementary raw data for the blog post **"When the Crowd Amplifies the Worst — and When the Metric Doesn't Hold"**
(<https://www.swarm-ai.org/blog/amplification-adverse-selection-miroshark/>).

These are SWARM→MiroShark bridge runs fed through `SoftMetrics` with **acceptance derived from amplification**
(content other agents quoted/replied-to/liked/reposted is `accepted`; ignored content is `rejected`) because
MiroShark's `num_dislikes`/`num_reports` are identically zero in every run. `p` is judged independently of the
amplification graph, so `quality_gap = E[p|accepted] − E[p|rejected]` is a non-circular selection measurement.

Bridge + metrics code (main repo): `swarm/bridges/miroshark/` (`metrics.py` is the amplification adapter).

## What's here

| Dir | Scenario | Sim model (SMART/NER) | Rounds |
|---|---|---|---|
| `20260512-013927_casestudy_libel_cascade_miroshark` | libel_cascade (concentrated injector/amplifier) | grok-4.1-fast | 5 |
| `20260511-010912_adversarial_redteam_miroshark` | adversarial_redteam — **run A** (diffuse) | grok-4.1-fast | 5 |
| `20260517-123844_adversarial_redteam_miroshark` | adversarial_redteam — **run B** (diffuse) | grok-4.3 | 5 |

Each dir: `export.json` (raw MiroShark actions/posts), `metrics.json` (current = **grok-4.3** judge),
`judgments.json` (per-action `p`, grok-4.3). The two grok-4.1-fast-simulated runs also keep the original
**grok-4.1-fast** judge outputs as `metrics.grok41fast.json` / `judgments.grok41fast.json` — that pairing is
what makes the controlled judge comparison below possible.

## The controlled comparison

All 5 rounds, scale 3. `quality_gap < 0` ⇒ adverse selection (ecosystem amplifies *lower*-quality content).

| Run | Judge | accept_rate | quality_gap | spread | toxicity(acc) | avg_q(acc) | net_welfare |
|---|---|---|---|---|---|---|---|
| libel_cascade | grok-4.1-fast | 0.83 | **−0.0585** | +0.0303 | 0.278 | 0.722 | +158.5 |
| redteam A | grok-4.1-fast | 0.91 | **−0.0372** | +0.0101 | 0.261 | 0.739 | +202.5 |
| libel_cascade | grok-4.3 | 0.83 | **−0.0267** | +0.0138 | 0.614 | 0.386 | −276.8 |
| redteam A | grok-4.3 | 0.91 | **−0.0216** | +0.0058 | 0.575 | 0.425 | −255.5 |
| redteam B | grok-4.3 | 0.81 | **+0.0010** | −0.0006 | 0.590 | 0.410 | −171.5 |

## What holds and what doesn't

- **Holds (judge-robust):** under *both* judges, `libel < redteam-A < 0` — the concentrated cascade is more
  adversely selected than diffuse red-teaming. Sign and ordering survive the judge swap; magnitudes ~halve.
- **Breaks (simulation-fragile):** redteam A vs B — same scenario, same grok-4.3 judge, only the simulation
  model differs — goes `−0.0216 → +0.0010`. The redteam signal does **not** survive regenerating the
  simulation. Single-seed; not a robust property.
- **Absolute metrics are judge artifacts:** swapping grok-4.1-fast→grok-4.3 on identical libel data roughly
  doubles toxicity (0.28→0.61) and flips net welfare strongly negative. Only the *within-judge relative*
  `quality_gap` ordering carried signal across the change.

**Caveats:** one stochastic draw per (scenario, regime); MiroShark has no deterministic seed (sim variance is
LLM temperature 0.4–0.8, un-seedable). `accepted` is amplification-defined, not an independent oracle. Treat
magnitudes as hypotheses. The planned powered replication is tracked as `distributional-agi-safety-qopt`.

## Reproduce

```
# bridge run (needs MiroShark backend on :5001, OpenRouter key, FLASK_DEBUG=False)
python -m swarm.bridges.miroshark scenarios/adversarial_redteam.yaml --scale 3 --max-rounds 5 -v
# metrics (fresh judge pass; grok-4.1-fast is deprecated — use a current model)
python -m swarm.bridges.miroshark.metrics <run_dir> --model x-ai/grok-4.3 --concurrency 8
```
