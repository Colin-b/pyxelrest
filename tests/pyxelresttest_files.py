import os.path
import tempfile
import unittest

from testsutils import (serviceshandler, loader)


class PyxelRestTestFiles(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.start_services()
        loader.load('files_services.yml')

    @classmethod
    def tearDownClass(cls):
        serviceshandler.stop_services()

    @classmethod
    def start_services(cls):
        from testsutils import (
            files_service,
        )
        serviceshandler.start_services(
            (files_service, 8959),
        )

    def test_files_parameter(self):
        from pyxelrest import pyxelrestgenerator
        with tempfile.TemporaryDirectory() as temp_dir:
            with open(os.path.join(temp_dir, 'temp_file'), 'wb') as temp_file:
                temp_file.write(b'This is the content of the temporary file.')

            self.assertEqual(pyxelrestgenerator.files_post_files(
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
