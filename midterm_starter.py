import time
import random
import statistics
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    Compare the algorithms on identical, duplicate-free inputs of increasing size.
    Duplicate-free inputs force both implementations to examine the full list.
    """
    sizes = (250, 500, 1000, 2000, 4000)
    trials = 5
    rng = random.Random(0)
    algorithms = (
        ("slow", find_duplicates_slow),
        ("fast", find_duplicates_fast),
    )

    slow_times = []
    fast_times = []
    for n in sizes:
        # Generate once then give the same input to both.
        data = rng.sample(range(2 * n), n)

        for _, algorithm in algorithms:
            if algorithm(data):
                raise AssertionError("Expected duplicate-free input")

        elapsed = {"slow": [], "fast": []}
        for trial in range(trials):
            run_order = algorithms if trial % 2 == 0 else algorithms[::-1]
            for name, algorithm in run_order:
                start_time = time.perf_counter()
                has_duplicates = algorithm(data)
                elapsed[name].append(time.perf_counter() - start_time)
                if has_duplicates:
                    raise AssertionError("Expected duplicate-free input")

        medians = {
            name: statistics.median(elapsed[name])
            for name, _ in algorithms
        }
        slow_times.append(medians["slow"])
        fast_times.append(medians["fast"])

    plt.figure()
    plt.loglog(sizes, slow_times, marker="o", label="Slow algorithm O(n^2)")
    plt.loglog(sizes, fast_times, marker="o", label="Fast algorithm O(n)")
    plt.xticks(sizes, [str(size) for size in sizes])
    plt.yticks(
        (0.00001, 0.0001, 0.001, 0.01, 0.1, 1),
        labels=["0.00001", "0.0001", "0.001", "0.01", "0.1", "1"],
    )
    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(lambda value, _: f"{value:.5f}".rstrip("0").rstrip("."))
    )
    plt.xlabel("Input size (n)")
    plt.ylabel("Median execution time (seconds)")
    plt.title("Empirical Algorithm Performance")
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    output_path = Path(__file__).with_name("results.png")
    plt.savefig(output_path, dpi=150)
    plt.show()
    plt.close()


if __name__ == "__main__":
    flawed_benchmark()