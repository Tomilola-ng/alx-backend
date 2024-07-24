#!/usr/bin/env python3
"""Module for LIFO caching mechanism."""
from collections import OrderedDict
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """LIFO cache that evicts the most recently added items first."""

    def __init__(self):
        """Initialize the LIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LIFO eviction policy."""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = next(reversed(self.cache_data))
                print(f"DISCARD: {last_key}")
                self.cache_data.popitem(last=True)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key)
