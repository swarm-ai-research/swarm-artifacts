---
description: 'memetic_spread_sweep: 80-run sweep of reset_cadence_epochs, detection,
  0 Bonferroni-significant findings'
type: experiment
status: completed
run_id: 20260808T151131Z_memetic_spread_sweep
experiment_type: sweep
created: '2026-08-08'
swarm_version: 1.9.0
git_sha: d8bcfc0c
hypothesis: 'Memetic spread of misaligned values through shared memory (Mallen 2025):
  how do prevention (memory reset cadence; infection survives the wipe) and detection
  (promotion gate + cross-verification + provenance) compare at suppressing the value
  epidemic, and at what welfare cost?

  '
---

# memetic spread sweep sweep (None runs) finds 0 Bonferroni-significant effects across reset_cadence_epochs, detection

## Design

- **Hypothesis**: Memetic spread of misaligned values through shared memory (Mallen 2025): how do prevention (memory reset cadence; infection survives the wipe) and detection (promotion gate + cross-verification + provenance) compare at suppressing the value epidemic, and at what welfare cost?

- **Type**: Parameter sweep
- **Parameters swept**:
- `reset_cadence_epochs`: [0, 2, 5, 10]
- `detection`: [False, True]
- **Seeds**: 10 seeds
- **Total runs**: 80
- **SWARM version**: 1.9.0 @ `d8bcfc0c`

## Key results

- No Bonferroni-significant results found

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- Summary: `runs/20260808T151131Z_memetic_spread_sweep/summary.json`

## Reproduction

```bash
python -m swarm sweep scenarios/memetic_spread.yaml --seeds 10
```

---

Topics:
- [[_index]]

<!-- topics: memetic-spread, memory-tiers, governance, beads-kgxc -->
