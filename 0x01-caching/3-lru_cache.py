#!/usr/bin/env python3
"""
LRUCache module
"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching

class LRUCache(BaseCaching):
    """
    LRUCache class
    """
    def __init__(self):
        """
        Initializes the class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.popitem(last = False)
            print(f"DISCARD: {self.cache_data.popitem(last = False)}")

    def get(self, key):
        """
        Gets an item from the cache
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        else:
            return None