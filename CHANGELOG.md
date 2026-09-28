# Changelog

## 1.0.0 (2026-09-28)

- First stable release. No API changes since 1.0.0-rc.1.
- Empty forecast responses return an empty list.
- Alert expiry is compared in UTC.
- Kelvin conversion.

## 1.0.0-rc.1 (2026-08-24)

- RateLimitError for 429 responses; WeatherAPIError keeps the response body.
- --json output for the current command.
- Geocoding lookups are cached.
- Python 3.11 or later is required.

## 0.4.0 (2026-07-20)

- Weather alerts with severity levels, and an alerts command.
- Geocoding of city names.
- Request timeout read from WEATHERKIT_TIMEOUT.
- Hourly forecast formatting.
- Fix: negative temperatures no longer print as -0.

## 0.3.0 (2026-06-05)

- New forecast command and WeatherClient.forecast.
- Pressure conversion (hPa to inHg).

## 0.2.0 (2026-04-28)

- Cache responses for 10 minutes.
- Wind speed conversion (km/h to mph).

## 0.1.0 (2026-03-20)

- First release: current weather for a city, unit conversions.
