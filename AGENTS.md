# AGENTS.md

## Development Rules

- Work on the `dev` branch. Do not create feature branches.
- Use [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `test:`, `ci:`, `chore:`, `refactor:`, `release:`.
- Split commits per logical change (one commit per feature, fix, or refactor).
- Match existing code style. Lint rules are in `pyproject.toml` (ruff + pyright).
- Python ≥ 3.11. Dependencies: `httpx`, `pydantic v2`.

## Workflow

1. Make changes.
2. Run `make test` (unit + contract tests) and `make check` (ruff + pyright). Fix any failures before committing.
3. Commit with a conventional commit message.
4. Repeat steps 1–3 for each logical change.
5. When finished, add entries to `CHANGELOG.md` under `## Unreleased` grouped by sub-header (`### New features`, `### Bug fixes`, `### Internal`, etc.) matching the existing style.
6. Commit the changelog update: `docs: update changelog`.

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
