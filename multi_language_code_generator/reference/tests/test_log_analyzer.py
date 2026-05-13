import unittest
import sys
import os

# Üst qovluqdakı log_analyzer modulunu oxumaq üçün path əlavə edirik
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()
        self.line_200 = '127.0.0.1 - - [10/May/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024'
        self.line_404 = '192.168.1.1 - - [10/May/2026:12:00:02 +0000] "POST /login HTTP/1.1" 404 512'

    def test_1_parse_valid(self):
        self.assertIsNotNone(self.analyzer.parse_line(self.line_200))

    def test_2_parse_empty(self):
        self.assertIsNone(self.analyzer.parse_line(""))

    def test_3_parse_malformed(self):
        self.assertIsNone(self.analyzer.parse_line("INVALID LOG FORMAT"))

    def test_4_analyze_empty(self):
        self.assertEqual(self.analyzer.analyze([])["total_requests"], 0)

    def test_5_analyze_success_rate(self):
        self.assertEqual(self.analyzer.analyze([self.line_200])["error_rate"], 0.0)

    def test_6_analyze_error_rate(self):
        self.assertEqual(self.analyzer.analyze([self.line_200, self.line_404])["error_rate"], 50.0)

    def test_7_unique_visitors(self):
        self.assertEqual(self.analyzer.analyze([self.line_200, self.line_200])["unique_visitors"], 1)

    def test_8_top_urls_content(self):
        self.assertIn("/index.html", self.analyzer.analyze([self.line_200])["top_3_urls"])

    def test_9_skip_corrupted_rows(self):
        self.assertEqual(self.analyzer.analyze(["BAD_ROW", self.line_200])["total_requests"], 1)

    def test_10_dash_size_handling(self):
        dash_line = '1.1.1.1 - - [1/Jan/2026:00:00:00 +0000] "GET / HTTP/1.1" 200 -'
        parsed = self.analyzer.parse_line(dash_line)
        self.assertEqual(parsed["size"], 0)

if __name__ == '__main__':
    unittest.main()
