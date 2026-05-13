import unittest
from reference.log_analyzer import LogAnalyzer

class TestMalformed(unittest.TestCase):
    def test_malformed(self):
        res = LogAnalyzer().analyze(["bad_data_line"])
        self.assertEqual(res["total_requests"], 0)
