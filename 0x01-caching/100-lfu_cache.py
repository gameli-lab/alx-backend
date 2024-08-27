#!/usr/bin/env python3
"""
LRUCache module
"""
BaseCaching = __import__('base_caching').BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    """
    LFUCache class
    """

    def __init__(self):
        """
        Initializes the class
        """
        self.cache_data = {}
        self.freq = defaultdict()
        super().__init__()

    def put(self, key, item):
        """
        Adds an item to the cache
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lfu_key = min(self.freq, key=lambda k: self.freq[k])
            self.cache_data.pop(lfu_key)
            self.freq.pop(lfu_key)
            print("DISCARD: {}".format(lfu_key))
        self.cache_data[key] = item
        self.freq.setdefault(key, 0)
        self.freq[key] += 1

    def get(self, key):
        """
        Gets an item from the cache
        """
        if key not in self.cache_data:
            return None
        self.freq[key] += 1
        return self.cache_data[key]