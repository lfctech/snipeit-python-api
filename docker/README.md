# Docker dev stack

This directory contains a throwaway Snipe-IT instance used for integration tests.

## Quick start

```bash
make docker-up   # Start Snipe-IT + MySQL + seeder
make test-all    # Run unit + integration tests
make docker-down # Stop and delete volumes
```

## How it works

1. `docker-compose.yml` starts three services: `db` (MySQL), `app` (Snipe-IT), and `seeder` (a one-shot container that creates an admin user and writes the API key to `api_key.txt`). The Snipe-IT image defaults to the pinned `snipe/snipe-it:v8.6.1-alpine`.
2. `make test-integration` waits up to 120 s for `api_key.txt` to be non-empty and up to 120 s for the authenticated API readiness check, then runs `pytest -m integration`.
3. `api_key.txt` is gitignored — it is generated at runtime and must not be committed.

To run the integration suite against the latest Snipe-IT image as an advisory
compatibility check:

```bash
SNIPEIT_IMAGE=snipe/snipe-it:latest-alpine make test-integration
```

## `.env`

The `.env` file is committed intentionally. It contains only local dev bootstrap values (no real secrets). See the comment block at the top of the file.
