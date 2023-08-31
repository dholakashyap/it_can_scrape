```python
import unittest
from web_scraper_api.utils.caching import cache_data, get_cached_data

class TestCaching(unittest.TestCase):

    def setUp(self):
        self.url = "https://example.com/product"
        self.data = {
            "product_name": "Test Product",
            "product_price": "100",
            "product_description": "This is a test product",
            "customer_reviews": ["Great product!", "Really useful."],
            "product_ratings": "4.5",
            "product_availability": "In stock"
        }

    def test_cache_data(self):
        cache_data(self.url, self.data)
        cached_data = get_cached_data(self.url)
        self.assertEqual(cached_data, self.data)

    def test_get_cached_data(self):
        cached_data = get_cached_data(self.url)
        self.assertEqual(cached_data, self.data)

    def test_get_cached_data_no_cache(self):
        cached_data = get_cached_data("https://example.com/non_existent_product")
        self.assertIsNone(cached_data)

if __name__ == '__main__':
    unittest.main()
```