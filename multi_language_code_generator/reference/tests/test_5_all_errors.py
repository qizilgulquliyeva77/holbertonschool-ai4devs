import unittest
from reference.log_analyzer import LogAnalyzer

class TestAllErrors(unittest.TestCase):
    def test_all_errors(self):
        logs = ['1.1.1.1 - - [..] "GET" 500']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["error_rate"], "100.0%")
