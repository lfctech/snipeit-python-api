# AGENTS.md

The role of this file is to describe common mistakes and confusion points that agents might encounter as they work in this project. If you ever encounter something in the project that surprises you, please alert the developer working with you and then document it in this file to help prevent future agents from having the same issue.

## Development Rules

- Work on the `dev` branch. Do not create feature branches.
- Use [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`, `refactor:`, `release:`.
- Split commits per logical change (one commit per feature, fix, or refactor).
- Match existing code style. Lint rules are in `pyproject.toml` (ruff + pyright).
- Python ≥ 3.11. Dependencies: `httpx`, `pydantic v2`.

## Workflow

**The workflow is mandatory — do not skip any step, even for small changes.**

1. Make changes.
2. Run `make test` (unit + contract tests) and `make check` (ruff + pyright). Fix any failures before committing.
3. Commit with a conventional commit message.
4. Repeat steps 1–3 for each logical change.
5. When finished, add entries to `CHANGELOG.md` under `## Unreleased` grouped by sub-header (`### New features`, `### Bug fixes`, `### Internal`, etc.) matching the existing style.
6. Commit the changelog update: `docs: update changelog`.

> **Past failure:** An agent completed a multi-file fix but skipped steps 3–6 entirely — no commits were made and the changelog was not updated. The workflow applies to every task, no matter how small.

## Common Surprises

- **Bare `docker compose` shares project state between checkouts.**
  Use the Make targets or `uv run python docker/compose.py` for every stack command, including logs and teardown. The wrapper derives a checkout-specific project name. Port 8000 is still shared, so stop an existing stack before starting another on the default port.
  Keep `docker/` in mutmut's `also_copy`: the wrapper regression tests need it in the mutation sandbox, and mutmut 3.x does not create parent directories for individual nested-file entries.

- **`make test` runs unit + contract tests (not just unit).**
  The `test` target includes `tests/contract` — the contract tests validate the public API surface. Don't skip them.

- **The `Asset` model overrides both `save()` and `_apply_server_data()`.**
  If you're modifying the base `ApiObject` persistence logic, you must also check `snipeit/resources/assets/model.py` — it has non-trivial overrides that handle Snipe-IT's custom field PATCH quirks (null `custom_fields` in responses, column-name echo at top level). Breaking the base class contract will silently break asset custom field workflows.

- **Pydantic v2 internals are used directly in `_apply_server_data`.**
  The base class writes to `__pydantic_extra__` and `__dict__` directly. On any pydantic version bump, run the full test suite — there are regression tests specifically for this (`test_apply_server_data_*`).

- **Integration tests require Docker and a two-stage wait.**
  `make test-integration` handles this automatically. Don't try to run `pytest tests/integration` directly — it needs `SNIPEIT_TEST_URL` and `SNIPEIT_TEST_TOKEN` env vars, which are set by the Makefile's wait loop after Docker is ready.

- **The `docker/api_key.txt` file must be a regular file (not a directory).**
  Docker will auto-create it as a directory if it doesn't exist before `docker compose up`. The Makefile handles this, but if you manually run docker compose, you'll hit a confusing bind-mount error.

- **Every test file must have `pytestmark = pytest.mark.unit` or `pytest.mark.integration`.**
  The Makefile runs tests with `-m unit` or `-m integration`. An unmarked test will be silently skipped (not fail), which is worse — you'll think your new test passes when it never ran.

- **The retry transport's sleep is patched to a no-op in the `snipeit_client` fixture.**
  Without this, tests that trigger retries (429/5xx paths) would sleep for real backoff delays. If you need to verify timing/backoff behavior, construct your own `RetryTransport` with an explicit `sleep=` callable (see `test_retries.py`).

## Releasing (at user's request)

1. Run `make test-all`. unit + contract + integration tests must pass. Fix any failures before proceeding.
2. Run `make mut` — review mutation results (advisory, non-blocking).
3. Decide the version bump following pre-1.0 semver:
   - **MINOR** — breaking changes or significant new features.
   - **PATCH** — bug fixes and non-breaking additions.
4. Update `version` in `pyproject.toml`.
5. Move `## Unreleased` entries in `CHANGELOG.md` under `## X.Y.Z (YYYY-MM-DD)`.
6. Commit: `release: vX.Y.Z`.
7. Tag: `git tag vX.Y.Z`.
8. Push: `git push -u origin dev --tags`.
9. Create PR to `main`: `gh pr create --base main --head dev`.
