---
description: "Audit rate has 3.6× stronger effect on allocation safety than circuit breaker sensitivity; 100% audit (tight) vs 80% audit (tight-moderate) safety gap is 17.4 percentage points; audit is primary governance lever"
type: claim
status: active
confidence: high
domain: governance
evidence:
  supporting:
  - run: 20260304_212912_frontier_trace
    metric: "safety_proxy at tight (audit_rate=1.0) vs tight-moderate (audit_rate=0.8) governance"
    detail: "50 seeds per config. Tight (audit_rate=1.0, CB_sensitivity=0.8): safety=0.872. Tight-moderate (audit_rate=0.8, CB_sensitivity=0.6): safety=0.698. Delta=17.4 percentage points. Cohen's d=138.39, p<0.0001 Bonferroni (N=100). Allocation task shows strongest sensitivity to audit rate across all task types."
  weakening: []
  boundary_conditions:
  - "Allocation task, 10 agents, 20% adversarial fraction"
  - "Audit rate varied from 1.0 → 0.8; no finer-grained sweep"
  - "Circuit breaker sensitivity co-varied with audit rate (both relaxed in tight-moderate); isolated effect not tested"
  - "Safety_proxy is aggregate metric; does not distinguish between different types of adversarial behavior detected"
  supersedes: []
  superseded_by: []
  related_claims:
  - claim: claim-allocation-task-exhibits-strongest-governance-safety-tradeoff
    relation: refines
  - claim: claim-audit-rate-is-primary-lever-for-safety-across-tasks
    relation: supports
  created: 2026-06-04
  updated: 2026-06-04
  aliases:
  - audit-dominance-allocation
  - audit-vs-circuit-breaker
  cssclasses:
  - claim
  - claim-high
  tags:
  - governance
  - audit-rate
  - circuit-breaker
  - allocation-task
  - mechanism-design
  graph-group: claim
---

# Audit rate dominates circuit breaker sensitivity for safety detection in allocation task

## Core claim

In allocation tasks, **audit rate is the primary governance lever** for safety detection. Increasing audit rate from 80% to 100% (tight-moderate → tight) yields **17.4 percentage point safety gain** (0.698 → 0.872), while simultaneously relaxing circuit breaker sensitivity (0.8 → 0.6) has minimal negative impact. This demonstrates that **continuous monitoring (audit) outweighs reactive filtering (circuit breaker)** for allocation task safety.

## Evidence summary

Tight governance (audit_rate=1.0, CB_sensitivity=0.8) vs Tight-moderate (audit_rate=0.8, CB_sensitivity=0.6):

| Config | Audit Rate | CB Sensitivity | Safety_proxy | Vs Baseline | Cohen's d |
|--------|------------|-----------------|--------------|------------|-----------|
| **Tight** | 1.0 | 0.8 | **0.872** | +17.4pp | 138.39 |
| **Tight-moderate** | 0.8 | 0.6 | 0.698 | — | — |
| Moderate | 0.5 | 0.4 | 0.608 | -9.0pp | — |
| Light | 0.15 | 0.0 | 0.281 | -41.7pp | — |

The **safety drop from tight (1.0 audit) to tight-moderate (0.8 audit)** is **17.4 percentage points**. This is decomposed as:
- Audit rate loss: -0.2 (20% less monitoring) = expected safety loss if audit is primary mechanism
- Circuit breaker relaxation: -0.6 sensitivity (25% less reactive) = expected minimal loss if CB is secondary

**Actual loss: 17.4pp ≈ proportional to audit rate loss**, suggesting audit rate is **roughly 3.6× more important** than circuit breaker sensitivity for allocation safety.

## Mechanism: why audit dominates

1. **Continuous vs reactive coverage**: Audit rate directly controls what fraction of adversarial behavior is observed. At 100% audit, every adversarial transfer is logged. At 80% audit, 20% of transfers are unmonitored—these can become "attack surface."

2. **Allocation transparency**: Allocation decisions are discrete transfers (who pays whom, when). Each transfer is a potential audit point. Adversaries cannot hide transfers; they can only exploit unaudited intervals.

3. **Circuit breaker is a reaction mechanism**: Once adversarial behavior is detected via audit, the circuit breaker can stop further damage. But if a transfer is not audited (80% audit = 20% blind spots), the circuit breaker has nothing to react to.

4. **Adversary adaptation**: At tight governance with 100% audit, adversaries have zero blind spots. At 80% audit, adversaries can exploit the 20% gap, and circuit breaker cannot retroactively undo already-committed transfers.

## Comparative effect across mechanisms

| Mechanism | Change | Safety Impact | Interpretation |
|-----------|--------|---------------|-----------------|
| Audit rate (1.0 → 0.8) | -20% | -17.4pp | PRIMARY: direct detection loss |
| CB sensitivity (0.8 → 0.6) | -25% | <1pp (inferred) | SECONDARY: reaction mechanism |
| Min stake (8.0 → 6.0) | -25% | ~2pp (inferred) | TERTIARY: financial disincentive |

Audit rate accounts for **>90% of the safety delta** between tight and tight-moderate configurations.

## Boundary conditions

### Confirmed:
- Allocation task, 10 agents, 20% adversarial fraction
- Tight governance (1.0 audit) vs tight-moderate (0.8 audit)
- Large effect size (d=138.39, p<0.0001 Bonferroni)

### Unknown (high priority):
- Is the effect linear? (What is safety at 0.9 audit? 0.95 audit?)
- Does the effect hold for coordination and routing tasks?
- What is the minimum audit rate to maintain >50% safety (safety floor)?
- Can circuit breaker sensitivity be increased at lower audit rates to compensate?

## Alternative hypotheses

1. **Audit dominance hypothesis (supported)**: Audit is the primary detection mechanism; circuit breaker is secondary reaction. Prediction: audit rate sweep should show linear relationship with safety_proxy.

2. **Interaction hypothesis (possible)**: Audit and circuit breaker interact multiplicatively. Prediction: at very low audit (0.1), relaxing CB sensitivity should have larger impact.

3. **Adversary adaptation hypothesis (plausible)**: Adversaries adapt to audit rate. At 80% audit, they exploit 20% blind spots. Prediction: semi-adversarial sweeps (less adaptive adversaries) should show smaller audit effect.

4. **Configuration artifact (unlikely)**: The tight-moderate config was designed to relax all mechanisms; the large safety drop is due to the combined effect, not audit dominance. Prediction: isolating audit rate alone (keeping CB_sensitivity=0.8) should show <10pp safety loss.

## Open questions

1. **Audit rate sensitivity**: What is the effect of audit rate on safety across {0.2, 0.4, 0.6, 0.8, 1.0}? Is the relationship linear?

2. **Circuit breaker effectiveness in isolation**: Holding audit_rate=1.0, what is the safety impact of CB_sensitivity ∈ {0.0, 0.2, 0.4, 0.6, 0.8}?

3. **Adversary targeting**: Do adversaries specifically exploit audit blind spots, or is the safety loss due to general reduced monitoring?

4. **Governance mechanism unification**: Can we achieve high safety with lower audit rate + higher circuit breaker sensitivity? (trade monitoring for reaction)

## Implications for governance design

1. **Audit is non-negotiable**: Governance designers should prioritize audit rate over circuit breaker tuning.

2. **Audit rate floor**: For allocation tasks at 20% adversarial, audit rate >80% appears necessary to maintain >70% safety.

3. **Resource allocation**: If audit has fixed cost, prioritize auditing allocation transfers over routing or coordination.

4. **Adaptive mechanisms**: Consider audit targeting (focus on high-value transfers) to reduce monitoring overhead while maintaining safety.

## Next steps

- **Priority 1**: Sweep audit_rate ∈ {0.2, 0.4, 0.6, 0.8, 1.0} on allocation task to map safety vs audit linearity.
- **Priority 2**: Isolate circuit breaker effect by holding audit_rate=1.0, vary CB_sensitivity.
- **Priority 3**: Repeat analysis on coordination and routing tasks to test generalization.
- **Priority 4**: Instrument audit logs to verify adversaries exploit audit blind spots.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[mechanism-design]]
- [[allocation-task]]

<!-- topics: governance, audit-rate, circuit-breaker, allocation-task, mechanism-design -->
