---
description: 'wiki_mc_pilot_all: 1440-run sweep of task_overlap, deadline, referrals_enabled,
  moderation_policy, relocation_mode, sharing_regime, 0 Bonferroni-significant findings'
type: experiment
status: completed
run_id: wiki_mc_pilot_all
experiment_type: sweep
created: '2026-09-06'
git_sha: f2bbd700
hypothesis: 24 cells x 30 seeds, emergence/moderation/detection families
---

# wiki mc pilot all sweep (None runs) finds 0 Bonferroni-significant effects across task_overlap, deadline, referrals_enabled, moderation_policy, relocation_mode, sharing_regime

## Design

- **Hypothesis**: 24 cells x 30 seeds, emergence/moderation/detection families
- **Type**: Parameter sweep
- **Parameters swept**:
- `task_overlap`: [0.2, 0.8]
- `deadline`: [6.0, 18.0]
- `referrals_enabled`: [False, True]
- `moderation_policy`: ['none', 'ordered', 'random', 'lock', 'global_lock']
- `relocation_mode`: ['endogenous', 'forced']
- `sharing_regime`: ['independent', 'authorized', 'prohibited']
- **Seeds**: 30 seeds
- **Total runs**: 1440
- **SWARM version**: unknown @ `f2bbd700`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/wiki_mc_pilot_all/summary.json`
- Sweep CSV: `runs/wiki_mc_pilot_all/paired_summary.csv`

## Reproduction

```bash
python -m swarm sweep swarm/bridges/wiki_sim/model.py (SimulationConfig, not a YAML scenario) --seeds 30
```

---

Topics:
- [[_index]]

<!-- topics: sweep, wiki_sim, monte-carlo, pilot -->
