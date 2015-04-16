import unittest

import mock

from longshot.actions import create_action


class ActionFactoryTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_testcase = mock.MagicMock(**{
            'assertEqual': self.assertEqual,
            'assertIn': self.assertIn,
            'assertTrue': self.assertTrue
        })

    def test_should_create_text_action(self):  # FIXME: Make this less crazy
        test_config = ('/', 'h1', 'text', 'Hello World!')
        self.mock_testcase.configure_mock(**{
            'browser.find.return_value.text.encode.return_value': test_config[3]
        })

        text_action_proxy = create_action(*test_config)
        text_action_proxy(self.mock_testcase)

    def test_should_throw_error_if_unknown_action(self):
        test_config = ('/', 'h1', 'INVALID-VALUE-IS-HERE', 'Hello World!')

        with self.assertRaises(ValueError):
            create_action(*test_config)

