# Docker Build Cache Guide for AoC

## How Caching Works

Your Dockerfile is optimized to maximize cache usage:

```dockerfile
# These layers are cached and rarely change
FROM python:3.13-slim                          # Layer 1: Base image (cached)
RUN apt-get install...                         # Layer 2: System deps (cached)
WORKDIR /workspace                             # Layer 3: Workdir (cached)

# Requirements layer - only rebuilds when requirements.txt changes
COPY 2024/requirements.txt /tmp/requirements.txt  # Layer 4: Req file
RUN pip install -r /tmp/requirements.txt          # Layer 5: Pip install (CACHED!)

# Your code - rebuilds frequently but pip install stays cached
COPY . /workspace                              # Layer 6: Code (rebuilds often)
```

## Build Times

| Scenario | Time | Reason |
|----------|------|--------|
| **First build** | 3-5 min | Downloads everything |
| **Code change only** | 5-10 sec | Uses pip cache |
| **requirements.txt change** | 2-3 min | Re-runs pip install |
| **Dockerfile change before pip** | 3-5 min | Invalidates cache |

## Verify Caching

### Test 1: Build twice without changes
```bash
# First build
docker-compose build

# Second build (should be instant)
docker-compose build
# You'll see: "Using cache" for most steps
```

### Test 2: Change code only
```bash
# Edit a notebook or Python file
echo "# test" >> 2024/days.ipynb

# Rebuild - only copies new code
docker-compose build
# Pip install step shows: "Using cache"
```

### Test 3: Add a package
```bash
# Add to requirements.txt
echo "pandas" >> 2024/requirements.txt

# Rebuild - pip install runs again
docker-compose build
# You'll see pip downloading pandas
```

## Force Full Rebuild

If you need to bypass cache:

```bash
# Docker Compose
docker-compose build --no-cache

# Docker directly
docker build --no-cache -t aoc-workspace .

# Nuclear option (clean everything)
docker system prune -a
docker-compose build
```

## Cache Management

### Check cache size
```bash
docker system df
```

### Clean old layers (keeps recent)
```bash
docker builder prune
```

### Remove specific images
```bash
docker images
docker rmi aoc-workspace
```

## Optimization Tips

✅ **Already done in your Dockerfile:**
- System deps installed before pip (rarely change)
- requirements.txt copied separately
- `--no-cache-dir` flag (doesn't cache pip downloads in container)
- `.dockerignore` excludes unnecessary files

🚀 **Additional optimizations (optional):**

### Use multi-stage build (smaller final image)
```dockerfile
# Build stage
FROM python:3.13-slim as builder
COPY 2024/requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM python:3.13-slim
COPY --from=builder /root/.local /root/.local
```

### Pin versions in requirements.txt
```txt
numpy==1.26.0  # Ensures consistent builds
jupyter==1.0.0
```

### Use BuildKit (faster builds)
```bash
DOCKER_BUILDKIT=1 docker-compose build
```

## Common Issues

### "No space left on device"
```bash
docker system prune -a  # Clean old images
```

### Slow builds even with cache
- Check `.dockerignore` excludes large files
- Use `DOCKER_BUILDKIT=1` for parallel builds
- Pin package versions to avoid re-resolving deps

### Cache not working
- Check if you modified Dockerfile lines before pip install
- Verify requirements.txt hasn't changed
- Check if using `--no-cache` flag accidentally

## Summary

✅ Your Dockerfile is already optimized!  
✅ pip install only runs when requirements.txt changes  
✅ Normal code edits rebuild in seconds  
✅ Docker caching is automatic and transparent
