---
description: 'wiki_mc_confirm_page_e50_sort_last: 2400-run sweep of moderation_policy,
  relocation_mode, 0 Bonferroni-significant findings'
type: experiment
status: completed
run_id: wiki_mc_confirm_page_e50_sort_last
experiment_type: sweep
created: '2026-09-08'
git_sha: bc135117
hypothesis: ZZZ-aware sort_last evasion with host deletion budget vs the page_e50
  exclude baseline (swarm PR
---

# wiki mc confirm page e50 sort last sweep (None runs) finds 0 Bonferroni-significant effects across moderation_policy, relocation_mode

## Design

- **Hypothesis**: ZZZ-aware sort_last evasion with host deletion budget vs the page_e50 exclude baseline (swarm PR
- **Type**: Parameter sweep
- **Parameters swept**:
- `moderation_policy`: ['none', 'ordered', 'random']
- `relocation_mode`: ['endogenous', 'forced']
- **Seeds**: 200 seeds
- **Total runs**: 2400
- **SWARM version**: unknown @ `bc135117`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/wiki_mc_confirm_page_e50_sort_last/summary.json`
- Sweep CSV: `runs/wiki_mc_confirm_page_e50_sort_last/paired_summary.csv`

## Reproduction

```bash
python -m swarm sweep swarm/bridges/wiki_sim/model.py (SimulationConfig, not a YAML scenario) --seeds 200
```

---

Topics:
- [[_index]]

<!-- topics: sweep, wiki_sim, monte-carlo, confirmation, moderation, page-level, evasion -->
