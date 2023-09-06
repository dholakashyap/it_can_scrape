```python
import unittest
from src.rate_limiting import RateLimiter

class TestRateLimiting(unittest.TestCase):

    def setUp(self):
        self.rate_limiter = RateLimiter()

    def test_rate_limiting(self):
        # Test that the rate limiter allows the first request
        self.assertTrue(self.rate_limiter.allow_request())

        # Simulate a large number of requests
        for _ in range(100):
            self.rate_limiter.allow_request()

        # Test that the rate limiter blocks further requests
        self.assertFalse(self.rate_limiter.allow_request())

    def test_reset(self):
        # Test that the rate limiter allows the first request
        self.assertTrue(self.rate_limiter.allow_request())

        # Simulate a large number of requests
        for _ in range(100):
            self.rate_limiter.allow_request()

        # Reset the rate limiter
        self.rate_limiter.reset()

        # Test that the rate limiter allows requests again after reset
        self.assertTrue(self.rate_limiter.allow_request())

if __name__ == '__main__':
    unittest.main()
```