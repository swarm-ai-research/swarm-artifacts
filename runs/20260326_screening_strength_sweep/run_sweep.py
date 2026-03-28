#!/usr/bin/env python
"""Screening strength sweep: 11 × 3 × 2 × 30 seeds = 1,980 primary runs.

Tests the diversity-consensus mechanism from the screening frontier shift
paper. If correct, routing under tight governance has an inverted-U
dose-response (crossover at strength 0.2-0.3), while coordination
improves monotonically.

Confirmatory arm: allocation + long_horizon at 10 seeds = 660 runs.
Total: 2,640 runs.

Key predictions:
  - Coordination: monotonic increase with screening strength
  - Routing × tight: non-monotonic (inverted U), crossover at 0.2-0.3
  - Routing × light: monotonic positive or flat
  - Long horizon: null across all strengths
"""

import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from swarm.analysis import SweepConfig, SweepParameter, SweepRunner  # noqa: E402
from swarm.scenarios import load_scenario  # noqa: E402

RUN_DIR = Path(__file__).resolve().parent
SCENARIO = (
    Path(__file__).resolve().parent.parent.parent
    / "scenarios"
    / "hypotheses"
    / "screening_strength_sweep.yaml"
)

PRIMARY_SEEDS = 30
CONFIRMATORY_SEEDS = 10
SEED_BASE = 42

SCREENING_STRENGTHS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
GOV_CONFIGS = ["tight", "moderate", "light"]
PRIMARY_TASKS = ["routing", "coordination"]
CONFIRMATORY_TASKS = ["allocation", "long_horizon"]


def progress(current: int, total: int, params: dict) -> None:
    param_str = ", ".join(f"{k.split('.')[-1]}={v}" for k, v in params.items())
    print(f"  [{current}/{total}] {param_str}")


def run_arm(
    base_scenario, task_types: list, seeds: int, arm_label: str
) -> dict:
    """Run one arm of the sweep (primary or confirmatory)."""
    print(f"\n--- {arm_label} arm: {task_types}, {seeds} seeds ---")

    sweep_config = SweepConfig(
        base_scenario=base_scenario,
        parameters=[
            SweepParameter(
                name="governance.screening_strength",
                values=SCREENING_STRENGTHS,
            ),
            SweepParameter(
                name="governance.config",
                values=GOV_CONFIGS,
            ),
            SweepParameter(
                name="task_type",
                values=task_types,
            ),
        ],
        runs_per_config=seeds,
        seed_base=SEED_BASE,
    )

    n_configs = len(SCREENING_STRENGTHS) * len(GOV_CONFIGS) * len(task_types)
    total_runs = n_configs * seeds
    print(f"Configurations: {n_configs}")
    print(f"Seeds per config: {seeds}")
    print(f"Total runs: {total_runs}")

    t0 = time.time()
    runner = SweepRunner(sweep_config, progress_callback=progress)
    runner.run()
    elapsed = time.time() - t0

    # Export per-task CSVs
    csv_dir = RUN_DIR / "csv"
    csv_dir.mkdir(exist_ok=True)

    for task in task_types:
        task_csv = csv_dir / f"{task}_raw.csv"
        runner.to_csv(task_csv, filter_params={"task_type": task})
        print(f"  Written: {task_csv}")

    # Summary
    summary = runner.summary()
    summary["elapsed_seconds"] = round(elapsed, 1)
    summary["arm"] = arm_label

    return summary


def main() -> int:
    print("=" * 70)
    print("Screening Strength Sweep — Dose-Response")
    print("Diversity-Consensus Mechanism Test")
    print("=" * 70)

    base_scenario = load_scenario(SCENARIO)

    all_summaries = []

    # Primary arm: routing + coordination × 30 seeds
    primary = run_arm(
        base_scenario, PRIMARY_TASKS, PRIMARY_SEEDS, "primary"
    )
    all_summaries.append(primary)

    # Confirmatory arm: allocation + long_horizon × 10 seeds
    confirmatory = run_arm(
        base_scenario, CONFIRMATORY_TASKS, CONFIRMATORY_SEEDS, "confirmatory"
    )
    all_summaries.append(confirmatory)

    # Combined summary
    total_runs = sum(s.get("total_runs", 0) for s in all_summaries)
    total_time = sum(s.get("elapsed_seconds", 0) for s in all_summaries)

    combined = {
        "total_runs": total_runs,
        "elapsed_seconds": total_time,
        "arms": all_summaries,
        "parameters": {
            "screening_strength": SCREENING_STRENGTHS,
            "governance_configs": GOV_CONFIGS,
            "primary_tasks": PRIMARY_TASKS,
            "confirmatory_tasks": CONFIRMATORY_TASKS,
            "primary_seeds": PRIMARY_SEEDS,
            "confirmatory_seeds": CONFIRMATORY_SEEDS,
        },
    }

    summary_path = RUN_DIR / "summary.json"
    with open(summary_path, "w") as f:
        json.dump(combined, f, indent=2)
    print(f"\nSummary written to: {summary_path}")

    print(f"\n{'=' * 70}")
    print(f"Completed {total_runs} total runs in {total_time:.0f}s")
    print(f"  Primary: {PRIMARY_TASKS} × {PRIMARY_SEEDS} seeds")
    print(f"  Confirmatory: {CONFIRMATORY_TASKS} × {CONFIRMATORY_SEEDS} seeds")
    print(f"{'=' * 70}")

    # Quick dose-response table for routing × tight
    print("\nDose-response preview: routing × tight governance")
    print(f"{'Strength':>10} {'Capability':>12} {'Safety':>10}")
    for s in all_summaries:
        for cfg in s.get("summaries", []):
            if (
                cfg.get("task_type") == "routing"
                and cfg.get("governance.config") == "tight"
            ):
                strength = cfg.get("governance.screening_strength", "?")
                cap = cfg.get("mean_capability", 0)
                saf = cfg.get("mean_safety_score", 0)
                print(f"{strength:>10} {cap:>12.4f} {saf:>10.4f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
