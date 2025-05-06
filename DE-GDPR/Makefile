#################################################################################
#
# Makefile for GDPR Obfuscator Project
#
#################################################################################

PROJECT_NAME = gdpr-obfuscator
REGION = eu-west-2
PYTHON_INTERPRETER = python3
PIP = pip
VENV_DIR = venv
SHELL := /bin/bash
WD := $(shell pwd)
PYTHONPATH := ${WD}
ACTIVATE_ENV := source $(VENV_DIR)/bin/activate

## --------------------------------------------------------------------------------
## Setup
## --------------------------------------------------------------------------------

create-environment:
	@echo ">>> Creating virtual environment..."
	$(PIP) install -q virtualenv
	virtualenv $(VENV_DIR) --python=$(PYTHON_INTERPRETER)

install-requirements:
	$(call execute_in_env, $(PIP) install -r requirements.txt)

dev-setup: create-environment install-requirements bandit safety black coverage

bandit:
	$(call execute_in_env, $(PIP) install bandit)

safety:
	$(call execute_in_env, $(PIP) install safety)

black:
	$(call execute_in_env, $(PIP) install black)

coverage:
	$(call execute_in_env, $(PIP) install coverage)

define execute_in_env
	$(ACTIVATE_ENV) && $1
endef

## --------------------------------------------------------------------------------
## Quality Checks
## --------------------------------------------------------------------------------

security-test:
	$(call execute_in_env, safety check -r requirements.txt)
	$(call execute_in_env, bandit -lll gdpr_obfuscator/*.py lambda_gdpr.py)

run-black:
	$(call execute_in_env, black gdpr_obfuscator lambda_gdpr.py)

unit-test:
	$(call execute_in_env, PYTHONPATH=$(PYTHONPATH) pytest -vvrP)

check-coverage:
	$(call execute_in_env, PYTHONPATH=$(PYTHONPATH) coverage run --omit 'venv/*' -m pytest && coverage report -m)

run-checks: security-test run-black unit-test check-coverage

## --------------------------------------------------------------------------------
## Lambda Packaging & Terraform
## --------------------------------------------------------------------------------

lambda-zip:
	@echo ">>> Packaging Lambda function..."
	cd terraform && zip -r lambda.zip ../lambda_function.py ../gdpr_obfuscator ../requirements.txt

terraform-init:
	cd terraform && terraform init

terraform-plan:
	cd terraform && terraform plan -out=tfplan

terraform-apply:
	cd terraform && terraform apply tfplan

terraform-destroy:
	cd terraform && terraform destroy

## --------------------------------------------------------------------------------
## Convenience
## --------------------------------------------------------------------------------

reset-env:
	rm -rf $(VENV_DIR) __pycache__ .pytest_cache .coverage
	find . -name '*.pyc' -delete

