#!/usr/bin/env python3
"""
LRUCache module
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache class
    """

    def __init__(self):
        """
        Initializes the class
        """
        self.cache_data = {}
        self.recent = None
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.recent is not None:
                self.cache_data.pop(self.recent)
                print(f"DISCARD: {self.recent}")
        self.recent = key
        self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache
        """
        if key in self.cache_data:
            self.recent = key
            return self.cache_data[key]
        return None

