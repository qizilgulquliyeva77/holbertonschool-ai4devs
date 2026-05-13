import unittest
from reference.log_analyzer import LogAnalyzer

class TestMultiple(unittest.TestCase):
    def test_multiple(self):
        logs = ['1.1.1.1 - - [..] "GET" 200', '2.2.2.2 - - [..] "GET" 200']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["unique_visitors"], 2)
