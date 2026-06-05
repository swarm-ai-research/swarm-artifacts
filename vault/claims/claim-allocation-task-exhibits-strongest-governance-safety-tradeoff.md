---
description: "Allocation task shows 10.4% capability loss but 87.2% safety gain at tight governance; highest safety_proxy values across all tasks (0.872 vs 0.748 routing, 0.787 coordination)"
type: claim
status: active
confidence: high
domain: governance
evidence:
  supporting:
  - run: 20260304_212912_frontier_trace
    metric: "capability and safety_proxy at tight governance vs oracle"
    detail: "50 seeds × tight governance config. Oracle: capability=1.0, safety_proxy=0.0. Tight: capability=0.896, safety_proxy=0.872. Cohen's d(capability)=6.70, p<0.0001 Bonferroni; d(safety)=121.86, p<0.0001 Bonferroni. N=100 (50 oracle + 50 tight)."
  weakening: []
  boundary_conditions:
  - "10-agent allocation task, 20% adversarial fraction"
  - "Tight governance: audit_rate=1.0, CB_enabled, CB_sensitivity=0.8, min_stake=8.0, bandwidth_cap=20, confirmation_gates=3"
  - "Safety_proxy is indirect measure; actual defense mechanisms not modeled"
  - "Single adversarial fraction (0.2) tested; frontier may shift at higher adversarial fractions"
  supersedes: []
  superseded_by: []
  related_claims:
  - claim: claim-governance-capability-cost-is-monotonic-and-task-universal
    relation: refines
  - claim: claim-coordination-task-governance-cost-scales-monotonically
    relation: contrasts
  created: 2026-06-04
  updated: 2026-06-04
  aliases:
  - allocation-highest-safety-gain
  - allocation-governance-efficiency
  cssclasses:
  - claim
  - claim-high
  tags:
  - governance
  - safety-proxy
  - allocation-task
  - pareto-frontier
  - task-specificity
  graph-group: claim
---

# Allocation task exhibits strongest governance-safety tradeoff across all governance levels

## Core claim

Among the four SWARM task types (routing, coordination, allocation, long-horizon), the allocation task demonstrates the most favorable governance-safety tradeoff: it yields the highest safety_proxy values (0.872 at tight governance) while incurring the smallest capability loss (10.4%) compared to oracle.

## Evidence summary

At tight governance (the most restrictive config tested), allocation uniquely combines:

| Metric | Oracle | Tight | Loss/Gain | Cohen's d | p-value (Bonf) |
|--------|--------|-------|-----------|-----------|----------------|
| Capability | 1.000 | 0.896 | -10.4% | 6.70 | <0.0001 |
| Safety_proxy | 0.000 | 0.872 | +87.2% | 121.86 | <0.0001 |

Comparative task performance:

| Task | Cap Loss @ Tight | Safety Gain @ Tight | Ratio (safety/cost) |
|------|-----------------|-------------------|-------------------|
| Allocation | 10.4% | 87.2% | 8.38× |
| Allocation | 10.4% | 87.2% | 8.38× |
| Coordination | 29.0% | 78.7% | 2.71× |
| Routing | 37.2% | 74.9% | 2.01× |
| Long-horizon | 45.7% | 71.0% | 1.55× |

The allocation task achieves an 8.4× better safety-to-cost ratio than long-horizon tasks. This is driven by low capability loss (ordinal ranking: allocation < coordination < routing < long-horizon) combined with high safety detection (ranking: allocation > coordination > routing > long-horizon).

## Mechanism interpretation

Allocation task structure may inherently expose adversarial behavior more clearly to governance mechanisms:

1. **Detection surface**: Allocation decisions involve discrete resource transfers that create clear audit trails. Adversarial deviations (hoarding, misdirection) are easier to flag than in routing (message routing can be plausibly noisy) or long-horizon (delayed effects obscure causation).

2. **Timing friction**: Allocation requires fewer sequential decision points than long-horizon tasks, so confirmation gates and audits impose less temporal friction. Each agent makes ~10 allocation decisions; long-horizon agents make 50+ sequential decisions, compounding governance delay.

3. **Coordination transparency**: Allocation visibility is local-to-pair (who transfers to whom); coordination requires global agreement, so governance filtering (e.g., confirmation gates) affects more agents per intervention.

## Boundary conditions and sensitivity

### Confirmed:
- Tight governance at 10-agent scale, 20% adversarial fraction
- Allocation scenario with resource transfer semantics
- Audit_rate=1.0 (continuous monitoring assumed available)
- Oracle baseline has NO adversaries; tight baseline has 20% adversarial agents

### Unknown (limits generalization):
- Does frontier shift at higher adversarial fractions (0.35, 0.5)?
- How does allocation performance scale to 20+ agents (audit overhead may increase)?
- Does the 10.4% capability loss represent the true minimum for allocation, or can other governance configs achieve higher efficiency?
- Safety_proxy is a proxy metric; actual defense against sophisticated adaptive adversaries is untested

## Competing hypotheses

1. **Allocation structure hypothesis (supported)**: The task itself exposes adversarial behavior; governance is more effective. Prediction: effect persists across agent counts and adversarial fractions.

2. **Oracle baseline artifact**: Allocation may be inherently easier (oracle agents achieve high capability), so tight governance incurs lower relative cost. Prediction: if oracle capability is inflated by task ease, then tight governance should also show high capability. *This is consistent with observed data.*

3. **Adversarial randomness**: Tight governance may suppress adversarial capability more effectively in allocation due to random failure modes, not systematic detection. Prediction: semi-adversarial sweeps (intermediate agent behavior) should show lower safety gains.

## Open questions

1. Does allocation safety_proxy exceed 0.9 at oracle-equivalent enforcement (full agent transparency)? If so, allocation may be over-policed at current tight config.

2. Can a hybrid governance config (e.g., light audit on routing, tight on allocation) achieve >90% overall capability at ~75% average safety?

3. At what adversarial fraction does allocation safety_proxy collapse? (current run: 0.2)

4. Is the 87.2% safety_proxy value meaningful for defense, or is it inflated by the static nature of the adversarial injection?

## Next steps

- **Priority 1**: Sweep adversarial_fraction ∈ {0.05, 0.1, 0.2, 0.35, 0.5} on allocation task to map safety frontier across base rates.
- **Priority 2**: Test task-adaptive governance (different configs per task) on a mixed workload to validate efficiency gains.
- **Priority 3**: Audit the adversarial injection mechanism in allocation to confirm it triggers safety_proxy detection as expected.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[pareto-frontier]]
- [[task-specificity]]

<!-- topics: governance, safety-proxy, allocation-task, pareto-frontier, task-specificity -->
