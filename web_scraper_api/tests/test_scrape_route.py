```python
import unittest
from web_scraper_api import app
from web_scraper_api.models.product import Product

class TestScrapeRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_scrape_route(self):
        response = self.app.post('/scrape', json={
            'url': 'https://www.example.com/product-page',
            'fields': ['product_name', 'product_price'],
            'pagination': False
        })

        self.assertEqual(response.status_code, 200)

        product_data = response.get_json()
        product = Product(**product_data)

        self.assertIsInstance(product, Product)
        self.assertTrue(hasattr(product, 'product_name'))
        self.assertTrue(hasattr(product, 'product_price'))

    def test_scrape_route_with_pagination(self):
        response = self.app.post('/scrape', json={
            'url': 'https://www.example.com/product-page',
            'fields': ['product_name', 'product_price'],
            'pagination': True
        })

        self.assertEqual(response.status_code, 200)

        product_data = response.get_json()
        product = Product(**product_data)

        self.assertIsInstance(product, Product)
        self.assertTrue(hasattr(product, 'product_name'))
        self.assertTrue(hasattr(product, 'product_price'))

    def test_scrape_route_with_invalid_url(self):
        response = self.app.post('/scrape', json={
            'url': 'invalid-url',
            'fields': ['product_name', 'product_price'],
            'pagination': False
        })

        self.assertEqual(response.status_code, 400)

    def test_scrape_route_with_invalid_fields(self):
        response = self.app.post('/scrape', json={
            'url': 'https://www.example.com/product-page',
            'fields': ['invalid_field'],
            'pagination': False
        })

        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
```