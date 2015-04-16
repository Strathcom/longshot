# -*- coding: utf-8 -*-

import re


ACTION_METHOD_NAME_MAP = {
    "text": "text_is",
    "value": "value_is",
    "click": "click_navigates_to",
    "submit": "form_navigates_to",
    "source": "page_contains",
    "css": "css_{}_is",
}

METHOD_NAME_ALLOW_CHARS_REGEX = re.compile(r"[^A-Za-z0-9_]")


def generate_python_method_name(path, element_specifier, action, expected_value):
    method_name = 'test_'
    path_ = path.replace('/', '_').replace('-', '_')
    action_ = action.strip().lower()
    expected_value_ = expected_value.strip().lower()

    if action_ in ('click', 'submit'):
        expected_value_ = expected_value_.replace('/', '_').replace('-', '_')
    elif action_.startswith('css'):
        css_property = action_.split('-', 1)[1]
        action_ = ACTION_METHOD_NAME_MAP['css'].format(css_property)
    else:
        action_ = ACTION_METHOD_NAME_MAP.get(action_, action_)

    expected_value_ = METHOD_NAME_ALLOW_CHARS_REGEX.sub('', expected_value_)

    if len(expected_value_) > 40:
        expected_value_ = expected_value_[:40]

    method_name = (method_name + '_' + path_ + '_' + element_specifier + '_' +
                   action_ + '_' + expected_value_)
    method_name = method_name.strip('_')
    method_name = METHOD_NAME_ALLOW_CHARS_REGEX.sub('', method_name)

    while '__' in method_name:
        method_name = method_name.replace('__', '_')

    return method_name


if __name__ == '__main__':
    # some_action('http://google.com', '/about', 'blockquote', 'text', u'Google’s mission is to organize the world’s information and make it universally accessible and useful.')
    print generate_python_method_name('/about', 'h2 #my-element', 'text', u'Google’s mission is to organize the world’s information and make it universally accessible and useful.')
    print generate_python_method_name('/contact-us', '#main-contact-form', 'submit', '/contact-us/success/')
    print generate_python_method_name('/contact-us', '#contact-name-field', 'value', 'Testy Testerson')
    print generate_python_method_name('/', '#sidebar', 'css-height', '100px')
    print generate_python_method_name('/', '#main-slider img[0]', 'click', '/specials/')
    print generate_python_method_name('/', 'html', 'source', 'UA-12345')
