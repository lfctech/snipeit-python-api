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

### Not yet supported

The following Snipe-IT API endpoints are **not** wrapped by this client:
Groups, Reports, Settings, Audit log, Maintenances (asset-level
`create_maintenance` is the only related method). Use the raw
`client.get`/`client.post` verbs against those paths if needed.

## Common Pitfalls

### Typos on model attributes are silently accepted

Pydantic models use `extra="allow"` so the client stays resilient to new
fields added by future Snipe-IT versions. The downside is that a typo in an
attribute name creates a new extra field instead of raising an error:

```python
asset.serail = "SN-001"  # typo — creates an extra field named "serail"
asset.save()             # PATCHes {"serail": "SN-001"} — server ignores it
```

The real `serial` field is never updated. To catch this class of bug, enable
strict type-checking in your editor (pyright or mypy) and rely on the declared
fields (`asset_tag`, `name`, `serial`, `model`) which are type-checked. For
fields not declared on the model, there is no static protection.

### Setting custom field values

Use the dedicated helpers on `Asset` to read and write custom fields by their
display label:

```python
asset = api.assets.get(1)

owner = asset.get_custom_field("Owner")        # read
asset.set_custom_field("Owner", "alice")       # stage
asset.save()                                   # persist
```

`set_custom_field()` raises `KeyError` if the label is not defined on the
asset (most often because the asset hasn't been fetched yet, or the field is
not associated with the asset's model fieldset). The methods chain, so
`asset.set_custom_field("Owner", "alice").save()` works too. You can also
combine custom and regular field updates in one save:

```python
asset.name = "Renamed"
asset.set_custom_field("Owner", "alice")
asset.save()  # PATCH {"name": "Renamed", "_snipeit_owner_3": "alice"}
```

#### Why the helpers exist

Snipe-IT's REST API uses two different shapes for custom fields:

* **Read shape** — GET responses return them under `custom_fields` keyed by
  display label: `custom_fields["Owner"] == {"field": "_snipeit_owner_3", "value": "alice", ...}`.
* **Write shape** — PATCH expects the underlying column name as a **top-level
  key**: `{"_snipeit_owner_3": "alice"}`. The nested `custom_fields` shape is
  silently ignored on the versions tested in CI.

The helpers exist because the manual write path has two surprises stacked
on top of each other: you need the column name (not the label), and the
library's dirty tracker treats any attribute starting with `_` as private and
skips it — so a plain `setattr(asset, "_snipeit_owner_3", "alice")` is
dropped from the PATCH unless followed by `mark_dirty()`. The helpers handle
both for you.

If you ever need to do it by hand (e.g. you only have the column name and not
the label), the manual pattern is:

```python
column_name = asset.custom_fields["Owner"]["field"]   # "_snipeit_owner_3"
setattr(asset, column_name, "alice")
asset.mark_dirty(column_name)
asset.save()
```

Mutating the nested response shape directly
(`asset.custom_fields["Owner"]["value"] = "alice"`) *is* detected by the
dirty tracker, but Snipe-IT's PATCH endpoint silently ignores the resulting
`{"custom_fields": {...}}` payload. Stick with `set_custom_field()`.

### In-place mutation of nested objects

Mutating a nested dict or list in-place is detected automatically via
snapshot-and-diff tracking:

```python
asset.tags.append("retired")
asset.save()  # correctly PATCHes tags
```

If you need to force a field into the PATCH payload regardless of whether it
changed (e.g. to trigger server-side recomputation), use `mark_dirty()`:

```python
asset.mark_dirty("custom_fields")
asset.save()
```

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
