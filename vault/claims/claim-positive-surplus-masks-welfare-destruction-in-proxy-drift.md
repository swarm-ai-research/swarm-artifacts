---
description: Proxy drift scenario has positive surplus (+5.72) but negative net welfare (−1.54), showing traditional toxicity threshold success criterion fails to detect welfare collapse
type: claim
status: active
confidence: high
domain: methodology
evidence:
  supporting:
  - run: dynamic_toxicity_2026-03-28
    metric: surplus_vs_welfare
    detail: 'Proxy drift (α=0.3): surplus +5.72, net welfare −1.54, N=42 seeds, Bonferroni-corrected. Metric divergence indicates failure of single-metric success criteria'
  - run: dynamic_toxicity_2026-03-28
    metric: metric_divergence
    detail: 'Surplus measures transaction volume; W_net = Σ_accepted [p*s+ − (1−p)*(s− + h)] captures quality mixture. Proxy drift increases acceptance rate (higher surplus) while inverting quality (negative welfare). N=42 seeds, Bonferroni-corrected'
  weakening: []
  boundary_conditions:
  - Proxy drift α=0.3 causing sigmoid_k degradation
  - 40% adversarial fraction, 10 agents, default topology
  - Episode length 30 epochs
  - "Old criterion: surplus ≥ 0; new criterion: W_net ≥ 0"
  - Break-even p=0.6 (fraction honest among accepted)
sensitivity:
  surplus_threshold: value depends on what positive surplus is considered success
  parameters: tested with specific circuit breaker, audit, reputation settings
  adversarial_strategy: surplus masking may vary with agent sophistication
supersedes: []
superseded_by: []
related_claims:
- claim-proxy-calibration-drift-causes-deterministic-welfare-collapse
created: 2026-06-02
updated: 2026-06-02
aliases:
- surplus-welfare-divergence
- metric-criterion-misalignment
cssclasses:
- claim
- claim-high
tags:
- metrics
- welfare
- adverse-selection
- measurement-error
graph-group: claim
---

# positive surplus masks welfare destruction in proxy drift

Proxy calibration drift produces negative net social welfare (−1.54) while maintaining positive surplus (+5.72), revealing a critical gap in governance success criteria. Traditional toxicity-threshold-based metrics would incorrectly classify proxy drift as safe.

## Evidence

| Metric | Value | Old Criterion Pass? | New Criterion Pass? | Interpretation |
|--------|-------|-------------------|-------------------|-----------------|
| Surplus | +5.72 | ✓ Yes | — | Trading occurs |
| Net Social Welfare | −1.54 | — | ✗ No | **Good trades don't dominate** |

### Why they diverge

**Surplus** = sum of all transaction payoffs, regardless of counterparty quality
- High surplus means agents are trading frequently
- Does not distinguish honest transactions from adversarial ones
- Proxy drift increases surplus because it increases acceptance rates (both good and bad trades)

**Net Social Welfare** = W_net = Σ accepted [ p × s+ − (1−p) × (s− + h) ]
- Where p = probability agent is honest, s+ = honest payoff, s− = adversarial payoff, h = harm
- With default params (s+=2, s−=1, h=2): break-even at p=0.6
- Captures the quality mixture of accepted agents
- Proxy drift decreases net welfare because degraded detection shifts acceptance toward adversarial agents

### The proxy drift mechanism

Under proxy calibration drift:
- True toxicity of adversarial agents remains constant
- But the detector sigmoid_k degrades (sigmoid becomes less discriminative)
- Result: adversarial agents accepted at higher rates
- Surplus increases (more transactions) but quality mixture inverts (more bad trades)
- Net welfare becomes negative

## Implications

This is a **measurement validation claim**. It demonstrates that single-metric success criteria are insufficient for governance evaluation. Previous SWARM studies using only toxicity or surplus metrics may have missed subtle welfare collapse modes.

The quality gap metric (honest vs adversarial outcome difference) from [[claim-soft-detection-maintains-negative-quality-gap-indicating-adverse-selection-control]] represents an alternative measurement approach that catches this failure mode. Under proxy drift, the quality gap collapses (honest agents no longer outperform adversarial agents) even as surplus remains positive. This suggests that detection system quality metrics (AUROC, calibration, quality gap) may be more sensitive indicators of governance health than transaction volume metrics (surplus, welfare).

The discovery that proxy drift produces positive surplus yet negative welfare suggests that:
1. **Adversarial agents can exploit accuracy degradation.** As detector calibration drifts, adversarial agents slip through.
2. **Volume metrics are poor governance proxies.** High transaction volume ≠ high quality outcomes.
3. **Quality mixture matters more than volume.** What types of agents are accepted determines welfare.

## Open questions

1. Are there other toxicity mechanisms that diverge between surplus and welfare?
2. What is the mapping between surplus and welfare across different agent compositions?
3. Can we design an early-warning metric that triggers before welfare crosses into negative territory?
4. How should governance parameters be tuned to prevent surplus-welfare divergence?

## Update history

**2026-06-02** — extracted from dynamic_toxicity_2026-03-28 experiment. Motivates the introduction of net_social_welfare as success criterion.

---

Topics:
- [[_index]]
- [[governance-dashboard]]
- [[toxicity-mechanisms]]

<!-- topics: metrics, welfare, adverse-selection, measurement-error -->
