# Error handling

Every call can raise `WeatherAPIError`. Its `status_code` and `body` attributes hold the service's answer.

`RateLimitError` is a subclass raised on 429 responses. Its `retry_after` attribute gives the wait in seconds when the service sends it.

    from weatherkit.errors import RateLimitError

    try:
        client.current("Oslo")
    except RateLimitError as error:
        time.sleep(error.retry_after or 60)
