import unittest
import time

from testsutils import (serviceshandler, loader)


class PyxelRestCachingTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        from testsutils import caching_service
        serviceshandler.start_services((caching_service, 8949))
        loader.load('caching_services.yml')

    @classmethod
    def tearDownClass(cls):
        serviceshandler.stop_services()

    def test_get_cached(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [1, '1', '2']
            ],
            pyxelrestgenerator.caching_get_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [2, '1', '3']
            ],
            pyxelrestgenerator.caching_get_cached(test1='1', test2='3')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [1, '1', '2']
            ],
            pyxelrestgenerator.caching_get_cached(test1='1', test2='2')
        )
        time.sleep(5)
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [3, '1', '2']
            ],
            pyxelrestgenerator.caching_get_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [3, '1', '2']
            ],
            pyxelrestgenerator.caching_get_cached(test1='1', test2='2')
        )

    def test_post_cached(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [1, '1', '2']
            ],
            pyxelrestgenerator.caching_post_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [2, '1', '3']
            ],
            pyxelrestgenerator.caching_post_cached(test1='1', test2='3')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [3, '1', '2']
            ],
            pyxelrestgenerator.caching_post_cached(test1='1', test2='2')
        )
        time.sleep(5)
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [4, '1', '2']
            ],
            pyxelrestgenerator.caching_post_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [5, '1', '2']
            ],
            pyxelrestgenerator.caching_post_cached(test1='1', test2='2')
        )

    def test_put_cached(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [1, '1', '2']
            ],
            pyxelrestgenerator.caching_put_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [2, '1', '3']
            ],
            pyxelrestgenerator.caching_put_cached(test1='1', test2='3')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [3, '1', '2']
            ],
            pyxelrestgenerator.caching_put_cached(test1='1', test2='2')
        )
        time.sleep(5)
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [4, '1', '2']
            ],
            pyxelrestgenerator.caching_put_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [5, '1', '2']
            ],
            pyxelrestgenerator.caching_put_cached(test1='1', test2='2')
        )

    def test_delete_cached(self):
        from pyxelrest import pyxelrestgenerator
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [1, '1', '2']
            ],
            pyxelrestgenerator.caching_delete_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [2, '1', '3']
            ],
            pyxelrestgenerator.caching_delete_cached(test1='1', test2='3')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [3, '1', '2']
            ],
            pyxelrestgenerator.caching_delete_cached(test1='1', test2='2')
        )
        time.sleep(5)
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [4, '1', '2']
            ],
            pyxelrestgenerator.caching_delete_cached(test1='1', test2='2')
        )
        self.assertEqual(
            [
                ['request_nb', 'test1', 'test2'],
                [5, '1', '2']
            ],
            pyxelrestgenerator.caching_delete_cached(test1='1', test2='2')
        )


if __name__ == '__main__':
    unittest.main()
