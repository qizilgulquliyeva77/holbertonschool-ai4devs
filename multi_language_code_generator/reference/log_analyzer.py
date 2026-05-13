import re

class LogAnalyzer:
    def __init__(self):
        self.log_pattern = re.compile(r'^(\S+) \S+ \S+ \[[^\]]+\] "([A-Z]+) (\S+)[^"]*" (\d{3}) (\d+|-)')

    def parse_line(self, line: str) -> dict:
        line = line.strip()
        if not line or not self.log_pattern.match(line): return None
        match = self.log_pattern.match(line)
        return {"ip": match.group(1), "method": match.group(2), "url": match.group(3), "status": int(match.group(4)), "size": 0 if match.group(5) == '-' else int(match.group(5))}

    def analyze(self, lines: list) -> dict:
        total, errors, unique_ips, url_counts = 0, 0, set(), {}
        for line in lines:
            parsed = self.parse_line(line)
            if not parsed: continue
            total += 1
            unique_ips.add(parsed["ip"])
            if parsed["status"] >= 400: errors += 1
            url_counts[parsed["url"]] = url_counts.get(parsed["url"], 0) + 1
        top_urls = [url for url, count in sorted(url_counts.items(), key=lambda x: x[1], reverse=True)[:3]]
        return {"total_requests": total, "unique_visitors": len(unique_ips), "error_rate": round((errors / total) * 100, 2) if total > 0 else 0.0, "top_3_urls": top_urls}
