#!/usr/bin/env python3

"""An implementation of a basic caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic caching system"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Stores the provided key, whose value is the provided item, into the
        cache.

        Args:
            key: The key to store in the cache
            item: The value of the key
        """
        if key is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value that is linked to a key in the cache.

        Args:
            key: The key whose value to get
        """
        return self.cache_data.get(key)
