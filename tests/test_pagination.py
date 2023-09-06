```python
import unittest
from src.pagination import handle_pagination

class TestPagination(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.example.com/products"
        self.pagination = True

    def test_handle_pagination(self):
        result = handle_pagination(self.url, self.pagination)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 1)

    def test_handle_pagination_no_pagination(self):
        result = handle_pagination(self.url, False)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 1)

    def test_handle_pagination_invalid_url(self):
        with self.assertRaises(ValueError):
            handle_pagination("invalid_url", self.pagination)

if __name__ == '__main__':
    unittest.main()
```