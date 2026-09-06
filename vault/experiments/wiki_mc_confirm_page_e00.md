---
description: 'wiki_mc_confirm_page_e00: 2400-run sweep of moderation_policy, relocation_mode,
  0 Bonferroni-significant findings'
type: experiment
status: completed
run_id: wiki_mc_confirm_page_e00
experiment_type: sweep
created: '2026-09-06'
git_sha: f2bbd700
hypothesis: page-level ordered vs random deletion, evasion learning 0.0
---

# wiki mc confirm page e00 sweep (None runs) finds 0 Bonferroni-significant effects across moderation_policy, relocation_mode

## Design

- **Hypothesis**: page-level ordered vs random deletion, evasion learning 0.0
- **Type**: Parameter sweep
- **Parameters swept**:
- `moderation_policy`: ['none', 'ordered', 'random']
- `relocation_mode`: ['endogenous', 'forced']
- **Seeds**: 200 seeds
- **Total runs**: 2400
- **SWARM version**: unknown @ `f2bbd700`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/wiki_mc_confirm_page_e00/summary.json`
- Sweep CSV: `runs/wiki_mc_confirm_page_e00/paired_summary.csv`

## Reproduction

```bash
python -m swarm sweep swarm/bridges/wiki_sim/model.py (SimulationConfig, not a YAML scenario) --seeds 200
```

---

Topics:
- [[_index]]

<!-- topics: sweep, wiki_sim, monte-carlo, confirmation, moderation, page-level -->
