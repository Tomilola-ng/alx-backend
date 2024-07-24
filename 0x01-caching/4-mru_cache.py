#!/usr/bin/env python3
"""Module for Most Recently Used (MRU) caching mechanism."""
from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRU cache that evicts the most recently used items first."""

    def __init__(self):
        """Initialize the MRU cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with MRU eviction policy."""
        if key is not None and item is not None:
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = next(reversed(self.cache_data))
                print(f"DISCARD: {mru_key}")
                self.cache_data.pop(mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieve an item from the cache by key and update its usage."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data[key]
        return None
