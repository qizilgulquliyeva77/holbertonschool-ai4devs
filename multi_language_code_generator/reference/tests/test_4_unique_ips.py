import unittest
from reference.log_analyzer import LogAnalyzer

class TestUnique(unittest.TestCase):
    def test_unique(self):
        logs = ['1.1.1.1 - - [..] "GET" 200', '1.1.1.1 - - [..] "GET" 200']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["unique_visitors"], 1)
