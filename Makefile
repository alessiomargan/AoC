SHELL := /usr/bin/env bash

#######
# Help
#######

.DEFAULT_GOAL := help
.PHONY: help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###################
# Conda Enviroment
###################

CONDA_ENV_NAME ?= aoc
ACTIVATE_ENV = conda activate $(CONDA_ENV_NAME)

mk-conda-env: $(CONDA_ENV_NAME)  ## Build the conda environment
$(CONDA_ENV_NAME):
	conda env create --quiet --file env_aoc.yml
	$(ACTIVATE_ENV)

rm-conda-env:  ## Remove the conda environment and the relevant file
	conda remove --name $(CONDA_ENV_NAME) --all

up-conda-env: $(CONDA_ENV_NAME)
$(CONDA_ENV_NAME):
	conda env update --file env_aoc.yml --prune
	$(ACTIVATE_ENV)

.PHONY: mk-conda-env rm-conda-env up-conda-env
