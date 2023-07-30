```python
from urllib.parse import urlparse

def validate_request(request):
    url = request.get('url', None)
    if not url:
        return False, "Missing 'url' in request parameters."

    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]):
        return False, "Invalid 'url' in request parameters."

    return True, "Valid request."
```