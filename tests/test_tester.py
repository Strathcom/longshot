import unittest
from longshot import tester


class TestTester(unittest.TestCase):

    def test_should_load_config_param(self):
        config = {
            'site': 'foo',
            'tests': ''
        }
        test = tester.SingleTest(config)
        self.assertEqual(test.site, config['site'])

    def test_should_complain_with_missing_site(self):
        config = {
            'tests': ''
        }
        self.assertRaises(AssertionError, tester.SingleTest, (config))

    def test_should_complain_with_missing_tests(self):
        config = {
            'site': ''
        }
        self.assertRaises(AssertionError, tester.SingleTest, (config))
