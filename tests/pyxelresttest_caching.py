import unittest
import os
import time


class PyxelRestCacheTest(unittest.TestCase):
    mod = 0

    def test_no_caching(self):
        from pyxelrest.caching import caching, no_cache
        no_cache()

        @caching
        def toto1(x):
            return x * x + self.mod

        self.mod = 0
        self.assertEqual(toto1(2), 4)
        self.mod = 1
        self.assertEqual(toto1(2), 5)

    def test_lru_caching(self):
        from pyxelrest.caching import caching, init_memory_cache
        init_memory_cache(5, 1)

        @caching
        def toto2(x):
            return x * x + self.mod

        self.mod = 0
        self.assertEqual(toto2(2), 4)
        # cache effect
        self.mod = 1
        self.assertEqual(toto2(2), 4)
        # cache expired
        time.sleep(2)
        self.assertEqual(toto2(2), 5)

    def test_disk_caching(self):
        from pyxelrest.caching import caching, init_disk_cache
        filename = "c:\\tmp\\cache.shelve"
        if os.path.exists(filename):
            os.remove(filename)
        init_disk_cache(filename)

        @caching
        def toto3(x):
            return x * x + self.mod

        self.mod = 0
        self.assertEqual(toto3(2), 4)
        # cache effect
        self.mod = 1
        self.assertEqual(toto3(2), 4)

if __name__ == '__main__':
    unittest.main()
