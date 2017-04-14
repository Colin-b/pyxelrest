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
    def _add_back_initial_config(cls):
        shutil.move(cls.backup_services_config_file_path, cls.services_config_file_path)

    def test_get_pet_by_id(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'category/id', 'category/name', 'name', 'photoUrls/0', 'tags/0/id', 'tags/0/name', 'status'],
            [5, 5, 'mohan', 'fsdfsdf', 'test', 6, 'test1' 'available']
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getPetById(5), expected_result)

    def test_get_find_pets_by_status(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'category/id', 'category/name', 'name', 'photoUrls/0', 'photoUrls/1', 'tags/0/id', 'tags/0/name',
             'status'],
            [83236, 0, 'Dog', 'test', '', '', '', '', 'pending'],
            [2197850958, 1026515888, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '1637139451', 'swagger-codegen-python-pet-tag', 'pending'],
            [1668716411, 279308646, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '3257163665', 'swagger-codegen-python-pet-tag', 'pending'],
            [336118545, 3883828534, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '894429811', 'swagger-codegen-python-pet-tag', 'pending'],
            [1628471707, 1628471707, 'cat', 'dory', 'urlpath', '', '1628471707', 'ph2', 'pending'],
            [1628223137, 1628223138, 'cat', 'dory', 'urlpath', '', '1628223138', 'ph2', 'pending'],
            [1632125630, 1632125630, 'cat', 'dory', 'urlpath', '', '1632125630', 'ph2', 'pending'],
            [16601277, 673307616, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1', 'http://foo.bar.com/2',
             '3918898528', 'swagger-codegen-python-pet-tag', 'pending'],
            [1632030815, 1632030815, 'cat', 'dory', 'urlpath', '', '1632030815', 'ph2', 'pending'],
            [71892, 0, 'Dog', 'gywa', '', '', '', '', 'pending'],
            [1636322718, 1636322718, 'cat', 'dory', 'urlpath', '', '1636322718', 'ph2', 'pending'],
            [1851408946, 775166626, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '853855891', 'swagger-codegen-python-pet-tag', 'pending'],
            [1037951706, 988818341, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '39820777', 'swagger-codegen-python-pet-tag', 'pending'],
            [1632233853, 1632233853, 'cat', 'dory', 'urlpath', '', '1632233853', 'ph2', 'pending'],
            [1630694335, 1630694335, 'cat', 'dory', 'urlpath', '', '1630694335', 'ph2', 'pending'],
            [3892609505, 648260058, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '3794241888', 'swagger-codegen-python-pet-tag', 'pending'],
            [1631953374, 1631953374, 'cat', 'dory', 'urlpath', '', '1631953374', 'ph2', 'pending'],
            [1631907889, 1631907889, 'cat', 'dory', 'urlpath', '', '1631907889', 'ph2', 'pending'],
            [984364262, 2122072061, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '3353832304', 'swagger-codegen-python-pet-tag', 'pending'],
            [46306, None, '', 'Findus', '', '', '', '', 'pending'],
            [3953182817, 464134285, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '3470675267', 'swagger-codegen-python-pet-tag', 'pending'],
            [1635690340, 1635690340, 'cat', 'dory', 'urlpath', '', '1635690340', 'ph2', 'pending'],
            [1417150791, 2011298132, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '3017794388', 'swagger-codegen-python-pet-tag', 'pending'],
            [1632172570, 1632172570, 'cat', 'dory', 'urlpath', '', '1632172570', 'ph2', 'pending'],
            [1631973656, 1631973656, 'cat', 'dory', 'urlpath', '', '1631973656', 'ph2', 'pending'],
            [42978, None, '', 'Findus', '', '', '', '', 'pending'],
            [78143, None, '', 'Findus', '', '', '', '', 'pending'],
            [2586331430, 2434243245, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '1408491198', 'swagger-codegen-python-pet-tag', 'pending'],
            [63864, None, '', 'Findus1', '', '', '', '', 'pending'],
            [62979, 0, 'Dog', 'HÃ¥kan', '', '', '', '', 'pending'],
            [1631361353, 1631361353, 'cat', 'dory', 'urlpath', '', '1631361353', 'ph2', 'pending'],
            [1635714346, 1635714346, 'cat', 'dory', 'urlpath', '', '1635714346', 'ph2', 'pending'],
            [1566606052, 1566606052, 'cat', 'dory', 'urlpath', '', '1566606052', 'ph2', 'pending'],
            [3562576499, 416633104, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '225445839', 'swagger-codegen-python-pet-tag', 'pending'],
            [1628322954, 1628322954, 'cat', 'dory', 'urlpath', '', '1628322954', 'ph2', 'pending'],
            [1631190433, 1631190433, 'cat', 'dory', 'urlpath', '', '1631190433', 'ph2', 'pending'],
            [1634303017, 1634303017, 'cat', 'dory', 'urlpath', '', '1634303017', 'ph2', 'pending'],
            [323205814, 3472650000, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '1734020249', 'swagger-codegen-python-pet-tag', 'pending'],
            [1634351262, 1634351262, 'cat', 'dory', 'urlpath', '', '1634351262', 'ph2', 'pending'],
            [1623875878, 1623875878, 'cat', 'dory', 'urlpath', '', '1623875878', 'ph2', 'pending'],
            [29439443, 4115580439, 'dog', 'hello kity with form updated', 'http://foo.bar.com/1',
             'http://foo.bar.com/2', '851270192', 'swagger-codegen-python-pet-tag', 'pending'],
            [1567610912, 1567610912, 'cat', 'dory', 'urlpath', '', '1567610912', 'ph2', 'pending'],
            [1636352223, 1636352223, 'cat', 'dory', 'urlpath', '', '1636352223', 'ph2', 'pending'],
            [1636336072, 1636336072, 'cat', 'dory', 'urlpath', '', '1636336072', 'ph2', 'pending'],
            [1635784582, 1635784582, 'cat', 'dory', 'urlpath', '', '1635784582', 'ph2', 'pending'],
            [1639741117, 1639741117, 'cat', 'dory', 'urlpath', '', '1639741117', 'ph2', 'pending'],
            [1639768573, 1639768573, 'cat', 'dory', 'urlpath', '', '1639768573', 'ph2', 'pending'],
            [1643624124, 1643624124, 'cat', 'dory', 'urlpath', '', '1643624124', 'ph2', 'pending'],
            [1651537019, 1651537019, 'cat', 'dory', 'urlpath', '', '1651537019', 'ph2', 'pending'],
            [1652161540, 1652161540, 'cat', 'dory', 'urlpath', '', '1652161540', 'ph2', 'pending'],
            [1710098583, 1710098583, 'cat', 'dory', 'urlpath', '', '1710098583', 'ph2', 'pending'],
            [1710447784, 1710447784, 'cat', 'dory', 'urlpath', '', '1710447784', 'ph2', 'pending'],
            [1563375150, 1563375150, 'cat', 'cat', 'urlpath', '', '1563375150', 'ph2', 'pending'],
            [7, None, '', 'TEJPET', '', '', '', '', 'pending'],
            [6739257, 10, 'string', 'Changed Kitty Price', 'string', '', '10', 'string', 'pending']
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_findPetsByStatus('pending'), expected_result)

    def test_get_find_pets_by_tags(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'category/id', 'category/name', 'name', 'photoUrls/0', 'tags/0/id', 'tags/0/name', 'status'],
            [1628471707, 1628471707, 'cat', 'dory', 'urlpath', 1628471707, 'ph2', 'pending'],
            [1628223137, 1628223138, 'cat', 'dory', 'urlpath', 1628223138, 'ph2', 'pending'],
            [1632125630, 1632125630, 'cat', 'dory', 'urlpath', 1632125630, 'ph2', 'pending'],
            [1632030815, 1632030815, 'cat', 'dory', 'urlpath', 1632030815, 'ph2', 'pending'],
            [1636322718, 1636322718, 'cat', 'dory', 'urlpath', 1636322718, 'ph2', 'pending'],
            [1632233853, 1632233853, 'cat', 'dory', 'urlpath', 1632233853, 'ph2', 'pending'],
            [1630694335, 1630694335, 'cat', 'dory', 'urlpath', 1630694335, 'ph2', 'pending'],
            [1631953374, 1631953374, 'cat', 'dory', 'urlpath', 1631953374, 'ph2', 'pending'],
            [1631907889, 1631907889, 'cat', 'dory', 'urlpath', 1631907889, 'ph2', 'pending'],
            [1635690340, 1635690340, 'cat', 'dory', 'urlpath', 1635690340, 'ph2', 'pending'],
            [1632172570, 1632172570, 'cat', 'dory', 'urlpath', 1632172570, 'ph2', 'pending'],
            [1631973656, 1631973656, 'cat', 'dory', 'urlpath', 1631973656, 'ph2', 'pending'],
            [1631361353, 1631361353, 'cat', 'dory', 'urlpath', 1631361353, 'ph2', 'pending'],
            [1635714346, 1635714346, 'cat', 'dory', 'urlpath', 1635714346, 'ph2', 'pending'],
            [1566606052, 1566606052, 'cat', 'dory', 'urlpath', 1566606052, 'ph2', 'pending'],
            [1628322954, 1628322954, 'cat', 'dory', 'urlpath', 1628322954, 'ph2', 'pending'],
            [1631190433, 1631190433, 'cat', 'dory', 'urlpath', 1631190433, 'ph2', 'pending'],
            [1634303017, 1634303017, 'cat', 'dory', 'urlpath', 1634303017, 'ph2', 'pending'],
            [1634351262, 1634351262, 'cat', 'dory', 'urlpath', 1634351262, 'ph2', 'pending'],
            [1623875878, 1623875878, 'cat', 'dory', 'urlpath', 1623875878, 'ph2', 'pending'],
            [1567610912, 1567610912, 'cat', 'dory', 'urlpath', 1567610912, 'ph2', 'pending'],
            [1636352223, 1636352223, 'cat', 'dory', 'urlpath', 1636352223, 'ph2', 'pending'],
            [1636336072, 1636336072, 'cat', 'dory', 'urlpath', 1636336072, 'ph2', 'pending'],
            [1635784582, 1635784582, 'cat', 'dory', 'urlpath', 1635784582, 'ph2', 'pending'],
            [1639741117, 1639741117, 'cat', 'dory', 'urlpath', 1639741117, 'ph2', 'pending'],
            [1639768573, 1639768573, 'cat', 'dory', 'urlpath', 1639768573, 'ph2', 'pending'],
            [1643624124, 1643624124, 'cat', 'dory', 'urlpath', 1643624124, 'ph2', 'pending'],
            [1651537019, 1651537019, 'cat', 'dory', 'urlpath', 1651537019, 'ph2', 'pending'],
            [1652161540, 1652161540, 'cat', 'dory', 'urlpath', 1652161540, 'ph2', 'pending'],
            [1710098583, 1710098583, 'cat', 'dory', 'urlpath', 1710098583, 'ph2', 'pending'],
            [1710447784, 1710447784, 'cat', 'dory', 'urlpath', 1710447784, 'ph2', 'pending'],
            [1563375150, 1563375150, 'cat', 'cat', 'urlpath', 1563375150, 'ph2', 'pending']
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_findPetsByTags('pending'), expected_result)

    def test_get_user_by_name(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'username', 'firstName', 'lastName', 'email', 'password', 'phone', 'userStatus'],
            [0, 'user1', 'user1', 'user1', 'user1@user1.com', 'user123', '12345678', 0]
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getUserByName('pending'), expected_result)

    def test_get_inventory(self):
        import pyxelrestgenerator
        expected_result = [
            ['1', '200', '565656566', 'dfgfghfg', 'New', 'Done', 'placed', 'unavailable', 'stud',
             'jxl.read.biff.LabelSSTRecord@75a2fef0', 'available', 'availablxxxxe', 'Duis et minim eiusmod dolore',
             'delivered', '有效的', 'three', 'good', 'confused', 'availabl123e', 'approved', 'no more', 'asdf', 'loco',
             'ex laboris', 'wolny', 'yolo', 'test', 'non ea commodo aliqua laboris', 'testtt', 'I am doing good',
             'testing', 'available15556', 'active', 'jxl.read.biff.LabelSSTRecord@62a289c0', 'whatever', 'undesirable',
             'Active', 'in ipsum sed', 'true', 'waitlist', 'availabltryrtyrtyye', 'available}', 'aveeeailable', 'dog',
             'asdfe', ' Not available', 'nn', 'jxl.read.biff.LabelSSTRecord@3fbdd262', 'string', 'sed ullamco', 'alive',
             'Adopted', 'Yes', 'foo', 'pending', 'dangerous', 'asdasd', 'dead', 'adulto', 'gshx', 'DELETED',
             'cillum aliqua dolor est amet', 'availaaaaable', 'hungry', 'availablee',
             'jxl.read.biff.LabelSSTRecord@7aa59195', 'busy', 'mort', 'not available', 'cuty', 'avaijlable',
             'nostrud dolor co', 'jxl.read.biff.LabelSSTRecord@1d3240a9', 'sold', 'consequat non in', 'available1',
             'TG', 'fds', 'available   yes', 'unavaiable', 'u', 'painting', 'Single', 'y', 'fatima3', 'fake', 'Good',
             'fgghfgh', 'jxl.read.biff.LabelSSTRecord@5cc91926', 'Pending'],
            [4, 3, 2, 1, 1, 1, 3, 3, 1, 1, 17166, 1, 1, 3, 1, 1, 2, 2, 1, 1, 1, 3, 3, 1, 1, 1, 3, 1, 6, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 3, 1, 1, 1141, 1, 1, 1, 1, 1, 64, 1, 1, 4, 2, 1, 1, 1, 3, 1, 1, 1, 4, 2,
             1, 1, 1, 1, 1, 636, 1, 5, 2, 1, 1, 37, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2]
        ]
        produced_result = pyxelrestgenerator.petstore_test_getInventory()
        self.assertEqual(len(produced_result), len(expected_result))
        self.assertEqual(sorted(produced_result[0]), sorted(expected_result[0]))

    def test_get_order_by_id(self):
        import pyxelrestgenerator
        expected_result = [
            ['id', 'petId', 'quantity', 'shipDate', 'status', 'complete'],
            [5, 7, 45, '2017-03-16T09:05:24.882Z', 'placed', True]
        ]
        self.assertEqual(pyxelrestgenerator.petstore_test_getOrderById(5), expected_result)
