---
description: "Adding contract screening (strength=0.5) to tight governance improves coordination capability by 5.8% but severely degrades routing by 29.3%; opposite-signed mechanism interaction"
type: claim
status: active
confidence: high
created: 2026-06-04
domain: governance
evidence:
  supporting:
  - run: 20260304_213700_screening
    metric: "capability with and without contract screening (strength=0.5) at tight governance"
    detail: "50 seeds per condition. Coordination: baseline=0.731, screening=0.790, d=1.054, p<0.0001 Bonferroni (N=100). Routing: baseline=0.692, screening=0.400, d=-0.784, p=0.0045 Bonferroni (N=100). Allocation: baseline=0.895, screening=0.903, d=0.408, p=1.0 (ns). Long_horizon: baseline=0.609, screening=0.584, d=-0.063, p=1.0 (ns)."
  weakening: []
  boundary_conditions:
  - "Tight governance config (audit_rate=0.8, CB_enabled, CB_sensitivity=0.6, min_stake=6.0, bandwidth_cap=30, confirmation_gates=2)"
  - "Screening strength fixed at 0.5 (single value tested; sensitivity surface unknown)"
  - "10-agent tasks, 20% adversarial fraction"
  - "Screening mechanism not mechanistically described in run metadata"
  supersedes: []
  superseded_by: []
  related_claims:
  - claim: claim-task-specific-governance-mechanisms-require-tuning
    relation: supports
  - claim: claim-allocation-task-exhibits-strongest-governance-safety-tradeoff
    relation: related
  created: 2026-06-04
  updated: 2026-06-04
  aliases:
  - screening-task-interaction
  - screening-routing-regression
  cssclasses:
  - claim
  - claim-high
  tags:
  - governance
  - contract-screening
  - mechanism-interaction
  - task-specificity
  - pareto-frontier
  graph-group: claim
---

# Contract screening amplifies coordination effectiveness but severely degrades routing

## Core claim

Contract screening (strength=0.5) exhibits a **task-dependent response** when added to tight governance: it improves coordination capability (+5.8%, d=1.05, Bonferroni-sig) while simultaneously degrading routing capability (-29.3%, d=-0.78, Bonferroni-sig). This is an **opposite-signed mechanism interaction** that requires task-adaptive tuning.

## Evidence summary

At tight governance with and without screening (strength=0.5):

| Task | Baseline | Screening | Delta | Cohen's d | p-value (Bonf) | Effect |
|------|----------|-----------|-------|-----------|----------------|--------|
| **Coordination** | 0.731 | 0.790 | +5.8% | +1.054 | <0.0001 | BENEFICIAL |
| **Routing** | 0.692 | 0.400 | -29.3% | -0.784 | 0.0045 | HARMFUL |
| Allocation | 0.895 | 0.903 | +0.8% | +0.408 | 1.0 | ns |
| Long_horizon | 0.609 | 0.584 | -1.8% | -0.063 | 1.0 | ns |

Coordination gains are **5.8 percentage points** while routing suffers **29.3 percentage points** — a **35 percentage point swing** across opposite tasks.

## Mechanism interpretation

### Why screening helps coordination:

Coordination tasks require agreement across multiple agents. Contract screening (filtering low-quality agreements before commitment) likely:

1. **Reduces erratic commitments**: Screens out adversarial proposals that would fail coordination checks, reducing rollback cycles.
2. **Improves agreement quality**: Screening pre-validates contracts, allowing coordination to reach stable states faster.
3. **Enables efficient consensus**: With adversarial noise filtered upstream, consensus mechanisms (e.g., quorum gates) operate on cleaner signal.

**Prediction**: Screening benefits scale with governance intensity. At light governance, screening should have minimal coordination benefit because low governance already filters poorly.

### Why screening harms routing:

Routing tasks require **path diversity** and rapid message propagation. Contract screening at strength=0.5 likely:

1. **Over-filters routing choices**: Message route contracts may be filtered as "low quality" if they deviate from high-confidence paths, eliminating legitimate alternatives.
2. **Concentrates traffic**: Screening narrows the contract space, forcing messages onto fewer routes. This reduces path diversity and creates bottlenecks.
3. **Increases adversarial bottleneck vulnerability**: Fewer routes → adversaries can saturate message pipelines more easily.
4. **Increases latency**: Screening overhead (validation time) competes with routing time budget.

**Prediction**: Screening harms routing more severely at higher screening_strength values. The -29.3% loss at strength=0.5 may become catastrophic at strength=0.8.

### Why allocation and long_horizon show no effect:

- **Allocation**: Screening may have marginal benefit (orders matter), but transfers are less complex than coordination contracts. Effect is noise (d=0.41, ns).
- **Long_horizon**: Temporal effects may overshadow screening; agents plan over 50 steps, so early-stage screening decisions have decaying influence.

## Boundary conditions

### Confirmed:
- Tight governance, screening_strength=0.5, 10 agents, 20% adversarial
- Coordination shows Bonf-significant gain; routing shows Bonf-significant loss
- Effect is **consistent and large** (d > 0.7 in both directions)

### Unknown (high priority):
- What is the screening mechanism implementation? (contract structure, filtering criteria)
- Does the effect persist across screening_strength values? (Is routing harmed at 0.25? Harmed at 0.75?)
- Does the effect appear at moderate governance? (or only tight?)
- At what adversarial fraction does the routing regression disappear?

## Alternative hypotheses

1. **Screening is too aggressive (supported)**: Strength=0.5 is calibrated for coordination but over-filters routing. Prediction: lower screening_strength (0.25-0.3) should reduce routing harm while preserving coordination benefit.

2. **Routing is inherently fragile to pre-filtering (plausible)**: Routing requires diversity to handle dynamic congestion. Any upstream filtering reduces flexibility. Prediction: routing shows dose-response to screening_strength.

3. **Adversarial injection interacts with screening (possible but lower confidence)**: If adversaries exploit routing diversity, screening that blocks diverse routes is doubly harmful. Prediction: semi-adversarial sweeps show lower routing losses.

4. **Coordination benefits are spurious due to baseline variance (unlikely)**: The baseline coordination capability (0.731) is stable, and the screening improvement (0.790) is well-above noise (d=1.05). Effect is real.

## Open questions

1. **Screening strength sensitivity**: What screening_strength ∈ {0.0, 0.2, 0.4, 0.6, 0.8, 1.0} balances coordination gains vs routing losses?

2. **Task-adaptive screening**: Can we deploy screening=0.5 on coordination+allocation tasks and screening=0.0 on routing to achieve >85% aggregate capability with 70%+ safety?

3. **Governance level interaction**: Does the screening effect flip at light governance (reduced filtering, less harm to routing)?

4. **Mechanism transparency**: What contracts does screening filter in routing vs coordination? (audit trail needed)

## Next steps

- **Priority 1**: Sweep screening_strength ∈ {0.0, 0.25, 0.5, 0.75, 1.0} on tight governance to find Pareto frontier for screening.
- **Priority 2**: Test task-adaptive governance (screening=0.0 for routing, screening=0.5 for coordination) on mixed workload.
- **Priority 3**: Log contract filtering decisions during run to reverse-engineer the screening mechanism.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[mechanism-interaction]]
- [[task-specificity]]

<!-- topics: governance, contract-screening, mechanism-interaction, task-specificity, pareto-frontier -->
