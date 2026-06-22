import os

import httpx

from weatherkit.cache import TTLCache
from weatherkit.errors import WeatherAPIError

BASE_URL = "https://api.example-weather.test/v1"


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
        if response.status_code != 200:
            raise WeatherAPIError(response.status_code, response.text)
        data = response.json()
        self.cache.set(city, data)
        return data

    def forecast(self, city: str, days: int = 3) -> list[dict]:
        if not 1 <= days <= 7:
            raise ValueError("days must be between 1 and 7")
        response = httpx.get(f"{BASE_URL}/forecast", params={"q": city, "days": days, "key": self.api_key}, timeout=self.timeout)
        if response.status_code != 200:
            raise WeatherAPIError(response.status_code, response.text)
        return response.json()["days"]
