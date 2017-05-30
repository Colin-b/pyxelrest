import unittest
import testsutils.serviceshandler as serviceshandler
import testsutils.loader as loader


class PyxelRestVBAKeywordsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import testsutils.vba_keywords_test_service as vba_keywords_test_service
        serviceshandler.start_services((vba_keywords_test_service, 8949))
        loader.load('pyxelresttest_vba_keywords_services_configuration.ini')

    @classmethod
    def tearDownClass(cls):
        loader.unload()
        serviceshandler.stop_services()

    def test_vba_restricted_keywords(self):
        import pyxelrestgenerator
        self.assertEqual(
            [['currency', 'end', 'type'], ['currency value', 'end value', 'type value']],
            pyxelrestgenerator.vba_keywords_test_get_test_vba_restricted_keywords(
                currency_visual_basic='currency value',
                end_visual_basic='end value',
                type_visual_basic='type value'
            )
        )
