# SWARM Research OS — Project Instructions

This repo is the artifact store and knowledge vault for the SWARM multi-agent simulation framework. It uses arscontexta conventions for knowledge management.

## Repo structure

```
runs/           # One folder per experiment run (run.yaml + data)
vault/          # arscontexta knowledge vault
  claims/       # Claim cards — atoms of scientific memory
  experiments/  # Auto-generated experiment notes (one per run)
  governance/   # Governance mechanism notes
  topologies/   # Network topology notes
  failures/     # Named failure/vulnerability patterns
  sweeps/       # Cross-run sweep aggregations
  methods/      # Methodology notes
  templates/    # Schema-enforced templates for all note types
  _index.md     # Master index (MOC)
schemas/        # JSON Schema for run.yaml, claims, sweeps
scripts/        # Python automation (validation, synthesis, indexing)
inngest/        # Durable orchestration pipeline (TypeScript)
scenarios/      # SWARM scenario definitions (benchmarks, sweeps)
skills/         # arscontexta plugin skills (vault-init, synthesize, claim, verify)
```

## Kernel invariants

These rules apply to ALL vault notes. Never violate them:

1. **Prose-as-title.** Every H1 heading is a complete proposition, not a label. Test: "This note argues that [title]"
2. **description ≤200 chars.** No trailing period. Must add info beyond the title.
3. **Topics footer mandatory.** Every note ends with `<!-- topics: tag1, tag2 -->` or a visible `Topics:` section linking to `[[_index]]`.
4. **Wiki-links inline as prose.** Example: "This replicates [[baseline governance v2 sweep]]"
5. **Evidence provenance mandatory.** Every evidence entry must reference a real run_id in `runs/`.
6. **Effect sizes with correction methods.** Never report raw p-values without Bonferroni/Holm/BH.

## Claim confidence criteria

| Level | Criteria |
|-------|----------|
| **high** | Bonferroni-significant AND replicated across ≥2 independent runs/seeds |
| **medium** | Nominally significant OR single-sweep support with BH correction |
| **low** | Suggestive but underpowered (<20 seeds) or unreplicated |
| **contested** | Conflicting evidence from different runs |

## Experiment types

| Type | Description |
|------|-------------|
| `single` | One scenario, one seed → `history.json` |
| `sweep` | Parameter grid, multiple seeds → `summary.json`, `sweep_results.csv` |
| `redteam` | Adversarial evaluation → `report.json` |
| `study` | Multi-factor analysis → `analysis/summary.json` |
| `calibration` | Hyperparameter tuning → `recommendation.json` |

## Key scripts

```bash
# Validation
python scripts/validate-run.py --all          # Validate run schemas
python scripts/validate-vault.py --all        # Validate vault notes
python scripts/vault-health.py                # Comprehensive vault audit

# Synthesis
python scripts/backfill-run-yaml.py           # Generate run.yaml for existing runs
python scripts/generate-note.py --all         # Synthesize experiment notes
python scripts/generate-sweep-notes.py        # Generate sweep summaries

# Enrichment
python scripts/enrich-tags.py                 # Mine semantic tags from run content
python scripts/obsidian-metadata.py           # Add Obsidian graph metadata

# Analysis
python scripts/claim-lifecycle.py             # Audit claim evidence and status
python scripts/cross-correlate.py             # Detect parameter interactions
python scripts/diff-runs.py <a> <b>           # Compare two runs
python scripts/claim-graph.py                 # Generate claim dependency graph
python scripts/run-provenance.py              # Detect run lineage chains

# Search & reporting
python scripts/vault-search.py "query"        # Search vault by keyword/tag/type
python scripts/vault-stats.py                 # Vault statistics summary
python scripts/vault-digest.py HEAD~5..HEAD   # Changelog between commits

# Indexing & events
python scripts/index-runs.py                  # Rebuild run-index.yaml
python scripts/emit-event.py <run_id>         # Emit Inngest event
```

## Working with claims

- Never auto-edit claim cards without human judgment
- Claim filenames use `claim-` prefix + kebab-case proposition
- Status flow: `active → weakened → superseded → retracted`
- Every status change must be visible and explained

## Inngest pipeline

```bash
cd inngest && npm ci && npx tsc --noEmit   # Typecheck
docker compose up                           # Run locally
```

## Skills

Available slash commands: `/vault-init`, `/synthesize`, `/claim`, `/verify`

Ars Contexta skills (installed in `.claude/skills/`):
- `/extract` — extract findings from experiment runs into claims
- `/cross-link` — find connections between claims, update topic maps
- `/update` — backward pass, update prior claims with new evidence
- `/validate` — validate provenance and schema (6-gate quality check)
- `/rethink` — review accumulated observations and tensions, system evolution
- `/remember` — capture methodology friction and operational corrections
- `/next` — surface next recommended action from synthesis pipeline
- `/stats` — vault metrics (claims by confidence, experiment coverage, queue state)
- `/graph` — knowledge graph analysis (orphans, hubs, evidence chains)
- `/learn` — research a topic and grow the vault with findings
- `/seed` — initialize pipeline processing for new experiment runs
- `/pipeline` — run full synthesis pipeline on one or more runs

Plugin commands (no restart required):
- `/arscontexta:ask` — query the 249-note methodology knowledge base + local vault/ops/methodology/
- `/arscontexta:health` — run vault diagnostics
- `/arscontexta:architect` — research-backed evolution advice
- `/arscontexta:rethink` — alias for /rethink via plugin
- `/arscontexta:remember` — alias for /remember via plugin

## Python dependencies

```bash
pip install pyyaml jsonschema
```

---

## Ars Contexta — Knowledge OS Layer

This vault runs on top of Ars Contexta conventions. The following applies in addition to the kernel invariants above.

### Philosophy

**If it won't exist next session, write it down now.**

You are the research memory system for SWARM AI safety experiments. Notes are your external memory. Wiki-links are your evidence chains. Topic maps are your attention managers.

Read `vault/self/identity.md` and `vault/self/goals.md` at every session start.

### Session Rhythm: Orient → Work → Persist

**Orient** (session start)
- Read `vault/self/identity.md` — who you are, what you care about
- Read `vault/self/goals.md` — active research threads
- Check `vault/ops/reminders.md` — time-bound items
- Check `/next` — queue state and highest-priority action

**Work**
- Extract findings from runs using `/extract`
- Cross-link evidence using `/cross-link`
- Update prior claims using `/update`
- Validate provenance using `/validate`

**Persist** (session end)
- Write new findings to vault/claims/
- Update vault/self/goals.md with thread status
- Capture friction to vault/ops/observations/ if anything went wrong
- Session capture hook fires automatically on Stop

### Discovery-First Design

Every claim must be findable by a future agent who doesn't know it exists.

Before creating any claim, verify:
1. **Title as proposition** — "this claim argues that [title]" makes sense
2. **Description adds info** — ≤200 chars, not a restatement of the title
3. **Topic map membership** — linked from at least one topic map
4. **Evidence provenance** — run_id points to a real run in runs/

### Synthesis Pipeline

```
/seed [run]  →  /extract [run]  →  /cross-link [claim]  →  /update [claim]  →  /validate [claim]
```

Queue state: `vault/ops/queue/queue.json`
Human-readable view: `vault/ops/tasks.md`

### Self-Knowledge

The vault knows how it works:
- `vault/self/identity.md` — research identity, values, working style
- `vault/self/methodology.md` — how to process, connect, and maintain claims
- `vault/self/goals.md` — current active research threads
- `vault/ops/methodology/` — derivation rationale, configuration state, evolution history

Query methodology: `/arscontexta:ask [question about why the system works this way]`

### Maintenance Triggers (condition-based)

- Pending observations ≥ 10 → run `/rethink`
- Pending tensions ≥ 5 → run `/rethink`
- Claim not updated in 30+ days → flag for `/update` pass
- Run `python scripts/vault-health.py` for comprehensive audit

### Common Pitfalls (HIGH risk for this vault)

1. **Collector's Fallacy** — absorbing 100+ experiment runs without synthesizing into claims. The synthesis pipeline exists for a reason. `runs/` is the inbox; `vault/claims/` is the knowledge.
2. **Orphan Drift** — creating claims without linking them to topic maps. Every claim needs a Topics footer and at least one incoming link from a topic map.
3. **Verbatim Risk** — copying experiment output instead of transforming it. Every claim title must be a testable proposition. "Experiment showed X" is not a claim. "Circuit breakers reduce toxicity by 11% under small-world topology" is.
4. **Evidence Without Correction** — reporting raw p-values without Bonferroni/Holm-Bonferroni/BH correction. This violates the kernel invariant. Every confidence level must match the statistical criteria table.

### Derivation

System derived from: `vault/ops/derivation.md`
Machine-readable config: `vault/ops/derivation-manifest.md`
Ars Contexta version: 0.8.0, 2026-02-20

<!-- gitnexus:start -->
# GitNexus — Code Intelligence

This project is indexed by GitNexus as **swarm-artifacts** (2388 symbols, 3555 relationships, 88 execution flows). Use the GitNexus MCP tools to understand code, assess impact, and navigate safely.

> If any GitNexus tool warns the index is stale, run `npx gitnexus analyze` in terminal first.

## Always Do

- **MUST run impact analysis before editing any symbol.** Before modifying a function, class, or method, run `gitnexus_impact({target: "symbolName", direction: "upstream"})` and report the blast radius (direct callers, affected processes, risk level) to the user.
- **MUST run `gitnexus_detect_changes()` before committing** to verify your changes only affect expected symbols and execution flows.
- **MUST warn the user** if impact analysis returns HIGH or CRITICAL risk before proceeding with edits.
- When exploring unfamiliar code, use `gitnexus_query({query: "concept"})` to find execution flows instead of grepping. It returns process-grouped results ranked by relevance.
- When you need full context on a specific symbol — callers, callees, which execution flows it participates in — use `gitnexus_context({name: "symbolName"})`.

## When Debugging

1. `gitnexus_query({query: "<error or symptom>"})` — find execution flows related to the issue
2. `gitnexus_context({name: "<suspect function>"})` — see all callers, callees, and process participation
3. `READ gitnexus://repo/swarm-artifacts/process/{processName}` — trace the full execution flow step by step
4. For regressions: `gitnexus_detect_changes({scope: "compare", base_ref: "main"})` — see what your branch changed

## When Refactoring

- **Renaming**: MUST use `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` first. Review the preview — graph edits are safe, text_search edits need manual review. Then run with `dry_run: false`.
- **Extracting/Splitting**: MUST run `gitnexus_context({name: "target"})` to see all incoming/outgoing refs, then `gitnexus_impact({target: "target", direction: "upstream"})` to find all external callers before moving code.
- After any refactor: run `gitnexus_detect_changes({scope: "all"})` to verify only expected files changed.

## Never Do

- NEVER edit a function, class, or method without first running `gitnexus_impact` on it.
- NEVER ignore HIGH or CRITICAL risk warnings from impact analysis.
- NEVER rename symbols with find-and-replace — use `gitnexus_rename` which understands the call graph.
- NEVER commit changes without running `gitnexus_detect_changes()` to check affected scope.

## Tools Quick Reference

| Tool | When to use | Command |
|------|-------------|---------|
| `query` | Find code by concept | `gitnexus_query({query: "auth validation"})` |
| `context` | 360-degree view of one symbol | `gitnexus_context({name: "validateUser"})` |
| `impact` | Blast radius before editing | `gitnexus_impact({target: "X", direction: "upstream"})` |
| `detect_changes` | Pre-commit scope check | `gitnexus_detect_changes({scope: "staged"})` |
| `rename` | Safe multi-file rename | `gitnexus_rename({symbol_name: "old", new_name: "new", dry_run: true})` |
| `cypher` | Custom graph queries | `gitnexus_cypher({query: "MATCH ..."})` |

## Impact Risk Levels

| Depth | Meaning | Action |
|-------|---------|--------|
| d=1 | WILL BREAK — direct callers/importers | MUST update these |
| d=2 | LIKELY AFFECTED — indirect deps | Should test |
| d=3 | MAY NEED TESTING — transitive | Test if critical path |

## Resources

| Resource | Use for |
|----------|---------|
| `gitnexus://repo/swarm-artifacts/context` | Codebase overview, check index freshness |
| `gitnexus://repo/swarm-artifacts/clusters` | All functional areas |
| `gitnexus://repo/swarm-artifacts/processes` | All execution flows |
| `gitnexus://repo/swarm-artifacts/process/{name}` | Step-by-step execution trace |

## Self-Check Before Finishing

Before completing any code modification task, verify:
1. `gitnexus_impact` was run for all modified symbols
2. No HIGH/CRITICAL risk warnings were ignored
3. `gitnexus_detect_changes()` confirms changes match expected scope
4. All d=1 (WILL BREAK) dependents were updated

## CLI

- Re-index: `npx gitnexus analyze`
- Check freshness: `npx gitnexus status`
- Generate docs: `npx gitnexus wiki`

<!-- gitnexus:end -->
