class WeatherAPIError(Exception):
    """Raised when the weather service answers with an error status."""

    def __init__(self, status_code: int, message: str):
        super().__init__(f"weather API error {status_code}: {message}")
        self.status_code = status_code
        self.body = message


class RateLimitError(WeatherAPIError):
    """Raised on 429 responses. retry_after is in seconds, if the service sent it."""

    def __init__(self, message: str, retry_after: int | None = None):
        super().__init__(429, message)
        self.retry_after = retry_after
