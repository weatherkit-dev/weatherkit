import time

from weatherkit.errors import RateLimitError


def with_backoff(call, retries: int = 3, base_delay: float = 1.0, max_total: float = 30.0):
    """Call call() and retry on RateLimitError, doubling the delay each time."""
    started = time.time()
    for attempt in range(retries + 1):
        try:
            return call()
        except RateLimitError as error:
            if attempt == retries or time.time() - started > max_total:
                raise
            time.sleep(error.retry_after or base_delay * 2 ** attempt)
