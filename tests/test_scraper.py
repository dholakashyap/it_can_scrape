```python
import unittest
from src.scraper import Scraper

class TestScraper(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()

    def test_extract_product_name(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_product_name(url)
        self.assertIsNotNone(result)

    def test_extract_product_price(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_product_price(url)
        self.assertIsNotNone(result)

    def test_extract_product_description(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_product_description(url)
        self.assertIsNotNone(result)

    def test_extract_customer_reviews(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_customer_reviews(url)
        self.assertIsNotNone(result)

    def test_extract_product_ratings(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_product_ratings(url)
        self.assertIsNotNone(result)

    def test_extract_product_availability(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_product_availability(url)
        self.assertIsNotNone(result)

    def test_extract_product_images(self):
        url = "https://www.amazon.com/dp/B08N5WRWNW"
        result = self.scraper.extract_product_images(url)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```