```python
import unittest
from web_scraper_api.models.product import Product

class TestProductModel(unittest.TestCase):

    def setUp(self):
        self.product = Product("Test Product", "100", "This is a test product", ["image1.jpg", "image2.jpg"])

    def test_product_name(self):
        self.assertEqual(self.product.name, "Test Product")

    def test_product_price(self):
        self.assertEqual(self.product.price, "100")

    def test_product_description(self):
        self.assertEqual(self.product.description, "This is a test product")

    def test_product_images(self):
        self.assertEqual(self.product.images, ["image1.jpg", "image2.jpg"])

if __name__ == '__main__':
    unittest.main()
```