import os

import httpx

from weatherkit.air_quality import AirQuality, parse_air_quality
from weatherkit.alerts import Alert, parse_alerts
from weatherkit.cache import TTLCache
from weatherkit.errors import RateLimitError, WeatherAPIError

BASE_URL = "https://api.example-weather.test/v1"


def _check(response: httpx.Response) -> None:
    if response.status_code == 429:
        retry_after = response.headers.get("Retry-After")
        raise RateLimitError(response.text, int(retry_after) if retry_after else None)
    if response.status_code != 200:
        raise WeatherAPIError(response.status_code, response.text)


class WeatherClient:
    def __init__(self, api_key: str, timeout: float | None = None):
        self.api_key = api_key
        self.timeout = timeout if timeout is not None else float(os.environ.get("WEATHERKIT_TIMEOUT", "10"))
        self.cache = TTLCache(ttl_seconds=600)

    def current(self, city: str) -> dict:
        cached = self.cache.get(city)
        if cached is not None:
            return cached
        response = httpx.get(f"{BASE_URL}/current", params={"q": city, "key": self.api_key}, timeout=self.timeout)
        _check(response)
        data = response.json()
        self.cache.set(city, data)
        return data

    def forecast(self, city: str, days: int = 3) -> list[dict]:
        if not 1 <= days <= 7:
            raise ValueError("days must be between 1 and 7")
        response = httpx.get(f"{BASE_URL}/forecast", params={"q": city, "days": days, "key": self.api_key}, timeout=self.timeout)
        _check(response)
        return response.json().get("days") or []

    def alerts(self, city: str) -> list[Alert]:
        response = httpx.get(f"{BASE_URL}/alerts", params={"q": city, "key": self.api_key}, timeout=self.timeout)
        _check(response)
        return parse_alerts(response.json())

    def air_quality(self, city: str) -> AirQuality:
        response = httpx.get(f"{BASE_URL}/air-quality", params={"q": city, "key": self.api_key}, timeout=self.timeout)
        _check(response)
        return parse_air_quality(response.json())
