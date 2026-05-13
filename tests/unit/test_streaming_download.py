"""Tests for T11: streaming file downloads."""

import pytest
from pytest_httpx import IteratorStream


@pytest.mark.unit
def test_download_file_streams_and_writes(snipeit_client, httpx_mock, tmp_path):
    """download_file writes streamed chunks to disk."""
    data = b"chunk1" + b"chunk2"
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/hardware/1/files/2",
        stream=IteratorStream([b"chunk1", b"chunk2"]),
        headers={"Content-Length": str(len(data))},
        status_code=200,
    )
    dest = tmp_path / "dl.bin"
    out = snipeit_client.assets.download_file(1, 2, str(dest))
    assert out == str(dest)
    assert dest.read_bytes() == data


@pytest.mark.unit
def test_download_file_progress_callback(snipeit_client, httpx_mock, tmp_path):
    """progress callback receives (bytes_written, total) on each chunk."""
    chunks = [b"a" * 100, b"b" * 200]
    total_bytes = sum(len(c) for c in chunks)
    httpx_mock.add_response(
        method="GET",
        url="https://test.snipeitapp.com/api/v1/hardware/1/files/3",
        stream=IteratorStream(chunks),
        headers={"Content-Length": str(total_bytes)},
        status_code=200,
    )
    calls: list[tuple[int, int | None]] = []
    dest = tmp_path / "progress.bin"
    snipeit_client.assets.download_file(1, 3, str(dest), progress=lambda n, t: calls.append((n, t)))
    assert calls[-1][0] == total_bytes
    assert all(t == total_bytes for _, t in calls)
