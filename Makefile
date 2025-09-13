# Simple local entrypoints

PY ?= python3

.PHONY: test cov cov-html property mut mut-report mut-reset clean

# Run tests
test:
	$(PY) -m pytest -q

# Run unit tests only
test-unit:
	$(PY) -m pytest tests/unit -q -m unit

# Run tests with coverage (branch coverage) and enforce 100%
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
