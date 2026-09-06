---
description: 'wiki_board_sweep: 120-run sweep of mode, detection, write_pref, side_host_attention,
  side_teardown_policy, side_evasion_rate, 0 Bonferroni-significant findings'
type: experiment
status: completed
run_id: 20260904T210021Z_wiki_board_sweep
experiment_type: sweep
created: '2026-09-04'
git_sha: a59b7ab4
---

# wiki board sweep sweep (None runs) finds 0 Bonferroni-significant effects across mode, detection, write_pref, side_host_attention, side_teardown_policy, side_evasion_rate

## Design

- **Hypothesis**: Not recorded
- **Type**: Parameter sweep
- **Parameters swept**:
- `mode`: ['deletion', 'revocation']
- `detection`: [0.05]
- `write_pref`: [0.7]
- `side_host_attention`: [None]
- `side_teardown_policy`: ['complete', 'ordered', 'random']
- `side_evasion_rate`: [0.0, 0.5]
- **Seeds**: 10 seeds
- **Total runs**: 120
- **SWARM version**: unknown @ `a59b7ab4`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/20260904T210021Z_wiki_board_sweep/summary.json`
- Sweep CSV: `runs/20260904T210021Z_wiki_board_sweep/sweep.csv`

## Reproduction

```bash
python -m swarm sweep scenarios/wiki_board.yaml --seeds 10
```

---

Topics:
- [[_index]]

<!-- topics: sweep, wiki_board, side_channel, pi02 -->
