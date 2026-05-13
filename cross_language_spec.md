# Cross-Language Specification - Log Analyzer

## Algorithm
Parse Apache and Nginx web server access logs to filter and compute:
- Total processed requests
- Total unique visitor IP addresses
- Percentage error rate (HTTP statuses >= 400)
- Top 3 most requested URL paths

## Inputs
- Plain text log files containing standard Combined Log Format entries (one record per line).

## Outputs
- Standard JSON object containing calculated statistics metrics.

## Edge Cases
- Empty log file payload.
- Completely malformed log entries containing corrupted text formats.
- Logs containing missing HTTP status code numbers or broken fields.
- Extremely large request timestamps out of linear sequence.

## Test Cases
1. `log_small.txt` → Contains 100 valid requests, returns exactly 20 status errors and 12 unique visitor IPs.
2. `log_empty.txt` → Completely blank file, returns 0 total requests, 0 unique visitor IPs, and 0% error rates.
3. `log_malformed.txt` → Contains 10 fully unparseable corrupted string rows, safely ignores rows and records 0 valid operations.
4. `log_high_errors.txt` → Contains 50 requests where 45 rows have 500 Internal Server Error status, registers exactly 90% error rating.
5. `log_large_unique.txt` → Contains 500 requests all initiated from 500 distinct client machine IP paths, records exactly 500 unique visitors count.
