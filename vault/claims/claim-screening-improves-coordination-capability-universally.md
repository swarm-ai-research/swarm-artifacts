---
description: "Contract screening (strength=0.5) improves coordination capability across all governance levels with d=0.97-1.10, Bonferroni-significant"
type: claim
status: active
confidence: high
domain: market
evidence:
  supporting:
  - run: 20260304_213700_screening
    metric: "capability (coordination)"
    detail: "50 seeds × 3 governance levels. Tight: 0.731→0.789, d=1.04, p<0.000001. Moderate: 0.785→0.826, d=0.97, p=0.000001. Light: 0.965→0.976, d=1.10, p<0.000001. All Bonferroni-significant at alpha/18=0.00278."
  weakening: []
  boundary_conditions:
  - "Coordination tasks only, 20% adversarial, 10 agents, screening_strength=0.5"
  - "Effect uniform across all three governance tightness levels"
  - "Absolute gains modest (1-6 percentage points) but effect sizes are large (d=0.97-1.10)"
  - "Does not generalize to routing or long_horizon tasks"
sensitivity:
  screening_strength: "tested at 0.5 only; unknown if 0.25 or 0.75 produce different gains"
  task_type: "coordination-specific; routing and long_horizon show different response profiles"
  adversarial_fraction: "tested at 20% only"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-contract-screening-achieves-perfect-type-separation
  relation: extends
- claim: claim-screening-effect-is-task-type-dependent
  relation: supports
- claim: claim-screening-harms-routing-under-tight-governance
  relation: contradicts
created: 2026-03-25
updated: 2026-03-25
aliases:
- screening-coordination-universal-improvement
cssclasses:
- claim
- claim-high
tags:
- screening
- coordination
- governance
- market
- mechanism-design
graph-group: claim
---

# Contract screening universally improves coordination capability across all governance levels

## Evidence summary

In a 50-seed comparison of baseline vs screening (strength=0.5), coordination tasks show consistent, large improvements at all three governance tightness levels. Effect sizes range d=0.97-1.10, all Bonferroni-significant (threshold alpha/18=0.00278). The absolute gains are modest (1-6 percentage points) but the consistency across governance levels and the large d values indicate a robust, replicable mechanism.

| Governance Level | Baseline | Screening | Improvement | Effect Size | p-value | Significant |
|-----------------|----------|-----------|-------------|------------|---------|-------------|
| Tight | 0.731 | 0.789 | +5.8pp | d=1.04 | p<0.000001 | Yes |
| Moderate | 0.785 | 0.826 | +4.1pp | d=0.97 | p=0.000001 | Yes |
| Light | 0.965 | 0.976 | +1.1pp | d=1.10 | p<0.000001 | Yes |

## Mechanism

Screening reduces variance in agent beliefs about partner intentions, enabling faster consensus formation. Coordination tasks specifically require belief alignment, making them the natural beneficiary of screening. Under all three governance regimes — from tightly constrained action spaces to loosely constrained ones — agents benefit from the common ground that screening provides.

## Implications

The universality of coordination improvement across governance levels suggests that screening is a fundamental coordination amplifier, not a governance-regime-dependent intervention. This contrasts sharply with routing and long_horizon tasks, which show task-specific sensitivities. The large effect sizes (d>0.97) despite modest absolute gains indicate that screening is reducing within-run variance substantially, making coordination outcomes more predictable and stable.

## Boundary conditions

Coordination tasks only. Routing is harmed under tight governance. Long_horizon shows no effect. Single screening strength (0.5) tested.

## Open questions

1. Does screening strength 0.25 or 0.75 produce different coordination gains?
2. Is there a ceiling effect at higher screening strengths?
3. Does the coordination benefit hold with >20% adversarial fraction?
4. Can the coordination gain be explained by reduced agent confusion, or are there alternative mechanisms?

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: screening, coordination, governance, market, mechanism-design -->
