#!/usr/bin/env python3
"""Module for FIFO caching mechanism."""
from collections import OrderedDict
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFO cache that evicts the oldest items first."""

    def __init__(self):
        """Initialize the FIFO cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with FIFO eviction policy."""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.popitem(last=False)

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key)
