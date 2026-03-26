---
description: "Contract screening reduces routing capability by 29 percentage points under tight governance (d=-0.78, Bonferroni-sig); over-constrains path diversity"
type: claim
status: active
confidence: medium
domain: market
evidence:
  supporting:
  - run: 20260304_213700_screening
    metric: "capability (routing, tight gov)"
    detail: "50 seeds. Tight gov: 0.692→0.400, d=-0.78, p=0.0001, Bonferroni-significant at alpha/18=0.00278. Moderate: 0.567→0.517, d=-0.12, p=0.534 (null). Light: 0.883→0.935, d=0.21, p=0.285 (null)."
  - run: 20260304_232817_screening
    metric: "capability (routing replication)"
    detail: "20 seeds. Tight: 0.636→0.449, d=-0.47, p=0.141. Direction replicates but underpowered at N=20."
  weakening: []
  boundary_conditions:
  - "Routing tasks, tight governance only"
  - "Moderate and light governance show null/positive trends"
  - "20% adversarial, 10 agents"
  - "Harm magnitude: 29.2 percentage point absolute reduction in tight governance"
sensitivity:
  governance_level: "effect specific to tight governance; absent under moderate and light"
  screening_strength: "tested at 0.5 only"
  replication_power: "main finding Bonferroni-significant but replication underpowered (N=20)"
  task_type: "routing-specific; coordination and allocation show different response profiles"
supersedes: []
superseded_by: []
related_claims:
- claim: claim-screening-improves-coordination-capability-universally
  relation: contradicts
- claim: claim-screening-effect-is-task-type-dependent
  relation: supports
- claim: claim-governance-parameters-have-narrow-safe-operating-envelopes
  relation: supports
created: 2026-03-25
updated: 2026-03-25
aliases:
- screening-routing-tight-gov-harm
cssclasses:
- claim
- claim-medium
tags:
- screening
- routing
- governance
- market
- mechanism-design
graph-group: claim
---

# Contract screening harms routing capability under tight governance by over-constraining path diversity

## Evidence summary

Under tight governance, screening reduces routing capability from 0.692 to 0.400 (d=-0.78, p=0.0001, Bonferroni-significant). The 20-seed replication directionally confirms (0.636→0.449, d=-0.47) but is underpowered. Under moderate and light governance, routing shows null or weakly positive trends, suggesting the harm is specific to the tight governance × screening interaction.

| Governance Level | Baseline | Screening | Change | Effect Size | p-value | Significant |
|-----------------|----------|-----------|--------|------------|---------|-------------|
| Tight | 0.692 | 0.400 | -29.2pp | d=-0.78 | p=0.0001 | Yes |
| Moderate | 0.567 | 0.517 | -5.0pp | d=-0.12 | p=0.534 | No |
| Light | 0.883 | 0.935 | +5.2pp | d=0.21 | p=0.285 | No |

## Confidence: Medium

Rated medium despite Bonferroni significance in the main run because:
1. The replication does not reach significance (N=20, underpowered)
2. Only one screening strength tested
3. The mechanism is hypothesized, not confirmed through causal analysis

## Mechanism

Screening enforces agent consensus on route selection. Under tight governance, agents already have constrained action spaces. Adding screening further reduces route diversity, preventing exploration of alternative paths that might be optimal. Under light governance, agents retain enough exploration capacity that screening helps by reducing wasteful disagreement. The sweet spot for routing is moderate governance with high path diversity.

## Implications

This finding highlights the [[claim-governance-parameters-have-narrow-safe-operating-envelopes|narrow operating envelopes]] for governance mechanisms. Screening is beneficial when the underlying task requires consensus (coordination) but harmful when the task requires diversity (routing under constraints). Tight governance is already diversity-limiting, and screening pushes the system past its capability threshold.

## Boundary conditions

Tight governance only. The harm does not appear under moderate or light governance. Single screening strength (0.5) and single adversarial fraction (20%) tested.

## Open questions

1. At what governance tightness does screening switch from harmful to neutral for routing?
2. Does screening strength 0.25 avoid the harm while preserving coordination benefits?
3. Is the harm reversible by slightly loosening governance, or is there hysteresis?
4. Do different routing topologies (hub-and-spoke vs distributed) show different sensitivity?

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[screening-mechanisms]]

<!-- topics: screening, routing, governance, market, mechanism-design, tight-governance -->
