#!/usr/bin/env python3
""" FIFO Cache
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import deque

class FIFOCache(BaseCaching):
    """
    FIFOCache class
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
            first = self.order.popleft()
            self.cache_data.pop(first)
            print(f"DISCARD: {first}")
        self.cache_data[key] = item
        self.order.append(key)
    
    def get(self, key):
        """
        Gets an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None