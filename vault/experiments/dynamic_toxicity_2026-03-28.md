---
description: Single baseline run of dynamic_toxicity_2026-03-28
type: experiment
status: completed
run_id: dynamic_toxicity_2026-03-28
experiment_type: single
created: '2026-06-02'
---

# single-run baseline (dynamic toxicity 2026-03-28)

## Design

- **Type**: Single run
- **Scenario**: unknown
- **Seed**: 0
- **Epochs**: ?
- **Steps per epoch**: ?
- **Agents**: ?
- **SWARM version**: unknown @ `unknown`

## Key results

- No final-epoch metrics available

## Claims affected

No claims with >=2 tag overlap found.

## Artifacts

- CSV: `runs/dynamic_toxicity_2026-03-28/csv/baseline/baseline_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/baseline/baseline_epochs.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/combined/dynamic_toxicity_combined_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/combined/dynamic_toxicity_combined_epochs.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/contagion/dynamic_toxicity_contagion_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/contagion/dynamic_toxicity_contagion_epochs.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/contagion_aggressive/dynamic_toxicity_contagion_aggressive_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/contagion_aggressive/dynamic_toxicity_contagion_aggressive_epochs.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/proxy_drift/dynamic_toxicity_proxy_drift_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/proxy_drift/dynamic_toxicity_proxy_drift_epochs.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/trust_erosion/dynamic_toxicity_trust_erosion_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/trust_erosion/dynamic_toxicity_trust_erosion_epochs.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/trust_erosion_aggressive/dynamic_toxicity_trust_erosion_aggressive_agents.csv`
- CSV: `runs/dynamic_toxicity_2026-03-28/csv/trust_erosion_aggressive/dynamic_toxicity_trust_erosion_aggressive_epochs.csv`

## Reproduction

```bash
python -m swarm run unknown --seed 0
```

---

Topics:
- [[_index]]

<!-- topics: untagged -->
