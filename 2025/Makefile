# common.mk

# Define the Conda environment name
ENV_NAME ?= aoc_25

# Define the path to the YAML file (default: environment.yml)
YAML_FILE ?= aoc_env_2025.yml

.PHONY: mk_env up_env rm_env pip_install run_day run_all test help

# Path to pip requirements (optional)
REQ_FILE ?= requirements.txt

# How to run commands inside the conda env without activating it in the shell
CONDA_RUN ?= conda run -n $(ENV_NAME) --no-capture-output

# Target to create the Conda environment
mk_env:
	conda env create -n $(ENV_NAME) -f $(YAML_FILE)

# Target to update the Conda environment
up_env:
	conda env update -n $(ENV_NAME) -f $(YAML_FILE) --prune

# Target to remove the Conda environment
rm_env:
	conda env remove -n $(ENV_NAME)

# Install pip requirements into the conda env (uses `conda run` so activation is not required)
pip_install: $(REQ_FILE)
	@echo "Installing pip requirements from $(REQ_FILE) into conda env '$(ENV_NAME)'"
	$(CONDA_RUN) pip install -r $(REQ_FILE)

# Run a single day script: make run_day DAY=14 (runs day_14.py)
# If DAY=all, it will fall back to run_all.
run_day:
	@if [ "$(DAY)" = "" ]; then echo "Please provide DAY=<n> (e.g. DAY=14) or DAY=all"; exit 1; fi
	@if [ "$(DAY)" = "all" ]; then $(MAKE) run_all; else \
		f=day_$(DAY).py; \
		if [ -f $$f ]; then echo "Running $$f..."; $(CONDA_RUN) python $$f; else echo "File $$f not found"; exit 1; fi; \
	fi

# Run all day_*.py scripts (non-recursive)
run_all:
	@echo "Running all day_*.py scripts in $(CURDIR)"
	@for f in day_*.py; do \
		echo "=== $$f ==="; \
		$(CONDA_RUN) python $$f || exit 1; \
	done

# Run tests with pytest inside the conda env
test:
	$(CONDA_RUN) pytest -q

help:
	@echo "Available targets:"; \
	@echo "  mk_env       - create the conda env from $(YAML_FILE)"; \
	@echo "  up_env       - update the conda env from $(YAML_FILE)"; \
	@echo "  rm_env       - remove the conda env '$(ENV_NAME)'"; \
	@echo "  pip_install  - pip install -r $(REQ_FILE) into the conda env (uses conda run)"; \
	@echo "  run_day DAY=<n>|all - run a specific day script (e.g. DAY=14) or all"; \
	@echo "  run_all      - run all day_*.py scripts"; \
	@echo "  test         - run pytest inside the conda env"; \
	@echo "  help         - show this help"
