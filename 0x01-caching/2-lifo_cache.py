#!/usr/bin/env python3
""" LIFO Cache
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import deque

class LIFOCache(BaseCaching):
    """
    LIFOCache class definition
    """

    def __init__(self):
        """
        Initializes the class
        """
        self.cache_data = {}
        self.order = deque()
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return None
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last = self.order.pop()
            del self.cache_data[last]
            print(f"DISCARD: {last}")
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """
        Gets an item from the cache
        """
        if key is None:
            return None
        
        return self.cache_data.get(key)