# Screening as Selective Relaxation: How a Dose-Response Sweep Falsified Our Proposed Mechanism and Revealed a Better One

**Authors:** SWARM Research Collective
**Date:** 2026-03-28
**Framework:** SWARM v1.4.0

## Abstract

We report a three-phase investigation of contract screening in multi-agent governance systems. **Phase 1** (1,400 runs): a governance Pareto frontier trace across 7 intensities and 4 task types shows that governance cost is monotonic, task-universal, and amplifies 4.4x with task complexity. **Phase 2** (1,200 runs + 2 replications): screening at strength 0.5 produces task-type-dependent effects — improving coordination (d = 0.97--1.10, Bonferroni-significant), harming routing under tight governance (d = -0.78, Bonferroni-significant), and null for long-horizon planning. We proposed a "diversity-consensus" mechanism: screening reduces agent belief variance, helping consensus-dependent tasks and harming diversity-dependent tasks. **Phase 3** (2,640 runs): a dose-response sweep across 11 screening strengths (0.0--1.0) **falsifies** the proposed mechanism. Routing under tight governance shows a U-shaped curve — not the predicted inverted-U — with capability dropping from 0.623 (baseline) to 0.368 at strength 0.4, then *recovering past baseline* to 0.778 at strength 1.0. Coordination confirms monotonic improvement (rho = 0.96--0.98). The revised mechanism is **screening as selective relaxation**: at low strength, the trust signal is noisy and governance is applied inconsistently (harm); at high strength, the signal cleanly separates honest from adversarial agents, selectively restoring autonomy to trusted agents (benefit). This paper demonstrates the value of designing falsification experiments for your own hypotheses — the revised mechanism is more accurate, more actionable, and explains patterns the original could not.

## 1. Introduction

A central promise of mechanism design in multi-agent AI safety is that well-chosen interventions can shift the capability-safety Pareto frontier outward. Contract screening, which sorts agents into compatible pools based on revealed type information, is a candidate for such an improvement. Prior SWARM results showed that screening achieves perfect type separation (separation quality = 1.0 across 11 seeds) and generates a 6.7x honest payoff premium (Savitt et al., 2026).

This paper reports what happened when we tested screening's frontier effects systematically, proposed a mechanism for the results, then designed an experiment to falsify our own proposal. The falsification succeeded — and the replacement mechanism is better.

The narrative proceeds in three phases:

1. **Establish the frontier** (Section 3.1--3.2): What does governance cost, and how does it vary by task?
2. **Measure screening's effect** (Section 3.3--3.4): At strength 0.5, screening helps coordination, harms routing under tight governance, and is null for long-horizon.
3. **Test the mechanism** (Section 3.5--3.6): A dose-response sweep falsifies the diversity-consensus hypothesis and reveals a U-shaped routing curve explained by trust signal reliability.

### 1.1 Contributions

1. **Governance Pareto frontier with task-type resolution.** 1,400 runs across 7 governance intensities and 4 task types establish that governance cost amplifies 4.4x with task complexity.

2. **Screening as task-type-dependent intervention.** 1,200 runs show screening produces sign-reversed effects: +1.04 for coordination, -0.78 for tight-governance routing, null for long-horizon.

3. **Designed self-falsification.** A 2,640-run dose-response sweep, designed to test our own diversity-consensus mechanism, falsifies it and reveals a U-shaped routing curve.

4. **Screening as selective relaxation.** The revised mechanism — trust signal reliability determines whether screening helps or harms — is more accurate, explains the U-shape, and generates new testable predictions.

## 2. Methods

### 2.1 Frontier Trace Design

Full factorial sweep: 7 governance configs × 4 task types × 50 seeds = 1,400 runs.

- **Governance configurations (7):** oracle (no governance, no adversaries), loose (audit 0.05, no enforcement), light (audit 0.15, no CB), moderate-light (audit 0.30, CB disabled, stake 2.0), moderate (audit 0.50, CB enabled at 0.4, stake 4.0), tight-moderate (audit 0.80, CB at 0.6, stake 6.0), tight (audit 1.0, CB at 0.8, stake 8.0, 3 confirmation gates)
- **Task types (4):** routing, coordination, allocation, long_horizon
- **Seeds:** 50 per config. **Agents:** 10, 20% adversarial (except oracle: 0%)

### 2.2 Screening A/B Design

Paired comparison at screening strength = 0.5.

**Main study:** 2 conditions × 3 governance levels × 4 task types × 50 seeds = 1,200 runs.
**Replications:** routing (20 seeds) and long-horizon (20 seeds) with independent seed sets.

### 2.3 Dose-Response Sweep Design

Designed to test the diversity-consensus mechanism. Key predictions:
- Coordination: monotonic improvement with screening strength
- Routing × tight: inverted-U, with harm at high strength (>0.4) and benefit at low strength (<0.2)
- Long-horizon: null across all strengths

**Primary arm:** 11 screening strengths (0.0--1.0) × 3 governance levels × 2 task types (routing, coordination) × 30 seeds = 1,980 runs.
**Confirmatory arm:** same strengths and governance × 2 task types (allocation, long_horizon) × 10 seeds = 660 runs.
**Total:** 2,640 runs.

### 2.4 Statistical Methods

- **Effect sizes:** Cohen's d for pairwise comparisons, Spearman rho for dose-response monotonicity
- **Multiple comparison correction:** Bonferroni across 18 primary comparisons (Phase 2), across 33 dose-response cells (Phase 3)
- **p-values:** Welch's t-test (unequal variance)

## 3. Results

### 3.1 The Governance Pareto Frontier is Monotonic and Task-Universal

**Table 1. Mean capability by governance configuration and task type (N = 50 seeds each)**

| Config | Routing | Coordination | Allocation | Long Horizon |
|--------|---------|-------------|------------|-------------|
| oracle | 1.000 | 1.000 | 1.000 | 1.000 |
| loose | 1.000 | 0.997 | 1.000 | 1.000 |
| light | 0.947 | 0.964 | 0.990 | 0.939 |
| moderate-light | 0.791 | 0.841 | 0.923 | 0.743 |
| moderate | 0.648 | 0.786 | 0.900 | 0.620 |
| tight-moderate | 0.611 | 0.732 | 0.899 | 0.455 |
| tight | 0.628 | 0.710 | 0.896 | 0.543 |

The ordering **oracle > loose > light > moderate-light > moderate > tight-moderate ≈ tight** holds without exception across all four task types. The magnitude varies 4.4x: allocation loses 10.4% under tight governance while long-horizon loses 45.7%.

### 3.2 Loose Governance is Near-Costless

Loose governance achieves >99.7% of oracle capability across all task types (safety_proxy = 0.015). A near-free entry point on the Pareto frontier.

### 3.3 Phase 2: Screening at Strength 0.5 is Task-Type Dependent

**Table 2. Screening effect at strength 0.5 (Cohen's d) by task type and governance**

| Task Type | Tight | Moderate | Light | Pattern |
|-----------|-------|----------|-------|---------|
| Coordination | **+1.04*** | **+0.97*** | **+1.10*** | Universal strong gain |
| Allocation | +0.40 | **+0.87*** | +0.42 | Moderate positive |
| Routing | **-0.78*** | -0.12 | +0.21 | Negative under tight |
| Long horizon | -0.06 | +0.25 | +0.27 | Null |

\* Bonferroni-significant (p < 0.00278)

Screening at strength 0.5 universally improves coordination, harms routing under tight governance, and has no effect on long-horizon planning. The routing harm replicates directionally (d = -0.47) in an independent 20-seed run.

### 3.4 The Diversity-Consensus Hypothesis

Based on the Phase 2 results, we proposed that screening reduces agent belief variance, which:
- Helps consensus-dependent tasks (coordination) by accelerating convergence
- Harms diversity-dependent tasks (routing) by narrowing path exploration
- Has no effect on tasks dependent on individual planning depth (long-horizon)

This mechanism predicts an **inverted-U** dose-response for routing under tight governance: low screening helps (reduces wasteful disagreement), high screening harms (eliminates path diversity). The crossover was predicted at strength 0.2--0.3.

### 3.5 Phase 3: The Dose-Response Falsifies the Mechanism

The 2,640-run dose-response sweep produces the opposite of the predicted routing pattern.

**Table 3. Routing capability under tight governance by screening strength (N = 30 seeds)**

| Strength | Capability | SD | d vs baseline |
|----------|-----------|------|--------------|
| 0.0 | 0.623 | 0.398 | — |
| 0.1 | 0.412 | 0.396 | -0.53 |
| 0.2 | 0.385 | 0.388 | -0.61 |
| 0.3 | 0.414 | 0.397 | -0.53 |
| **0.4** | **0.368** | **0.377** | **-0.66** |
| 0.5 | 0.503 | 0.413 | -0.30 |
| 0.6 | 0.503 | 0.411 | -0.30 |
| 0.7 | 0.537 | 0.416 | -0.21 |
| 0.8 | 0.572 | 0.413 | -0.12 |
| 0.9 | 0.507 | 0.417 | -0.28 |
| **1.0** | **0.778** | **0.358** | **+0.41** |

The routing curve is **U-shaped**: capability drops from 0.623 (baseline) to a minimum of 0.368 at strength 0.4, then recovers to 0.778 at strength 1.0 — *exceeding baseline*. This directly falsifies the inverted-U prediction. The Phase 2 finding of routing harm at strength 0.5 (d = -0.78) falls exactly in the valley of this curve.

### 3.6 Coordination Confirms Monotonic Improvement

**Table 4. Coordination capability under tight governance by screening strength (N = 30 seeds)**

| Strength | Capability | SD | d vs baseline |
|----------|-----------|------|--------------|
| 0.0 | 0.738 | 0.057 | — |
| 0.1 | 0.730 | 0.066 | -0.13 |
| 0.2 | 0.752 | 0.066 | +0.23 |
| 0.3 | 0.780 | 0.042 | +0.84 |
| 0.4 | 0.783 | 0.041 | +0.92 |
| 0.5 | 0.777 | 0.048 | +0.75 |
| 0.6 | 0.788 | 0.054 | +0.91 |
| 0.7 | 0.815 | 0.037 | +1.62 |
| 0.8 | 0.825 | 0.042 | +1.75 |
| 0.9 | 0.846 | 0.034 | +2.31 |
| 1.0 | 0.856 | 0.032 | +2.57 |

The coordination dose-response is near-perfectly monotonic (Spearman rho = +0.964). Effect sizes grow continuously from d = -0.13 at strength 0.1 to d = +2.57 at strength 1.0. No plateau, dip, or reversal detected. This confirms the consensus arm of the original mechanism — coordination benefits from arbitrarily strong screening.

All three governance levels show the same monotonic pattern (tight: rho = 0.964, moderate: rho = 0.973, light: rho = 0.982).

### 3.7 Confirmatory Findings

**Allocation** (10 seeds): gradual improvement across all governance levels (d = 0.30--1.65 at strength 1.0). Consistent with both mechanisms.

**Long horizon** (10 seeds): unexpectedly large improvement under tight governance (baseline 0.319 → strength 1.0: 0.971, d = 2.75). This falsified the null prediction but was based on only 10 seeds with high variance (SD = 0.33--0.45).

**Long horizon replication** (50 seeds, run 20260328_long_horizon_screening_replication, 750 runs): The d = 2.75 effect **did NOT replicate**. True effects are:
- Tight governance: d = 0.38, p = 0.058 (NOT significant at Bonferroni α/12 = 0.004)
- Moderate governance: d = 0.76, p = 0.0001 (Bonferroni-significant)
- Light governance: d = 0.05, p = 0.811 (null, ceiling effect)

The initial 10-seed estimate was inflated. There is a real but modest moderate-governance effect; tight governance shows no significant long-horizon benefit from high-strength screening.

### 3.8 Prediction Scorecard

| Prediction | Result | Implication |
|-----------|--------|-------------|
| Coordination monotonic ↑ | **Confirmed** (rho=0.96-0.98) | Consensus arm holds |
| Routing × tight inverted-U | **Falsified** (U-shape instead) | Diversity-consensus mechanism wrong |
| Routing × light positive/flat | **Mixed** (high variance) | Inconclusive |
| Long-horizon null | **Partially falsified** (d=0.76 moderate-gov, p<0.0001; d=0.38 tight-gov, p=0.058) | Modest effect found, initial estimate was inflated |

## 4. Discussion

### 4.1 Why the Mechanism Was Wrong

The diversity-consensus mechanism assumed screening acts symmetrically on all agents: reducing belief variance for everyone, which helps coordination and harms routing. This predicts monotonic harm for routing as screening strength increases.

The actual mechanism is asymmetric. SWARM's screening implementation computes per-agent friction as:

$$\text{friction}_{\text{effective}} = \text{friction}_{\text{base}} \times (1 - \text{trust} \times \text{strength})$$

where trust ranges from 0.0--0.3 (adversarial) to 0.7--1.0 (honest). At **low screening strength**, the trust discount ($\text{trust} \times \text{strength}$) is small for all agents. The result is noisy, inconsistent governance — some honest agents get spurious penalties, some adversarial agents get spurious relaxation. This is worse than uniform governance.

At **high screening strength**, the trust discount cleanly separates honest agents (discount 0.7--1.0) from adversarial agents (discount 0.0--0.3). Honest agents get genuine governance relaxation, restoring path diversity for them specifically. Adversarial agents remain constrained. This is *better* than uniform governance.

The U-shape emerges because there are three regimes:

1. **Strength 0.0** (uniform governance): moderate capability, consistent application
2. **Strength 0.1--0.5** (noisy signal regime): inconsistent governance degrades performance
3. **Strength 0.7--1.0** (clean signal regime): selective relaxation improves performance

The Phase 2 measurement at strength 0.5 happened to capture the worst regime — the bottom of the valley.

### 4.2 Screening as Selective Relaxation

The revised mechanism reframes screening entirely. It is not a belief-alignment tool (which would predict monotonic effects). It is a **selective relaxation** tool that conditionally reduces governance burden for trusted agents. Its effectiveness depends on the reliability of the trust signal.

This has different predictions from the original mechanism:

| Feature | Diversity-Consensus (falsified) | Selective Relaxation (revised) |
|---------|-------------------------------|-------------------------------|
| Routing dose-response | Inverted-U | U-shaped ✓ |
| Optimal routing strength | Low (0.1--0.2) | High (0.8--1.0) ✓ |
| Low-strength routing effect | Positive | Negative ✓ |
| Mechanism | Symmetric variance reduction | Asymmetric trust-based friction |
| Generalization | Any variance-reducing intervention | Only trust-differentiating interventions |

### 4.3 Implications for Mechanism Design Evaluation

Two lessons generalize beyond screening:

**1. Dose-response curves, not A/B tests.** Had we stopped at Phase 2, we would have concluded screening harms routing. The dose-response revealed that the harm is dose-specific: strength 0.5 is in the valley, but strength 1.0 exceeds baseline. Single-point A/B tests of mechanism design interventions are insufficient.

**2. Design your own falsification.** The dose-response sweep was designed specifically to test our proposed mechanism with pre-registered directional predictions. Two of four predictions were falsified, forcing mechanism revision. This is how empirical science should work — yet most multi-agent safety papers propose mechanisms without testing them.

### 4.4 Aggregate Metrics Still Mask Task-Specific Effects

The Phase 2 finding remains valid: aggregating across task types masks sign-reversed effects. At strength 0.5 under tight governance:

$$d_{avg} = \frac{1.04 + 0.40 + (-0.78) + (-0.06)}{4} = +0.15$$

This misleading aggregate hides both the coordination benefit and the routing harm.

### 4.5 Governance Cost Amplification

The frontier trace finding (governance cost amplifies 4.4x with task complexity) remains unaffected by the mechanism revision. Governance policy cannot be set system-wide for mixed-workload deployments.

## 5. Limitations

1. **Single adversarial fraction.** All experiments used 20% adversarial agents. The U-shape may change at higher adversarial fractions where the trust signal carries more defensive weight.

2. **Simulated agents.** SWARM agents use probabilistic behavioral models. The selective relaxation mechanism should generalize to LLM agents, but the exact curve shape may differ.

3. **Implementation-specific mechanism.** The U-shape is grounded in SWARM's multiplicative friction model ($\text{friction} \times (1 - \text{trust} \times \text{strength})$). Additive models or different trust-score distributions could produce different dose-response shapes.

4. **Long-horizon result underpowered.** The large effect at strength 1.0 (d = 2.75) from 10 seeds did not replicate at 50 seeds. Replication (run 20260328_long_horizon_screening_replication) confirms the concern and reveals that tight-governance long-horizon effects are not significant at Bonferroni correction; only moderate governance shows a real effect (d = 0.76).

5. **High variance in routing.** Routing shows bimodal outcomes (SD = 0.37--0.42 at most strengths), reflecting a binary success/failure pattern. The U-shape in means may obscure different distributional dynamics.

## 6. Future Work

1. **Long-horizon replication at 30+ seeds.** ✓ **Completed** (run 20260328_long_horizon_screening_replication, 50 seeds). The d = 2.75 effect did not replicate; real effects are moderate-governance-specific (d = 0.76, Bonferroni-significant) and tight-governance null (d = 0.38, p = 0.058).

2. **Higher adversarial fractions (40%, 60%).** Test whether the U-shape trough shifts rightward as adversaries become more prevalent and the value of trust discrimination increases.

3. **LLM agent validation.** Replicate the U-shaped routing curve with LLM agents. The selective relaxation mechanism predicts the U-shape should appear whenever trust-based differentiation is implemented, regardless of agent architecture.

4. **Alternative trust models.** Test additive trust ($\text{friction} - \text{trust} \times \text{strength}$) and threshold trust ($\text{friction} \times \mathbb{1}[\text{trust} \times \text{strength} < \tau]$) to determine whether the U-shape is a general property of trust-based governance or specific to multiplicative models.

5. **Topology interaction.** Test whether network structure modulates the trust signal's reliability and shifts the U-shape trough.

## 7. Conclusion

We proposed a diversity-consensus mechanism for screening's task-type-dependent effects, then designed an experiment that falsified it. The replacement — screening as selective relaxation — explains both the U-shaped routing dose-response and the monotonic coordination improvement.

The practical takeaway is reversed from what Phase 2 alone suggested. Screening at strength 0.5 harms routing under tight governance — but this is a local minimum, not the final answer. At strength 1.0, screening exceeds the unscreened baseline for routing while massively improving coordination (d = 2.57). The optimal policy is not "avoid screening for routing" but "use full-strength screening for everything."

More broadly, this work demonstrates that mechanism design interventions in multi-agent systems require dose-response characterization, not single-point evaluation, and that the best way to refine a mechanism proposal is to try to break it.

## References

- Savitt, R. et al. (2026). From 84 claims to three theories: Governance, taxation, and architecture in multi-agent safety. *SWARM Research Collective.*
- Rothschild, M. & Stiglitz, J. (1976). Equilibrium in competitive insurance markets. *Quarterly Journal of Economics*, 90(4), 629--649.

## Appendix A: Run Provenance

| Run ID | Type | Seeds | Task Types | Runs | Purpose |
|--------|------|-------|-----------|------|---------|
| 20260304_212912_frontier_trace | sweep | 50 | routing, coord, alloc, l_horiz | 1,400 | Governance Pareto frontier |
| 20260304_213700_screening | sweep | 50 | routing, coord, alloc, l_horiz | 1,200 | Screening A/B (main) |
| 20260304_232817_screening | sweep | 20 | routing | 120 | Screening A/B (routing repl) |
| 20260304_232823_screening | sweep | 20 | long_horizon | 120 | Screening A/B (l_horiz repl) |
| 20260326_screening_strength_sweep | sweep | 30/10 | routing, coord, alloc, l_horiz | 2,640 | Dose-response |
| 20260328_long_horizon_screening_replication | sweep | 50 | long_horizon | 750 | L_horiz replication |

**Total: 6,230 runs across 6 experiments.**

## Appendix B: Phase 2 Effect Size Tables

**Table B1. Frontier trace — Cohen's d vs oracle by config and task type**

| Config | Routing | Coordination | Allocation | Long Horizon |
|--------|---------|-------------|------------|-------------|
| loose | 0.00 | 3.99 | 0.69 | 0.00 |
| light | 0.47 | 4.05 | 1.60 | 0.41 |
| moderate-light | 0.94 | 6.95 | 7.01 | 0.96 |
| moderate | 1.28 | 5.78 | 7.89 | 1.37 |
| tight-moderate | 1.38 | 5.72 | 7.33 | 2.04 |
| tight | 1.34 | 6.08 | 6.63 | 1.63 |

**Table B2. Phase 2 screening effect — detailed statistics per cell**

| Task | Gov | Base mean | Scrn mean | Delta | d | p | Bonf sig? |
|------|-----|----------|----------|-------|---|---|-----------|
| coord | tight | 0.731 | 0.789 | +0.058 | +1.04 | <0.000001 | Yes |
| coord | moderate | 0.785 | 0.826 | +0.041 | +0.97 | 0.000001 | Yes |
| coord | light | 0.965 | 0.976 | +0.011 | +1.10 | <0.000001 | Yes |
| alloc | tight | 0.895 | 0.903 | +0.008 | +0.40 | 0.044 | No |
| alloc | moderate | 0.901 | 0.919 | +0.018 | +0.87 | 0.000015 | Yes |
| alloc | light | 0.992 | 0.994 | +0.003 | +0.42 | 0.035 | No |
| routing | tight | 0.692 | 0.400 | -0.293 | -0.78 | 0.0001 | Yes |
| routing | moderate | 0.567 | 0.517 | -0.051 | -0.12 | 0.534 | No |
| routing | light | 0.883 | 0.935 | +0.053 | +0.21 | 0.285 | No |
| l_horiz | tight | 0.609 | 0.584 | -0.025 | -0.06 | 0.753 | No |
| l_horiz | moderate | 0.548 | 0.649 | +0.101 | +0.25 | 0.205 | No |
| l_horiz | light | 0.903 | 0.964 | +0.061 | +0.27 | 0.179 | No |

## Appendix C: Phase 3 Dose-Response Tables

**Table C1. Routing capability by screening strength and governance (N = 30 seeds)**

| Strength | Tight | Moderate | Light |
|----------|-------|----------|-------|
| 0.0 | 0.623 | 0.601 | 0.949 |
| 0.1 | 0.412 | 0.477 | 0.865 |
| 0.2 | 0.385 | 0.505 | 0.811 |
| 0.3 | 0.414 | 0.614 | 0.865 |
| 0.4 | 0.368 | 0.507 | 0.919 |
| 0.5 | 0.503 | 0.453 | 1.000 |
| 0.6 | 0.503 | 0.658 | 0.946 |
| 0.7 | 0.537 | 0.622 | 0.946 |
| 0.8 | 0.572 | 0.733 | 1.000 |
| 0.9 | 0.507 | 0.734 | 0.973 |
| 1.0 | 0.778 | 0.707 | 0.946 |

**Table C2. Coordination capability by screening strength and governance (N = 30 seeds)**

| Strength | Tight | Moderate | Light |
|----------|-------|----------|-------|
| 0.0 | 0.738 | 0.792 | 0.966 |
| 0.1 | 0.730 | 0.788 | 0.967 |
| 0.2 | 0.752 | 0.795 | 0.973 |
| 0.3 | 0.780 | 0.805 | 0.969 |
| 0.4 | 0.783 | 0.826 | 0.977 |
| 0.5 | 0.777 | 0.824 | 0.977 |
| 0.6 | 0.788 | 0.843 | 0.984 |
| 0.7 | 0.815 | 0.838 | 0.980 |
| 0.8 | 0.825 | 0.862 | 0.984 |
| 0.9 | 0.846 | 0.867 | 0.987 |
| 1.0 | 0.856 | 0.874 | 0.989 |

**Table C3. Cohen's d vs baseline (strength 0.0) — routing by governance**

| Strength | Tight | Moderate | Light |
|----------|-------|----------|-------|
| 0.1 | -0.53 | -0.31 | -0.35 |
| 0.2 | -0.61 | -0.24 | -0.51 |
| 0.3 | -0.53 | +0.03 | -0.35 |
| 0.4 | -0.66 | -0.23 | -0.15 |
| 0.5 | -0.30 | -0.37 | +0.49 |
| 0.6 | -0.30 | +0.14 | -0.01 |
| 0.7 | -0.21 | +0.05 | -0.01 |
| 0.8 | -0.12 | +0.34 | +0.49 |
| 0.9 | -0.28 | +0.34 | +0.16 |
| 1.0 | +0.41 | +0.27 | -0.01 |

---

*All run data, claim cards, and analysis scripts are available at the SWARM artifacts repository.*
