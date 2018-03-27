import unittest
import datetime
from dateutil.tz import tzutc
import testsutils.loader as loader


class PyxelRestPetstoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader.load('pyxelresttest_petstore_services_configuration.ini')

    @classmethod
    def tearDownClass(cls):
        loader.unload()

    def test_get_order_by_id(self):
        from pyxelrest import pyxelrestgenerator
        new_order_response = pyxelrestgenerator.petstore_placeOrder({
            'id': 444444,
            'petId': 222222,
            'quantity': 1,
            'shipDate': '2017-04-24T13:29:32.019Z',
            'status': 'placed',
            'complete': False
        })
        if new_order_response != [
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, datetime.datetime(2017, 4, 24, 13, 29, 32, 19000, tzinfo=tzutc()), 'placed', False]
        ]:
            self.fail('Order was not placed: ' + str(new_order_response))

        self.assertEqual(pyxelrestgenerator.petstore_getOrderById(444444), [
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, datetime.datetime(2017, 4, 24, 13, 29, 32, 19000, tzinfo=tzutc()), 'placed', False]
        ])

    def test_get_user_by_name(self):
        from pyxelrest import pyxelrestgenerator
        new_user_response = pyxelrestgenerator.petstore_createUser({
            'id': 666666,
            'username': 'JD',
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'jdoe@petstore.com',
            'password': 'azerty',
            'phone': '0123456789',
            'userStatus': 0
        })
        if new_user_response != [['']]:
            self.fail('User was not created: ' + str(new_user_response))

        self.assertEqual(pyxelrestgenerator.petstore_getUserByName('JD'), [
            ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'],
            [666666, 'JD', 'John', 'Doe', 'jdoe@petstore.com', 'azerty', '0123456789', 0]
        ])

    def test_proxy(self):
        from pyxelrest import pyxelrestgenerator
        self.assertIsNotNone(pyxelrestgenerator.proxy_createUser)

    def test_proxies(self):
        from pyxelrest import pyxelrestgenerator
        self.assertIsNotNone(pyxelrestgenerator.proxies_createUser)


if __name__ == '__main__':
    unittest.main()
