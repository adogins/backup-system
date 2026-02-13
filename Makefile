# Makefile for Backup System

PYTHON := python3
PYTHONPATH := src

run: 
	PYTHONPATH=$(PYTHONPATH) $(PYTHON) -m backup_system.scanner

test:
	PYTHONPATH=$(PYTHONPATH) pytest -v

format:
	black src/backup_system tests

lint: 
	flake8 src/backup_system tests

shell:
	PYTHONPATH=$(PYTHONPATH) $(PYTHON)