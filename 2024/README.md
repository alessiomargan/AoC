# Advent of Code 2024 — project notes

This folder contains my Advent of Code 2024 solutions and helper files.

Environment and setup
- Preferred (reproducible): create the conda environment from the included YAML:

```bash
conda env create -f aoc_env_2024.yml
conda activate aoc
```

- Alternative (pip): install required Python packages into an existing venv using `requirements.txt`:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Notes
- The conda environment pins Python 3.13. If you use pip, ensure your interpreter is Python 3.11+ (3.13 recommended).
- `requirements.txt` is an approximation of the conda env: some conda-only package names may differ slightly on PyPI (for example `memory_profiler` vs `memory-profiler`). If a package fails to install via pip, prefer the conda route.

Running
- Most solutions are standalone scripts or notebooks. I can add a `run_all.py` to execute each day and collect results — tell me if you want that next.
