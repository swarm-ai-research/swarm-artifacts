---
description: Trust erosion mechanism (honest agents exit under high toxicity) requires proximity to phase boundary; 30% adversarial fraction too far from threshold to trigger collapse
type: claim
status: active
confidence: medium
domain: toxicity-dynamics
evidence:
  supporting:
  - run: dynamic_toxicity_2026-03-28
    metric: trust_erosion_welfare
    detail: 'Trust erosion (beta=0.3, threshold=0.35) at 30% adversarial: net welfare +6.27 (PASS). Interaction volume declines but ecosystem survives. Contrast with hypothesis that phase boundary around 37.5-50% adversarial fraction'
  - run: dynamic_toxicity_2026-03-28
    metric: trust_erosion_aggressive_welfare
    detail: 'Trust erosion aggressive (beta=0.6, threshold=0.25) at 30% adversarial: net welfare +3.32 (still positive). Doubling erosion rate (beta) and lowering threshold do not trigger collapse'
  weakening: []
  boundary_conditions:
  - Tested at 30% starting adversarial fraction
  - Hypothesis: phase boundary for ecosystem collapse at 37.5-50% adversarial fraction
  - Beta parameter controls erosion rate (fraction of honest agents exiting per epoch)
  - Toxicity threshold determines exit trigger
  - Not tested above 30% adversarial fraction
sensitivity:
  adversarial_fraction: tested only at 30%; untested above phase boundary
  erosion_rate: tested at beta=0.3 and beta=0.6; may vary with rate
  phase_boundary_location: assumed to be 37.5-50% based on prior work, untested
  toxicity_threshold: tested at 0.35 and 0.25; effect size varies with threshold
supersedes: []
superseded_by: []
related_claims:
- claim-proxy-calibration-drift-causes-deterministic-welfare-collapse
- claim-toxicity-contagion-absorbed-by-memory-decay-in-reputation-systems
created: 2026-06-02
updated: 2026-06-02
aliases:
- trust-erosion-phase-boundary
- erosion-proximity-requirement
cssclasses:
- claim
- claim-medium
tags:
- toxicity-dynamics
- trust-erosion
- phase-transition
- ecosystem-stability
graph-group: claim
---

# trust erosion requires proximity to phase boundary for ecosystem impact

Trust erosion—honest agents exiting under sustained high toxicity—requires the ecosystem to be proximate to a phase boundary (estimated 37.5-50% adversarial fraction) to trigger collapse. At 30% adversarial fraction, erosion produces welfare decline but not collapse (net welfare +6.27, not negative).

## Evidence

| Mechanism | Parameters | Adv% | Net Welfare | Toxicity | Outcome | Interpretation |
|-----------|-----------|------|------------|----------|---------|-----------------|
| Trust erosion | beta=0.3, thresh=0.35 | 30% | **+6.27** | 0.297 | PASS | Below phase boundary |
| Trust erosion aggressive | beta=0.6, thresh=0.25 | 30% | **+3.32** | 0.321 | PASS | Still below phase boundary |
| Combined (all 3) | (all mechanisms) | 40% | **−0.91** | 0.429 | **FAIL** | Drift dominates |

### Interpretation

Trust erosion at 30% adversarial produces welfare decline (6.27 < 12.05 for contagion), indicating the mechanism is operating. But it does not cause collapse. The phase boundary is predicted to be around 37.5-50% based on the proximity assumption.

## Mechanism

Trust erosion operates via honest agent exit:

```python
if cumulative_toxicity > toxicity_threshold:
    honest_agents_exit_rate = beta
    ecosystem_composition_shifts()
```

When honest agents exit:
1. Interaction volume declines (fewer trading partners)
2. Remaining agents have higher adversarial fraction
3. Toxicity increases (fewer honest agents = fewer quality transactions)
4. Positive feedback loop: erosion → exit → higher adv% → more erosion

**Phase boundary hypothesis**: At low adversarial fractions (say 10-30%), exiting honest agents doesn't shift the composition enough to cross the phase boundary. At high fractions (37.5-50%), exit accelerates the crossing and triggers ecosystem collapse.

## Why 30% is insufficient

At 30% adversarial starting fraction:
- Erosion rate: if 50% of honest agents exit per epoch, adv% rises from 30% to ~38-42%
- But the experiment runs 30 epochs; erosion spread over time
- Ecosystem gradually becomes more adversarial but doesn't cross the critical threshold quickly enough
- Result: welfare declines but doesn't collapse

At 40%+ starting, the same erosion rate would push through the boundary.

## Open questions

1. Where exactly is the phase boundary (37.5%? 45%? 50%)?
2. What is the causal chain: erosion → adv% rise → phase boundary crossing → collapse?
3. Can we detect this phase boundary by testing trust erosion at 5% increments of starting adv%?
4. Is the erosion rate beta tunable to trigger crossing from 30%?
5. Does the combined scenario's failure (−0.91 welfare) occur because [[claim-proxy-calibration-drift-causes-deterministic-welfare-collapse]] dominates, not because erosion crosses the boundary?

## Update history

**2026-06-02** — extracted from dynamic_toxicity_2026-03-28 experiment.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[toxicity-mechanisms]]

<!-- topics: toxicity-dynamics, trust-erosion, phase-transition, ecosystem-stability -->
