```python
import time
from functools import wraps
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'simple'})

def cache_data(timeout=5*60):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = f"{f.__name__}_{str(args)}_{str(kwargs)}"
            result = cache.get(cache_key)
            if result is not None:
                return result
            result = f(*args, **kwargs)
            cache.set(cache_key, result, timeout=timeout)
            return result
        return decorated_function
    return decorator
```