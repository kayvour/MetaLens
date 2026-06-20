from fetcher.client import fetch_page
from parser.html_parser import parse_html

from checks.title_check import check_title
from checks.meta_check import check_meta_description
from checks.h1_check import check_h1
from checks.canonical_check import check_canonical
from checks.og_check import check_open_graph
from checks.alt_check import check_alt_text
from checks.link_check import check_links

from scoring.score_engine import calculate_score
from reporting.json_report import generate_json_report

url = input("Enter URL to audit: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

html = fetch_page(url)
soup = parse_html(html)

issues = []

issues.extend(check_title(soup))
issues.extend(check_meta_description(soup))
issues.extend(check_h1(soup))
issues.extend(check_canonical(soup))
issues.extend(check_open_graph(soup))
issues.extend(check_alt_text(soup))
issues.extend(check_links(soup))

score = calculate_score(issues)
generate_json_report(url, score, issues)

print("\nMetaLens Audit Results")
print("=" * 30)
print(f"SEO Score: {score}/100\n")

if not issues:
    print("No SEO issues found.")
else:
    for issue in issues:
        print(f"[{issue.severity}] {issue.message}")

print(f"\nTotal Issues Found: {len(issues)}")
print("\nJSON report saved to reports/audit_report.json")
