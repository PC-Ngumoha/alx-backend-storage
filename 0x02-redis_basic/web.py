#!/usr/bin/env python3
"""
web.py

contains the code that seeks to use redis to create a web cache and
track system that gets pages and caches the results for 10 seconds
while also keeping count of how many times said page has been accessed
"""
from functools import wraps
from typing import Any, Callable
import redis
import requests


def cache_and_track(method: Callable) -> Callable:
    """
    cache_and_track decorator
    """
    @wraps(method)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function
        """
        url = args[0]
        cache = redis.Redis()
        page = cache.get('{}'.format(url))
        if page is None:
            page = method(*args, **kwargs)
            cache.setex('{}'.format(url), 10, page)
            cache.incr('count:{}'.format(url))
        return page
    return wrapper


@cache_and_track
def get_page(url: str) -> str:
    """
    get_page(url)

    Args:
      - url (str) -> URL address of website whose content we want

    Returns:
      - HTML content of @url
    """
    return requests.get(url).text
