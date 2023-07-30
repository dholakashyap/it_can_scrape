```python
import unittest
from web_scraper_api.scraper import scrape

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.example.com/product-page"
        self.fields = ["product_name", "product_price", "product_description", "customer_reviews", "product_ratings", "product_availability"]

    def test_scrape(self):
        result = scrape(self.url, self.fields)
        self.assertIsInstance(result, dict)
        self.assertIn('product_name', result)
        self.assertIn('product_price', result)
        self.assertIn('product_description', result)
        self.assertIn('customer_reviews', result)
        self.assertIn('product_ratings', result)
        self.assertIn('product_availability', result)

    def test_scrape_with_invalid_url(self):
        with self.assertRaises(ValueError):
            scrape("invalid_url", self.fields)

    def test_scrape_with_invalid_fields(self):
        with self.assertRaises(ValueError):
            scrape(self.url, ["invalid_field"])

if __name__ == '__main__':
    unittest.main()
```