# Snipe-IT Python API Client

A Python client for the [Snipe-IT](https://snipeitapp.com/) API. This library provides a convenient way to interact with a Snipe-IT instance, manage assets, users, and other resources.

## Features

*   Object-oriented interface for Snipe-IT resources.
*   Handles API authentication, request signing, and response parsing.
*   Support for CRUD operations (Create, Read, Update, Delete) on various resources.
*   Automatic retry mechanism for transient server errors.
*   Integration with a local Dockerized Snipe-IT for development and testing.

### Supported Resources

*   Accessories
*   Assets
*   Categories
*   Components
*   Consumables
*   Departments
*   Fields
*   Fieldsets
*   Licenses
*   Locations
*   Manufacturers
*   Models
*   Status Labels
*   Users

## Getting Started

### Installation

To install the library, you can use `pip`:

```bash
pip install .
```

### Development Setup

A Docker environment is provided for local development and testing. This will spin up a Snipe-IT instance with all necessary dependencies.

1.  **Start the Docker containers:**

    ```bash
    cd docker
    docker-compose up -d
    ```

2.  **API Key:**

    The first time you start the containers, an API key will be generated and saved to `docker/api_key.txt`. This key is used by the integration tests to communicate with the local Snipe-IT instance.

## Usage

Here is a basic example of how to use the client to fetch assets:

```python
from snipeit import SnipeIT

# Initialize the client with your Snipe-IT URL and API token
with SnipeIT(url="http://localhost:8000", token="your-api-token") as client:
    # List all assets
    try:
        assets = client.assets.list()
        for asset in assets:
            print(f"Asset Name: {asset.name}, Tag: {asset.asset_tag}")
    except Exception as e:
        print(f"An error occurred: {e}")
    # ...
```

## Testing

The project uses `pytest` for testing and provides `make` commands for convenience. Tests are separated into `unit` and `integration` tests.

### Running Unit Tests

Unit tests are self-contained and do not require a running Snipe-IT instance.

```bash
make test-unit
```

### Running Integration Tests

Integration tests run against a real Snipe-IT instance and require the Docker environment to be running.

1.  **Start the Docker environment:**

    ```bash
    cd docker
    docker-compose up -d
    ```

2.  **Run the integration tests:**

    ```bash
    make test-integration
    ```

### Running All Tests

To run all tests (both unit and integration), use:

```bash
make test-all
```

## License

This project is licensed under the MIT License.
