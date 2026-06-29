from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Alert:
    title: str
    area: str
    expires: datetime


def parse_alerts(payload: dict) -> list[Alert]:
    """Turn the alerts section of an API response into Alert objects."""
    return [
        Alert(a["title"], a["area"], datetime.fromisoformat(a["expires"]))
        for a in payload.get("alerts", [])
    ]


def active(alerts: list[Alert], now: datetime) -> list[Alert]:
    return [a for a in alerts if a.expires > now]
