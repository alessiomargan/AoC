# GitHub Codespaces Setup (Conda-Based)

This repository is configured to work seamlessly with GitHub Codespaces, providing a fully configured conda-based development environment in your browser.

## Quick Start

### Option 1: Create a Codespace (Browser or VS Code)

1. Go to your GitHub repository
2. Click the green **Code** button
3. Select the **Codespaces** tab
4. Click **Create codespace on main**

Your environment will automatically:

- Build the conda-based Docker container
- Create conda environment with Python 3.14 and all packages
- Set up JupyterLab on port 8888
- Configure VS Code extensions (Python, Jupyter, Copilot)

### Option 2: Open in VS Code Desktop

```bash
# If you have GitHub CLI installed
gh codespace create
gh codespace code
```

## Access JupyterLab

Once your Codespace is running:

1. **Automatic port forwarding** - Codespaces will forward port 8888
2. Click the **Ports** tab in VS Code
3. Click the globe icon next to port 8888 to open JupyterLab in your browser
4. Or use the local URL: `http://localhost:8888`

## Working with Notebooks

### In VS Code

- Open any `.ipynb` file directly in VS Code
- Jupyter extension provides inline notebook editing
- Run cells with `Shift+Enter`
- Select kernel: Python 3.14 (from conda env `aoc`)

### In JupyterLab Browser

- Access full JupyterLab interface at port 8888
- All years (2019-2024) are accessible
- Terminal available for running scripts

## Features Enabled

✅ **Python 3.14** via conda-forge  
✅ **Conda environment** with all AoC dependencies  
✅ **Jupyter Notebooks** with inline editing  
✅ **VS Code Extensions**: Python, Pylance, Jupyter  
✅ **GitHub Copilot** (if you have access)  
✅ **Port Forwarding** for JupyterLab  
✅ **Persistent Storage** - Changes are saved  
✅ **AoC Session** - Set as Codespaces secret  

## Configuration Files

- `.devcontainer/devcontainer.json` - Codespaces configuration
- `docker-compose.yml` - Container orchestration
- `Dockerfile` - Conda-based container image
- `2024/aoc_env_2024.yml` - Conda environment definition
- `.vscode/settings.json` - VS Code workspace settings

## Advent of Code Setup in Codespaces

### Set Your AoC Session Token

1. Go to GitHub repo → **Settings** → **Secrets and variables** → **Codespaces**
2. Click **New repository secret**
3. Name: `AOC_SESSION`
4. Value: Your session token from [adventofcode.com](https://adventofcode.com)
5. Save

The devcontainer automatically injects this as an environment variable.

### Using advent-of-code-data

```python
from aocd import get_data
data = get_data(day=1, year=2024)  # Uses AOC_SESSION automatically
```

## Tips

### Run Python Scripts

```bash
# Open terminal in Codespace
python 2024/day_14_part_2.py
```

### Install Additional Packages

```bash
# Add to conda environment
conda install -n aoc package-name

# Or via pip
pip install package-name

# To persist, add to 2024/aoc_env_2024.yml
```

### Customize Environment

Edit `.devcontainer/devcontainer.json` to:

- Add VS Code extensions
- Change Python settings
- Add post-create commands
- Mount additional volumes

### Codespace Size

Default: 2-core, 8GB RAM, 32GB storage  
To change: GitHub repo → Settings → Codespaces → Set minimum machine type

## Troubleshooting

### Jupyter not accessible

```bash
# Check if Jupyter is running
ps aux | grep jupyter

# Restart if needed
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

### Port not forwarded

1. Open **Ports** tab in VS Code
2. Manually add port 8888 if missing
3. Set visibility to **Public** if you need external access

### Rebuild container

If dependencies change:

1. Command Palette (`Ctrl+Shift+P`)
2. Select: **Codespaces: Rebuild Container**

### Conda environment issues

```bash
# Check conda environment
conda env list

# Activate environment
conda activate aoc

# Update environment
conda env update -f 2024/aoc_env_2024.yml
```

### Performance Issues

- Stop unused Codespaces (billed by time)
- Increase machine size in repository settings
- Close unnecessary extensions

## Cost Considerations

- **Free tier**: 120 core-hours/month (60 hours on 2-core)
- **Pricing**: ~$0.18/hour for 2-core machine
- **Auto-stop**: Codespaces stop after 30 min inactivity (configurable)

Set timeout:

```bash
gh codespace edit --idle-timeout 30m
```

## Conda vs pip in Codespaces

This setup uses conda because:

✅ **Faster builds** - Pre-compiled binaries  
✅ **Reliable** - No pip backtracking  
✅ **Python flexibility** - Works with any Python version  
✅ **System packages** - pygraphviz from conda-forge  

## Local Development Alternative

If you prefer local development, use the same Docker setup:

```bash
docker-compose up --build
```

See `docker-README.md` for details.
