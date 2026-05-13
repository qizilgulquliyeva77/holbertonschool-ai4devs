import unittest
from multi_language_code_generator.reference.log_analyzer import LogAnalyzer

class TestLogAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = LogAnalyzer()
        # Testlər üçün istifadə ediləcək nümunə log sətirləri
        self.valid_line_200 = '127.0.0.1 - - [10/May/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 1024'
        self.valid_line_404 = '192.168.1.1 - - [10/May/2026:12:00:02 +0000] "POST /login HTTP/1.1" 404 512'
        self.valid_line_500 = '10.0.0.5 - - [10/May/2026:12:00:03 +0000] "GET /api/v1/data HTTP/1.1" 500 256'

    def test_1_parse_valid_line(self):
        parsed = self.analyzer.parse_line(self.valid_line_200)
        self.assertIsNotNone(parsed)
        self.assertEqual(parsed["ip"], "127.0.0.1")
        self.assertEqual(parsed["status"], 200)
        self.assertEqual(parsed["url"], "/index.html")

    def test_2_parse_empty_line(self):
        self.assertIsNone(self.analyzer.parse_line(""))
        self.assertIsNone(self.analyzer.parse_line("   "))

    def test_3_parse_malformed_line(self):
        self.assertIsNone(self.analyzer.parse_line("INVALID LOG LINE STRING"))

    def test_4_analyze_empty_list(self):
        result = self.analyzer.analyze([])
        self.assertEqual(result["total_requests"], 0)
        self.assertEqual(result["unique_visitors"], 0)
        self.assertEqual(result["error_rate"], 0.0)
        self.assertEqual(result["top_3_urls"], [])

    def test_5_analyze_all_successful(self):
        lines = [self.valid_line_200, self.valid_line_200]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 2)
        self.assertEqual(result["error_rate"], 0.0)

    def test_6_analyze_with_errors(self):
        lines = [self.valid_line_200, self.valid_line_404, self.valid_line_500]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 3)
        self.assertEqual(result["error_rate"], 66.67)

    def test_7_unique_visitors_count(self):
        # Eyni IP-dən gələn fərqli sorğular
        lines = [self.valid_line_200, self.valid_line_200, self.valid_line_404]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["unique_visitors"], 2) # 127.0.0.1 və 192.168.1.1

    def test_8_top_3_urls_filtering(self):
        lines = [
            self.valid_line_200, self.valid_line_200, # /index.html (2 dəfə)
            self.valid_line_404,                      # /login (1 dəfə)
            self.valid_line_500                       # /api/v1/data (1 dəfə)
        ]
        result = self.analyzer.analyze(lines)
        self.assertIn("/index.html", result["top_3_urls"])
        self.assertEqual(result["top_3_urls"][0], "/index.html")

    def test_9_mixed_malformed_and_valid(self):
        lines = ["CORRUPTED ROW", self.valid_line_200, "ANOTHER BAD ROW"]
        result = self.analyzer.analyze(lines)
        self.assertEqual(result["total_requests"], 1)

    def test_10_missing_size_dash_handling(self):
        dash_size_line = '127.0.0.1 - - [10/May/2026:12:00:01 +0000] "GET /index.html HTTP/1.1" 200 -'
        parsed = self.analyzer.parse_line(dash_size_line)
        self.assertEqual(parsed["size"], 0)

if __name__ == '__main__':
    unittest.main()
