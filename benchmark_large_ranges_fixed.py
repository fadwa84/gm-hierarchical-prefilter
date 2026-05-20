"""Benchmark large ranges for the hierarchical GM pre-filter.

This corrected version fixes the missing import of ``segmented_gm_prefilter_numba``
that existed in the earlier benchmark script. It imports the function from the
reproducible corrected core module shipped with the manuscript.
"""

import time
import tracemalloc

import psutil

try:
    from memory_profiler import profile
except ImportError:  # keep the benchmark runnable when memory_profiler is absent
    def profile(func):
        return func

from hgm_prefilter_core_fixed import segmented_gm_prefilter_numba


@profile
def benchmark_large_range(low=1_000_000_000, high=1_000_100_000, segment_size=2_000_000):
    """Run a reproducible large-range benchmark for the GM pre-filter.

    Parameters
    ----------
    low : int
        Lower endpoint of the tested interval.
    high : int
        Upper endpoint of the tested interval.
    segment_size : int
        Segment length used by the segmented implementation.
    """
    tracemalloc.start()
    start_time = time.perf_counter()
    psutil.cpu_percent(interval=None)

    prime_count = segmented_gm_prefilter_numba(low, high, segment_size=segment_size)

    end_time = time.perf_counter()
    cpu_after = psutil.cpu_percent(interval=None)
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed = end_time - start_time
    print(f"Range          : {low:,} - {high:,}")
    print(f"Primes found   : {prime_count:,}")
    print(f"Time taken     : {elapsed:.2f} seconds")
    print(f"Memory peak    : {peak / 1024**2:.2f} MB")
    print(f"CPU Utilization: ~{cpu_after}%")
    return prime_count


if __name__ == "__main__":
    benchmark_large_range()
