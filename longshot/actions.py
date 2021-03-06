# -*- coding: utf-8 -*-


def text_action(self, path, element_specifier, expected_value):
    self.navigate(path)
    element = self.browser.find(element_specifier)

    assert element is not None, ("Could not find element for selector: " +
                                 element_specifier)

    expected_value = expected_value.encode("ascii", "ignore").lower().strip()
    actual_value = element.text.encode("ascii", "ignore").lower().strip()

    if expected_value.startswith('^'):
        expected_value = expected_value[1:]
        actual_value = actual_value[:len(expected_value)]
        self.assertEqual(expected_value, actual_value)
    elif expected_value.startswith('~'):
        expected_value = expected_value[1:]
        self.assertIn(expected_value, actual_value)
    else:
        self.assertEqual(expected_value, actual_value)


def create_action(path, element_specifier, action, expected_value):
    if action == "text":
        def _text_action_proxy(self):
            return text_action(self, path, element_specifier, expected_value)
        return _text_action_proxy
    else:
        raise ValueError("Unknown action: " + action)
