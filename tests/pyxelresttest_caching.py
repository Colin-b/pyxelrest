import unittest
import os
import time


class PyxelRestAuthenticationTest(unittest.TestCase):
    mod = 0

    def test_no_caching(self):
        from caching import caching, init_nothing
        init_nothing()

        @caching
        def toto1(x):
            return x * x + self.mod

        self.mod = 0
        self.assertEqual(toto1(2), 4)
        self.mod = 1
        self.assertEqual(toto1(2), 5)

    def test_lru_caching(self):
        from caching import caching, init_lru
        init_lru(5, 1)

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

    def test_dbm_caching(self):
        from caching import caching, init_dbm
        os.remove("c:\\tmp\\cache.dbm")
        init_dbm("c:\\tmp\\cache.dbm")

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
