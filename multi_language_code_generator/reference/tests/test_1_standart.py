import unittest
from reference.log_analyzer import LogAnalyzer

class TestStandard(unittest.TestCase):
    def test_standard(self):
        logs = ['1.1.1.1 - - [..] "GET" 200', '2.2.2.2 - - [..] "GET" 404']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 2)
