# Advent of Code Solutions

Solutions for [Advent of Code](https://adventofcode.com/) challenges from 2019-2024.

## Links
- [AoC 2019](https://adventofcode.com/2019)
- [AoC 2020](https://adventofcode.com/2020)
- [AoC 2021](https://adventofcode.com/2021)
- [AoC 2022](https://adventofcode.com/2022)
- [AoC 2023](https://adventofcode.com/2023)
- [AoC 2024](https://adventofcode.com/2024)

## Containerization Options

### 1. Local Docker Development
```bash
docker-compose up --build
# Open http://localhost:8888
```

### 2. GitHub Codespaces (Ready to Use!)
Go to: `https://github.com/alessiomargan/AoC`
- Click **Code** → **Codespaces** 
- Click **Create codespace on main**
- Wait ~2-3 minutes for setup
- Start coding!

### 3. VS Code Remote Containers
In VS Code:
- `Ctrl+Shift+P` → "Dev Containers: Reopen in Container"
- Uses the same configuration as Codespaces

## What You Get

| Feature | Local Docker | Codespaces | VS Code Dev Container |
|---------|-------------|------------|---------------------|
| **Setup Time** | ~3 min | ~2 min | ~3 min |
| **Cost** | Free | 60h/month free | Free |
| **Internet Required** | Build only | Always | Build only |
| **JupyterLab** | ✅ Port 8888 | ✅ Auto-forwarded | ✅ Port 8888 |
| **VS Code Integration** | Manual | ✅ Full | ✅ Full |
| **File Persistence** | ✅ Volume mount | ✅ Cloud storage | ✅ Volume mount |

## Quick Tips

**To customize extensions**, edit `.devcontainer/devcontainer.json`:
```json
"extensions": [
  "ms-python.python",
  "ms-toolsai.jupyter",
  "GitHub.copilot",
  "your-extension-here"  // Add more
]
```

**To change Jupyter settings**, edit `Dockerfile`:
```dockerfile
# Add password protection
RUN jupyter lab password
```

**To use conda instead of pip**, see the instructions in `docker-README.md`

## Legacy Setup (Conda)

```bash
# create conda env
make aoc

ipython kernel install --user --name=aoc

jupyter kernelspec remove aoc
```

## Documentation

- [docker-README.md](docker-README.md) - Detailed Docker setup guide
- [CODESPACES.md](CODESPACES.md) - GitHub Codespaces usage guide
