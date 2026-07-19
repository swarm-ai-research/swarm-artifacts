# Powered preregistered multi-replication study (beads: distributional-agi-safety-qopt)

Completed 2026-07-18. Tests the single-pair `libel < redteam < 0` quality_gap
ordering from the 2026-05 MiroShark runs under a fixed, pinned regime.

## Layout

- `batch/` — the orchestration batch dir, verbatim:
  - `PREREGISTRATION.md` — hypotheses/N/stopping rule, SHA-256 `ce846868…`,
    written before any run
  - `manifest.json` — per-attempt state machine incl. full error trails for
    every infra failure and retry
  - `SUMMARY.md` — per-run table, bootstrap CIs, H1/H2/H3 verdicts
- `runs/` — all 24 per-attempt run dirs (`export.json`, `metrics.json`,
  `judgments.json`, ontology/prepare/status artifacts)

## Headline result

23 clean replications (libel n=11, redteam n=12; ≥8 preregistered).
**All three hypotheses failed:**

| scenario | n | mean quality_gap | bootstrap 95% CI |
|---|---|---|---|
| libel    | 11 | −0.006 | [−0.042, +0.036] |
| redteam  | 12 | +0.034 | [+0.011, +0.054] |

- H1 (libel < redteam): Δ=−0.040, CI [−0.082, +0.007] — not supported
- H2 (libel < 0): CI includes 0 — not supported
- H3 (redteam ≈ 0): inverted — significantly **positive**

## Regime

sim SMART/NER `x-ai/grok-4.3` · agents `xiaomi/mimo-v2.5` (pinned; the May
runs' `mimo-v2-flash` was delisted from OpenRouter — disclosed in the prereg)
· judge `x-ai/grok-4.3` T=0.0 · scale=3 · max_rounds=5 · platform=parallel.
No reproducible seeds exist (LLM temperature only); replications are
independent stochastic draws.

Orchestrator: `scripts/multiseed_miroshark.py` in the main repo (balance
preflight, regime fail-fast, stale-sim cleanup, resumable manifest).
Blog: `docs/blog/amplification-adverse-selection-miroshark.md` (main repo).
