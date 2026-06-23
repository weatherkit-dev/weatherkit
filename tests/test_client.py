from weatherkit.client import WeatherClient


def test_timeout_from_environment(monkeypatch):
    monkeypatch.setenv("WEATHERKIT_TIMEOUT", "3.5")
    assert WeatherClient(api_key="test").timeout == 3.5


def test_explicit_timeout_wins(monkeypatch):
    monkeypatch.setenv("WEATHERKIT_TIMEOUT", "3.5")
    assert WeatherClient(api_key="test", timeout=20).timeout == 20
