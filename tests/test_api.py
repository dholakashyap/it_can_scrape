```python
import unittest
import requests
from src.api import app

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_scrape_endpoint(self):
        response = self.app.post('/scrape',
                                 json={
                                     'url': 'https://www.amazon.com/dp/B07FZ8S74R/',
                                     'fields': ['Product Name', 'Product Price'],
                                     'pagination': False,
                                     'async': False
                                 })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product Name', data)
        self.assertIn('Product Price', data)

    def test_error_handling(self):
        response = self.app.post('/scrape',
                                 json={
                                     'url': 'https://www.nonexistentwebsite.com/',
                                     'fields': ['Product Name', 'Product Price'],
                                     'pagination': False,
                                     'async': False
                                 })
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_pagination(self):
        response = self.app.post('/scrape',
                                 json={
                                     'url': 'https://www.amazon.com/s?k=laptop',
                                     'fields': ['Product Name', 'Product Price'],
                                     'pagination': True,
                                     'async': False
                                 })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) > 1)

    def test_async_scraping(self):
        response = self.app.post('/scrape',
                                 json={
                                     'url': 'https://www.amazon.com/s?k=laptop',
                                     'fields': ['Product Name', 'Product Price'],
                                     'pagination': True,
                                     'async': True
                                 })
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(data) > 1)

if __name__ == "__main__":
    unittest.main()
```