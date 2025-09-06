# Simple local entrypoints

PY ?= python3

.PHONY: test cov cov-html property mut mut-report mut-reset clean

# Run tests
test:
	$(PY) -m pytest -q

# Run tests with coverage (branch coverage) and enforce 100%
cov:
	$(PY) -m coverage run -m pytest -q && \
	$(PY) -m coverage report -m --fail-under=100

# Generate HTML coverage report into htmlcov/
cov-html:
	$(PY) -m coverage html && \
	python3 -c 'import webbrowser; webbrowser.open("htmlcov/index.html")' || true

# Run only property-based tests (by marker or filename pattern)
# Adjust -k if you organize property tests under a specific name pattern
property:
	$(PY) -m pytest -q -k property

# Mutation testing (can be slow)
mut:
	$(PY) -m mutmut run --paths-to-mutate snipeit --tests-dir tests || true

mut-report:
	$(PY) -m mutmut results

mut-reset:
	$(PY) -m mutmut reset || true

clean:
	rm -rf .pytest_cache htmlcov .coverage .mutmut-cache

