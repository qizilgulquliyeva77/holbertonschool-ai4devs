import re

class LogAnalyzer:
    def __init__(self):
        # Combined Log Format üçün standart Regex şablonu
        self.log_pattern = re.compile(
            r'^(\S+) \S+ \S+ \[[^\]]+\] "([A-Z]+) (\S+)[^"]*" (\d{3}) (\d+|-)'
        )

    def parse_line(self, line: str) -> dict:
        line = line.strip()
        if not line:
            return None
        
        match = self.log_pattern.match(line)
        if not match:
            return None
            
        return {
            "ip": match.group(1),
            "method": match.group(2),
            "url": match.group(3),
            "status": int(match.group(4)),
            "size": 0 if match.group(5) == '-' else int(match.group(5))
        }

    def analyze(self, lines: list) -> dict:
        total_requests = 0
        errors = 0
        unique_ips = set()
        url_counts = {}

        for line in lines:
            parsed = self.parse_line(line)
            if not parsed:
                continue
                
            total_requests += 1
            unique_ips.add(parsed["ip"])
            
            if parsed["status"] >= 400:
                errors += 1
                
            url = parsed["url"]
            url_counts[url] = url_counts.get(url, 0) + 1

        # Ən çox sorğu alan top 3 URL-i tapırıq
        top_urls = sorted(url_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        top_urls_list = [url for url, count in top_urls]

        error_rate = 0.0
        if total_requests > 0:
            error_rate = round((errors / total_requests) * 100, 2)

        return {
            "total_requests": total_requests,
            "unique_visitors": len(unique_ips),
            "error_rate": error_rate,
            "top_3_urls": top_urls_list
        }
