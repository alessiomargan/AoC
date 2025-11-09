# Advent of Code Solutions

Solutions for [Advent of Code](https://adventofcode.com/) challenges from 2019-2024.

## Links
- [AoC 2019](https://adventofcode.com/2019)
- [AoC 2020](https://adventofcode.com/2020)
- [AoC 2021](https://adventofcode.com/2021)
- [AoC 2022](https://adventofcode.com/2022)
- [AoC 2023](https://adventofcode.com/2023)
- [AoC 2024](https://adventofcode.com/2024)

## Quick Start (Conda-Based Setup)

### 1. Local Docker Development
```bash
docker-compose up --build
# Open http://localhost:8888
```

### 2. GitHub Codespaces
Go to: `https://github.com/alessiomargan/AoC`
- Click **Code** → **Codespaces** 
- Click **Create codespace on main**
- Wait ~2 minutes for conda environment setup
- Start coding!

### 3. VS Code Remote Containers
In VS Code:
- `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
- Container uses conda environment from `2024/aoc_env_2024.yml`

## What You Get

| Feature | Status | Details |
|---------|--------|---------|
| **Python** | 3.14 | Via conda-forge |
| **Environment Manager** | Conda | Fast, reliable package management |
| **JupyterLab** | ✅ Port 8888 | Browser-based notebook interface |
| **VS Code Integration** | ✅ Full | Python, Jupyter, Copilot extensions |
| **Git/GitHub** | ✅ Mounted | Your .gitconfig shared with container |
| **AoC Data** | ✅ Auto | advent-of-code-data with ~/.config/aocd mounted |
| **Build Time** | ~2 min | Pre-compiled conda packages |

## Key Features

### Conda Environment
All packages managed via `2024/aoc_env_2024.yml`:
- Core: numpy, matplotlib, networkx, pygraphviz
- Jupyter: jupyterlab, ipykernel
- Profiling: line_profiler, memory_profiler
- AoC: advent-of-code-data (pip)

### Mounted Volumes
- **Workspace**: Live code editing (`.:/workspace`)
- **Conda env**: Persisted across rebuilds (`conda-env` volume)
- **Git config**: Shared from host (`~/.gitconfig`)
- **AoC data**: Shared session token (`~/.config/aocd`)

### GitHub Copilot
- Copilot and Copilot Chat pre-installed
- Authentication via mounted .gitconfig
- Works in both local containers and Codespaces

## Environment Configuration

Edit `2024/aoc_env_2024.yml` to add/update packages:
```yaml
dependencies:
  - python=3.14
  - your-new-package
  - pip:
    - your-pip-package
```

Then rebuild:
```bash
docker-compose up --build
```

## Advent of Code Setup

The container mounts `~/.config/aocd` so your AoC session token persists:

```python
from aocd import get_data
data = get_data(day=1, year=2024)  # Automatically uses your session
```

For Codespaces, set `AOC_SESSION` as a repository secret.

## Documentation

- **[docker-README.md](docker-README.md)** - Docker usage and troubleshooting
- **[CODESPACES.md](CODESPACES.md)** - GitHub Codespaces guide
- **[CONDA-SETUP.md](CONDA-SETUP.md)** - Why conda vs pip
- **[DOCKER-CACHING.md](DOCKER-CACHING.md)** - Build optimization details

## Legacy Setup (Local Conda)

```bash
# create conda env locally
make aoc

ipython kernel install --user --name=aoc

jupyter kernelspec remove aoc
```
