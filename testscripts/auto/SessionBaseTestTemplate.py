from scripts.auto.SessionBase import SessionBase
import unittest


class SessionBaseTestTemplate(unittest.TestCase):
    def setUp(self):
        self.obj = SessionBase()

    def runTest(self):
        self.obj.read_config()
        self.obj.try_login()

    def tearDown(self):
        assert True, 'accept'
