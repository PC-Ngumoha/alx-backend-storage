#!/usr/bin/env python3
"""
Creates the 'Cache' class
"""
from functools import wraps
from typing import Union, Callable, Any, Optional
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """
    count_calls decorator
    """
    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """
        Direct wrapper
        """
        r = redis.Redis()
        r.incr(method.__qualname__)  # increment the value at that point
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """
    Cache class implementation
    """
    def __init__(self):
        """
        __init__() dunder method

        Enables the creation of the Cache class instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store(data)

        Args:
          - data -> data to cache in redis

        Returns:
          - str(value) -> key to fetch stored data
        """
        key: str = str(uuid.uuid4())  # Generates random UUID value
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        get(key, fn)

        Args:
          - key (str) -> key for the value we want to retrieve from redis
          - fn (callable) -> conversion function for the retrieved value

        Returns:
          - value (any) -> value stored in redis converted to it's appropriate
                          type.
        """
        value: Any = self._redis.get(key)
        return fn(value) if fn is not None else value

    def get_str(self, key: str) -> str:
        """
        get_str(key)

        Args:
          - key (str) -> key for str value to retrieve from redis

        Returns:
          - value (str) -> stringified value
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> int:
        """
        get_str(key)

        Args:
          - key (str) -> key for value to retrieve from redis

        Returns:
          - value (int) -> integer value retrieved from redis
        """
        return self.get(key, fn=int)
