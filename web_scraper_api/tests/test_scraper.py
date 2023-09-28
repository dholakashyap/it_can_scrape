```python
import unittest
from web_scraper_api.scraper import scrape_product_data

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.valid_url = "https://www.amazon.com/dp/B08N5WRWNW"
        self.invalid_url = "https://www.invalidurl.com"

    def test_scraper_valid_url(self):
        result = scrape_product_data(self.valid_url)
        self.assertIsInstance(result, dict)
        self.assertIn('product_name', result)
        self.assertIn('price', result)
        self.assertIn('description', result)
        self.assertIn('product_images', result)

    def test_scraper_invalid_url(self):
        with self.assertRaises(Exception):
            scrape_product_data(self.invalid_url)

if __name__ == '__main__':
    unittest.main()
```