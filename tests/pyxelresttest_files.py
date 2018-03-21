import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader
import tempfile
import os.path


class PyxelRestTestFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_services()
        loader.load('pyxelresttest_files_services_configuration.ini')

    @classmethod
    def tearDownClass(cls):
        loader.unload()
        serviceshandler.stop_services()

    @classmethod
    def start_services(cls):
        from testsutils import (
            files_test_service,
        )
        serviceshandler.start_services(
            (files_test_service, 8959),
        )

    def test_files_parameter(self):
        from pyxelrest import pyxelrestgenerator
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'temp_file'), 'wb') as temp_file:
                temp_file.write(b'This is the content of the temporary file.')

            self.assertEqual(pyxelrestgenerator.files_test_post_test_files(
                mandatory_file='This is the content of the mandatory file.',
                optional_file=temp_file.name
            ),
                [
                    ['mandatory_file', 'optional_file'],
                    ['This is the content of the mandatory file.', 'This is the content of the temporary file.']
                ]
            )


if __name__ == '__main__':
    unittest.main()
