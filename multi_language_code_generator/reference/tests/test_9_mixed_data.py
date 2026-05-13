import unittest
from reference.log_analyzer import LogAnalyzer

class TestMixed(unittest.TestCase):
    def test_mixed(self):
        logs = ['1.1.1.1 - - [..] "GET" 200', 'invalid data']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 1)
