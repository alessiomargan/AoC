# Dockerfile for Advent of Code workspace
FROM python:3.14-slim

# Install system dependencies for pygraphviz and development tools
RUN apt-get update && apt-get install -y \
    git \
    graphviz \
    graphviz-dev \
    pkg-config \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy requirements first for better caching
COPY 2024/requirements.txt /tmp/requirements.txt

# Install Python dependencies (including setuptools for compatibility)
RUN pip install --no-cache-dir setuptools && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the entire workspace
COPY . /workspace

# Expose Jupyter port
EXPOSE 8888

# Set up Jupyter configuration (using jupyter lab instead of deprecated notebook)
RUN mkdir -p ~/.jupyter && \
    echo "c.ServerApp.token = ''" >> ~/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.password = ''" >> ~/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.allow_root = True" >> ~/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.ip = '0.0.0.0'" >> ~/.jupyter/jupyter_lab_config.py

# Default command: start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
