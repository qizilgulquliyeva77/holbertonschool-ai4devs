import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log_analyzer import LogAnalyzer

class TestReferenceImplementation(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()
        self.line_200 = '127.0.0.1 - - [10/May/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024'
        self.line_404 = '192.168.1.1 - - [10/May/2026:12:00:02 +0000] "POST /login HTTP/1.1" 404 512'

    def test_one(self):
        self.assertIsNotNone(self.analyzer.parse_line(self.line_200))

    def test_two(self):
        self.assertIsNone(self.analyzer.parse_line(""))

    def test_three(self):
        self.assertIsNone(self.analyzer.parse_line("INVALID ROW FORMAT"))

    def test_four(self):
        self.assertEqual(self.analyzer.analyze([])["total_requests"], 0)

    def test_five(self):
        self.assertEqual(self.analyzer.analyze([self.line_200])["error_rate"], 0.0)

    def test_six(self):
        self.assertEqual(self.analyzer.analyze([self.line_200, self.line_404])["error_rate"], 50.0)

    def test_seven(self):
        self.assertEqual(self.analyzer.analyze([self.line_200, self.line_200])["unique_visitors"], 1)

    def test_eight(self):
        self.assertIn("/index.html", self.analyzer.analyze([self.line_200])["top_3_urls"])

    def test_nine(self):
        self.assertEqual(self.analyzer.analyze(["CORRUPTED", self.line_200])["total_requests"], 1)

    def test_ten(self):
        dash_line = '1.1.1.1 - - [1/Jan/2026:00:00:00 +0000] "GET / HTTP/1.1" 200 -'
        self.assertEqual(self.analyzer.parse_line(dash_line)["size"], 0)

if __name__ == '__main__':
    unittest.main()
