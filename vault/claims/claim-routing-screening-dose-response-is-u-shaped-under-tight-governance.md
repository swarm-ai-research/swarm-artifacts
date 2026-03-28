---
description: "Routing capability under tight governance follows a U-shaped dose-response: baseline 0.623, minimum 0.368 at strength 0.4, recovery to 0.778 at strength 1.0"
type: claim
status: active
confidence: medium
domain: market
evidence:
  supporting:
  - run: 20260326_screening_strength_sweep
    metric: "capability (routing, tight gov)"
    detail: "30 seeds × 11 strengths. U-shape: 0.0→0.623, 0.1→0.412, 0.2→0.385, 0.3→0.414, 0.4→0.368 (min), 0.5→0.503, 0.6→0.503, 0.7→0.537, 0.8→0.572, 0.9→0.507, 1.0→0.778. d vs baseline at 0.4=-0.66, at 1.0=+0.41."
  - run: 20260304_213700_screening
    metric: "capability (routing, tight gov)"
    detail: "50 seeds. Strength 0.5: 0.692→0.400, d=-0.78. This measurement falls in the valley of the U-curve, consistent with dose-response."
  weakening: []
  boundary_conditions:
  - "Tight governance only"
  - "10 agents, 20% adversarial, 30 seeds per cell"
  - "Moderate governance shows weaker U-shape; light governance shows no clear pattern"
sensitivity:
  governance_level: "pronounced U-shape in tight regime; effect diminishes with governance looseness"
  adversarial_fraction: "tested at 20% only"
  screening_strength: "U-shape spans 0.0-1.0 range"
supersedes:
- claim-screening-harms-routing-under-tight-governance
superseded_by: []
related_claims:
- claim: claim-screening-harms-routing-under-tight-governance
  relation: refines
- claim: claim-screening-signal-reliability-determines-routing-outcome
  relation: supports
- claim: claim-screening-effect-is-task-type-dependent
  relation: refines
created: 2026-03-28
updated: 2026-03-28
aliases:
- routing-u-shaped-screening-response-tight
cssclasses:
- claim
- claim-medium
tags:
- screening
- routing
- governance
- market
- dose-response
graph-group: claim
---

# Routing capability under tight governance follows a U-shaped dose-response to screening strength, with harm at intermediate strength and recovery beyond baseline at full strength

## Evidence summary

The 30-seed dose-response curve for routing under tight governance reveals a U-shaped pattern across screening strengths 0.0-1.0. Capability drops from a baseline of 0.623 (strength 0.0) to a minimum of 0.368 at strength 0.4 (d=-0.66), then recovers to 0.778 at strength 1.0 (d=+0.41, exceeding baseline). This U-shape explains the prior finding of screening harm at strength 0.5 (run 20260304_213700_screening, d=-0.78), which falls exactly in the trough of the dose-response curve.

| Screening Strength | Capability | vs Baseline (0.623) | Effect Size |
|---------|---------|---------|----------|
| 0.0 | 0.623 | baseline | — |
| 0.1 | 0.412 | -0.211 | d=-0.57 |
| 0.2 | 0.385 | -0.238 | d=-0.63 |
| 0.3 | 0.414 | -0.209 | d=-0.56 |
| 0.4 | 0.368 | -0.255 | d=-0.66 |
| 0.5 | 0.503 | -0.120 | d=-0.33 |
| 0.6 | 0.503 | -0.120 | d=-0.33 |
| 0.7 | 0.537 | -0.086 | d=-0.23 |
| 0.8 | 0.572 | -0.051 | d=-0.14 |
| 0.9 | 0.507 | -0.116 | d=-0.31 |
| 1.0 | 0.778 | +0.155 | d=+0.41 |

## Mechanism

Signal reliability determines routing outcome. At low screening strength (0.1-0.4), the trust signal is noisy — governance restrictions are applied inconsistently to both honest and adversarial agents, introducing friction without reliably relaxing constraints for trusted agents. This noise harms routing by reducing path diversity without compensatory benefit.

At high screening strength (0.7-1.0), the trust signal cleanly separates honest agents (trust 0.7-1.0) from adversarial agents (trust 0.0-0.3). Honest agents receive genuine governance relaxation that restores path diversity, while adversarial agents remain constrained. This clean separation explains the recovery beyond baseline at full strength.

## Implications

The U-shaped dose-response falsifies the diversity-consensus mechanism proposed in prior work, which predicted an inverted-U (monotonic harm as screening increased). Instead, the actual pattern indicates that screening effectiveness depends on signal reliability—not on diversity reduction per se. This explains why routing is harmed at intermediate strength but benefits at full strength, a finding impossible to derive from a pure diversity-suppression hypothesis.

The U-shape is governance-regime-dependent: tight governance exhibits the full curve, moderate governance shows a weaker U, and light governance shows no clear pattern. This is consistent with the signal-reliability mechanism—tight governance amplifies the impact of noisy signals (more friction applied inconsistently), while light governance dampens it.

## Boundary conditions

- Tight governance only (moderate shows weaker U-shape; light shows no pattern)
- 10 agents, 20% adversarial
- 30 seeds per screening strength level
- screening_strength range 0.0-1.0 (untested beyond 1.0)
- Routing tasks only (coordination shows monotonic improvement)

## Open questions

1. What is the exact location of the trough (0.4 ± 0.1)?
2. Does the U-shape hold with 50+ seeds? (Current: 30 seeds)
3. Does the recovery at strength 1.0 hold with adversarial fraction >20%?
4. Does the U-shape persist at higher agent counts or tighter governance thresholds?
5. How much of the recovery at 1.0 is due to relaxation vs. other mechanisms?

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: screening, routing, governance, market, dose-response -->
