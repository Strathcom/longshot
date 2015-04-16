import unittest

import mock

from longshot.actions import create_action


class ActionFactoryTestCase(unittest.TestCase):

    def test_should_create_text_action(self):  # FIXME: Make this less crazy
        test_config = ('/', 'h1', 'text', 'Hello World!')
        text_action_proxy = create_action(*test_config)

        mock_testcase = mock.MagicMock(**{
            'browser.find.return_value.text.encode.return_value': test_config[3],
            'assertEqual': self.assertEqual
        })
        text_action_proxy(mock_testcase)


if __name__ == '__main__':
    unittest.main()
