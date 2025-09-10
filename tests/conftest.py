import os
import pytest
from snipeit import SnipeIT


@pytest.fixture
def snipeit_client():
    """Provides a SnipeIT client instance for unit tests (mocked)."""
    return SnipeIT(url="https://test.snipeitapp.com", token="fake-token")


@pytest.fixture(scope="session")
def real_snipeit_client():
    """Provides a real SnipeIT client for integration tests.
    
    Requires environment variables:
    - SNIPEIT_TEST_URL: The URL of the test SnipeIT instance (e.g., http://localhost:8000)
    - SNIPEIT_TEST_TOKEN: The API token for the test instance
    
    Skips integration tests if not set.
    """
    url = os.environ.get("SNIPEIT_TEST_URL")
    token = os.environ.get("SNIPEIT_TEST_TOKEN")
    if not url or not token:
        pytest.skip("SNIPEIT_TEST_URL and SNIPEIT_TEST_TOKEN must be set for integration tests")
    return SnipeIT(url=url, token=token)
