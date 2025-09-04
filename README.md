# Inventory-library

A Python client library for the Snipe-IT API. It provides a simple, typed interface to common resources (assets, models, users, etc.) with request retries, error handling, and a convenient change-tracking model for patch updates.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Manager-First Approach

```python
from snipeit import SnipeIT

client = SnipeIT(
    url="https://your.snipeitapp.com",
    token="{{SNIPE_IT_API_TOKEN}}",
)

# List assets
assets = client.assets.get()

# Get a single asset
asset = client.assets.get(1)

# Create an asset
new_asset = client.assets.create(status_id=1, model_id=1, name="Laptop")

# Delete an asset by ID
client.assets.delete(1)
```

### Object-Oriented Approach

This library also allows for a more object-oriented approach, where you can call methods directly on the resource objects.

```python
# Get a single asset
asset = client.assets.get(1)

# Update fields and save only changed fields (PATCH)
asset.name = "Updated Name"
asset.save()

# Update the entire object (PUT)
asset.notes = "New notes"
asset.update()

# Delete the asset
asset.delete()

# Asset-specific actions
asset.checkout(user_id=123)
asset.checkin()
asset.audit()
```

### Available Resources

The following resources are available:

*   `client.accessories`
*   `client.assets`
*   `client.categories`
*   `client.components`
*   `client.consumables`
*   `client.departments`
*   `client.fields`
*   `client.fieldsets`
*   `client.licenses`
*   `client.locations`
*   `client.manufacturers`
*   `client.models`
*   `client.status_labels`
*   `client.users`

Each resource has the following manager methods: `get()`, `create()`, `update()`, `patch()`, and `delete()`.

Resource objects also have `save()`, `update()`, and `delete()` methods.

### Retry behavior
By default, retries are enabled for idempotent methods only (HEAD, GET, OPTIONS). You can override this using `retry_allowed_methods` when constructing the client, but retrying write methods (POST/PUT/PATCH/DELETE) is generally discouraged unless your server guarantees idempotency.

```python
client = SnipeIT(
    url="https://your.snipeitapp.com",
    token="{{SNIPE_IT_API_TOKEN}}",
    retry_allowed_methods={"HEAD", "GET", "OPTIONS"},
)
```

## Running tests

```bash
pytest -q
```

## License

Add your preferred license here.
