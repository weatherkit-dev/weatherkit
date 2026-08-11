import json
import sys

from weatherkit import cli


class FakeClient:
    def __init__(self, api_key):
        pass

    def current(self, city):
        return {"city": city, "temp_c": 18.0, "temp_f": 64.4, "condition": "Cloudy"}


def test_json_output(monkeypatch, capsys):
    monkeypatch.setenv("WEATHERKIT_API_KEY", "test")
    monkeypatch.setattr(cli, "WeatherClient", FakeClient)
    monkeypatch.setattr(sys, "argv", ["weatherkit", "--json", "current", "Oslo"])
    cli.main()
    assert json.loads(capsys.readouterr().out)["city"] == "Oslo"
