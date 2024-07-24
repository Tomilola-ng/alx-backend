#!/usr/bin/env python3
"""Module for Least Recently Used (LRU) caching mechanism."""
from collections import OrderedDict
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """LRU cache that evicts the least recently used items first."""

    def __init__(self):
        """Initialize the LRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LRU eviction policy."""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = next(iter(self.cache_data))
                print(f"DISCARD: {lru_key}")
                self.cache_data.pop(lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)

    def get(self, key):
        """Retrieve an item from the cache by key and update its usage."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data[key]
        return None
