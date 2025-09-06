import pytest
from snipeit import SnipeIT

def test_https_required():
    with pytest.raises(ValueError) as excinfo:
        SnipeIT(url="http://test.snipeitapp.com", token="test")
    assert str(excinfo.value) == "URL must start with https://"
