import unittest
from reference.log_analyzer import LogAnalyzer

class TestEmpty(unittest.TestCase):
    def test_empty(self):
        res = LogAnalyzer().analyze([])
        self.assertEqual(res["total_requests"], 0)
