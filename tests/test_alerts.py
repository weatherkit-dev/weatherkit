from datetime import datetime, timezone

from weatherkit.alerts import Severity, parse_alerts

PAYLOAD = {"alerts": [{"title": "Heat warning", "area": "Seville", "expires": "2026-07-03T18:00:00+00:00", "severity": "severe"}]}


def test_parse_alerts():
    [alert] = parse_alerts(PAYLOAD)
    assert alert.severity is Severity.SEVERE
    assert alert.expires == datetime(2026, 7, 3, 18, tzinfo=timezone.utc)


def test_no_alerts():
    assert parse_alerts({}) == []
