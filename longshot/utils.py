# -*- coding: utf-8 -*-

import re
import urlparse


ACTION_METHOD_NAME_MAP = {
    "text": "text_is",
    "value": "value_is",
    "click": "click_navigates_to",
    "submit": "form_navigates_to",
    "source": "page_contains",
    "css": "css_{}_is",
}

METHOD_NAME_ALLOW_CHARS_REGEX = re.compile(r"[^A-Za-z0-9_]")


def generate_test_method_name(path, element_specifier, action, expected_value):
    generated_name = 'test_'
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

    generated_name = (generated_name + '_' + path_ + '_' + element_specifier +
                      '_' + action_ + '_' + expected_value_)
    generated_name = generated_name.strip('_')
    generated_name = METHOD_NAME_ALLOW_CHARS_REGEX.sub('', generated_name)

    while '__' in generated_name:
        generated_name = generated_name.replace('__', '_')

    return generated_name


def generate_test_class_name(site_url):
    site_url = urlparse.urlparse(site_url)

    assert site_url.hostname is not None

    generated_name = ''

    for hostname_part in site_url.hostname.split('.'):
        generated_name += hostname_part.capitalize()

    generated_name += 'TestCase'

    if generated_name[0].isdigit():
        generated_name = 'Site' + generated_name

    return generated_name
