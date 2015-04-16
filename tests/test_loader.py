import os
import unittest


from longshot import loader


class TestRowParsing(unittest.TestCase):

    def test_should_parse_simple_row(self):
        test = loader.parse_row('/ h2:click Welcome')
        expected = ('/', 'h2:click', 'Welcome')
        self.assertTupleEqual(test, expected)

    def test_should_parse_extra_spaces(self):
        test = loader.parse_row('/ h2:click Welcome to our site')
        expected = ('/', 'h2:click', 'Welcome to our site')
        self.assertTupleEqual(test, expected)

    def test_should_parse_handle_extra_space(self):
        test = loader.parse_row('/  h2:click  Welcome to our site ')
        expected = ('/', 'h2:click', 'Welcome to our site')
        self.assertTupleEqual(test, expected)

    def test_should_parse_handle_double_quotes_in_value(self):
        test = loader.parse_row('/ h2:click "Welcome to our site"')
        expected = ('/', 'h2:click', 'Welcome to our site')
        self.assertTupleEqual(test, expected)

    def test_should_parse_handle_lots_of_quotes(self):
        test = loader.parse_row('/ h2:click "Welcome \'\'\' "to ou"""r site"')
        expected = ('/', 'h2:click', 'Welcome to our site')
        self.assertTupleEqual(test, expected)


class TestLoader(unittest.TestCase):

    def test_should_parse_config(self):
        path = os.path.join(os.path.dirname(__file__), 'data/test_site.txt')
        config = loader.parse(path)
        expected = {
            'site': 'www.strathcom.ca',
            'tests': {
                '/': [{
                    'expression': 'h2:text',
                    'value': 'One Dealer Platform: Unlimited Potential'
                }]
            }
        }

        self.assertDictEqual(config, expected)

    def test_should_complain_if_site_missing(self):
        path = os.path.join(os.path.dirname(__file__), 'data/bad_file.txt')
        self.assertRaises(AssertionError, loader.parse, (path))
