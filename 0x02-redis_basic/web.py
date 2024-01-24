#!/usr/bin/env python3

"""
Redis basics advanced tasks

"""

import redis
import requests
import time
from functools import wraps
from typing import Callable


def cache_expiring(seconds: int) -> Callable:
    """Decorator that caches the function result with an expiration time."""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            key = f"cache:{url}"
            cached_result = redis_client.get(key)
            if cached_result is not None:
                return cached_result.decode("utf-8")

            result = func(url)
            redis_client.setex(key, seconds, result)
            return result

        return wrapper

    return decorator


def track_count(func: Callable) -> Callable:
    """Decorator that tracks the number of times a URL is accessed."""
    @wraps(func)
    def wrapper(url: str) -> str:
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)

    return wrapper


@cache_expiring(seconds=10)
@track_count
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL."""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    redis_client = redis.Redis()

    get_page('http://slowwly.robertomurray.co.uk')