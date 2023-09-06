```python
import unittest
from src.error_handling import ErrorHandler

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.error_handler = ErrorHandler()

    def test_invalid_url_error(self):
        with self.assertRaises(ValueError):
            self.error_handler.handle_error("Invalid URL", 400)

    def test_missing_fields_error(self):
        with self.assertRaises(ValueError):
            self.error_handler.handle_error("Missing fields", 400)

    def test_pagination_error(self):
        with self.assertRaises(ValueError):
            self.error_handler.handle_error("Pagination error", 400)

    def test_async_error(self):
        with self.assertRaises(ValueError):
            self.error_handler.handle_error("Async error", 400)

    def test_rate_limit_error(self):
        with self.assertRaises(ValueError):
            self.error_handler.handle_error("Rate limit exceeded", 429)

    def test_unknown_error(self):
        with self.assertRaises(Exception):
            self.error_handler.handle_error("Unknown error", 500)

if __name__ == '__main__':
    unittest.main()
```