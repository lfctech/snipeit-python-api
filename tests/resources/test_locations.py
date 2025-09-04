import pytest
from snipeit.resources.locations import Location


def test_get_locations_list(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/locations", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Location"}]
    })
    locations = snipeit_client.locations.get()
    assert len(locations) == 1
    assert isinstance(locations[0], Location)
    assert locations[0].name == "Test Location"

def test_create_location(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/locations", json={"status": "success", "payload": {"id": 2, "name": "New Location"}})
    new_location = snipeit_client.locations.create(name="New Location")
    assert isinstance(new_location, Location)
    assert new_location.name == "New Location"
    assert requests_mock.last_request.json()["name"] == "New Location"
