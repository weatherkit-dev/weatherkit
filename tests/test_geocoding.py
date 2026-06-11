import httpx
import pytest

from weatherkit import geocoding


def fake_get(payload):
    return lambda *args, **kwargs: httpx.Response(200, json=payload, request=httpx.Request("GET", "https://geo.test"))


def test_lookup_returns_first_result(monkeypatch):
    monkeypatch.setattr(httpx, "get", fake_get({"results": [{"name": "Porto", "country": "PT", "lat": 41.15, "lon": -8.61}]}))
    assert geocoding.lookup("Porto", api_key="test").country == "PT"


def test_lookup_unknown_city(monkeypatch):
    monkeypatch.setattr(httpx, "get", fake_get({"results": []}))
    with pytest.raises(LookupError):
        geocoding.lookup("Atlantis", api_key="test")
