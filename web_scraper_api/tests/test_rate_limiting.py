```python
import unittest
from web_scraper_api.utils.rate_limiting import RateLimiter

class TestRateLimiting(unittest.TestCase):

    def setUp(self):
        self.rate_limiter = RateLimiter()

    def test_rate_limiting(self):
        # Test that the rate limiter allows the first request
        self.assertTrue(self.rate_limiter.allow_request())

        # Simulate a large number of requests
        for _ in range(100):
            self.rate_limiter.record_request()

        # Test that the rate limiter blocks further requests
        self.assertFalse(self.rate_limiter.allow_request())

if __name__ == '__main__':
    unittest.main()
```