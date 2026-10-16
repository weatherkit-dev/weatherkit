import pytest

from weatherkit.errors import RateLimitError
from weatherkit.retry import with_backoff


def test_succeeds_after_retries(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda seconds: None)
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RateLimitError("slow down", retry_after=1)
        return "ok"

    assert with_backoff(flaky) == "ok"
    assert len(calls) == 3


def test_gives_up(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda seconds: None)

    def always_limited():
        raise RateLimitError("slow down")

    with pytest.raises(RateLimitError):
        with_backoff(always_limited, retries=2)
