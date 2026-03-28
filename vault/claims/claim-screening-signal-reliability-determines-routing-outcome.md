---
description: "Screening outcome depends on trust signal reliability: noisy signals (low strength) harm routing, clean signals (high strength) help by selectively relaxing governance for trusted agents"
type: claim
status: active
confidence: medium
domain: market
evidence:
  supporting:
  - run: 20260326_screening_strength_sweep
    metric: "routing capability dose-response mechanism"
    detail: "30 seeds × 11 strengths × 3 gov levels. U-shaped routing curve under tight gov: harm at 0.1-0.4 (noisy signal), recovery at 0.7-1.0 (clean signal). Mechanism: friction_effective = base_friction * (1 - agent_trust * screening_strength). At low strength, trust_discount is small and noisy. At high strength, trust_discount cleanly separates honest (trust 0.7-1.0) from adversarial (0.0-0.3)."
  weakening: []
  boundary_conditions:
  - "Mechanistic claim grounded in SWARM multiplicative friction implementation"
  - "Generalizability to other screening implementations untested"
  - "10 agents, 20% adversarial, 30 seeds per cell"
sensitivity:
  screening_strength: "signal reliability improves monotonically with screening strength"
  trust_distribution: "assumes bimodal honest-vs-adversarial trust; may differ with continuous trust"
  friction_model: "specific to SWARM multiplicative model; additive models may differ"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-routing-screening-dose-response-is-u-shaped-under-tight-governance
  relation: supports
- claim: claim-coordination-capability-increases-monotonically-with-screening-strength
  relation: supports
- claim: claim-screening-effect-is-task-type-dependent
  relation: refines
created: 2026-03-28
updated: 2026-03-28
aliases:
- screening-signal-reliability-routing-mechanism
cssclasses:
- claim
- claim-medium
tags:
- screening
- routing
- mechanism
- signal-reliability
- market
graph-group: claim
---

# Screening outcome is determined by trust signal reliability, not by diversity reduction, explaining both U-shaped routing response and monotonic coordination improvement

## Evidence summary

The empirical U-shaped dose-response for routing (minimum at strength 0.4, recovery at 1.0) falsifies the diversity-consensus mechanism proposed in prior work. Instead, the pattern is explained by signal reliability: trust signals that are too weak produce noisy governance application, harming routing. Trust signals that are strong produce clean separation between honest and adversarial agents, enabling selective governance relaxation that restores routing performance beyond baseline.

The mechanism operates via SWARM's multiplicative friction model: friction_effective = base_friction * (1 - agent_trust * screening_strength). When screening_strength is low (0.1-0.4), the product agent_trust * screening_strength is small for all agents—honest and adversarial alike—producing negligible and noisy friction reduction. When screening_strength is high (0.7-1.0), honest agents (trust 0.7-1.0) experience large friction reductions (0.7-1.0 discount) while adversarial agents (trust 0.0-0.3) experience minimal reduction.

## Mechanism detail

**At low screening strength (0.1-0.4): noisy signal regime**

- Honest agents (trust 0.8): friction_effective = base * (1 - 0.8 * 0.2) = base * 0.84 (12% reduction, small)
- Adversarial agents (trust 0.1): friction_effective = base * (1 - 0.1 * 0.2) = base * 0.98 (2% reduction, noise)
- Result: Both groups get minimal, inconsistent friction reduction. Noise prevents stable route differentiation. Routing harmed.

**At high screening strength (0.7-1.0): clean signal regime**

- Honest agents (trust 0.8): friction_effective = base * (1 - 0.8 * 1.0) = base * 0.2 (80% reduction, large)
- Adversarial agents (trust 0.1): friction_effective = base * (1 - 0.1 * 1.0) = base * 0.9 (10% reduction, small)
- Result: Clean separation. Trusted agents get genuine relaxation enabling path diversity. Routing restored and exceeds baseline.

**For coordination (monotonic improvement at all strengths)**

- Coordination benefits from any variance reduction, regardless of noise
- Even weak, noisy trust signals reduce agent belief variance
- No task-specific requirement for clean agent separation
- Result: monotonic improvement across full strength range

## Implications

This mechanism explains why prior findings reported routing harm at intermediate screening strength (e.g., strength 0.5, d=-0.78 in run 20260304_213700_screening) while coordination improved universally. The same screening intervention produces opposite task-specific outcomes because the tasks have different sensitivities to signal noise: routing requires selective, clean relaxation; coordination requires only variance reduction.

The finding also constrains design: screening strength should not be tuned to an intermediate value (0.3-0.6) for mixed-task environments. Either commit to high strength (0.8+) to avoid routing harm, or implement task-specific screening (high strength for coordination tasks, bypass for routing tasks).

## Boundary conditions

- Mechanistic claim grounded in SWARM's multiplicative friction implementation
- Generalizability to additive friction models or other screening implementations untested
- 10 agents, 20% adversarial
- Trust values: honest agents 0.7-1.0, adversarial agents 0.0-0.3 (bimodal assumption)
- screening_strength range 0.0-1.0 (untested beyond 1.0)

## Open questions

1. Is this mechanism implementation-specific (SWARM's multiplicative model) or general?
2. Would additive trust models (friction_effective = base - agent_trust * screening_strength) show the same U-shape?
3. How does the mechanism behave with continuous trust distributions (not bimodal)?
4. What trust distribution threshold separates "noisy" from "clean" signal regime (currently estimated ~0.3-0.4)?
5. Does the mechanism predict optimal screening strength for mixed-task workloads?

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: screening, routing, mechanism, signal-reliability, market -->
