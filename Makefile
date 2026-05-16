# Simple local entrypoints

PY ?= python3

.PHONY: test test-unit check cov cov-html property mut mut-quick mut-report mut-reset clean docker-up docker-down test-integration test-all

# Run unit tests only
test:
	$(PY) -m pytest tests/unit tests/contract -q -m unit

# Run unit tests only (alias)
test-unit:
	$(PY) -m pytest tests/unit tests/contract -q -m unit

# Lint and type check
check:
	.venv/bin/ruff check .
	.venv/bin/pyright

# Run tests with coverage (branch coverage) and enforce 95%
cov:
	$(PY) -m coverage run -m pytest tests/unit tests/contract -q -m unit && \
	$(PY) -m coverage report -m --fail-under=95

# Mutation testing (can be slow)
mut:
	$(PY) -m mutmut run --paths-to-mutate snipeit --tests-dir tests || true

# Quick mutation run scoped to the highest-value source files (used in CI)
mut-quick:
	$(PY) -m mutmut run \
		--paths-to-mutate snipeit/client.py,snipeit/_retry.py,snipeit/resources/base.py \
		--tests-dir tests/unit tests/contract || true

mut-report:
	$(PY) -m mutmut results

mut-reset:
	$(PY) -m mutmut reset || true

clean:
	rm -rf .pytest_cache htmlcov .coverage .mutmut-cache .hypothesis .ruff_cache
	$(MAKE) docker-down

# Start Snipe-IT stack
# Ensure docker/api_key.txt exists as a regular empty file BEFORE docker compose
# bind-mounts it. If the path doesn't exist (or is a directory), Docker will
# auto-create it as a directory, breaking the seeder's `> /api_key.txt` redirect.
docker-up:
	@if [ ! -f docker/api_key.txt ] || [ -d docker/api_key.txt ]; then \
		rm -rf docker/api_key.txt; \
		touch docker/api_key.txt; \
	fi
	cd docker && docker compose up -d

# Stop stack and delete volumes. Restore api_key.txt as an empty regular file
# so the next `make docker-up` has a valid bind-mount target.
docker-down:
	cd docker && docker compose down -v
	rm -rf docker/api_key.txt
	touch docker/api_key.txt

# Run integration tests: bring up docker, wait for api_key.txt, then test
test-integration:
	$(MAKE) docker-up
	@echo "Waiting for docker/api_key.txt (up to ~120s)..."
	@i=0; \
	while [ ! -s docker/api_key.txt ] && [ $$i -lt 120 ]; do \
		sleep 1; i=$$((i+1)); \
	done; \
	if [ -d docker/api_key.txt ]; then \
		echo "ERROR: docker/api_key.txt is a directory, not a file. Run 'make docker-down' to reset."; \
		exit 1; \
	fi; \
	if [ ! -s docker/api_key.txt ]; then \
		echo "Timed out waiting for docker/api_key.txt. Check 'docker compose logs --follow seeder'."; \
		exit 1; \
	fi
	.venv/bin/python -m pytest tests/integration -q -m integration
	

# Run both unit and integration tests
test-all:
	$(MAKE) test
	$(MAKE) test-integration
	$(MAKE) check
