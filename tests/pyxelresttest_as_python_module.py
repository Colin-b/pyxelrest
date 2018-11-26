import unittest
import datetime


class PyxelRestAsPythonModuleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import pyxelrest
        pyxelrest.load({
            'petstore': {
                'open_api': {
                    'definition': 'http://petstore.swagger.io/v2/swagger.json'
                },
                'proxies': {
                    'http': 'http://10.22.218.80:8088',
                },
                'udf_name_prefix': '',
            }
        })

    def test_get_order_by_id(self):
        from pyxelrest import user_defined_functions
        now = datetime.datetime.utcnow()
        new_order_response = user_defined_functions.placeOrder(
            id=10,
            petId=222222,
            quantity=1,
            shipDate=now,
            status='placed',
            complete=False
        )
        del new_order_response['shipDate']  # Petstore is replying with server time...
        self.assertEqual({'id': 10, 'petId': 222222, 'quantity': 1, 'status': 'placed', 'complete': False}, new_order_response)

        get_order_response = user_defined_functions.getOrderById(10)
        del get_order_response['shipDate']  # Petstore is replying with server time...
        self.assertEqual({'id': 10, 'petId': 222222, 'quantity': 1, 'status': 'placed', 'complete': False}, get_order_response)

    def test_get_user_by_name(self):
        from pyxelrest import user_defined_functions
        new_user_response = user_defined_functions.createUser(
            id=666666,
            username='JD',
            firstName='John',
            lastName='Doe',
            email='jdoe@petstore.com',
            password='azerty',
            phone='0123456789',
            userStatus=0
        )
        if new_user_response:
            self.fail('User was not created: ' + str(new_user_response))

        self.assertEqual(user_defined_functions.getUserByName('JD'), {
            'id': 666666, 'username': 'JD', 'firstName': 'John', 'lastName': 'Doe', 'email': 'jdoe@petstore.com',
            'password': 'azerty', 'phone': '0123456789', 'userStatus': 0
        })


if __name__ == '__main__':
    unittest.main()
