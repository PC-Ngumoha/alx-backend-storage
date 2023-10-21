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
        Wrapper function
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    call_history decorator
    """
    @wraps(method)
    def wrapper(self, *args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function
        """
        output = method(self, *args, *kwargs)
        self._redis.rpush('{}:inputs'.format(method.__qualname__), str(args))
        self._redis.rpush('{}:outputs'.format(method.__qualname__), output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    replay(method)

    Args:
      - method (callable): method whose call history we want to replay.

    Returns:
      - None
    """
    r = redis.Redis()
    inputs = [data.decode() for data in
              r.lrange('{}:inputs'.format(method.__qualname__), 0, -1)]
    outputs = [data.decode() for data in
               r.lrange('{}:outputs'.format(method.__qualname__), 0, -1)]
    history_length = r.llen('{}:inputs'.format(method.__qualname__))
    print('{} was called {} times:'.format(
        method.__qualname__, history_length))
    for row in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(
            method.__qualname__, row[0], row[1]
        ))


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
    @call_history
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
