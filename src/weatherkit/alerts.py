from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum


class Severity(Enum):
    MINOR = 1
    MODERATE = 2
    SEVERE = 3
    EXTREME = 4


@dataclass(frozen=True)
class Alert:
    title: str
    area: str
    expires: datetime
    severity: Severity


def parse_alerts(payload: dict) -> list[Alert]:
    """Turn the alerts section of an API response into Alert objects."""
    return [
        Alert(a["title"], a["area"], datetime.fromisoformat(a["expires"]), Severity[a["severity"].upper()])
        for a in payload.get("alerts", [])
    ]


def active(alerts: list[Alert], now: datetime | None = None) -> list[Alert]:
    """Alerts that have not expired. Times are compared in UTC."""
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    return [a for a in alerts if a.expires.astimezone(timezone.utc) > now]
