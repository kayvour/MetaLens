from fetcher.client import fetch_page
from parser.html_parser import parse_html
from checks.title_check import check_title

url = "https://example.com"

html = fetch_page(url)
soup = parse_html(html)

issues = check_title(soup)

for issue in issues:
    print(f"[{issue.severity}] {issue.message}")
