# Dockerfile for Advent of Code workspace
FROM python:3.14-slim

# Install system dependencies for pygraphviz
RUN apt-get update && apt-get install -y \
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

# Install Python dependencies
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy the entire workspace
COPY . /workspace

# Expose Jupyter port
EXPOSE 8888

# Set up Jupyter configuration
RUN jupyter notebook --generate-config && \
    echo "c.NotebookApp.token = ''" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.password = ''" >> ~/.jupyter/jupyter_notebook_config.py && \
    echo "c.NotebookApp.allow_root = True" >> ~/.jupyter/jupyter_notebook_config.py

# Default command: start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
