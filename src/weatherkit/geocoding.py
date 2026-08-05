from dataclasses import dataclass
from functools import lru_cache

import httpx

GEOCODING_URL = "https://geo.example-weather.test/v1/search"


@dataclass(frozen=True)
class Place:
    name: str
    country: str
    latitude: float
    longitude: float


@lru_cache(maxsize=256)
def lookup(city: str, api_key: str, timeout: float = 10.0) -> Place:
    """Return the best match for a city name."""
    response = httpx.get(GEOCODING_URL, params={"q": city, "key": api_key, "limit": 1}, timeout=timeout)
    response.raise_for_status()
    results = response.json()["results"]
    if not results:
        raise LookupError(f"no place named {city!r}")
    top = results[0]
    return Place(top["name"], top["country"], top["lat"], top["lon"])
