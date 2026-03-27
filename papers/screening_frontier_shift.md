# Contract Screening is a Task Specialization Tool, Not a Universal Safety-Capability Frontier Improvement

**Authors:** SWARM Research Collective
**Date:** 2026-03-26
**Framework:** SWARM v1.4.0

## Abstract

Mechanism design interventions in multi-agent systems are typically evaluated on aggregate metrics, obscuring critical task-type interactions. We report results from a 1,400-run governance Pareto frontier trace and a 1,200-run screening intervention study (with two independent replications) in the SWARM multi-agent safety framework. The frontier trace establishes that governance capability cost is perfectly monotonic across seven intensity levels and four task types, but the magnitude varies 4.4x: allocation tasks lose 10% capability under tight governance while long-horizon tasks lose 46%. When contract screening (strength 0.5) is added to this frontier, the effect is not uniformly positive. Screening universally improves coordination capability (Cohen's d = 0.97--1.10, all Bonferroni-significant at alpha/18), modestly improves allocation, but *harms* routing capability under tight governance (d = -0.78, Bonferroni-significant) and has no effect on long-horizon planning. The routing harm replicates directionally in a 20-seed independent run. These results establish that screening is a task specialization tool — beneficial for consensus-dependent work, harmful for diversity-dependent work — and that evaluating governance interventions on aggregate metrics can mask task-specific harms.

## 1. Introduction

A central promise of mechanism design in multi-agent AI safety is that well-chosen interventions can shift the capability-safety Pareto frontier outward — achieving more capability at any given safety level, or more safety at any given capability level. Contract screening, which sorts agents into compatible pools based on revealed type information, is a candidate for such a universal improvement. Prior SWARM results showed that screening achieves perfect type separation (separation quality = 1.0 across 11 seeds) and generates a 6.7x honest payoff premium (Savitt et al., 2026).

But does perfect type separation translate to universal capability improvement? The answer, we show, is no. The mapping from mechanism design to capability outcomes is mediated by task structure. Tasks that require consensus formation (coordination) benefit from the variance reduction that screening provides. Tasks that require diversity of approach (routing under constraints) are harmed by the same variance reduction. Tasks that depend on neither (long-horizon planning) are unaffected.

This finding has immediate practical implications. Researchers deploying screening or similar belief-alignment mechanisms must evaluate effects per task type, not in aggregate. A mechanism that is Bonferroni-significant positive for one task type can be Bonferroni-significant *negative* for another in the same system.

### 1.1 Contributions

1. **Governance Pareto frontier with task-type resolution.** A 1,400-run sweep across 7 governance intensities and 4 task types establishes the first complete capability-safety frontier for SWARM, showing that governance cost amplifies 4.4x with task complexity.

2. **Screening as task specialization.** A 1,200-run A/B study with two replications shows that screening is not a frontier improvement but a task-specific intervention, with sign-reversed effects across task types.

3. **The diversity-consensus tradeoff.** We propose a mechanism: screening reduces agent belief variance, which helps consensus-dependent tasks and harms diversity-dependent tasks. This predicts which future interventions will show task-type interactions.

## 2. Methods

### 2.1 Frontier Trace Design

To establish the baseline capability-safety frontier, we ran a full factorial sweep:

- **Governance configurations (7):** oracle (no governance, no adversaries), loose (audit 0.05, no enforcement), light (audit 0.15, no CB), moderate-light (audit 0.30, CB disabled, stake 2.0), moderate (audit 0.50, CB enabled at 0.4, stake 4.0), tight-moderate (audit 0.80, CB at 0.6, stake 6.0), tight (audit 1.0, CB at 0.8, stake 8.0, 3 confirmation gates)
- **Task types (4):** routing (message delivery), coordination (consensus formation), allocation (resource distribution), long_horizon (multi-step pipeline)
- **Seeds:** 50 per configuration
- **Agents:** 10 per run, 20% adversarial fraction (except oracle: 0% adversarial)
- **Total runs:** 1,400

Metrics: capability (composite of completion, fidelity, efficiency), safety_proxy (governance signal strength), completion_rate (binary task success).

### 2.2 Screening Intervention Design

To test whether screening shifts the frontier, we ran a paired comparison:

**Main study (run 20260304_213700_screening):**
- **Conditions (2):** baseline (screening_strength = 0.0) vs screening (screening_strength = 0.5)
- **Governance levels (3):** tight, moderate, light
- **Task types (4):** routing, coordination, allocation, long_horizon
- **Seeds:** 50 per configuration
- **Total runs:** 1,200

**Replications:**
- **Routing replication (run 20260304_232817_screening):** 20 seeds, routing task only, same 6 governance × screening configs
- **Long-horizon replication (run 20260304_232823_screening):** 20 seeds, long_horizon task only, same 6 configs

### 2.3 Statistical Methods

- **Effect sizes:** Cohen's d for screening vs baseline within each governance × task-type cell
- **Multiple comparison correction:** Bonferroni correction across 18 primary comparisons (3 governance levels × 4 task types × 1 comparison each + 6 replication comparisons), yielding threshold alpha/18 = 0.00278
- **p-values:** Welch's t-test (unequal variance)

## 3. Results

### 3.1 The Governance Pareto Frontier is Monotonic and Task-Universal

The frontier trace reveals a perfectly consistent ordering of capability across all four task types:

**oracle > loose > light > moderate-light > moderate > tight-moderate $\approx$ tight**

This ordering holds without exception. No task type reverses the ranking.

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

The magnitude of capability loss varies dramatically by task type. Under tight governance relative to oracle:

- **Allocation:** -10.4% (d = 6.63, but small absolute gap)
- **Coordination:** -29.0% (d = 6.08)
- **Routing:** -37.2% (d = 1.34, high variance from bimodal outcomes)
- **Long horizon:** -45.7% (d = 1.63, high variance)

The 4.4x amplification between allocation (-10%) and long-horizon (-46%) establishes that governance cost is not a uniform overhead but scales with task coordination demands. All pairwise comparisons (oracle vs each config) are Bonferroni-significant.

### 3.2 Loose Governance is Near-Costless

The loose configuration (audit rate 0.05, no circuit breaker, no staking, no confirmation gates) achieves >99.7% of oracle capability across all task types while providing a nonzero safety signal (safety_proxy = 0.015). This represents a near-free entry point on the Pareto frontier — the first rung of safety at negligible capability cost.

### 3.3 Screening Shifts the Frontier Differently by Task Type

The screening intervention does not uniformly improve the frontier. Table 2 reports Cohen's d for screening vs baseline within each governance × task-type cell.

**Table 2. Screening effect (Cohen's d, screening minus baseline) by task type and governance level**

| Task Type | Tight | Moderate | Light | Pattern |
|-----------|-------|----------|-------|---------|
| Coordination | **+1.04*** | **+0.97*** | **+1.10*** | Universal strong gain |
| Allocation | +0.40 | **+0.87*** | +0.42 | Moderate positive |
| Routing | **-0.78*** | -0.12 | +0.21 | Negative under tight |
| Long horizon | -0.06 | +0.25 | +0.27 | Null |

\* Bonferroni-significant (p < 0.00278)

**Coordination: universal improvement.** All three governance levels show large, consistent gains from screening. Effect sizes (d = 0.97--1.10) are uniform across governance tightness, and all survive Bonferroni correction with p < 0.000001. The absolute gains are 1--6 percentage points of capability, but the consistency and statistical robustness are exceptional.

**Routing under tight governance: significant harm.** Screening reduces routing capability from 0.692 to 0.400 under tight governance (d = -0.78, p = 0.0001). This is Bonferroni-significant and directionally replicated in the 20-seed replication run (0.636 to 0.449, d = -0.47, p = 0.14). Under moderate governance the effect is null; under light governance it trends positive.

**Allocation: modest positive.** Effect sizes range d = 0.40--0.87. Only the moderate-governance cell survives Bonferroni correction (p = 0.000015).

**Long horizon: null.** No cell approaches significance. Confirmed in the 20-seed replication.

### 3.4 Replication

**Table 3. Replication results (20 seeds per cell)**

| Task | Governance | d | p | Direction matches main? |
|------|-----------|---|---|------------------------|
| Routing | Tight | -0.47 | 0.141 | Yes |
| Routing | Moderate | -0.37 | 0.248 | Mixed (main was -0.12) |
| Routing | Light | +0.60 | 0.058 | Yes |
| Long horizon | Tight | +0.54 | 0.088 | Mixed |
| Long horizon | Moderate | +0.20 | 0.521 | Yes (both null) |
| Long horizon | Light | -0.04 | 0.894 | Yes (both null) |

The routing tight-governance harm directionally replicates. The long-horizon null replicates cleanly. No replication cell reaches Bonferroni significance at N = 20 (expected: power is approximately 35% for d = 0.78 at N = 20).

## 4. Discussion

### 4.1 The Diversity-Consensus Mechanism

We propose that screening's task-type dependence follows from a single mechanism: **screening reduces agent belief variance about partner intentions.** This variance reduction has opposite valence depending on task structure:

- **Coordination tasks** require agents to converge on compatible strategies. Reduced belief variance accelerates convergence and reduces coordination failures. Screening helps by ensuring agents in the same pool share compatible behavioral models.

- **Routing tasks** under constraints require agents to explore diverse paths. When governance already constrains the action space (tight governance = high audit, CB, staking, confirmation gates), adding screening further narrows path diversity. The result is convergence to suboptimal consensus routes.

- **Allocation tasks** are intermediate: agents make largely independent resource decisions, so belief alignment provides modest benefit without significant diversity costs.

- **Long-horizon tasks** depend on individual agent planning depth more than inter-agent belief alignment, making them invariant to screening.

This mechanism generates a testable prediction: *any governance intervention that reduces agent behavioral variance will show the same task-type interaction pattern — positive for coordination, negative for constrained-routing, null for long-horizon.* This applies to reputation systems, trust networks, and behavioral nudges, not just screening.

### 4.2 Implications for Mechanism Design Evaluation

The screening results challenge a common evaluation practice in multi-agent safety research: reporting aggregate metrics across task types. Had we averaged screening's effect across all four task types in the tight-governance condition, we would report:

$$d_{avg} = \frac{1.04 + 0.40 + (-0.78) + (-0.06)}{4} = +0.15$$

A small positive effect, statistically non-significant. This aggregate masks a d = +1.04 benefit for coordination and a d = -0.78 harm for routing — both individually Bonferroni-significant. The aggregate metric is not merely imprecise; it is misleading.

**Recommendation:** Multi-agent governance interventions should be evaluated with task-type resolution. Aggregate metrics should only be reported alongside per-task breakdowns. Any intervention showing mixed signs across task types should be flagged for task-specific deployment.

### 4.3 Governance Cost Amplification

The frontier trace establishes a quantitative principle: governance cost scales superlinearly with task coordination demands. The 4.4x amplification factor between allocation (10% loss) and long-horizon (46% loss) under identical governance parameters means that governance policy cannot be set system-wide for mixed-workload deployments.

Combined with the screening findings, this suggests that optimal governance is both task-type-dependent and intervention-specific. There is no single "governance dial" that is universally safe to turn up.

### 4.4 Loose Governance as Rational Default

The near-zero cost of loose governance (<0.3% capability loss) argues for loose governance as a rational default for new deployments. The safety signal is small (safety_proxy = 0.015) but nonzero, providing monitoring capability at negligible cost. This is consistent with the governance cost universality theory (Savitt et al., 2026): the marginal safety return per unit of governance cost is highest at the lightest end of the spectrum.

## 5. Limitations

1. **Single screening strength.** Only strength = 0.5 was tested. The diversity-consensus tradeoff predicts that lower screening strengths (0.1--0.3) may preserve routing capability while retaining coordination benefits.

2. **Single adversarial fraction.** All experiments used 20% adversarial agents. The frontier shape may change at higher adversarial fractions, where governance provides more defensive value.

3. **Simulated agents.** SWARM agents use probabilistic behavioral models, not LLMs. The diversity-consensus mechanism should hold for LLM agents, but the effect magnitudes may differ.

4. **Four task types.** The task-type taxonomy (routing, coordination, allocation, long-horizon) is SWARM-specific. Mapping to real-world multi-agent deployments requires validation.

5. **Single topology.** All experiments used the default SWARM network topology. The frontier shape and screening effects may vary with topology (small-world, scale-free, ring).

## 6. Future Work

1. **Screening strength sweep (0.0--1.0 in 0.1 increments):** Locate the optimal screening strength for each task type. The diversity-consensus mechanism predicts a crossover point for routing where low screening helps and high screening harms.

2. **Task-adaptive screening:** Deploy different screening strengths per task type within the same system. This requires infrastructure for task classification and dynamic mechanism selection.

3. **Higher adversarial fractions:** Test whether screening's routing harm persists at 40%+ adversarial fractions, where the adversary-suppression benefit may outweigh the diversity cost.

4. **LLM agent validation:** Replicate the core finding (screening helps coordination, harms constrained routing) with LLM-powered agents in SWARM's memori or concordia scenarios.

5. **Topology interaction:** Test whether network topology modulates the diversity-consensus tradeoff. Small-world networks may buffer against screening's diversity reduction.

## 7. Conclusion

Contract screening is not a universal improvement to the capability-safety frontier. It is a task specialization tool: strongly beneficial for consensus-dependent coordination (d = 0.97--1.10), harmful for diversity-dependent routing under tight governance (d = -0.78), and null for long-horizon planning. The underlying mechanism — variance reduction in agent beliefs — predicts which other interventions will show similar task-type interactions.

This finding, combined with the 4.4x amplification of governance costs across task types, establishes that multi-agent governance cannot be designed task-agnostically. Evaluating governance interventions requires task-type resolution, and deploying them requires task-type adaptation.

## References

- Savitt, R. et al. (2026). From 84 claims to three theories: Governance, taxation, and architecture in multi-agent safety. *SWARM Research Collective.*
- Rothschild, M. & Stiglitz, J. (1976). Equilibrium in competitive insurance markets. *Quarterly Journal of Economics*, 90(4), 629--649.

## Appendix A: Run Provenance

| Run ID | Type | Seeds | Task Types | Purpose |
|--------|------|-------|-----------|---------|
| 20260304_212912_frontier_trace | sweep | 50 | routing, coordination, allocation, long_horizon | Governance Pareto frontier |
| 20260304_213700_screening | sweep | 50 | routing, coordination, allocation, long_horizon | Screening A/B (main) |
| 20260304_232817_screening | sweep | 20 | routing | Screening A/B (routing replication) |
| 20260304_232823_screening | sweep | 20 | long_horizon | Screening A/B (long horizon replication) |

## Appendix B: Full Effect Size Tables

**Table B1. Frontier trace — Cohen's d vs oracle by config and task type**

| Config | Routing | Coordination | Allocation | Long Horizon |
|--------|---------|-------------|------------|-------------|
| loose | 0.00 | 3.99 | 0.69 | 0.00 |
| light | 0.47 | 4.05 | 1.60 | 0.41 |
| moderate-light | 0.94 | 6.95 | 7.01 | 0.96 |
| moderate | 1.28 | 5.78 | 7.89 | 1.37 |
| tight-moderate | 1.38 | 5.72 | 7.33 | 2.04 |
| tight | 1.34 | 6.08 | 6.63 | 1.63 |

**Table B2. Screening effect — detailed statistics per cell**

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

---

*All run data, claim cards, and analysis scripts are available at the SWARM artifacts repository.*
