#!/usr/bin/env python
"""Screening strength sweep: 11 strengths × 3 gov × 4 tasks.

Tests the diversity-consensus mechanism from the screening frontier shift
paper. Uses the screening_frontier experiment API directly.

Primary arm: routing + coordination × 30 seeds = 1,980 runs
Confirmatory arm: allocation + long_horizon × 10 seeds = 660 runs
Total: 2,640 runs.
"""

import json
import os
import sys
import time
from dataclasses import asdict
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")

sys.path.insert(0, "/Users/raelisavitt/distributional-agi-safety")

import numpy as np
import pandas as pd

from swarm.benchmarks.allocation.resource_auction import ResourceAuctionBenchmark
from swarm.benchmarks.coordination.distributed_allocation import (
    DistributedAllocationBenchmark,
)
from swarm.benchmarks.governance_run_fns import RUN_FN_REGISTRY
from swarm.benchmarks.long_horizon.pipeline_task import PipelineTaskBenchmark
from swarm.benchmarks.routing.message_routing import MessageRoutingBenchmark
from swarm.benchmarks.runner import BenchmarkRunner

from experiments.screening_frontier import (
    SCREENING_RUN_FNS,
    _generate_trust_scores,
    _make_configs,
)

RUN_DIR = Path(__file__).resolve().parent

N_AGENTS = 10
PRIMARY_SEEDS = 30
CONFIRMATORY_SEEDS = 10

SCREENING_STRENGTHS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

BENCHMARKS = {
    "routing": MessageRoutingBenchmark(),
    "coordination": DistributedAllocationBenchmark(),
    "allocation": ResourceAuctionBenchmark(),
    "long_horizon": PipelineTaskBenchmark(),
}


def run_task_strength(
    task_type: str,
    screening_strength: float,
    n_seeds: int,
) -> pd.DataFrame:
    """Run one task type at one screening strength across all gov configs."""
    benchmark = BENCHMARKS[task_type]
    screening_run_fn = SCREENING_RUN_FNS[task_type]
    uniform_run_fn = RUN_FN_REGISTRY[task_type]
    runner = BenchmarkRunner(n_agents=N_AGENTS)

    configs = _make_configs(screening_strength=screening_strength)

    all_rows = []
    for seed in range(n_seeds):
        trust_scores = _generate_trust_scores(N_AGENTS, seed)
        instance, oracle = benchmark.generate(seed, N_AGENTS)

        for config in configs:
            redacted = benchmark.redact(instance)

            if screening_strength == 0.0:
                result = uniform_run_fn(redacted, config)
            else:
                result = screening_run_fn(redacted, config, trust_scores)

            score = benchmark.score(
                result, oracle,
                adversarial_fraction=float(config.get("adversarial_fraction", 0.0)),
            )
            interaction = benchmark.to_soft_interaction(score)

            row = {
                "benchmark": benchmark.task_id,
                "task_type": benchmark.task_type,
                "gov_config": config["id"],
                "seed": seed,
                "adversarial_fraction": float(config.get("adversarial_fraction", 0.0)),
                "screening_strength": screening_strength,
                "p": interaction.p,
                **asdict(score),
            }
            for k, v in config.items():
                if k not in ("id", "adversarial_fraction", "screening_strength"):
                    row[f"gov_{k}"] = v
            all_rows.append(row)

    df = pd.DataFrame(all_rows)
    df["capability"] = df["completion_rate"] * 0.6 + df["fidelity"] * 0.3 + df["efficiency"] * 0.1
    return df


def main() -> int:
    print("=" * 70)
    print("Screening Strength Sweep — Dose-Response")
    print("Diversity-Consensus Mechanism Test")
    print("=" * 70)
    print(f"Strengths: {SCREENING_STRENGTHS}")
    print(f"Primary tasks: routing, coordination ({PRIMARY_SEEDS} seeds)")
    print(f"Confirmatory tasks: allocation, long_horizon ({CONFIRMATORY_SEEDS} seeds)")

    csv_dir = RUN_DIR / "csv"
    csv_dir.mkdir(exist_ok=True)

    t0 = time.time()
    total_runs = 0

    # Primary arm: routing + coordination
    for task_type in ["routing", "coordination"]:
        print(f"\n{'='*60}")
        print(f"Primary: {task_type} ({PRIMARY_SEEDS} seeds)")
        print(f"{'='*60}")

        task_dfs = []
        for strength in SCREENING_STRENGTHS:
            print(f"  screening_strength={strength:.1f} ...", end="", flush=True)
            df = run_task_strength(task_type, strength, PRIMARY_SEEDS)
            task_dfs.append(df)
            n = len(df)
            total_runs += n
            print(f" {n} runs")

        combined = pd.concat(task_dfs, ignore_index=True)
        combined.to_csv(csv_dir / f"{task_type}_raw.csv", index=False)
        print(f"  Saved: csv/{task_type}_raw.csv ({len(combined)} rows)")

        # Quick dose-response for tight governance
        tight = combined[combined["gov_config"].str.startswith("tight")]
        if len(tight) > 0:
            print(f"\n  Dose-response ({task_type} × tight):")
            print(f"  {'Strength':>10} {'Capability':>12} {'N':>5}")
            for s in SCREENING_STRENGTHS:
                subset = tight[tight["screening_strength"] == s]
                if len(subset) > 0:
                    print(f"  {s:>10.1f} {subset['capability'].mean():>12.4f} {len(subset):>5}")

    # Confirmatory arm: allocation + long_horizon
    for task_type in ["allocation", "long_horizon"]:
        print(f"\n{'='*60}")
        print(f"Confirmatory: {task_type} ({CONFIRMATORY_SEEDS} seeds)")
        print(f"{'='*60}")

        task_dfs = []
        for strength in SCREENING_STRENGTHS:
            print(f"  screening_strength={strength:.1f} ...", end="", flush=True)
            df = run_task_strength(task_type, strength, CONFIRMATORY_SEEDS)
            task_dfs.append(df)
            n = len(df)
            total_runs += n
            print(f" {n} runs")

        combined = pd.concat(task_dfs, ignore_index=True)
        combined.to_csv(csv_dir / f"{task_type}_raw.csv", index=False)
        print(f"  Saved: csv/{task_type}_raw.csv ({len(combined)} rows)")

    elapsed = time.time() - t0

    # Summary
    summary = {
        "total_runs": total_runs,
        "elapsed_seconds": round(elapsed, 1),
        "screening_strengths": SCREENING_STRENGTHS,
        "governance_configs": ["tight", "moderate", "light"],
        "primary_tasks": ["routing", "coordination"],
        "confirmatory_tasks": ["allocation", "long_horizon"],
        "primary_seeds": PRIMARY_SEEDS,
        "confirmatory_seeds": CONFIRMATORY_SEEDS,
        "n_agents": N_AGENTS,
    }
    with open(RUN_DIR / "summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n{'='*70}")
    print(f"Completed {total_runs} total runs in {elapsed:.0f}s")
    print(f"{'='*70}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
