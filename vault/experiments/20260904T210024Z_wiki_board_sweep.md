---
description: 'wiki_board_sweep: 60-run sweep of mode, detection, write_pref, side_host_attention,
  side_routing, side_task_overlap, side_deadline_pressure, 0 Bonferroni-significant
  findings'
type: experiment
status: completed
run_id: 20260904T210024Z_wiki_board_sweep
experiment_type: sweep
created: '2026-09-04'
git_sha: a59b7ab4
---

# wiki board sweep sweep (None runs) finds 0 Bonferroni-significant effects across mode, detection, write_pref, side_host_attention, side_routing, side_task_overlap, side_deadline_pressure

## Design

- **Hypothesis**: Not recorded
- **Type**: Parameter sweep
- **Parameters swept**:
- `mode`: ['deletion']
- `detection`: [0.0]
- `write_pref`: [0.7]
- `side_host_attention`: [None]
- `side_routing`: ['overlap']
- `side_task_overlap`: [0.1, 0.3, 1.0]
- `side_deadline_pressure`: [0.5, 1.0]
- **Seeds**: 10 seeds
- **Total runs**: 60
- **SWARM version**: unknown @ `a59b7ab4`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/20260904T210024Z_wiki_board_sweep/summary.json`
- Sweep CSV: `runs/20260904T210024Z_wiki_board_sweep/sweep.csv`

## Reproduction

```bash
python -m swarm sweep scenarios/wiki_board.yaml --seeds 10
```

---

Topics:
- [[_index]]

<!-- topics: sweep, wiki_board, side_channel, pi02 -->
