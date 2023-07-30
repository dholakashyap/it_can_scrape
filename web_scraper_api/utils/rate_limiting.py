```python
import time
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

def rate_limit():
    """
    This function applies rate limiting to the API requests.
    """
    @limiter.limit("100/minute")
    def limit_requests():
        time.sleep(1)
        return "Request processed"

    return limit_requests
```