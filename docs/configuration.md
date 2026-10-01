# Configuration

| Variable | Meaning | Default |
|---|---|---|
| WEATHERKIT_API_KEY | API key of the weather service | required |
| WEATHERKIT_TIMEOUT | Request timeout in seconds | 10 |
| WEATHERKIT_CACHE_TTL | Cache lifetime in seconds | 600 |

The cache lives in memory and is not shared between processes. Geocoding results are cached separately, for the life of the process.
