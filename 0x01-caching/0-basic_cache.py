#!/usr/bin/env python3
"""Module for basic caching mechanism."""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic cache with simple put and get methods."""

    def put(self, key, item):
        """Add an item to the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key."""
        return self.cache_data.get(key)
