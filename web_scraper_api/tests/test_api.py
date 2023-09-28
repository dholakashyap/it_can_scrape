```python
import unittest
import json
from web_scraper_api import api

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()
        self.app.testing = True

    def test_scrape_product_data(self):
        response = self.app.post('/scrape', data=json.dumps(dict(url='https://www.amazon.com/dp/B07FZ8S74R/')), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 200)
        self.assertIn('product_name', data)
        self.assertIn('price', data)
        self.assertIn('description', data)
        self.assertIn('product_images', data)

    def test_invalid_url(self):
        response = self.app.post('/scrape', data=json.dumps(dict(url='invalid_url')), content_type='application/json')
        data = json.loads(response.get_data(as_text=True))

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == "__main__":
    unittest.main()
```