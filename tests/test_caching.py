```python
import unittest
from src.caching import Caching

class TestCaching(unittest.TestCase):

    def setUp(self):
        self.cache = Caching()

    def test_cache_insertion(self):
        self.cache.insert('test_url', 'test_data')
        self.assertEqual(self.cache.get('test_url'), 'test_data')

    def test_cache_retrieval(self):
        self.cache.insert('test_url', 'test_data')
        self.assertEqual(self.cache.get('test_url'), 'test_data')

    def test_cache_removal(self):
        self.cache.insert('test_url', 'test_data')
        self.cache.remove('test_url')
        self.assertIsNone(self.cache.get('test_url'))

    def test_cache_clear(self):
        self.cache.insert('test_url', 'test_data')
        self.cache.clear()
        self.assertIsNone(self.cache.get('test_url'))

if __name__ == '__main__':
    unittest.main()
```