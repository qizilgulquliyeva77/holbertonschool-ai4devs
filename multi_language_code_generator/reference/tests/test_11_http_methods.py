import unittest
from reference.log_analyzer import LogAnalyzer

class TestMethods(unittest.TestCase):
    def test_http_methods(self):
        # Analizatorun yalnız "GET" deyil, digər metodları da saydığını yoxlayın
        logs = [
            '1.1.1.1 - - [..] "POST" 201',
            '2.2.2.2 - - [..] "DELETE" 204',
            '3.3.3.3 - - [..] "PUT" 403'
        ]
        res = LogAnalyzer().analyze(logs)
        self.assertEqual(res["total_requests"], 3)
        self.assertEqual(res["unique_visitors"], 3)
        # 3 sorğudan 1-i xətadır (403) = 33.3%
        self.assertEqual(res["error_rate"], "33.3%")
