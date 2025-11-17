# common.mk

# Define the Conda environment name
ENV_NAME ?= aoc_23

# Define the path to the YAML file (default: environment.yml)
YAML_FILE ?= aoc_env_2022.yml

.PHONY: mk_env up_env rm_env

# Target to create the Conda environment
mk_env:
	conda env create -n $(ENV_NAME) -f $(YAML_FILE)

# Target to update the Conda environment
up_env:
	conda env update -n $(ENV_NAME) -f $(YAML_FILE) --prune

# Target to remove the Conda environment
rm_env:
	conda env remove -n $(ENV_NAME)
