from iron_cache import *
import unittest
import requests

class TestIronCache(unittest.TestCase):

    def setUp(self):
        self.cache = IronCache("test_cache")

    def test_get(self):
        self.cache.put("test_item", "testing")
        item = self.cache.get("test_item")
        self.assertEqual(item.value, "testing")
        
    def test_delete(self):
        self.cache.put("test_item", "will be deleted")
        self.cache.delete("test_item")
        self.assertRaises(requests.exceptions.HTTPError,
                self.cache.get, "test_item")

    def test_increment(self):
        self.cache.put("test_item", 2)
        self.cache.increment("test_item")
        item = self.cache.get("test_item")
        self.assertEqual(item.value, 3)
        self.cache.increment("test_item", amount=42)
        item = self.cache.get("test_item")
        self.assertEqual(item.value, 45)

    def test_decrement(self):
        self.cache.put("test_item", 100)
        self.cache.decrement("test_item")
        item = self.cache.get("test_item")
        self.assertEqual(item.value, 99)
        self.cache.decrement("test_item", amount=98)
        item = self.cache.get("test_item")
        self.assertEqual(item.value, 1)

if __name__ == '__main__':
    unittest.main()
