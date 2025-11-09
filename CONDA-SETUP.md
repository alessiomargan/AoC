# Conda-Based Docker Setup

## Why Conda?

✅ **Faster builds** - Pre-compiled binaries for all packages  
✅ **No version conflicts** - Conda resolves dependencies correctly  
✅ **Python version flexibility** - Works with any Python version  
✅ **System packages included** - graphviz, pygraphviz work out of the box  
✅ **No pip backtracking** - No 18-minute dependency resolution  

## Quick Start

### Option 1: Use Conda Dockerfile

```bash
# Build with conda
docker build -f Dockerfile.conda -t aoc-conda .

# Run
docker run -p 8888:8888 -v $(pwd):/workspace aoc-conda
```

### Option 2: Use Conda Docker Compose

```bash
# Build and run
docker-compose -f docker-compose.conda.yml up --build

# Access JupyterLab at http://localhost:8888
```

### Option 3: VS Code Devcontainer with Conda

1. Copy `.devcontainer/devcontainer-conda.json` to `.devcontainer/devcontainer.json`
2. Reopen in container
3. VS Code uses conda environment automatically

## Build Time Comparison

| Method | Python | Build Time | Issues |
|--------|--------|------------|--------|
| **pip (old)** | 3.14 | 18+ min | ❌ Failed (backtracking) |
| **pip (fixed)** | 3.12 | ~3 min | ✅ Works (pinned versions) |
| **conda** | 3.12 | ~2 min | ✅ Works (pre-built) |

## Switch Between pip and conda

### Currently using pip:
```bash
# Keep using current setup
docker-compose up
```

### Switch to conda:
```bash
# Use conda-based setup
docker-compose -f docker-compose.conda.yml up
```

### In VS Code:
Edit `.devcontainer/devcontainer.json`:
```json
{
  "dockerComposeFile": "../docker-compose.conda.yml",  // Change this line
  "service": "aoc-jupyter",
  ...
}
```

## Update Conda Environment

Edit `2024/aoc_env_2024.yml`:
```yaml
dependencies:
  - python=3.12
  - your-new-package
```

Then rebuild:
```bash
docker-compose -f docker-compose.conda.yml build --no-cache
```

## Advantages of Conda Approach

1. **No version pinning needed** - Conda handles compatibility
2. **Faster updates** - Just edit .yml file
3. **Reproducible** - Same exact versions across machines
4. **System libs included** - No separate apt-get for graphviz
5. **Better for science** - Conda-forge optimized for data science

## Which Should You Use?

**Use Conda if:**
- You're familiar with conda
- Want fastest, most reliable builds
- Need complex packages (pygraphviz, opencv, etc.)
- Working with multiple Python versions

**Use pip if:**
- Simpler requirements (pure Python packages)
- Want smaller final image (~500MB smaller)
- Team prefers pip workflow
- Need latest package versions (conda can lag slightly)

## Current Recommendation

Since you mentioned conda works better for you, **I recommend switching to the conda setup**:

```bash
# Switch your devcontainer
mv .devcontainer/devcontainer.json .devcontainer/devcontainer-pip.json
mv .devcontainer/devcontainer-conda.json .devcontainer/devcontainer.json

# Rebuild
# VS Code will prompt to rebuild, or run:
# Ctrl+Shift+P -> "Dev Containers: Rebuild Container"
```

Your original conda env file (`aoc_env_2024.yml`) now has:
- ✅ Python 3.12 (stable, fast)
- ✅ jupyterlab instead of jupyter
- ✅ pygraphviz from conda (no compilation needed)
- ✅ All your packages
