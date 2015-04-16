

class SingleTest(object):

    def __init__(self, config):
        assert 'site' in config
        assert 'tests' in config

        self.site = config.get('site')
        self.test = config.get('test')

    def run(self):

        # test item should be 3 length
        assert len(self.test) == 3, 'test has incorrect number of parameters'

        # parse test case, determine action
        # spin up the runner/process
        # proceed with test
        # return results
