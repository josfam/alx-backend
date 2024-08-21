#!/usr/bin/enb python3

"""An implementation of a basic caching system"""


class BaseCaching:
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """Initiliaze"""
        self.cache_data = {}

    def print_cache(self):
        """Print the cache"""
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache"""
        raise NotImplementedError(
            "put must be implemented in your cache class"
        )

    def get(self, key):
        """Get an item by key"""
        raise NotImplementedError(
            "get must be implemented in your cache class"
        )


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
