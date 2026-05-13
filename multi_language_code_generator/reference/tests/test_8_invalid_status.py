import unittest
from reference.log_analyzer import LogAnalyzer

class TestInvalidStatus(unittest.TestCase):
    def test_invalid_status(self):
        logs = ['1.1.1.1 - - [..] "GET" invalid']
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 0)
