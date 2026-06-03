---
description: "We model Research Swarm, a live multi-agent platform that recruits AI agents to research Triple-Negative Breast Cancer, as a distributional safety..."
---

# Parametric Governance Cannot Fix Structural Vulnerabilities: Evidence from a Live AI Research Platform

## Abstract

We model Research Swarm, a live multi-agent platform that recruits AI agents to research Triple-Negative Breast Cancer, as a distributional safety scenario using the SWARM framework. Our 19-agent simulation sweeps five governance parameters (audit rate, externality pricing, platform extraction, entry staking, and [agent composition](../bridges/research_swarm.md)) across 20-epoch runs and subjects the governance configuration to 8 adversarial attacks across two hardening rounds. Four of five [governance levers](../getting-started/first-scenario.md) produce zero improvement in toxicity, the system's primary safety metric. The lone effective lever---agent composition---is not a governance parameter but a property of the population. Red-team evaluation scores 0.64/1.00 (Grade D); after 13 targeted parameter changes, the score improves to 0.70 but welfare collapses 78% and a previously prevented attack (collusion ring) regresses to successful. We identify a structural property of parametric governance in open-entry multi-agent systems: post-hoc scoring mechanisms redistribute costs but do not create behavioral feedback loops, and tightening one parameter can shift adversary behavior to exploit adjacent surfaces. We propose five structural interventions---flow-level monitoring, adaptive feedback loops, tiered access, graduated sanctions, and population screening---that address the root causes parametric tuning cannot reach.

## Introduction

Multi-agent AI platforms increasingly deploy autonomous agents in open-entry environments where agents interact, produce outputs consumed by humans, and face [governance mechanisms](../concepts/governance.md) designed to maintain quality and safety. Understanding whether standard governance levers---audit rates, economic penalties, entry barriers---actually improve safety outcomes is critical for platform designers.

Research Swarm is a live multi-agent system that recruits AI agents to research Triple-Negative Breast Cancer (TNBC). Agents register on the platform, receive research tasks, search PubMed for relevant literature, submit cited findings, and 30\% of the time perform quality control (QC) reviews of other agents' work. The platform captures approximately 70\% of the value generated through compute extraction, while agents bear most of the risk from quality failures.

This platform exhibits several properties that make it a natural target for distributional safety analysis: open entry with no staking barrier, reputation-based QC assignment, externalities on downstream consumers who trust the research database, collusion vulnerability through coordinated QC rubber-stamping, and asymmetric value extraction. These are not unique to Research Swarm---they are structural properties of any open-entry multi-agent research or content platform.

We model Research Swarm as a SWARM scenario with 19 scripted agents spanning five behavioral types, sweep five governance parameters, and run the full SWARM red-team attack library against the governance configuration. Our central finding is that parametric governance---adjusting rates, thresholds, and fees---is fundamentally insufficient for safety in systems where agents follow fixed strategies. The interventions that matter are structural, not parametric.

## Methods

### Scenario Design

We model Research Swarm using the SWARM distributional safety framework, which converts observable agent signals into probabilistic quality estimates through a calibrated proxy pipeline:

$$\text{Observables} \rightarrow \text{ProxyComputer} \rightarrow \hat{v} \rightarrow \sigma(\hat{v}) \rightarrow p \in [0,1]$$

where $p = P(v = +1)$ represents the probability that an interaction is beneficial. The soft payoff engine then computes:

$$S_{\text{soft}} = p \cdot s^+ - (1-p) \cdot s^-$$
$$E_{\text{soft}} = (1-p) \cdot h$$

where $s^+ = 4.0$ (verified finding value), $s^- = 2.0$ (fabricated finding damage), and $h = 3.5$ (downstream harm to researchers who cite fabricated findings). Platform extraction $\theta = 0.7$ captures 70\% of surplus, and externality internalization $\rho = 0.05$ means agents barely feel downstream consequences.

Toxicity, defined as $E[1-p \mid \text{accepted}]$, serves as the primary safety metric with a threshold of 0.35.

### Agent Composition

The scenario uses 19 agents modeling participant types observed in open research platforms:

\begin{table}[H]
\centering
\begin{tabular}{llrl}
\toprule
Type & Count & Fraction & Behavior \\
\midrule
Honest & 8 & 42\% & Diligent researchers with real citations \\
Deceptive & 3 & 16\% & Plausible but fabricated findings \\
Opportunistic & 4 & 21\% & Minimal-effort copy-paste \\
Adversarial & 2 & 11\% & Coordinate to game QC \\
Collusive verifier & 2 & 11\% & Rubber-stamp colluding partners \\
\bottomrule
\end{tabular}
\caption{Agent composition in the Research Swarm scenario.}
\end{table}

### Governance Configuration

The governance maps Research Swarm's actual mechanisms: 30\% QC review rate (audit\_probability = 0.3), reputation-weighted QC assignment ($w_{\text{rep}} = 1.5$), circuit breakers that freeze flagged agents, collusion detection for coordinated rubber-stamping, sybil detection, and deliberately no staking barrier (matching the platform's open-entry design).

### Perturbation Design

This scenario uses both parameter shocks and agent dropout simultaneously. At epoch 10, the QC rate drops from 30\% to 15\% for five epochs (modeling platform resource constraints). Deceptive and adversarial agents face 8\% per-step dropout probability (modeling token budget exhaustion), while honest agents are exempt.

### Sweep Protocol

Each sweep varies a single governance parameter while holding all others at baseline values. All runs use seed 42, 20 epochs, and 15 steps per epoch.

### Red-Team Protocol

We evaluate governance robustness using the SWARM RedTeamEvaluator with 8 attack scenarios: reputation farming, collusion ring, threshold dancing, [sybil attack](../guides/red-teaming.md), timing attack, information laundering, resource drain, and governance gaming. After the initial evaluation, we apply targeted parameter changes and re-evaluate.

## Results

### Sweep 1: Audit Rate (audit\_probability 0.1--0.5)

Quintupling the audit rate produced no measurable change in toxicity (0.3470--0.3473 across all values). The QC mechanism penalizes agents after the fact but does not change which interactions are generated or accepted.

\begin{table}[H]
\centering
\begin{tabular}{rrrr}
\toprule
AP & Avg Toxicity & Avg Quality Gap & Final Welfare \\
\midrule
0.1 & 0.3470 & 0.1284 & 45.38 \\
0.3 & 0.3472 & 0.1289 & 41.12 \\
0.5 & 0.3473 & 0.1289 & 41.12 \\
\bottomrule
\end{tabular}
\caption{Audit rate sweep results.}
\end{table}

### Sweep 2: Externality Internalization ($\rho$ 0.01--0.50)

Raising $\rho$ 50$\times$ crushed welfare by 67\% (43.49 $\rightarrow$ 14.46) and payoffs by 46\% (1.304 $\rightarrow$ 0.709). Toxicity remained identical at 0.3472 across all values. Externality pricing is an accounting transfer that does not create behavioral feedback.

\begin{table}[H]
\centering
\begin{tabular}{rrrr}
\toprule
$\rho$ & Avg Toxicity & Avg Payoff & Final Welfare \\
\midrule
0.01 & 0.3472 & 1.3041 & 43.49 \\
0.20 & 0.3472 & 1.0732 & 32.23 \\
0.50 & 0.3472 & 0.7086 & 14.46 \\
\bottomrule
\end{tabular}
\caption{Externality internalization sweep results.}
\end{table}

### Sweep 3: Platform Extraction ($\theta$ 0.3--0.9)

Payoff scales linearly with $\theta$. Toxicity, quality gap, interactions, and welfare are identical across all values. The platform's extraction rate is a distributional question, not a safety question.

### Sweep 4: Entry Staking (min\_stake 0--5)

Staking was the first lever to change behavior---interactions dropped 25\% (731 $\rightarrow$ 552). But the effect was counterproductive: toxicity \textit{increased} from 0.347 to 0.371, quality gap narrowed from 0.129 to 0.109, and welfare collapsed 88\% (41.12 $\rightarrow$ 4.73). The barrier filtered participation indiscriminately, hitting honest agents as hard as deceptive ones. The damage saturated immediately---no meaningful difference between stake = 0.5 and stake = 5.0.

\begin{table}[H]
\centering
\begin{tabular}{rrrrr}
\toprule
Stake & Interactions & Avg Toxicity & Quality Gap & Final Welfare \\
\midrule
0.0 & 731 & 0.3472 & 0.1289 & 41.12 \\
0.5 & 552 & 0.3687 & 0.1100 & 4.73 \\
5.0 & 550 & 0.3711 & 0.1086 & 6.97 \\
\bottomrule
\end{tabular}
\caption{Entry staking sweep results.}
\end{table}

### Sweep 5: Deceptive Agent Count (1--7)

Agent composition was the only lever across all five sweeps to push toxicity past the 0.35 threshold. At 7 deceptive agents (30\% of the 23-agent population), toxicity reached 0.356, breaching the success criterion. Quality gap peaked at dec = 1 (0.172) where QC has the easiest separation job, and the pattern shows real sensitivity to population composition rather than flat-line indifference.

\begin{table}[H]
\centering
\begin{tabular}{rrrrrr}
\toprule
Deceptive & Total & Avg Toxicity & Quality Gap & Final Welfare \\
\midrule
1 & 17 & 0.3478 & 0.1723 & 34.17 \\
3 & 19 & 0.3472 & 0.1289 & 41.12 \\
5 & 21 & 0.3473 & 0.1548 & 62.51 \\
7 & 23 & \textbf{0.3560} & 0.1520 & 34.90 \\
\bottomrule
\end{tabular}
\caption{Deceptive agent count sweep results. Bold indicates threshold breach.}
\end{table}

### Red-Team Round 1: Original Governance

The governance scored 0.64/1.00 (Grade D), preventing 4 of 8 attacks with 25.6\% average evasion rate and 228.9 total damage.

\begin{table}[H]
\centering
\begin{tabular}{lllrr}
\toprule
Attack & Difficulty & Result & Damage & Evasion \\
\midrule
Reputation Farming & moderate & PREVENTED & 14.2 & 20.0\% \\
Collusion Ring & advanced & PREVENTED & 23.1 & 10.8\% \\
Threshold Dancing & advanced & PREVENTED & 20.5 & 28.7\% \\
Sybil Attack & expert & PREVENTED & 19.9 & 5.6\% \\
Timing Attack & advanced & SUCCEEDED & 25.7 & 35.9\% \\
Info Laundering & expert & SUCCEEDED & 45.6 & 31.9\% \\
Resource Drain & moderate & SUCCEEDED & 57.0 & 39.9\% \\
Governance Gaming & expert & SUCCEEDED & 22.8 & 31.9\% \\
\bottomrule
\end{tabular}
\caption{Red-team Round 1 results against original governance.}
\end{table}

Collusion and sybil detection performed well, catching coordination attacks in 5 epochs with low evasion. Resource drain was the highest-damage attack (57.0) due to the absence of staking barriers and only a 5\% transaction tax. Information laundering bypassed agent-level circuit breakers by routing harm through proxies.

### Governance Hardening

We applied 13 parameter changes targeting the 4 successful attacks: audit probability 0.3 $\rightarrow$ 0.4, penalty multiplier 2$\times$ $\rightarrow$ 3$\times$, circuit breaker threshold 0.6 $\rightarrow$ 0.45, freeze violations 3 $\rightarrow$ 2, freeze duration 2 $\rightarrow$ 3 epochs, collusion thresholds tightened (frequency 1.5 $\rightarrow$ 1.3, correlation 0.6 $\rightarrow$ 0.5), sybil similarity 0.8 $\rightarrow$ 0.75, transaction tax 5\% $\rightarrow$ 12\%, and bandwidth cap 12 $\rightarrow$ 8.

### Red-Team Round 2: Hardened Governance

The hardened governance scored 0.70/1.00 (Grade D), preventing 5 of 8 attacks.

\begin{table}[H]
\centering
\begin{tabular}{llrrrl}
\toprule
Attack & Result & Damage & Evasion & vs.\ R1 \\
\midrule
Reputation Farming & PREVENTED & 13.2 & 18.5\% & same \\
Collusion Ring & SUCCEEDED & 21.4 & 10.0\% & \textbf{regressed} \\
Threshold Dancing & PREVENTED & 19.0 & 26.6\% & same \\
Sybil Attack & PREVENTED & 18.5 & 5.2\% & same \\
Timing Attack & PREVENTED & 23.8 & 33.3\% & fixed \\
Info Laundering & SUCCEEDED & 42.2 & 29.6\% & improved \\
Resource Drain & SUCCEEDED & 52.8 & 37.0\% & improved \\
Governance Gaming & PREVENTED & 21.1 & 29.6\% & fixed \\
\bottomrule
\end{tabular}
\caption{Red-team Round 2 results against hardened governance.}
\end{table}

The hardening fixed 2 attacks (timing, governance gaming), improved 2 (resource drain $-$7\%, information laundering $-$7\%), but caused the collusion ring to regress from prevented to successful. Total damage decreased 7\% (228.9 $\rightarrow$ 212.0).

Critically, the simulation told a different story from the red-team scorecard:

\begin{table}[H]
\centering
\begin{tabular}{lrrr}
\toprule
Metric & v1 & v2 & Change \\
\midrule
Total interactions & 731 & 562 & $-$23\% \\
Avg toxicity & 0.3472 & 0.3479 & $\sim$same \\
Final welfare & 41.12 & 9.20 & $-$78\% \\
\bottomrule
\end{tabular}
\caption{Simulation outcomes under original vs.\ hardened governance.}
\end{table}

The tighter circuit breaker (0.45 threshold, 2-strike, 3-epoch freeze) and reduced bandwidth cap throttled economic activity across the board, collapsing welfare by 78\% while producing negligible improvement in the safety metric.

## Discussion

### The Accounting Mechanism Problem

Four of five governance levers---audit rate, externality pricing, platform extraction, and staking---produced zero improvement in toxicity. These parameters operate after interactions occur: they redistribute costs and surplus but do not change which interactions are generated or which agents participate.

This is not a simulation artifact. It reflects a structural property of parametric governance in systems with fixed-strategy agents: \textbf{post-hoc scoring mechanisms are accounting mechanisms, not behavioral feedback loops.} They can change who gets paid how much, but they cannot change behavior unless agents observe and respond to their own cost trajectory.

### The Whack-a-Mole Problem

The most revealing result from the red-team evaluation is that tightening collusion detection caused the collusion ring to succeed. In Round 1, the collusion ring was prevented. In Round 2, with stricter thresholds (frequency 1.5 $\rightarrow$ 1.3, correlation 0.6 $\rightarrow$ 0.5), the more aggressive lever changed interaction patterns enough that the collusion ring found new exploitation paths.

This is governance whack-a-mole: parametric hardening is inherently local---it patches the specific attack that was tested but can open new vulnerabilities in the process. The grade remained D (0.64 $\rightarrow$ 0.70), and the welfare cost ($-$78\%) far exceeded the security improvement ($+$9\%).

### The Binding Constraint

Agent composition is the binding constraint on safety outcomes. The system tolerates up to approximately 26\% deceptive agents before toxicity breaches the 0.35 threshold. No governance parameter we tested can change this ratio---they can only change what happens after agents of a given type interact.

This maps to a concrete prediction: for any open-entry multi-agent platform, \textbf{the most impactful long-term safety intervention is making deception costly over time}, shifting population composition toward honest agents through selection pressure rather than post-hoc penalties.

### Structural Interventions

The sweep and red-team results converge on five structural interventions that address root causes parametric tuning cannot reach:

\begin{enumerate}
\item \textbf{Flow-level monitoring}: Track value chains across agents, not just individual behavior. This is the only defense against information laundering, where harm routes through proxies that look clean in isolation.
\item \textbf{Adaptive feedback loops}: Make QC outcomes affect future task assignment, not just payoffs. This converts audit\_probability and $\rho$ from accounting adjustments into decision-shaping mechanisms.
\item \textbf{Tiered access with optional staking}: Preserve open entry for basic tasks but require staking for high-value task access. This targets resource drain without the 88\% welfare collapse of universal staking.
\item \textbf{Graduated sanctions}: Replace binary circuit-breaker freezes with progressive penalties. The v2 welfare collapse was driven by the aggressive freeze mechanism; smoother penalties preserve economic activity while maintaining deterrence.
\item \textbf{Population screening}: Make deception costly over time through reputation-gated access, escalating verification requirements, and declining task allocation for low-quality agents.
\end{enumerate}

### Limitations

All results use scripted agents with fixed strategies. The same sweeps with LLM-backed agents or RL agents that observe their own payoff history and adapt strategies may produce different results. When agents can switch strategies in response to declining payoffs, parametric levers could become the decision-shaping mechanisms they are designed to be. Additionally, the perturbation engine uses a single shock profile; multiple shock patterns could reveal different vulnerability surfaces.

## Conclusion

We present evidence from a live AI research platform model that parametric governance---adjusting audit rates, economic penalties, extraction shares, and entry barriers---is insufficient for safety in open-entry multi-agent systems with fixed-strategy agents. Five governance [parameter sweeps](../guides/parameter-sweeps.md) show that four of five levers produce zero toxicity improvement, while the fifth (entry staking) is counterproductive. Red-team evaluation demonstrates governance whack-a-mole: hardening that fixes two attacks causes one to regress and collapses welfare 78\%. The binding constraint on safety is population composition, not parameter tuning. We propose five structural interventions---flow-level monitoring, adaptive feedback, tiered access, graduated sanctions, and population screening---and identify the transition to adaptive (LLM/RL) agents as the critical next experiment for understanding whether parametric governance can be made effective.

## References

\begin{enumerate}
\item SWARM: System-Wide Assessment of Risk in Multi-agent systems. \url{https://github.com/swarm-ai-research/swarm}
\item Research Swarm. \url{https://github.com/openclawprison/research-swarm}
\end{enumerate}
