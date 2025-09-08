# Inventory-library

A Python client library for the Snipe-IT API. It provides a simple, typed interface to common resources (assets, models, users, etc.) with request retries, error handling, and a convenient change-tracking model for patch updates.

## Installation

### For Users (in another project)

To use this library in another project

```bash
pip install /path/to/inventory-library
```

### For Developers (to work on this library)

To set up a development environment to work on this library, clone the repository and then run the following command in the project's root directory:

```bash
pip install -e .[dev]
```

This will install the project in "editable" mode and include the development dependencies needed for testing.

## Usage

First, initialize the client with your Snipe-IT URL and API token:

```python
from snipeit import SnipeIT

client = SnipeIT(
    url="https://your.snipeitapp.com",
    token="{{SNIPE_IT_API_TOKEN}}",
)
```

### Finding Resources

**List all resources of a type:**

Use the `list()` method on a manager to get a list of all items.

```python
# Get a list of all assets
assets = client.assets.list()

# Get a list of all users
users = client.users.list()
```

**Get a specific resource by ID:**

Use the `get()` method with an ID to retrieve a single item.

```python
# Get the asset with ID 1
asset = client.assets.get(1)
```

### Creating, Updating, and Deleting

**Create a resource:**

Use the `create()` method on the appropriate manager.

```python
new_asset = client.assets.create(
    name="New Laptop",
    status_id=1, 
    model_id=1,
    asset_tag="54321"
)
```

**Update a resource (Recommended Approach):**

The easiest and safest way to update a resource is to get the object, change its attributes, and call the `save()` method. This efficiently sends only the changed fields to the API.

```python
# Get an asset
asset = client.assets.get(1)

# Update its attributes
asset.name = "Updated Laptop Name"
asset.notes = "Added more RAM."

# Save the changes
asset.save()
```

**Delete a resource:**

You can delete a resource using the manager's `delete()` method or by calling `delete()` on the object itself.

```python
# Using the manager
client.assets.delete(2)

# Or, on the object
asset_to_delete = client.assets.get(3)
asset_to_delete.delete()
```

### Object-Specific Actions

Some resources have unique actions you can perform on the object.

```python
# Get an asset
asset = client.assets.get(1)

# Checkout the asset to a user
asset.checkout(checkout_to_type='user', assigned_to_id=123)

# Check the asset back in
asset.checkin(note="Returned to inventory")
```

### Available Resources

The following resource managers are available on the `client` object:

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

Each manager generally provides `list()`, `get(id)`, `create()`, `update(id)`, `patch(id)`, and `delete(id)` methods.

Each resource object provides `save()` and `delete()` methods.

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

- Quick run:

```bash
pytest -q
```

- With coverage (enforces 100% and shows missing lines):

```bash
make cov
```

- HTML coverage report:

```bash
make cov-html
```

- Property-based tests only (Hypothesis):

```bash
make property
```

### Mutation testing (optional)

Mutation testing flips bits in your source to ensure your tests actually detect behavioral changes. It can be slow. We use mutmut configured via setup.cfg.

- Run mutation tests (may take time):

```bash
make mut
```

- See surviving mutants (things your tests didn’t catch):

```bash
make mut-report
```

- Reset mutation state:

```bash
make mut-reset
```

## License

Add your preferred license here.

## Local Docker Environment for Testing

This project includes a `docker-compose.yml` and `.env` file in the `docker` directory to run a local Snipe-IT instance for testing purposes.

### First-time Setup

1.  Navigate to the `docker` directory:
    ```bash
    cd docker
    ```
2.  Generate a new `APP_KEY` for the Snipe-IT instance. Run the following command and copy the output:
    ```bash
    docker compose run --rm app php artisan key:generate --show
    ```
3.  Open the `.env` file and paste the generated key as the value for the `APP_KEY` variable.

### Starting and Stopping the Environment

*   **To start the environment**, run the following command from the `docker` directory:
    ```bash
    docker compose up -d
    ```
    The application will be available at [http://localhost:8000](http://localhost:8000).

*   **To stop the environment**, run the following command from the `docker` directory:
    ```bash
    docker compose down
    ```