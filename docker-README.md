# Docker Setup for Advent of Code Workspace (Conda-Based)

## Two Ways to Use

### 1. With docker-compose (Development - Volume Mounted)

```bash
docker-compose up
```

**How it works:**
- Files are live-mounted: `.:/workspace`
- Edit on host → changes appear in container instantly
- Commit from host or container (both work)
- No rebuild needed after code changes

**Best for:** Daily development, solving AoC puzzles

### 2. Standalone (Production/Distribution - Files Baked In)

```bash
# Build image with files baked in
docker build -t aoc-standalone .

# Run without volume mount
docker run -p 8888:8888 aoc-standalone
```

**How it works:**
- Files are copied into image during build
- No live editing (image is immutable)
- Portable image you can share/deploy
- Includes all your solutions

**Best for:** Sharing solutions, CI/CD, archiving

### Comparison

| Scenario | COPY Behavior | Use Case |
|----------|---------------|----------|
| **docker-compose** | Overridden by volume | Development, live editing |
| **docker run** (no -v) | Used from image | Distribution, deployment |
| **docker run -v** | Overridden by -v | Custom development setup |

## Quick Start

### Build and Run with Docker Compose (Recommended)

```bash
docker-compose up --build
```

Then open your browser to: <http://localhost:8888>

### Alternative: Using Docker directly

```bash
# Build the image
docker build -t aoc-workspace .

# Run the container
docker run -p 8888:8888 -v $(pwd):/workspace aoc-workspace
```

## Usage

### Access JupyterLab

Once the container is running, access JupyterLab at:
- **URL:** <http://localhost:8888>
- **No password required** (configured for local development)

### Run a specific year's notebook

```bash
# Execute commands in the running container
docker-compose exec aoc-jupyter bash

# Or run a script directly
docker-compose exec aoc-jupyter python 2024/day_14_part_2.py
```

### Stop the container

```bash
docker-compose down
```

## Features

✅ **Python 3.14** - Via conda-forge channel  
✅ **Conda environment** - Fast, reliable package management  
✅ **All dependencies** - numpy, jupyterlab, matplotlib, networkx, pygraphviz, etc.  
✅ **System libraries** - git, curl for GitHub operations  
✅ **Volume mounting** - Edit files on host, changes reflect in container  
✅ **Persistent conda env** - Environment saved between restarts  
✅ **Persistent AoC data** - Session token mounted from `~/.config/aocd`  
✅ **Git config** - Your .gitconfig shared for Copilot/GitHub  

## Customization

### Change Jupyter port

Edit `docker-compose.yml`:
```yaml
ports:
  - "9999:8888"  # Access on port 9999
```

### Add a password

Edit `Dockerfile`:
```dockerfile
RUN jupyter lab password
# Enter your password when prompted during build
```

### Update conda environment

Edit `2024/aoc_env_2024.yml`:
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

### Change Python version

Edit `2024/aoc_env_2024.yml`:
```yaml
dependencies:
  - python=3.12  # or 3.11, 3.10, etc.
```

## Troubleshooting

### Port already in use

```bash
# Change port in docker-compose.yml or stop conflicting service
lsof -i :8888
```

### Conda environment not activating

```bash
# Check environment exists
docker-compose exec aoc-jupyter conda env list

# Activate manually
docker-compose exec aoc-jupyter conda activate aoc
```

### Package installation fails

```bash
# Update conda environment
docker-compose exec aoc-jupyter conda install -n aoc your-package

# Or use pip in the conda environment
docker-compose exec aoc-jupyter pip install your-package
```

### Rebuild after dependency changes

```bash
docker-compose up --build --force-recreate
```

### Clear conda cache

```bash
docker-compose exec aoc-jupyter conda clean -afy
```

## Advantages Over pip-Based Setup

| Aspect | Conda (Current) | pip (Old) |
|--------|-----------------|-----------|
| **Build time** | ~2 min | 3+ min |
| **Dependency resolution** | ✅ Pre-resolved | ❌ Backtracking |
| **Python version** | Any version | Limited by wheels |
| **System packages** | Included | Manual apt-get |
| **pygraphviz** | ✅ Pre-built | ❌ Compile from source |
| **Reproducibility** | ✅ Excellent | ⚠️ Requires pinning |

## Volumes Explained

The setup uses three mounted volumes:

1. **Workspace** (`.:/workspace`):
   - Your code is live-mounted
   - Edit on host, run in container
   - Changes persist automatically

2. **Conda environment** (`conda-env` volume):
   - Persists installed packages
   - Faster rebuilds (env cached)
   - Survives container restarts

3. **Git config** (`~/.gitconfig`):
   - Shares your Git identity
   - Enables Copilot authentication
   - Read-only for security

4. **AoC data** (`~/.config/aocd`):
   - Shares your AoC session token
   - No need to re-authenticate
   - Works with advent-of-code-data

## Build Performance

### First Build
- Downloads miniconda3 base image (~450 MB)
- Creates conda environment (~1 GB)
- Installs all packages from conda-forge
- Total time: ~2-3 minutes

### Subsequent Builds (code changes only)
- Uses cached conda environment
- Only copies updated code
- Total time: ~5-10 seconds

### Subsequent Builds (environment changes)
- Reuses base image
- Updates conda environment incrementally
- Total time: ~30 seconds - 1 minute

## Why This Is Fast

1. **Pre-compiled binaries**: Conda packages are pre-built
2. **No source compilation**: No gcc/g++ compilation delays
3. **Dependency caching**: Conda solves deps once
4. **Layer caching**: Docker reuses unchanged layers
5. **Environment persistence**: Conda env stored in volume
