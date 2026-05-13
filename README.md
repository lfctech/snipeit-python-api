# Snipe-IT Python API Client

A Python client for the [Snipe-IT](https://snipeitapp.com/) API.

## Features

- Object-oriented interface for Snipe-IT resources.
- Handles authentication, retries, timeouts, and response parsing.
- CRUD operations on all major resources.
- Automatic retry with exponential backoff and `Retry-After` support.
- Streaming file downloads with optional progress callback.
- Structured logging (`snipeit` / `snipeit.http` loggers).
- Pydantic v2 models with `extra="allow"` — resilient to Snipe-IT version drift.

### Supported Resources

Accessories, Assets, Categories, Companies, Components, Consumables,
Departments, Fields, Fieldsets, Licenses, Locations, Manufacturers,
Models, Status Labels, Suppliers, Users.

## Installation

```bash
# Using uv
uv add git+https://github.com/lfctech/snipeit-python-api@main

# Or using pip
pip install git+https://github.com/lfctech/snipeit-python-api@main
```

## Quick Start

```python
import logging
from snipeit import SnipeIT, SnipeITNotFoundError

# Optional: enable HTTP-level debug logging
logging.basicConfig(level=logging.DEBUG)

with SnipeIT(url="https://snipe.example.com", token="your-api-token") as api:
    # List assets
    for asset in api.assets.list_all(page_size=100):
        print(asset)

    # Get by tag
    try:
        asset = api.assets.get_by_tag("LAPTOP-001")
    except SnipeITNotFoundError:
        print("Not found")

    # Modify and save
    asset.name = "Updated Name"
    asset.save()

    # Checkout
    asset.checkout(checkout_to_type="user", assigned_to_id=42)

    # Download a file with progress
    api.assets.download_file(
        asset_id=1,
        file_id=2,
        save_path="/tmp/attachment.pdf",
        progress=lambda n, t: print(f"{n}/{t or '?'} bytes"),
    )
```

## Development Setup

```bash
make docker-up   # Start local Snipe-IT in Docker
make test        # Unit tests
make check       # Lint + type-check
make test-all    # Unit + integration tests
```

## Testing

```bash
make test            # Unit tests only (default)
make test-unit       # Alias
make test-integration  # Requires Docker
make test-all        # Both
make check           # ruff + pyright
make cov             # Coverage (≥85% enforced)
```

## What's New in 0.2

- **httpx** replaces `requests` as the HTTP backend.
- **Pydantic v2** models with `extra="allow"` and proper dirty tracking.
- **Streaming downloads** — large files no longer load into memory.
- **3xx redirects raise** `SnipeITApiError` instead of silently returning HTML.
- **Localization-safe** `get_by_tag` / `get_by_serial` — works on any Snipe-IT locale.
- **Exceptions at top level** — `from snipeit import SnipeITNotFoundError`.
- **`repr(client)`** redacts the token.
- **CI** on Python 3.11, 3.12, 3.13.

See [CHANGELOG.md](CHANGELOG.md) for the full list.
