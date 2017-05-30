import unittest
import datetime
from dateutil.tz import tzutc
import testsutils.loader as loader


class PyxelRestPetstoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader.load('pyxelresttest_petstore_services_configuration.ini')
        cls._add_order()
        cls._add_user()

    @classmethod
    def tearDownClass(cls):
        loader.unload()

    @classmethod
    def _add_order(cls):
        import pyxelrestgenerator
        new_order = {
            'id': 444444,
            'petId': 222222,
            'quantity': 1,
            'shipDate': '2017-04-24T13:29:32.019Z',
            'status': 'placed',
            'complete': False
        }
        order_response = pyxelrestgenerator.petstore_test_placeOrder(new_order)
        if order_response != [
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, datetime.datetime(2017, 4, 24, 13, 29, 32, 19000, tzinfo=tzutc()), 'placed', False]
        ]:
            loader.unload()
            raise Exception('Order was not placed: ' + str(order_response))

    @classmethod
    def _add_user(cls):
        import pyxelrestgenerator
        new_user = {
            'id': 666666,
            'username': 'JD',
            'firstName': 'John',
            'lastName': 'Doe',
            'email': 'jdoe@petstore.com',
            'password': 'azerty',
            'phone': '0123456789',
            'userStatus': 0
        }
        user_response = pyxelrestgenerator.petstore_test_createUser(new_user)
        if user_response != [['']]:
            loader.unload()
            raise Exception('User was not created: ' + str(user_response))

    def test_get_order_by_id(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, datetime.datetime(2017, 4, 24, 13, 29, 32, 19000, tzinfo=tzutc()), 'placed', False]
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getOrderById(444444), expected_result)

    def test_get_user_by_name(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'],
            [666666, 'JD', 'John', 'Doe', 'jdoe@petstore.com', 'azerty', '0123456789', 0]
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getUserByName('JD'), expected_result)
