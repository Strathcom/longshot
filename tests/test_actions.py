import unittest

import mock

from longshot.actions import create_action, text_action


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


class TextActionTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_testcase = mock.MagicMock(**{
            'assertEqual': self.assertEqual,
            'assertIn': self.assertIn,
            'assertTrue': self.assertTrue
        })

    def test_startswith_value(self):  # FIXME: Make this less crazy
        page_text = "Hello World! This is a test."
        test_config = ('/', 'h1', '^Hello World!')
        self.mock_testcase.configure_mock(**{
            'browser.find.return_value.text.encode.return_value': page_text
        })

        text_action(self.mock_testcase, *test_config)

    def test_startswith_value_fails(self):  # FIXME: Make this less crazy
        page_text = "Hello World, this should fail."
        test_config = ('/', 'h1', '^Hello World!')
        self.mock_testcase.configure_mock(**{
            'browser.find.return_value.text.encode.return_value': page_text
        })

        with self.assertRaises(AssertionError):
            text_action(self.mock_testcase, *test_config)

    def test_contains_value(self):  # FIXME: Make this less crazy
        page_text = "Hello World! This is a test."
        test_config = ('/', 'h1', '~This')
        self.mock_testcase.configure_mock(**{
            'browser.find.return_value.text.encode.return_value': page_text
        })

        text_action(self.mock_testcase, *test_config)

    def test_contains_value_fails(self):  # FIXME: Make this less crazy
        page_text = "Hello World! This is a test."
        test_config = ('/', 'h1', '~That')
        self.mock_testcase.configure_mock(**{
            'browser.find.return_value.text.encode.return_value': page_text
        })

        with self.assertRaises(AssertionError):
            text_action(self.mock_testcase, *test_config)
