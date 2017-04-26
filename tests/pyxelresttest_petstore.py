import os
import os.path
import shutil
import unittest
from importlib import import_module

try:
    # Python 3
    from importlib import reload
except ImportError:
    # Python 2
    from imp import reload


class PyxelRestPetstoreTest(unittest.TestCase):
    service_process = None
    services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                             'pyxelrest',
                                             'configuration',
                                             'services.ini')
    backup_services_config_file_path = os.path.join(os.getenv('APPDATA'),
                                                    'pyxelrest',
                                                    'configuration',
                                                    'services.ini.back')

    @classmethod
    def setUpClass(cls):
        cls._add_test_config()
        reload(import_module('pyxelrestgenerator'))
        cls._add_pet()
        cls._add_order()
        cls._add_user()

    @classmethod
    def tearDownClass(cls):
        cls._add_back_initial_config()

    @classmethod
    def _add_test_config(cls):
        this_dir = os.path.abspath(os.path.dirname(__file__))
        shutil.copyfile(cls.services_config_file_path, cls.backup_services_config_file_path)
        shutil.copyfile(os.path.join(this_dir, 'pyxelresttest_petstore_services_configuration.ini'),
                        cls.services_config_file_path)

    @classmethod
    def _add_pet(cls):
        import pyxelrestgenerator
        new_pet = {
            'id': 222222,
            'category': {
                'id': 222,
                'name': 'doggy'
            },
            'name': 'canigou',
            'photoUrls': [],
            'tags': [
                {
                    'id': 1,
                    'name': 'dog'
                }
            ],
            'status': '3'
        }
        pyxelrestgenerator.petstore_test_addPet(new_pet)

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
        pyxelrestgenerator.petstore_test_placeOrder(new_order)

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
        pyxelrestgenerator.petstore_test_createUser(new_user)

    @classmethod
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_get_pet_by_id(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'category/id', 'category/name', 'name', 'photoUrls/0', 'tags/0/id', 'tags/0/name', 'status'],
            [222222, 222, 'doggy', 'canigou', None, 1, 'dog', 'sold']
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getPetById(222222), expected_result)

    def test_get_order_by_id(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [444444, 222222, 1, '2017-04-24T13:29:32.019Z', 'placed', False]
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getOrderById(444444), expected_result)

    def test_get_user_by_name(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'],
            [666666, 'JD', 'John', 'Doe', 'jdoe@petstore.com', 'azerty', '0123456789', 0]
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getUserByName('JD'), expected_result)
