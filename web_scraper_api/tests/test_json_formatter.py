```python
import unittest
import json
from web_scraper_api.utils.json_formatter import format_to_json
from web_scraper_api.models.product import Product

class TestJsonFormatter(unittest.TestCase):
    def setUp(self):
        self.product = Product(
            name="Test Product",
            price="100",
            description="This is a test product",
            images=["http://test.com/image1.jpg", "http://test.com/image2.jpg"]
        )

    def test_format_to_json(self):
        expected_json = json.dumps({
            "name": "Test Product",
            "price": "100",
            "description": "This is a test product",
            "images": ["http://test.com/image1.jpg", "http://test.com/image2.jpg"]
        })

        result = format_to_json(self.product)
        self.assertEqual(result, expected_json)

if __name__ == '__main__':
    unittest.main()
```