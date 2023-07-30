```python
import unittest
from web_scraper_api.error_handler import handle_error

class TestErrorHandler(unittest.TestCase):

    def test_handle_error(self):
        # Test case: Invalid URL
        error_message = handle_error("Invalid URL")
        self.assertEqual(error_message, {"error": "Invalid URL"})

        # Test case: Page not found
        error_message = handle_error("Page not found")
        self.assertEqual(error_message, {"error": "Page not found"})

        # Test case: Product not found
        error_message = handle_error("Product not found")
        self.assertEqual(error_message, {"error": "Product not found"})

if __name__ == '__main__':
    unittest.main()
```