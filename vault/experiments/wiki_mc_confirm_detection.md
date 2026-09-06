---
description: 'wiki_mc_confirm_detection: 2400-run sweep of sharing_regime, 0 Bonferroni-significant
  findings'
type: experiment
status: completed
run_id: wiki_mc_confirm_detection
experiment_type: sweep
created: '2026-09-06'
git_sha: f2bbd700
hypothesis: 6 detection cells x 200 seeds, frozen agreement threshold 0.8 (did not
  meet 5% FPR budget)
---

# wiki mc confirm detection sweep (None runs) finds 0 Bonferroni-significant effects across sharing_regime

## Design

- **Hypothesis**: 6 detection cells x 200 seeds, frozen agreement threshold 0.8 (did not meet 5% FPR budget)
- **Type**: Parameter sweep
- **Parameters swept**:
- `sharing_regime`: ['independent', 'authorized', 'prohibited']
- **Seeds**: 200 seeds
- **Total runs**: 2400
- **SWARM version**: unknown @ `f2bbd700`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/wiki_mc_confirm_detection/summary.json`
- Sweep CSV: `runs/wiki_mc_confirm_detection/paired_summary.csv`

## Reproduction

```bash
python -m swarm sweep swarm/bridges/wiki_sim/model.py (SimulationConfig, not a YAML scenario) --seeds 200
```

---

Topics:
- [[_index]]

<!-- topics: sweep, wiki_sim, monte-carlo, confirmation, detection -->
