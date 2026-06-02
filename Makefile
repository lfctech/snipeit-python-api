# Simple local entrypoints

PY ?= .venv/bin/python

.PHONY: test test-unit check cov cov-html property mut mut-quick mut-report mut-reset clean docker-up docker-down test-integration test-all

# Run the fast suite: unit + public API contract tests
test:
	$(PY) -m pytest tests/unit tests/contract -q -m unit

# Run the fast suite (alias)
test-unit:
	$(PY) -m pytest tests/unit tests/contract -q -m unit

# Lint and type check
check:
	.venv/bin/ruff check .
	.venv/bin/ruff format --check .
	.venv/bin/pyright

# Run the fast suite with source branch coverage and enforce 95%
cov:
	$(PY) -m coverage run --branch --source=snipeit -m pytest tests/unit tests/contract -q -m unit && \
	$(PY) -m coverage report -m --fail-under=95

# Mutation testing (can be slow)
mut:
	$(PY) -m mutmut run --max-children 1 || true

# Advisory mutation run used in CI. Scope is controlled by [tool.mutmut].
mut-quick:
	$(PY) -m mutmut run --max-children 1 || true

mut-report:
	$(PY) -m mutmut results

mut-reset:
	rm -rf .mutmut-cache

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

# Run integration tests: bring up docker, wait for api_key.txt AND for the API
# to actually respond to authenticated requests, then test.
#
# Two-stage wait is required because the seeder writes the token to
# api_key.txt as soon as it generates one, but the Snipe-IT app container is
# usually still booting Apache/PHP at that point. Hitting the API before it's
# ready causes ECONNRESET on the first few requests, which manifests as
# "flaky" test failures that disappear on a re-run once the app is warm.
test-integration:
	$(MAKE) docker-up
	./docker/wait-for-snipeit.sh
	.venv/bin/python -m pytest tests/integration -q -m integration
	

# Run both unit and integration tests
test-all:
	$(MAKE) test
	$(MAKE) test-integration
	$(MAKE) check
