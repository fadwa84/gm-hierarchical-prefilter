# GM Hierarchical Pre-Filter

A reproducible fixed-base hierarchical pre-filter for reducing candidate workloads before Miller–Rabin primality testing.

## Overview

This repository contains the implementation and benchmark scripts accompanying the research paper:

"A Reproducible Fixed-Base Hierarchical Pre-Filter for Reducing Miller–Rabin Candidate Workloads"

The project provides:

* A lightweight deterministic composite pre-filter
* Hybrid preprocessing before Miller–Rabin testing
* Benchmark scripts for large ranges
* Reproducible computational experiments

## Files

* `hgm_prefilter_core.py` — core implementation
* `benchmark_large_ranges_fixed.py` — benchmark script
* `compare_with_wheel.py` — comparison placeholder
* `requirements.txt` — required Python packages

## Requirements

Install dependencies using:

pip install -r requirements.txt

## Example

python benchmark_large_ranges_fixed.py

## Data Availability

Zenodo archive:
https://doi.org/10.5281/zenodo.17684105

GitHub repository:
https://github.com/fadwa84/gm-hierarchical-prefilter

## License

MIT License
