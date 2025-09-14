import pytest


@pytest.mark.unit
def test_asset_repr_model_none(snipeit_client, requests_mock):
    requests_mock.get(
        "https://test.snipeitapp.com/api/v1/hardware/12",
        json={
            "id": 12,
            "name": "Foo",
            "asset_tag": "T12",
            "serial": "S12",
            "model": None,
        },
    )
    asset = snipeit_client.assets.get(12)
    assert repr(asset) == "<Asset T12 (Foo - S12 - N/A)>"