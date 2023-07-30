```python
import time
from collections import OrderedDict

class Cache:
    def __init__(self, max_size=100):
        self.cache = OrderedDict()
        self.max_size = max_size

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.max_size:
                self.cache.popitem(last=False)
        self.cache[key] = {
            'date_accessed': time.time(),
            'value': value
        }

    def size(self):
        return len(self.cache)

    def clear(self):
        self.cache.clear()

cache = Cache(max_size=500)
```