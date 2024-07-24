#!/usr/bin/env python3
"""Module for Least Frequently Used (LFU) caching mechanism."""
from collections import OrderedDict
from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """LFU cache that evicts the least frequently used items first."""

    def __init__(self):
        """Initialize the LFU cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, key):
        """Reorder items in the cache based on frequency of usage."""
        for i, (k, freq) in enumerate(self.keys_freq):
            if k == key:
                freq += 1
                self.keys_freq.pop(i)
                break
        else:
            freq = 1
        self.keys_freq.insert(next((i for i, (_, f) in enumerate(self.keys_freq) if f > freq), len(self.keys_freq)), (key, freq))

    def put(self, key, item):
        """Add an item to the cache with LFU eviction policy."""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq.pop()
                del self.cache_data[lfu_key]
                print(f"DISCARD: {lfu_key}")
            self.cache_data[key] = item
            self.__reorder_items(key)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key and update its frequency."""
        if key in self.cache_data:
            self.__reorder_items(key)
            return self.cache_data[key]
        return None
