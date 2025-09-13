from snipeit.resources.locations import Location


def test_list_locations(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/locations", json={
        "total": 1,
        "rows": [{"id": 1, "name": "Test Location"}]
    })
    locations = snipeit_client.locations.list()
    assert len(locations) == 1
    assert isinstance(locations[0], Location)
    assert locations[0].name == "Test Location"

def test_get_location(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/locations/1", json={"id": 1, "name": "Test Location"})
    location = snipeit_client.locations.get(1)
    assert isinstance(location, Location)
    assert location.name == "Test Location"

def test_create_location(snipeit_client, requests_mock):
    requests_mock.post("https://test.snipeitapp.com/api/v1/locations", json={"status": "success", "payload": {"id": 2, "name": "New Location"}})
    new_location = snipeit_client.locations.create(name="New Location")
    assert isinstance(new_location, Location)
    assert new_location.name == "New Location"
    assert requests_mock.last_request.json() == {"name": "New Location"}


def test_patch_location(snipeit_client, requests_mock):
    requests_mock.patch("https://test.snipeitapp.com/api/v1/locations/1", json={"status": "success", "payload": {"id": 1, "name": "Patched Location"}})
    patched_location = snipeit_client.locations.patch(1, name="Patched Location")
    assert isinstance(patched_location, Location)
    assert patched_location.name == "Patched Location"

def test_delete_location(snipeit_client, requests_mock):
    requests_mock.delete("https://test.snipeitapp.com/api/v1/locations/1", json={"status": "success", "messages": "Location deleted"})
    snipeit_client.locations.delete(1)
    assert requests_mock.called

def test_save_location(snipeit_client, requests_mock):
    requests_mock.get("https://test.snipeitapp.com/api/v1/locations/1", json={"id": 1, "name": "Test Location"})
    requests_mock.patch("https://test.snipeitapp.com/api/v1/locations/1", json={"status": "success", "payload": {"id": 1, "name": "Saved Location"}})
    location = snipeit_client.locations.get(1)
    location.name = "Saved Location"
    location.save()
    assert location.name == "Saved Location"