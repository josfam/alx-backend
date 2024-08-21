#!/usr/bin/env python3

"""A basic caching system that uses LIFO for cache replacement"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A basic caching system that uses LIFO for cache replacement"""

    def __init__(self):
        super().__init__()
        self.newest_key = None

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
        elif key in cache_data:
            # replace, and mark this as newest
            cache_data[key] = item
            self.newest_key = key
        else:
            if len(self.cache_data) + 1 > self.MAX_ITEMS:
                # pop the newest key, and update
                del cache_data[self.newest_key]
                print('DISCARD: {}'.format(self.newest_key))
            cache_data[key] = item
            self.newest_key = key

    def get(self, key):
        """Returns the value that is linked to a key in the cache.

        Args:
            key: The key whose value to get

        Returns:
            The value of the provided key from the cache, or None if no such
            key exists, or if the key is
        """
        return self.cache_data.get(key)
