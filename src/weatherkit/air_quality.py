from dataclasses import dataclass

BANDS = [(20, "good"), (40, "fair"), (50, "moderate"), (100, "poor"), (150, "very poor")]


@dataclass(frozen=True)
class AirQuality:
    city: str
    pm2_5: float
    pm10: float


def band(pm10: float) -> str:
    """European air quality band for a PM10 value."""
    for limit, name in BANDS:
        if pm10 <= limit:
            return name
    return "extremely poor"


def parse_air_quality(payload: dict) -> AirQuality:
    return AirQuality(payload["city"], payload["pm2_5"], payload["pm10"])
