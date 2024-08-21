#!/usr/bin/env python3

"""A basic caching system that uses FIFO for cache replacement"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A basic caching system that uses FIFO for cache replacement"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Stores the provided key, whose value is the provided item, into the
        cache. Removes the first inserted key before placing the provided one,
        if the cache is full.

        Args:
            key: The key to store in the cache
            item: The value of the key
        """
        cache_data = self.cache_data
        if key is None or item is None:
            pass

        cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            keys = [key for key in cache_data.keys()]
            del cache_data[keys[0]]
            print('DISCARD: {}'.format(keys[0]))

    def get(self, key):
        """Returns the value that is linked to a key in the cache.

        Args:
            key: The key whose value to get

        Returns:
            The value of the provided key from the cache, or None if no such
            key exists, or if the key is
        """
        return self.cache_data.get(key)
