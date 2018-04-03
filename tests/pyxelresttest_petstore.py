import unittest
import datetime

from testsutils import loader


class PyxelRestPetstoreTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        loader.load('petstore_services.yml')

    def test_get_order_by_id(self):
        from pyxelrest import pyxelrestgenerator
        now = datetime.datetime.utcnow()
        new_order_response = pyxelrestgenerator.petstore_placeOrder(
            id=444444,
            petId=222222,
            quantity=1,
            shipDate=now,
            status='placed',
            complete=False
        )
        # Petstore is replying with server time...
        del new_order_response[1][3]
        self.assertEqual([
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, 'placed', False]
        ], new_order_response)

        get_order_response = pyxelrestgenerator.petstore_getOrderById(444444)
        # Petstore is replying with server time...
        del get_order_response[1][3]
        self.assertEqual([
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, 'placed', False]
        ], get_order_response)

    def test_get_user_by_name(self):
        from pyxelrest import pyxelrestgenerator
        new_user_response = pyxelrestgenerator.petstore_createUser(
            id=666666,
            username='JD',
            firstName='John',
            lastName='Doe',
            email='jdoe@petstore.com',
            password='azerty',
            phone='0123456789',
            userStatus=0
        )
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
