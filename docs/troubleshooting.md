# Troubleshooting

- **401 errors:** check WEATHERKIT_API_KEY.
- **Timeouts:** raise WEATHERKIT_TIMEOUT.
- **429 errors:** the service limits requests; catch RateLimitError and wait retry_after seconds.
