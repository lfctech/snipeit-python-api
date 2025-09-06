import pytest
from snipeit import SnipeIT


@pytest.fixture
def snipeit_client():
    """Provides a SnipeIT client instance for tests."""
    return SnipeIT(url="https://test.snipeitapp.com", token="fake-token")
