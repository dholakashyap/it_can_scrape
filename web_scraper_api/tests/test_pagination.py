```python
import unittest
from web_scraper_api.utils.pagination import handle_pagination

class TestPagination(unittest.TestCase):

    def setUp(self):
        self.url = "http://example.com/products"
        self.pagination = True

    def test_handle_pagination(self):
        result = handle_pagination(self.url, self.pagination)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 1)

    def test_handle_pagination_no_pagination(self):
        self.pagination = False
        result = handle_pagination(self.url, self.pagination)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    def test_handle_pagination_invalid_url(self):
        self.url = "invalid_url"
        with self.assertRaises(ValueError):
            handle_pagination(self.url, self.pagination)

if __name__ == '__main__':
    unittest.main()
```