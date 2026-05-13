import unittest
from reference.log_analyzer import LogAnalyzer

class TestThreshold(unittest.TestCase):
    def test_threshold(self):
        logs = ['1.1.1.1 - - [..] "GET" 399', '2.2.2.2 - - [..] "GET" 400']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["error_rate"], "50.0%")
