#!/usr/bin/env python3
"""
Creates the 'Cache' class
"""
from typing import Union
import redis
import uuid


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
