import os
import pytest

from snipeit.exceptions import SnipeITApiError


@pytest.mark.unit
def test_labels_pdf_content(snipeit_client, requests_mock, tmp_path):
    pdf_bytes = b"%PDF-1.4\n...binary..."
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/labels",
        content=pdf_bytes,
        headers={"Content-Type": "application/pdf"},
        status_code=200,
    )
    save_path = tmp_path / "labels.pdf"
    result = snipeit_client.assets.labels(str(save_path), ["TAG1", "TAG2"])
    assert result == str(save_path)
    assert os.path.exists(save_path)
    assert os.path.getsize(save_path) == len(pdf_bytes)


@pytest.mark.unit
def test_labels_rejects_non_pdf_content_type(snipeit_client, requests_mock, tmp_path):
    # The API must return a PDF; JSON/HTML responses are a misconfiguration.
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/labels",
        json={"pdf_base64": "not-supported-anymore"},
        headers={"Content-Type": "application/json"},
        status_code=200,
    )
    save_path = tmp_path / "labels_from_json.pdf"
    with pytest.raises(SnipeITApiError) as excinfo:
        snipeit_client.assets.labels(str(save_path), ["TAGX"])
    assert "application/json" in str(excinfo.value)


@pytest.mark.unit
def test_labels_sends_exactly_one_accept_header(tmp_path):
    """Regression: labels() previously copied client headers into a dict
    (lowercasing keys) and then added ``Accept: application/pdf``, resulting
    in two ``Accept`` headers sent to the server.
    """
    import httpx
    from snipeit import SnipeIT

    captured: dict[str, list[str]] = {"accept": []}

    class CaptureTransport(httpx.BaseTransport):
        def handle_request(self, request):
            captured["accept"] = [
                v.decode() for (k, v) in request.headers.raw if k.lower() == b"accept"
            ]
            return httpx.Response(
                200,
                content=b"%PDF-1.4",
                headers={"Content-Type": "application/pdf"},
            )

    client = SnipeIT(url="https://test.snipeitapp.com", token="t")
    client._http = httpx.Client(
        base_url="https://test.snipeitapp.com/api/v1/",
        headers={
            "Authorization": "Bearer t",
            "Accept": "application/json",
            "User-Agent": "x",
        },
        transport=CaptureTransport(),
    )
    client.session = client._http

    out = client.assets.labels(str(tmp_path / "x.pdf"), ["TAG1"])
    assert out == str(tmp_path / "x.pdf")
    # Exactly one Accept header, and it's the PDF one.
    assert captured["accept"] == ["application/pdf"], (
        f"expected a single Accept: application/pdf header, got {captured['accept']!r}"
    )
