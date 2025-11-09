# Conda Setup (Now Default!)

## Current Status

✅ **Conda is now the default setup** for this repository.

All containerization (Docker, Codespaces, Dev Containers) now uses conda-based package management via `continuumio/miniconda3`.

## Why Conda is Default

✅ **Faster builds** - Pre-compiled binaries for all packages  
✅ **No version conflicts** - Conda resolves dependencies correctly  
✅ **Python version flexibility** - Works with Python 3.14  
✅ **System packages included** - graphviz, pygraphviz work out of the box  
✅ **No pip backtracking** - No 18-minute dependency resolution  
✅ **Reliable** - Tested package combinations from conda-forge  

## Quick Start

### Use Current Conda Setup

```bash
# Build and run (uses conda by default)
docker-compose up --build

# Access JupyterLab at http://localhost:8888
```

## Configuration Files

### Main Environment: `2024/aoc_env_2024.yml`

```yaml
name: aoc
channels:
  - conda-forge
dependencies:
  - python=3.14
  - numpy
  - jupyterlab
  - ipykernel
  - matplotlib
  - networkx
  - pygraphviz
  - pip:
    - advent-of-code-data
    - browser-cookie3
    - dict-to-dataclass
```

### Container: `Dockerfile`

Uses `continuumio/miniconda3:latest` base image and creates environment from the .yml file.

### Compose: `docker-compose.yml`

Mounts:
- Workspace (live editing)
- Conda environment (persistence)
- Git config (authentication)
- AoC data (session token)

## Update Packages

### Add Conda Package

Edit `2024/aoc_env_2024.yml`:

```yaml
dependencies:
  - python=3.14
  - your-new-package  # Add here
```

Then rebuild:

```bash
docker-compose up --build
```

### Add pip Package

Edit `2024/aoc_env_2024.yml`:

```yaml
dependencies:
  - python=3.14
  - pip:
    - your-pip-package  # Add here
```

## Build Time Comparison

| Setup | Python | Build Time | Issues |
|-------|--------|------------|--------|
| **Conda (current)** | 3.14 | ~2 min | ✅ None |
| **pip (old)** | 3.14 | 18+ min | ❌ Failed (backtracking) |
| **pip (fixed)** | 3.12 | ~3 min | ✅ Works (pinned versions) |

## Features

### What Conda Provides

1. **Pre-built binaries** - No compilation needed
2. **System libraries** - Includes graphviz, compilers
3. **Dependency resolution** - Solved once, no conflicts
4. **Reproducibility** - Same versions everywhere
5. **Fast updates** - Incremental environment updates

### Mounted Data

The setup preserves:
- **Code**: Live mounted from host
- **Conda env**: Persisted in Docker volume
- **Git config**: Shared from `~/.gitconfig`
- **AoC session**: Shared from `~/.config/aocd`

## Advantages Over pip

### Conda Wins For:
- Complex packages (pygraphviz, opencv, scipy)
- Scientific computing libraries
- Multiple Python versions
- System-level dependencies
- Reproducible environments

### Why Not pip?
- Slower dependency resolution
- Requires version pinning
- No system packages
- Source builds on missing wheels
- Backtracking issues with Python 3.14

## Local Conda Usage

You can also use conda locally without Docker:

```bash
# Create environment
conda env create -f 2024/aoc_env_2024.yml

# Activate
conda activate aoc

# Run Jupyter
jupyter lab

# Install Jupyter kernel
python -m ipykernel install --user --name=aoc
```

## Migration Notes

If you were using the old pip-based setup:

### What Changed
- `Dockerfile` now uses `continuumio/miniconda3`
- Packages installed via `aoc_env_2024.yml`
- Python path: `/opt/conda/envs/aoc/bin/python`
- No more `requirements.txt` for primary deps (kept for reference)

### What Stayed Same
- JupyterLab on port 8888
- VS Code devcontainer support
- GitHub Codespaces support
- All the same packages available

### Rebuild Required
After pulling latest changes:

```bash
# Rebuild with new conda setup
docker-compose build --no-cache
docker-compose up
```

## Troubleshooting

### Conda environment not found

```bash
docker-compose exec aoc-jupyter conda env list
# Should show 'aoc' environment
```

### Package not available in conda

Add to pip section:

```yaml
dependencies:
  - pip:
    - your-package  # Install via pip in conda env
```

### Slow conda solver

Use mamba (faster conda):

```dockerfile
RUN conda install -n base conda-libmamba-solver
RUN conda config --set solver libmamba
```

## Summary

✅ Conda is now default and recommended  
✅ Faster, more reliable than pip for this use case  
✅ All documentation updated  
✅ Works in Docker, Codespaces, and local dev  

The old pip-based setup is no longer maintained but requirements.txt is kept for reference.
