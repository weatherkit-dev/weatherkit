class WeatherAPIError(Exception):
    """Raised when the weather service answers with an error status."""

    def __init__(self, status_code: int, message: str):
        super().__init__(f"weather API error {status_code}: {message}")
        self.status_code = status_code
        self.body = message
