---
description: Kernel invariant lists Bonferroni/Holm/BH as equally valid, but Bonferroni dominates the vault by default — Holm is a Pareto improvement worth evaluating
type: observation
status: pending
created: 2026-06-02
source: session friction during cross-link/validate of detection cohort
trigger: /rethink — methodology default change proposal
---

# Bonferroni dominates the vault by default, but Holm-Bonferroni is strictly better in nearly every case we use

## Observation

CLAUDE.md kernel invariant 6 allows `Bonferroni/Holm/BH` interchangeably. In practice, ~90% of vault claims use plain Bonferroni. This is a path-dependency artifact (older claims locked in the choice), not a deliberate methodology decision.

## Why this matters

For the test-family sizes SWARM actually produces:

| Family size | Typical SWARM context | Optimal correction |
|-------------|----------------------|--------------------|
| ≤10 | Single-scenario governance comparison | Bonferroni or Holm (equivalent) |
| 10–50 | Multi-metric sweep, factorial study | **Holm-Bonferroni** (same FWER, strictly more power) |
| >50 | Sweeps, screening exploration | **Benjamini-Hochberg** (FDR, not FWER) |

Plain Bonferroni on a 20-hypothesis family wastes power vs Holm with no guarantee benefit. The detection cohort already deviated from default and used Holm correctly — but the validator's confidence-gate check greps for "Bonferroni-significant" specifically, creating pressure to either:
1. Re-run analyses with Bonferroni (lose power), or
2. Add Holm to the validator's allowlist (right answer)

## Evidence triggers

- 20260524-231533_soft_vs_binary_detection: 11-hypothesis family analyzed with Holm; some findings would be missed under Bonferroni
- validate run on 2026-06-02 flagged 6 high-conf claims for "missing Bonferroni-significant" when several actually used Holm-Bonferroni or had Holm-strength evidence
- screening sweeps (1440-run grid) currently report nominal p-values — these should use BH, not any FWER method

## Direct contradiction: validator vs manual read (2026-06-02)

Within a single session we got conflicting signals on the same 15 claims:

| Source | Verdict |
|--------|---------|
| `/validate` skill | 0/15 claims fully pass, 49/90 gates passed (54%) |
| Manual file-by-file audit (general-purpose agent) | 15/15 pass gates 1, 2, 3, 5 |

The manual audit confirmed every claim has effect-size tokens (`d=`, `AUROC=`, `ECE=`, `Brier=`), N counts, correction method names, and enumerated boundary conditions in the expected fields. The validator is almost certainly doing a literal grep for `Bonferroni-significant` and failing to recognize valid `Holm-significant` / `Holm-Bonferroni` / `Holm-corrected` tokens that the detection cohort correctly used.

**This is no longer a hypothetical concern** — it's actively producing false-negative validation gates on well-formed claims, which would (a) waste session time on phantom remediation, or (b) pressure agents to rewrite Holm analyses as Bonferroni to satisfy the validator, losing statistical power.

**Highest-priority fix from this evidence**: update `/validate` gate 3's token list to accept the Holm and BH families before any further validation runs. Treat this as a validator bug, not a claim-quality issue.

## Proposal for /rethink

1. Amend kernel invariant 6 to **prefer Holm-Bonferroni over plain Bonferroni** as the FWER default; reserve plain Bonferroni for ≤5-hypothesis families where they coincide
2. Add explicit FDR guidance: sweeps with >50 hypotheses use BH, not FWER
3. Update validator's gate-3 token list to accept `Holm-significant`, `Holm-Bonferroni-significant`, `BH-significant`, `FDR-controlled` as equivalent to `Bonferroni-significant`
4. Decide: do we re-validate existing Bonferroni claims under Holm (would likely promote some medium→high)? Or grandfather them?

## Open questions

- Are there any claims where the choice of correction was load-bearing for the conclusion? (i.e., effect survives Holm but not Bonferroni, or vice versa)
- Does the screening cohort have any nominal-p-value findings that would change confidence under BH?

## Next action

Run `/rethink` when observation queue reaches threshold (currently 7/10 per CLAUDE.md trigger). Bundle with any other pending methodology observations.

---

Topics:
- [[_index]]

<!-- topics: methodology, statistics, multiple-testing, kernel-invariants -->
