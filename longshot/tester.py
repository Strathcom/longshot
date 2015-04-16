import unittest
import os

from urlparse import urljoin
from webdriverplus import WebDriver

from longshot.actions import create_action
from longshot.utils import generate_test_class_name, \
    generate_test_method_name


def should_pass(self):
    self.assertTrue(True)


def should_fail(self):
    self.assertTrue(False)


class BaseSiteTestCase(unittest.TestCase):
    SITE_URL = None
    browser = None

    @classmethod
    def setUpClass(cls):
        driver_name = os.environ.get("SELENIUM_DRIVER", "firefox")
        cls.browser = WebDriver(driver_name, reuse_browser=True)
        cls.browser.maximize_window()
        cls.browser = cls.browser.get(cls.SITE_URL)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def navigate(self, path):
        full_url = urljoin(self.SITE_URL, path)

        if full_url != self.browser.current_url:
            self.browser.get(full_url)



class Runner(object):

    def __init__(self, config):
        assert 'site' in config
        assert 'tests' in config

        self.site = config.get('site')
        self.tests = config.get('tests')
        self.test_case = None

    def build_test(self):

        class_name = generate_test_class_name(self.site)
        members = {'SITE_URL': self.site}

        for test in self.tests:
            path, element_specifier, action, expected_value = test
            method_name = generate_test_method_name(path, element_specifier,
                                                    action, expected_value)
            assert method_name not in members, (method_name + " already exists "
                                                "-- duplicate test?")
            test_method = create_action(path, element_specifier, action,
                                        expected_value)
            members[method_name] = test_method

        self.test_case = type(class_name, (BaseSiteTestCase,), members)

    def run(self):

        self.build_test()

        test_suite = unittest.TestLoader().loadTestsFromTestCase(self.test_case)
        result = unittest.TestResult()
        test_suite.run(result)

        for err in result.errors:
            print err
        for fail in result.failures:
            print fail

        # TODO: better output
        # import pdb; pdb.set_trace()

        # self.test_case.run()


def run(config):
    runner = Runner(config)
    return runner.run()


if __name__ == "__main__":
    runner = Runner({
        'site': 'http://uptime.is',
        'tests': [
            ('/', 'h1', 'text', 'Uptime and downtime with 99.9 % SLxxxA'),
        ]
    })

    runner.run()
