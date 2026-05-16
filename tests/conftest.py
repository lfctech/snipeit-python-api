import os
import pytest
from snipeit import SnipeIT


@pytest.fixture
def snipeit_client():
    """Provides a SnipeIT client instance for unit tests (mocked).

    Uses snipe.example.test — an RFC 6761 reserved domain that will never
    resolve in DNS, preventing accidental real network calls if a mock is missed.
    """
    return SnipeIT(url="https://snipe.example.test", token="fake-token")


@pytest.fixture(scope="session")
def real_snipeit_client():
    """Provides a real SnipeIT client for integration tests.

    Requires environment variables:
    - SNIPEIT_TEST_URL: The URL of the test SnipeIT instance (e.g., http://localhost:8000)
    - SNIPEIT_TEST_TOKEN: The API token for the test instance

    Skips integration tests if not set.

    The integration client is configured to retry mutating methods (POST/PATCH/
    PUT/DELETE) on 429 responses. This is safe in the test environment because
    Snipe-IT returns 429 *before* processing the request body, so retrying does
    not risk double-create or double-mutation. In production code, you should
    keep the default ``retry_allowed_methods={"HEAD", "GET", "OPTIONS"}``.
    """
    url = os.environ.get("SNIPEIT_TEST_URL")
    token = os.environ.get("SNIPEIT_TEST_TOKEN")
    if not url or not token:
        pytest.skip("SNIPEIT_TEST_URL and SNIPEIT_TEST_TOKEN must be set for integration tests")
    client = SnipeIT(
        url=url,
        token=token,
        max_retries=5,
        retry_allowed_methods={"HEAD", "GET", "OPTIONS", "POST", "PUT", "PATCH", "DELETE"},
    )
    yield client
    client.close()
