```python
import unittest
from web_scraper_api.utils.error_handling import handle_error

class TestErrorHandling(unittest.TestCase):

    def setUp(self):
        self.error_message = "An error occurred"
        self.error_code = 500

    def test_handle_error(self):
        try:
            raise Exception(self.error_message)
        except Exception as e:
            error_response = handle_error(e, self.error_code)
            self.assertEqual(error_response.status_code, self.error_code)
            self.assertEqual(error_response.json['error'], self.error_message)

if __name__ == '__main__':
    unittest.main()
```