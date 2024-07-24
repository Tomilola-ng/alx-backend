#!/usr/bin/env python3
"""Defines the base caching class."""

class BaseCaching:
    """Base class for caching system with constants and storage."""
    
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the cache storage."""
        self.cache_data = {}

    def print_cache(self):
        """Display the current state of the cache."""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")

    def put(self, key, item):
        """Add an item to the cache."""
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Retrieve an item from the cache."""
        raise NotImplementedError("get must be implemented in your cache class")
