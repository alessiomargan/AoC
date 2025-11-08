# Docker Setup for Advent of Code Workspace

## Quick Start

### Build and Run with Docker Compose (Recommended)
```bash
docker-compose up --build
```

Then open your browser to: http://localhost:8888

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
- **URL:** http://localhost:8888
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

✅ **Python 3.14** - Latest Python version as specified in your conda env
✅ **All dependencies** - numpy, jupyter, matplotlib, networkx, etc.
✅ **System libraries** - graphviz for pygraphviz
✅ **Volume mounting** - Edit files on host, changes reflect in container
✅ **Persistent Jupyter config** - Settings saved between restarts

## Customization

### Change Jupyter port
Edit `docker-compose.yml`:
```yaml
ports:
  - "9999:8888"  # Access on port 9999
```

### Add a password
Uncomment and modify in `Dockerfile`:
```dockerfile
RUN jupyter lab password
# Enter your password when prompted during build
```

### Use conda instead of pip
Replace the pip installation in `Dockerfile` with:
```dockerfile
FROM continuumio/miniconda3:latest
COPY 2024/aoc_env_2024.yml /tmp/environment.yml
RUN conda env create -f /tmp/environment.yml
RUN echo "conda activate aoc" >> ~/.bashrc
SHELL ["conda", "run", "-n", "aoc", "/bin/bash", "-c"]
```

## Troubleshooting

### Port already in use
```bash
# Change port in docker-compose.yml or stop conflicting service
lsof -i :8888
```

### Permission issues
```bash
# Fix ownership of created files
docker-compose exec aoc-jupyter chown -R $(id -u):$(id -g) /workspace
```

### Rebuild after dependency changes
```bash
docker-compose up --build --force-recreate
```
