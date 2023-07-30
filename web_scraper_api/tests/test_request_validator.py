```python
import unittest
from web_scraper_api.utils.request_validator import validate_request

class TestRequestValidator(unittest.TestCase):

    def setUp(self):
        self.valid_url = "https://www.amazon.com/product"
        self.invalid_url = "not a url"

    def test_validate_request_with_valid_url(self):
        result = validate_request(self.valid_url)
        self.assertTrue(result)

    def test_validate_request_with_invalid_url(self):
        with self.assertRaises(ValueError):
            validate_request(self.invalid_url)

if __name__ == '__main__':
    unittest.main()
```