# Docker dev stack

This directory contains a throwaway Snipe-IT instance used for integration tests.

## Quick start

```bash
make docker-up   # Start Snipe-IT + MySQL + seeder
make test-all    # Run unit + integration tests
make docker-down # Stop and delete volumes
```

## How it works

1. `docker-compose.yml` starts three services: `db` (MySQL), `app` (Snipe-IT), and `seeder` (a one-shot container that creates an admin user and writes the API key to `api_key.txt`).
2. `make test-integration` waits up to 120 s for `api_key.txt` to be non-empty, then runs `pytest -m integration` with `SNIPEIT_TEST_URL` and `SNIPEIT_TEST_TOKEN` set from that file.
3. `api_key.txt` is gitignored — it is generated at runtime and must not be committed.

## `.env`

The `.env` file is committed intentionally. It contains only local dev bootstrap values (no real secrets). See the comment block at the top of the file.
