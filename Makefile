# Simple local entrypoints

PY ?= python3

.PHONY: test test-unit check cov cov-html property mut mut-report mut-reset clean docker-up docker-down test-integration test-all

# Run unit tests only
test:
	$(PY) -m pytest tests/unit -q -m unit

# Run unit tests only (alias)
test-unit:
	$(PY) -m pytest tests/unit -q -m unit

# Lint and type check
check:
	.venv/bin/ruff check .
	.venv/bin/pyright

# Run tests with coverage (branch coverage) and enforce 95%
cov:
	$(PY) -m coverage run -m pytest -q && \
	$(PY) -m coverage report -m --fail-under=95

# Mutation testing (can be slow)
mut:
	$(PY) -m mutmut run --paths-to-mutate snipeit --tests-dir tests || true

mut-report:
	$(PY) -m mutmut results

mut-reset:
	$(PY) -m mutmut reset || true

clean:
	rm -rf .pytest_cache htmlcov .coverage .mutmut-cache .hypothesis .ruff_cache

# Start Snipe-IT stack
docker-up:
	cd docker && docker compose up -d

# Stop stack and delete volumes
docker-down:
	cd docker && docker compose down -v

# Run integration tests: bring up docker, wait for api_key.txt, then test
test-integration:
	$(MAKE) docker-up
	@echo "Waiting for docker/api_key.txt (up to ~120s)..."
	@i=0; \
	while [ ! -s docker/api_key.txt ] && [ $$i -lt 120 ]; do \
		sleep 1; i=$$((i+1)); \
	done; \
	if [ ! -s docker/api_key.txt ]; then \
		echo "Timed out waiting for docker/api_key.txt. Check 'docker compose logs --follow seeder'."; \
		exit 1; \
	fi
	.venv/bin/python -m pytest -q -m integration
	$(MAKE) docker-down

# Run both unit and integration tests
test-all:
	$(MAKE) test
	$(MAKE) test-integration
	$(MAKE) check
