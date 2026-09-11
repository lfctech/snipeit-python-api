# Docker dev stack

This directory contains a throwaway Snipe-IT instance used for integration tests.

## Quick start

```bash
uv sync --locked # Install the local Python environment (from the repository root)
make docker-up   # Start Snipe-IT + MySQL + seeder
make test-all    # Run unit + integration tests
make docker-down # Stop and delete volumes
```

## How it works

1. `docker-compose.yml` starts three services: `db` (MySQL), `app` (Snipe-IT), and `seeder` (a one-shot container that creates an admin user and writes the API key to `api_key.txt`). Both Snipe-IT services are pinned to `snipe/snipe-it:v8.7.2-alpine` for reproducible compatibility tests.
2. `make test-integration` waits up to 120 s for `api_key.txt` to be non-empty, then runs `pytest -m integration` with `SNIPEIT_TEST_URL` and `SNIPEIT_TEST_TOKEN` set from that file.
3. `api_key.txt` is gitignored — it is generated at runtime and must not be committed.

## Checkout isolation

The Make targets and CI use `docker/compose.py`. It derives a deterministic
Compose project name from the canonical checkout path, so separate clones and
worktrees receive separate database/storage volumes and seeder state. Startup,
logs, and teardown must use the same wrapper:

```bash
uv run python docker/compose.py ps
uv run python docker/compose.py logs --follow seeder
uv run python docker/compose.py stop # Keep this checkout's volumes for later
make docker-down                    # Delete only this checkout's test volumes
```

Do not use bare `docker compose` for this stack: it defaults to the shared
`docker` project. Existing legacy `docker` volumes are not deleted or migrated.
The default HTTP port remains 8000; stop one stack before starting another on
that port. State isolation does not provide simultaneous HTTP port allocation.

An explicit `COMPOSE_PROJECT_NAME` environment variable overrides the derived
name. Use the same value for every command in that stack's lifecycle, and never
reuse a name across checkouts unless sharing state is intentional. A project
name set only in `docker/.env` does not override the wrapper's explicit name.

## `.env`

The `.env` file is committed intentionally. It contains only local dev bootstrap values (no real secrets). See the comment block at the top of the file.
