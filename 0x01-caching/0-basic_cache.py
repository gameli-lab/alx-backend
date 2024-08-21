#!/usr/bin/env python3
"""
BasicCache module
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class
    """

    def __init__(self):
        """
            Initializes the class
        """
        self.cache_data = {}

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if key is None or item is None:
            return None
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        else:
            return None
