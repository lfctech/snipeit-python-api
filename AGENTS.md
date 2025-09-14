# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

Project: snipeit-python-api — a Python 3.11+ client for the Snipe-IT API.

Quick setup
- Use Python 3.11+.
- Create and activate a virtual environment, then install dev extras:
  - python3 -m venv .venv && source .venv/bin/activate
  - pip install -e ".[dev]"
- To install the library (non-editable): pip install .

Common commands
- Lint (Ruff):
  - ruff check .
  - ruff check --fix .
- Type check (Pyright):
  - pyright
- Tests (pytest):
  - All tests: make test
  - Unit-only: make test-unit
  - Run a single test: python -m pytest -q tests/unit/resources/test_assets.py::test_list_assets
  - Filter by keyword: python -m pytest -q -k "assets and not labels"
- Coverage (branch coverage, fail-under=95):
  - make cov
- Mutation testing (Mutmut):
  - make mut        # run mutations (may be slow)
  - make mut-report # show results
  - make mut-reset  # clear cache
- Cleanup test artifacts:
  - make clean

Testing and environment
- Unit tests use requests-mock and a local fixture snipeit_client.
- real_snipeit_client requires env vars and skips if absent:
  - export SNIPEIT_TEST_URL=http://localhost:8000
  - export SNIPEIT_TEST_TOKEN=<your_api_token>
  - Then run pytest as usual (tests using this fixture will exercise a live instance when present).

High-level architecture
- Entry point: snipeit/client.py — SnipeIT
  - Manages a requests.Session with retries (urllib3 Retry) and timeouts.
  - Normalizes URL (requires https://, except http://localhost) and sets headers (Bearer token, JSON, UA including package version when available).
  - Exposes HTTP helpers get/post/put/patch/delete that delegate to _request, which builds URLs as {base}/api/v1/{path}.
  - Error handling maps HTTP status codes to custom exceptions (snipeit/exceptions.py). 204 returns None. Non-JSON 2xx bodies raise a clear SnipeITException.
  - Dynamic resource managers via __getattr__: resolves names like assets, users, models to modules in snipeit.resources, instantiates and caches the manager instance.

- Core model layer: snipeit/resources/base.py
  - ApiObject: holds resource data, tracks modified public attributes via _dirty_fields; save() PATCHes only changed fields; refresh() re-GETs and resets dirty state; delete() issues DELETE.
  - Manager: thin wrapper binding a SnipeIT client, providing internal _get/_create/_patch/_delete.
  - BaseResourceManager[T]: generic CRUD + pagination.
    - list(**params) expects {"rows": [...]}; returns [T].
    - list_all(limit=None, page_size=50, **params) iterates pages using limit/offset; yields T lazily.
    - get(id), create(**data), patch(id, **data), delete(id) map to standard endpoints. Path resolves from resource_cls._path.

- Resource modules (selected)
  - assets.py
    - Asset._path = "hardware"; operations include checkout, checkin, audit; __repr__ shows tag/name/serial/model.
    - AssetsManager extends create(status_id, model_id, asset_tag?=None, **kwargs), get_by_tag, get_by_serial.
    - labels(save_path, assets_or_tags): POSTs to /hardware/labels, requests application/pdf, writes PDF to save_path; falls back to base64 in JSON when necessary.
  - accessories.py: Accessory manager includes checkin_from_user(accessory_user_id) helper.
  - users.py: UsersManager.me() returns the authenticated user (GET users/me).
  - models.py, fields.py: simple create(...) helpers with required arguments.

Notable behaviors
- URL constraint: client enforces https:// except for http://localhost.
- Retries: default total=3, backoff_factor=0.3, status_forcelist={429,500,502,503,504}, and allowed_methods defaults to idempotent methods (HEAD, GET, OPTIONS). You can broaden via retry_allowed_methods.
- HTTP 204 responses return None; other 2xx must return JSON or a SnipeITException is raised.

