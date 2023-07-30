```python
import asyncio
import unittest
from web_scraper_api.utils.async_scraping import async_scrape

class TestAsyncScraping(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.example.com"
        self.fields = ["product_name", "product_price", "product_description"]
        self.pagination = True

    def test_async_scrape(self):
        loop = asyncio.get_event_loop()
        result = loop.run_until_complete(async_scrape(self.url, self.fields, self.pagination))
        self.assertIsInstance(result, dict)
        self.assertIn('product_name', result)
        self.assertIn('product_price', result)
        self.assertIn('product_description', result)

if __name__ == '__main__':
    unittest.main()
```