# Dockerfile for Advent of Code workspace (Conda-based)
FROM continuumio/miniconda3:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Copy conda environment file for better caching
COPY 2025/aoc_env_2025.yml /tmp/environment.yml

# Create conda environment and install packages
RUN conda env create -f /tmp/environment.yml && \
    conda clean -afy

# Make RUN commands use the new environment
ENV PATH=/opt/conda/envs/aoc/bin:$PATH
ENV CONDA_DEFAULT_ENV=aoc

# Create a non-root user that will match the host user (UID/GID provided at build time)
ARG USERNAME=aoc
ARG USER_UID=1000
ARG USER_GID=1000
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m -s /bin/bash ${USERNAME}

# Ensure the workspace exists and is owned by the non-root user
RUN mkdir -p /workspace \
    && chown -R ${USERNAME}:${USER_GID} /workspace

# Pre-create common config directories for the non-root user (for bind mounts)
RUN mkdir -p /home/${USERNAME}/.config \
    && chown -R ${USERNAME}:${USER_GID} /home/${USERNAME}/.config

# Copy workspace into image (for standalone use)
# Note: This is overridden by volume mount when using docker-compose
COPY . /workspace

# Expose Jupyter port
EXPOSE 8888

# Set up Jupyter configuration
RUN mkdir -p /home/${USERNAME}/.jupyter && \
    echo "c.ServerApp.token = ''" >> /home/${USERNAME}/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.password = ''" >> /home/${USERNAME}/.jupyter/jupyter_lab_config.py && \
    echo "c.ServerApp.ip = '0.0.0.0'" >> /home/${USERNAME}/.jupyter/jupyter_lab_config.py && \
    chown -R ${USERNAME}:${USER_GID} /home/${USERNAME}/.jupyter

# Set default HOME and user for runtime
ENV HOME=/home/${USERNAME}
USER ${USERNAME}

# Default command: start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
