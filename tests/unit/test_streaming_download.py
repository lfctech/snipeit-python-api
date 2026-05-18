"""Tests for T11: streaming file downloads."""

import pytest
from pytest_httpx import IteratorStream

pytestmark = pytest.mark.unit


@pytest.mark.unit
def test_download_file_streams_and_writes(snipeit_client, httpx_mock, tmp_path):
    """download_file writes streamed chunks to disk."""
    data = b"chunk1" + b"chunk2"
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1/files/2",
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
        url="https://snipe.example.test/api/v1/hardware/1/files/3",
        stream=IteratorStream(chunks),
        headers={"Content-Length": str(total_bytes)},
        status_code=200,
    )
    calls: list[tuple[int, int | None]] = []
    dest = tmp_path / "progress.bin"
    snipeit_client.assets.download_file(1, 3, str(dest), progress=lambda n, t: calls.append((n, t)))
    assert calls[-1][0] == total_bytes
    assert all(t == total_bytes for _, t in calls)


# ---------------------------------------------------------------------------
# Task 11: _stream_request error paths via download_file
# ---------------------------------------------------------------------------

@pytest.mark.unit
def test_download_file_timeout_raises_snipeit_timeout_error(snipeit_client, httpx_mock, tmp_path):
    """A timeout during streaming must surface as SnipeITTimeoutError, not a raw httpx error."""
    import httpx

    from snipeit.exceptions import SnipeITTimeoutError

    httpx_mock.add_exception(
        httpx.TimeoutException("timed out"),
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1/files/9",
    )
    with pytest.raises(SnipeITTimeoutError):
        snipeit_client.assets.download_file(1, 9, str(tmp_path / "out.bin"))


@pytest.mark.unit
def test_download_file_connect_error_raises_snipeit_exception(snipeit_client, httpx_mock, tmp_path):
    """A connection error during streaming must surface as SnipeITException."""
    import httpx

    from snipeit.exceptions import SnipeITException

    # ConnectError on GET is retried (default max_retries=3); register 4 exceptions.
    for _ in range(4):
        httpx_mock.add_exception(
            httpx.ConnectError("refused"),
            method="GET",
            url="https://snipe.example.test/api/v1/hardware/1/files/10",
        )
    with pytest.raises(SnipeITException):
        snipeit_client.assets.download_file(1, 10, str(tmp_path / "out.bin"))


# ---------------------------------------------------------------------------
# Task 15: Streaming download without Content-Length
# ---------------------------------------------------------------------------

@pytest.mark.unit
def test_download_file_progress_without_content_length(snipeit_client, httpx_mock, tmp_path):
    """When Content-Length is absent, progress callback receives total=None."""
    from pytest_httpx import IteratorStream

    chunks = [b"x" * 50, b"y" * 50]
    httpx_mock.add_response(
        method="GET",
        url="https://snipe.example.test/api/v1/hardware/1/files/11",
        stream=IteratorStream(chunks),
        # No Content-Length header
        status_code=200,
    )
    calls: list[tuple[int, int | None]] = []
    dest = tmp_path / "no_len.bin"
    snipeit_client.assets.download_file(1, 11, str(dest), progress=lambda n, t: calls.append((n, t)))
    assert dest.read_bytes() == b"x" * 50 + b"y" * 50
    assert all(t is None for _, t in calls), "total must be None when Content-Length is absent"
    assert calls[-1][0] == 100
