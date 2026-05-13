import unittest
from reference.log_analyzer import LogAnalyzer

class TestNoErrors(unittest.TestCase):
    def test_no_errors(self):
        logs = ['1.1.1.1 - - [..] "GET" 200']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["error_rate"], "0.0%")
