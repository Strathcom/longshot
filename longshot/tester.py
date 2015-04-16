import unittest

from urlparse import urljoin
from webdriverplus import WebDriver


def should_pass(self):
    self.assertTrue(True)


def should_fail(self):
    self.assertTrue(False)


class BaseSiteTestCase(unittest.TestCase):
    SITE_URL = None

    @classmethod
    def setUpClass(cls):
        cls.browser = WebDriver().get(cls.SITE_URL)

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

    def build_test(self):

        methods = {
            'test_should_pass': should_pass,
            'test_should_fail': should_fail,
        }

        self.test_case = type('MyTestCase', (BaseSiteTestCase,), methods)

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
        'site': 'uptime.is',
        'tests': [
            ('/', 'h1:text', 'Uptime and downtime with 99.9 % SLA'),
        ]
        })

    runner.run()
