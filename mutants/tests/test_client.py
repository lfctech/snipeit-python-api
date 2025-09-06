import pytest
from snipeit import SnipeIT

def test_https_required():
    with pytest.raises(ValueError, match="URL must start with https://"):
        SnipeIT(url="http://test.snipeitapp.com", token="test")
