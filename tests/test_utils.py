# -*- coding: utf-8 -*-

import unittest

from longshot.utils import generate_python_method_name


class GeneratePythonMethodNameTestCase(unittest.TestCase):

    def test_should_generate_expected_method_names(self):
        test_samples = [
            {'args': ('/about', 'h2 #my-element', 'text', u'Google’s mission is to organize the world’s information and make it universally accessible and useful.'),
             'expected_value': 'test_about_h2myelement_text_is_googlesmissionistoorganizetheworldsinfor'},
            {'args': ('/contact-us', '#main-contact-form', 'submit', '/contact-us/success/'),
             'expected_value': 'test_contact_us_maincontactform_submit_contact_us_success'},
            {'args': ('/contact-us', '#contact-name-field', 'value', 'Testy Testerson'),
             'expected_value': 'test_contact_us_contactnamefield_value_is_testytesterson'},
            {'args': ('/', '#sidebar', 'css-height', '100px'),
             'expected_value': 'test_sidebar_css_height_is_100px'},
            {'args': ('/', '#main-slider img[0]', 'click', '/specials/'),
             'expected_value': 'test_mainsliderimg0_click_specials'},
            {'args': ('/', 'html', 'source', 'UA-12345'),
             'expected_value': 'test_html_page_contains_ua12345'},
        ]

        for sample in test_samples:
            actual_value = generate_python_method_name(*sample['args'])
            self.assertEqual(actual_value, sample['expected_value'])


if __name__ == '__main__':
    unittest.main()
