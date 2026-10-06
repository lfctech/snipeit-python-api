import base64
import json

import pytest

from snipeit.exceptions import SnipeITApiError

pytestmark = pytest.mark.unit


@pytest.mark.unit
@pytest.mark.parametrize("relative_path", ["labels.pdf", "missing/nested/labels.pdf"])
def test_labels_pdf_content(snipeit_client, httpx_mock, tmp_path, relative_path):
    pdf_bytes = b"%PDF-1.4\n...binary..."
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        content=pdf_bytes,
        headers={"Content-Type": "application/pdf"},
        status_code=200,
    )
    save_path = tmp_path / relative_path
    result = snipeit_client.assets.labels(str(save_path), ["TAG1", "TAG2"])
    assert result == str(save_path)
    assert save_path.read_bytes() == pdf_bytes


@pytest.mark.unit
def test_labels_rejects_malformed_json_payload(snipeit_client, httpx_mock, tmp_path):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        json={"pdf_base64": "not-supported-anymore"},
        headers={"Content-Type": "application/json"},
        status_code=200,
    )
    save_path = tmp_path / "labels_from_json.pdf"
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.assets.labels(str(save_path), ["TAGX"])
    assert excinfo.value.response is not None
    assert not save_path.exists()


@pytest.mark.unit
def test_labels_sends_exactly_one_accept_header(tmp_path):
    """Regression: labels() previously sent duplicate Accept headers."""
    import httpx

    from snipeit import SnipeIT

    captured: dict[str, list[str]] = {"accept": []}

    class CaptureTransport(httpx.BaseTransport):
        def handle_request(self, request):
            captured["accept"] = [v.decode() for (k, v) in request.headers.raw if k.lower() == b"accept"]
            return httpx.Response(
                200,
                content=b"%PDF-1.4",
                headers={"Content-Type": "application/pdf"},
            )

    client = SnipeIT(url="https://snipe.example.test", token="t")
    client._http = httpx.Client(
        base_url="https://snipe.example.test/api/v1/",
        headers={"Authorization": "Bearer t", "Accept": "application/json", "User-Agent": "x"},
        transport=CaptureTransport(),
    )

    out = client.assets.labels(str(tmp_path / "x.pdf"), ["TAG1"])
    assert out == str(tmp_path / "x.pdf")
    assert captured["accept"] == ["application/pdf, application/json"], (
        f"expected a single Accept header, got {captured['accept']!r}"
    )


# ---------------------------------------------------------------------------
# Task 14: labels() validation paths
# ---------------------------------------------------------------------------


@pytest.mark.unit
def test_labels_empty_list_raises_value_error(snipeit_client, tmp_path):
    """labels() with an empty list must raise ValueError before any HTTP call."""
    with pytest.raises(ValueError, match="At least one"):
        snipeit_client.assets.labels(str(tmp_path / "out.pdf"), [])


@pytest.mark.unit
def test_labels_all_blank_strings_raises_value_error(snipeit_client, tmp_path):
    """labels() with only blank/whitespace strings must raise ValueError."""
    with pytest.raises(ValueError, match="No valid asset tags"):
        snipeit_client.assets.labels(str(tmp_path / "out.pdf"), ["", "  "])


@pytest.mark.unit
def test_labels_with_asset_objects_sends_only_valid_tags(snipeit_client, httpx_mock, tmp_path):
    """labels() accepts Asset objects; only assets with a non-None asset_tag are sent."""
    import json as _json

    from snipeit.resources.assets import Asset

    class _Mgr:
        api = snipeit_client

    # Asset with tag, Asset without tag
    a1 = Asset(_Mgr(), {"id": 1, "asset_tag": "TAG-A"})
    a2 = Asset(_Mgr(), {"id": 2})  # no asset_tag

    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        content=b"%PDF-1.4",
        headers={"Content-Type": "application/pdf"},
        status_code=200,
    )
    snipeit_client.assets.labels(str(tmp_path / "out.pdf"), [a1, a2])
    body = _json.loads(httpx_mock.get_requests()[-1].content)
    assert body["asset_tags"] == ["TAG-A"], "only the asset with a tag should be sent"


@pytest.mark.parametrize("relative_path", ["labels.pdf", "missing/nested/labels.pdf"])
def test_labels_decodes_official_json_response(snipeit_client, httpx_mock, tmp_path, relative_path):
    pdf = b"%PDF-1.7\n\x00\xffbinary fixture\n%%EOF\n"
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        json={
            "status": "success",
            "messages": "Labels generated successfully.",
            "payload": {"pdf": base64.b64encode(pdf).decode("ascii")},
        },
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    output = tmp_path / relative_path
    assert snipeit_client.assets.labels(str(output), ["001639"]) == str(output)
    assert output.read_bytes() == pdf
    request = httpx_mock.get_requests()[0]
    assert json.loads(request.content) == {"asset_tags": ["001639"]}
    assert request.headers["Accept"] == "application/pdf, application/json"


@pytest.mark.parametrize(
    "body",
    [
        None,
        [],
        "PDF",
        {},
        {"status": "error", "payload": {"pdf": "JVBERi0xLjQ="}},
        {"status": "success"},
        {"status": "success", "payload": None},
        {"status": "success", "payload": []},
        {"status": "success", "payload": {}},
        *[
            {"status": "success", "payload": {"pdf": value}}
            for value in [None, 42, [], "", "%%%", "é", "JVBERi0xLjQ", "SGVsbG8=", "JVBERi1mYWtl"]
        ],
    ],
)
def test_labels_rejects_invalid_envelope_without_overwriting(snipeit_client, httpx_mock, tmp_path, body):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        content=json.dumps(body).encode(),
        headers={"Content-Type": "application/json"},
    )
    output = tmp_path / "existing.pdf"
    output.write_bytes(b"existing label")
    with pytest.raises(SnipeITApiError) as error:
        snipeit_client.assets.labels(str(output), ["001639"])
    assert error.value.status_code == 200
    assert error.value.response is not None
    assert output.read_bytes() == b"existing label"


@pytest.mark.parametrize(
    "content_type,content",
    [
        ("text/html", b"<html>Login</html>"),
        ("", b"%PDF-1.4"),
        ("application/notapplication/pdf", b"%PDF-1.4"),
        ("application/json", b"not JSON"),
        ("application/pdf", b""),
        ("application/pdf", b"<html>Server Error</html>"),
        ("application/pdf", b"%PDF-fake"),
    ],
)
def test_labels_rejects_invalid_bytes_before_creating_directory(
    snipeit_client,
    httpx_mock,
    tmp_path,
    content_type,
    content,
):
    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        content=content,
        headers={"Content-Type": content_type},
    )
    output = tmp_path / "missing" / "label.pdf"
    with pytest.raises(SnipeITApiError) as error:
        snipeit_client.assets.labels(str(output), ["001639"])
    assert error.value.response is not None
    assert not output.parent.exists()


def test_labels_preserves_server_error_response(snipeit_client, httpx_mock, tmp_path):
    from snipeit.exceptions import SnipeITServerError

    httpx_mock.add_response(
        method="POST",
        url="https://snipe.example.test/api/v1/hardware/labels",
        status_code=500,
        json={"message": "Server Error"},
    )
    output = tmp_path / "label.pdf"
    with pytest.raises(SnipeITServerError) as error:
        snipeit_client.assets.labels(str(output), ["001639"])
    assert error.value.status_code == 500
    assert error.value.response.json() == {"message": "Server Error"}
    assert not output.exists()
