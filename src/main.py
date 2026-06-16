from fetcher.client import fetch_page
from parser.html_parser import parse_html
from checks.title_check import check_title
from checks.meta_check import check_meta_description
from checks.h1_check import check_h1
from checks.canonical_check import check_canonical
from checks.og_check import check_open_graph

url = "https://example.com"

html = fetch_page(url)
soup = parse_html(html)

issues = []

issues.extend(check_title(soup))
issues.extend(check_meta_description(soup))
issues.extend(check_h1(soup))
issues.extend(check_canonical(soup))
issues.extend(check_open_graph(soup))

for issue in issues:
    print(f"[{issue.severity}] {issue.message}")
