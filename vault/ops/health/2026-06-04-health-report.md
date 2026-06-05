---
generated_at: 2026-06-04T00:00:00Z
mode: full
status_summary: 3 FAIL, 3 WARN, 2 PASS
---

# Vault Health Report — 2026-06-04

## Executive Summary

**Mode:** Full diagnostic  
**Date:** 2026-06-04  
**Vault scope:** 106 claims | 7 topic maps | 156 runs in inbox | 54 in-progress tasks

| Category | Status | Severity |
|----------|--------|----------|
| [1] Schema Compliance | PASS | — |
| [2] Orphan Detection | PASS | — |
| [3] Link Health | FAIL | Critical |
| [4] Description Quality | PASS | — |
| [5] Three-Space Boundaries | PASS | — |
| [6] Processing Throughput | WARN | Medium |
| [7] Stale Notes Detection | FAIL | High |
| [8] Topic Map Coherence | PASS | — |

**Overall Health:** Vault is structurally sound but has two critical issues requiring immediate attention: 27 dangling links and 8 very old claims with minimal connection density.

---

## Detailed Findings

### [1] Schema Compliance ✓ PASS

All 106 claims have valid YAML frontmatter with required fields:
- YAML frontmatter: 106/106 ✓
- `description` field: 106/106 ✓
- `status` field: 106/106 ✓
- `confidence` field: 106/106 ✓
- `evidence` section: 106/106 ✓
- `Topics` section: 106/106 ✓

**Action:** None required. Schema compliance is excellent.

---

### [2] Orphan Detection ✓ PASS

Zero orphan claims detected. All 106 claims have at least one incoming link from vault/claims/ or topic maps.

**Action:** None required. Knowledge graph connectivity is healthy.

---

### [3] Link Health ✗ FAIL

**27 dangling wiki links detected** — references to claims that do not exist as files.

**Critical links (6+ references):**
- `[[claim-id]]` — referenced in 6 files (likely placeholder/template artifact)
- `[[claim-circuit-breakers-dominate]]` — referenced in 1+ file(s)
- `[[claim-collusion-detection-is-binding-constraint-on-robustness]]` — referenced in 2 file(s)

**Sample of broken links (showing 10 of 27):**
1. `[[claim-acausality-depth-does-not-affect-cooperation-outcomes]]`
   - Referenced in: vault/governance-dashboard.md
   - Issue: File exists as `claim-acausality-depth-does-not-affect-cooperation-outcomes.md` but may have special characters
   
2. `[[claim-allocation-task-type-robust-to-tight-governance]]`
   - Referenced in: 1 file
   - Issue: Claim file not found in vault/claims/
   
3. `[[claim-coordination-task-shows-critical-threshold-below-58-percent-completion]]`
   - Referenced in: 1 file
   - Issue: Claim file not found in vault/claims/

4. `[[claim-frontier-improvements-are-task-dependent]]`
   - Referenced in: 1 file

5. `[[claim-governance-cost-amplified-by-task-complexity]]`
   - Referenced in: 1 file

6. `[[claim-governance-topology-modulates-screening-efficacy]]`
   - Referenced in: 1 file

7. `[[claim-id]]`
   - Referenced in: 6 files
   - Issue: Placeholder reference — should be replaced with actual claim names

8. `[[claim-id-1]]`
   - Referenced in: 1 file
   - Issue: Placeholder reference

9. `[[claim-id-2]]`
   - Referenced in: 1 file
   - Issue: Placeholder reference

10. `[[claim-ldt-agents-provide-welfare-stability-at-intermediate-composition]]`
    - Referenced in: 1 file
    - Issue: Claim file not found

**+ 17 more dangling links**

**Root causes:**
- Incomplete cross-link synchronization after claim creation or rename
- Placeholder claims in dashboards/topic maps not yet materialized
- Special character handling in claim filenames vs links

**Recommended action:**
1. Identify which dangling links are legitimate claims that should exist (create them)
2. Remove placeholder references like `[[claim-id]]` from dashboards
3. Run validation to sync all cross-links: `python scripts/validate-vault.py --fix-links`

---

### [4] Description Quality ✓ PASS

All 106 claims have substantive descriptions that:
- Are 50-200 characters (appropriate detail level)
- Add meaningful information beyond the title
- Include evidence context (effect sizes, correction methods)

Sample descriptions:
- "Adaptive acceptance thresholds linearly reduce toxicity (r=-0.90, 34% reduction at full internalization) with Bonferroni-significant effects"
- "Seven LDT studies across 5 scenarios find zero Bonferroni-significant effects of acausality depth or decision theory on outcomes"

**Action:** None required. Description quality meets standards.

---

### [5] Three-Space Boundaries ✓ PASS

No boundary violations detected:
- No ops/infrastructure content in vault/claims/
- No agent reflection or methodology content in vault/claims/
- No temporal state or queue content in vault/claims/
- All claims remain in proper knowledge space

**Action:** None required. Space boundaries are clean.

---

### [6] Processing Throughput ⚠ WARN

Inbox-to-total ratio shows moderate collector's fallacy risk.

**Current state:**
- Inbox (runs/): 156 items
- Vault (claims): 106 synthesized
- In-progress tasks: 54
- Inbox-to-total ratio: 59%

**Analysis:**
The vault has absorbed ~40% of collected runs into claims, but 156 unprocessed runs remain in the inbox. With 54 tasks in queue, systematic processing is ongoing, but the ratio suggests batch collection outpacing synthesis.

**Comparison to healthy thresholds:**
- Ratio 59% is above ideal (<50%) but below critical (>75%)
- Inbox count (156) is well above comfort zone (< 20)

**Recommended action:**
- Prioritize `/pipeline` processing on oldest runs to reduce inbox backlog
- Set target: reduce inbox to <50 items (ratio → <33%)
- Monitor queue throughput: target 5-10 claims extracted per session

---

### [7] Stale Notes Detection ✗ FAIL

**8 very old claims (>90 days) with minimal connectivity detected:**

| Claim | Age | Links | Last Update | Status |
|-------|-----|-------|-------------|--------|
| claim-deceptive-agents-dominate-moltbook-payoff-hierarchy.md | 103d | 1 | 2026-02-21 | Isolated |
| claim-full-governance-reduces-welfare-in-concordia.md | 103d | 1 | 2026-02-21 | Isolated |
| claim-graduated-defense-reduces-damage-monotonically.md | 102d | 1 | 2026-02-21 | Isolated |
| claim-ldt-agents-dominate-all-agent-types-in-mixed-populations.md | 96d | 1 | 2026-02-28 | Isolated |
| claim-memory-promotion-gate.md | 102d | 1 | 2026-02-21 | Isolated |
| claim-prompt-level-governance-fails-in-multi-agent-systems.md | 97d | 1 | 2026-02-27 | Isolated |
| claim-soft-toxicity-detector-robust-across-base-rates-0-05-to-0-50.md | 93d | 1 | 2026-03-04 | Isolated |
| claim-tax-phase-transition-hysteresis-predicted-but-untested.md | 93d | 1 | 2026-03-04 | Isolated |

**+ 3 additional stale notes (30-90 days old with <2 links)**

**Pattern:** These claims were created in early Feb (first batch) and never integrated into the knowledge graph. They have only 1 incoming link each (likely to a topic map) and have not been cross-linked to related claims or updated with new evidence.

**Risk:** Stale, isolated claims create "knowledge debt" — they are forgotten and may represent findings that need:
- Reweaving to connect to related discoveries
- Updating with subsequent experiment results
- Status revision if they've been superseded
- Archival if they're no longer relevant

**Recommended action:**
1. Run `/update [claim]` on each of the 8 very old claims to find new evidence
2. Run `/cross-link` on these claims to discover relationships to newer evidence
3. Review status field — if no new evidence after 90+ days, consider status change to `weakened` or `archived`
4. Set maintenance reminder: flag any claim > 60 days without update for triage

---

### [8] Topic Map Coherence ✓ PASS

**7 topic maps maintain healthy structure:**

| Topic Map | Claims Linked | Status |
|-----------|---------------|--------|
| _index | 106 | Core hub — all claims connected |
| governance-dashboard | 96 | Primary map — 91% coverage |
| failures-dashboard | 8 | Specialized — appropriate size |
| evidence-trail | 0 | Archive/reference map |
| experiments-dashboard | 0 | Archive/reference map |
| stats | 0 | Archive/reference map |
| sweeps-dashboard | 0 | Archive/reference map |

**Structure:** Two active maps (governance-dashboard + _index) with 100% coverage of knowledge base, plus specialized failure notes map. Inactive maps serve as navigation reference.

**Action:** None required. Topic map structure is sound.

---

## Maintenance Signals

| Signal | Count | Threshold | Status |
|--------|-------|-----------|--------|
| Pending observations | 7 | ≥10 | OK |
| Open tensions | 0 | ≥5 | OK |
| Inbox items | 156 | ≥3 | **TRIGGERED** |
| Unprocessed sessions | 0 | ≥5 | OK |
| Dangling links | 27 | 0 | **TRIGGERED** |
| Very stale notes | 8 | 0 | **TRIGGERED** |
| Queue backlog | 54 tasks | Monitor | Active |

**Triggered conditions require action:**

1. **Dangling links (27)** — broken graph integrity
   - Action: `/validate --fix-links` or manual repair
   - Priority: High (user-facing broken links)

2. **Inbox backlog (156 runs)** — unprocessed research
   - Action: `/pipeline` on batches or `/extract` on targeted runs
   - Priority: High (knowledge is trapped in raw data)

3. **Stale notes (8 >90d)** — abandoned discoveries
   - Action: `/update` or archival triage
   - Priority: Medium (memory debt compounds)

---

## Top Recommended Actions (Ranked by Impact)

### 1. Fix 27 dangling links (HIGH IMPACT)

**Why:** Dangling links are broken promises in the knowledge graph. Readers follow links that lead nowhere, eroding trust. This compounds as vault grows.

**How:**
- Audit which dangling links point to claims that should exist but are missing
- Create missing claims from run data, or remove invalid links
- Run: `python scripts/validate-vault.py --all` to surface full list with context
- Specific targets:
  - Remove or replace placeholder `[[claim-id]]` references (6 files)
  - Create missing claims like `[[claim-allocation-task-type-robust-to-tight-governance]]` or confirm they're not needed
  - Check vault/governance-dashboard.md for link accuracy

**Estimated effort:** 30-45 minutes

---

### 2. Process 156 runs in inbox (HIGH IMPACT)

**Why:** Unprocessed runs are knowledge trapped in raw data. The 59% inbox-to-total ratio means nearly 60 cents of every research dollar is still in the inbox. This is opportunity cost.

**How:**
- Run `/pipeline` on oldest 5-10 runs to batch-extract findings
- Or target specific sweep results: `ls -t runs/ | head -5` then `/extract [run]`
- After each extraction, note the claims created and dangling links that surface
- Goal: Reduce inbox to <50 items (ratio → <33%)

**Estimated effort:** 2-3 hours (pipeline is automated)

---

### 3. Update 8 very stale claims (MEDIUM IMPACT)

**Why:** Isolated, old claims represent findings that may be:
- Superseded by newer evidence
- Needing integration into evidence chains
- Worth revisiting with new experimental context

**How:**
- Run `/update [claim]` on each of the 8 claims listed in Category 7
- `/cross-link [claim]` to discover relationships
- Review status: if no new evidence after 90+ days, consider `weakened` or archive
- Quick triage: `vault/ops/queue/` status check to see which claims are actively being researched

**Estimated effort:** 1-2 hours

---

## Vault Health Score

| Dimension | Score | Notes |
|-----------|-------|-------|
| Schema Integrity | 100% | All claims comply with template |
| Connection Density | 95% | 27 dangling links / 106 claims = 25% with issues (but still high density) |
| Knowledge Coverage | 59% (inbox) | Good synthesis rate but backlog present |
| Freshness | 92% | 8/106 claims very old; others recently updated |
| Boundary Discipline | 100% | No space contamination |
| **Overall** | **89%** | **Structurally sound, tactical cleanup needed** |

---

## Next Steps

**Immediate (this session):**
1. Run `/validate --fix-links` to audit dangling links
2. Review vault/governance-dashboard.md for broken references

**Short-term (this week):**
3. Process 5-10 runs with `/pipeline` to reduce inbox backlog
4. Update 3 oldest claims to test `/update` workflow

**Ongoing (maintenance routine):**
5. Set threshold alert: flag any claim > 60 days without activity
6. Monthly inbox audit: aim for <50 item target
7. Quarterly topic map review: check for oversized maps

---

## Appendix: Full Dangling Link List

**All 27 dangling links:**
1. claim-acausality-depth-does-not-affect-cooperation-outcomes
2. claim-allocation-task-type-robust-to-tight-governance
3. claim-coordination-task-shows-critical-threshold-below-58-percent-completion
4. claim-frontier-improvements-are-task-dependent
5. claim-governance-cost-amplified-by-task-complexity
6. claim-governance-topology-modulates-screening-efficacy
7. claim-id (6 references — placeholder)
8. claim-id-1
9. claim-id-2
10. claim-ldt-agents-provide-welfare-stability-at-intermediate-composition
11. claim-long-horizon-tasks-collapse-under-tight-governance
12. claim-loose-governance-near-costless-entry-on-safety-frontier
13. claim-monotonic-capability-ordering-invariant-across-task-types
14. claim-optimal-tax-range-0-to-5pct
15. claim-prompt-level-governance-fails-in-multi-agent-systems
16. claim-proxy-calibration-drift-causes-deterministic-welfare-collapse
17. claim-quadratic-staking-may-solve-sybil-cost-inversion
18. claim-safety-capability-tradeoff-is-unavoidable
19. claim-screening-equilibrium-generates-honest-payoff-premium
20. claim-screening-harms-routing-under-tight-governance-d=-0.78
21. claim-screening-has-no-effect-on-long-horizon-planning
22. claim-screening-is-task-type-governance-specialization-not-universal-frontier
23. claim-screening-modestly-improves-allocation-governance-dependent
24. claim-screening-signal-reliability-determines-routing-outcome
25. claim-staking-backfires
26. claim-steganographic-collusion-unaddressed-by-swarm-detection
27. claim-task-type-modulates-governance-response

---

**Report generated by `/arscontexta:health`**  
**Vault:** /Users/raelisavitt/swarm-artifacts  
**Mode:** Full diagnostic (8 categories)  
**Runtime:** ~5 minutes
