import base64
import os
import pytest


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
def test_labels_base64_fallback(snipeit_client, requests_mock, tmp_path):
    pdf_bytes = b"%PDF-1.4\nFAKEPDF"
    b64 = base64.b64encode(pdf_bytes).decode("ascii")
    requests_mock.post(
        "https://test.snipeitapp.com/api/v1/hardware/labels",
        json={"pdf_base64": b64},
        headers={"Content-Type": "application/json"},
        status_code=200,
    )
    save_path = tmp_path / "labels_from_json.pdf"
    result = snipeit_client.assets.labels(str(save_path), ["TAGX"])
    assert result == str(save_path)
    with open(save_path, "rb") as f:
        assert f.read() == pdf_bytes