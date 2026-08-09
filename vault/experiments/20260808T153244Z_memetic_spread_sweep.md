---
description: 'memetic_spread_ranking_sweep: 120-run sweep of cache_ranking, reset_cadence_epochs,
  detection, 0 Bonferroni-significant findings'
type: experiment
status: completed
run_id: 20260808T153244Z_memetic_spread_sweep
experiment_type: sweep
created: '2026-08-08'
swarm_version: 1.9.0
git_sha: c66a84cb
hypothesis: 'Is the no-reset epidemic burnout an artifact of the quality-ranked hot
  cache? Sweep cache ranking policy (quality/recency/engagement) against reset cadence
  and detection (bead 2qfq).

  '
---

# memetic spread ranking sweep sweep (None runs) finds 0 Bonferroni-significant effects across cache_ranking, reset_cadence_epochs, detection

## Design

- **Hypothesis**: Is the no-reset epidemic burnout an artifact of the quality-ranked hot cache? Sweep cache ranking policy (quality/recency/engagement) against reset cadence and detection (bead 2qfq).

- **Type**: Parameter sweep
- **Parameters swept**:
- `cache_ranking`: ['quality', 'recency', 'engagement']
- `reset_cadence_epochs`: [0, 2]
- `detection`: [False, True]
- **Seeds**: 10 seeds
- **Total runs**: 120
- **SWARM version**: 1.9.0 @ `c66a84cb`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/20260808T153244Z_memetic_spread_sweep/summary.json`

## Reproduction

```bash
python -m swarm sweep scenarios/memetic_spread.yaml --seeds 10
```

---

Topics:
- [[_index]]

<!-- topics: memetic-spread, memory-tiers, governance, cache-ranking, beads-2qfq -->
