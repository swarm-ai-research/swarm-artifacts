---
description: "Coordination capability increases monotonically with screening strength (rho=0.96-0.98, d=2.57 at strength 1.0) across all governance levels"
type: claim
status: active
confidence: high
domain: market
evidence:
  supporting:
  - run: 20260326_screening_strength_sweep
    metric: "capability (coordination)"
    detail: "30 seeds × 11 strengths × 3 gov levels = 990 runs. Tight: rho=+0.964, 0.730→0.856, d=2.57. Moderate: rho=+0.973, 0.788→0.874, d=2.54. Light: rho=+0.982, 0.966→0.989, d=2.59. All monotonically increasing. No plateau detected."
  weakening: []
  boundary_conditions:
  - "10 agents, 20% adversarial, 30 seeds per cell"
  - "screening_strength 0.0-1.0 in 0.1 steps"
  - "All three governance levels show identical monotonic behavior"
sensitivity:
  screening_strength: "tested across full 0.0-1.0 range; no indication of ceiling effect"
  task_type: "coordination-specific finding"
  governance_level: "uniform monotonicity across tight, moderate, light"
supersedes:
- claim-screening-improves-coordination-capability-universally
superseded_by: []
related_claims:
- claim: claim-screening-improves-coordination-capability-universally
  relation: extends
- claim: claim-screening-signal-reliability-determines-routing-outcome
  relation: supports
created: 2026-03-28
updated: 2026-03-28
aliases:
- coordination-monotonic-screening-response
cssclasses:
- claim
- claim-high
tags:
- screening
- coordination
- governance
- market
- dose-response
graph-group: claim
---

# Coordination capability increases monotonically with screening strength across all governance levels without plateau

## Evidence summary

The dose-response across 11 screening strengths (0.0-1.0 in 0.1 increments) reveals a clean, monotonically increasing relationship between screening strength and coordination capability. All three governance tightness levels exhibit rank correlations rho=0.96-0.98, indicating near-perfect monotonicity. Effect sizes grow continuously from d=0.13 at strength 0.1 to d=2.57 at strength 1.0 under tight governance. No plateau, dip, or reversal is detected at any intermediate strength.

| Governance Level | Strength 0.0 | Strength 1.0 | Improvement | rho | Effect Size (d) |
|-----------------|---------|---------|-------------|-----|------------------|
| Tight | 0.730 | 0.856 | +12.6pp | +0.964 | d=2.57 |
| Moderate | 0.788 | 0.874 | +8.6pp | +0.973 | d=2.54 |
| Light | 0.966 | 0.989 | +2.3pp | +0.982 | d=2.59 |

## Mechanism

Screening reduces agent belief variance about partner intentions, enabling faster consensus formation. The monotonic dose-response indicates that coordination tasks benefit from any level of variance reduction—there is no "too much consensus" regime. Higher screening strength produces cleaner belief alignment, which translates directly into improved ability to coordinate actions.

The consistency of monotonicity across all governance levels indicates that the coordination improvement is fundamental to the screening mechanism, not an artifact of a specific governance regime.

## Implications

The absence of plateau or ceiling effect up to screening strength 1.0 suggests that the coordination gains are not bounded by task difficulty or agent capacity constraints within the tested parameter space. This monotonic behavior contrasts sharply with routing tasks, which show a U-shaped dose-response, indicating that coordination and routing have fundamentally different sensitivities to screening strength.

## Boundary conditions

- Coordination tasks only (routing and long_horizon show different profiles)
- 10 agents, 20% adversarial
- 30 seeds per screening strength × governance level combination
- screening_strength range 0.0-1.0 (untested beyond 1.0)

## Open questions

1. Does monotonicity continue with screening_strength > 1.0?
2. Is there a ceiling effect at very high agent counts (>20)?
3. Does the monotonic trend hold with adversarial fraction >20%?
4. What is the minimum effective screening strength for coordination improvement?

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: screening, coordination, governance, market, dose-response -->
