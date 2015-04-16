import unittest

def should_pass(self):
    self.assertTrue(True)

def should_fail(self):
    self.assertTrue(False)


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

        self.test_case = type('MyTestCase', (unittest.TestCase,), methods)

    def run(self):

        # test item should be 3 length
        # assert len(self.test) == 3, 'test has incorrect number of parameters'
        # test_case = self.test_case.initialize()

        test_suite = unittest.TestLoader().loadTestsFromTestCase(self.test_case)
        result = unittest.TestResult()
        test_suite.run(result)

        for err in result.errors:
            print err
        for fail in result.failures:
            print fail
        # import pdb; pdb.set_trace()

        # self.test_case.run()


if __name__ == "__main__":
    runner = Runner({
        'site': 'uptime.is',
        'tests': [
            ('/', 'h1:text', 'Uptime and downtime with 99.9 % SLA'),
        ]
        })

    runner.build_test()
    runner.run()










