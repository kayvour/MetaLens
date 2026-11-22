import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fetcher.client import fetch_page
from parser.html_parser import parse_html

from crawler.crawler import crawl_website

from models.page import Page

from checks.title_check import check_title
from checks.meta_check import check_meta_description
from checks.h1_check import check_h1
from checks.canonical_check import check_canonical
from checks.og_check import check_open_graph
from checks.alt_check import check_alt_text
from checks.link_check import check_links

from scoring.score_engine import calculate_score
from reporting.json_report import generate_json_report
from reporting.html_report import generate_html_report


def run_audit(url, max_pages=20):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    discovered_pages = crawl_website(url, max_pages=max_pages)
    pages = []

    print(f"\nDiscovered {len(discovered_pages)} page(s).\n")

    for page_url in discovered_pages:
        try:
            print(f"Auditing: {page_url}")
            page_html = fetch_page(page_url)
            page_soup = parse_html(page_html)

            issues = []
            issues.extend(check_title(page_soup))
            issues.extend(check_meta_description(page_soup))
            issues.extend(check_h1(page_soup))
            issues.extend(check_canonical(page_soup))
            issues.extend(check_open_graph(page_soup))
            issues.extend(check_alt_text(page_soup))
            issues.extend(check_links(page_soup))
            score = calculate_score(issues)

            pages.append(
                Page(
                    url=page_url,
                    score=score,
                    issues=issues
                )
            )
        except Exception as e:
            print(f"Failed to audit {page_url}")
            print(f"Reason: {e}")

    for page in pages:
        print(f"\nURL: {page.url}")
        print(f"SEO Score: {page.score}/100")
        if not page.issues:
            print("No SEO issues found.")
        else:
            for issue in page.issues:
                print(f"[{issue.severity}] {issue.message}")
        print(f"Total Issues Found: {len(page.issues)}")

    return url, pages


def main():
    parser = argparse.ArgumentParser(
        description="MetaLens - a very early prototype website SEO auditor"
    )
    parser.add_argument("url", nargs="?", help="Website URL to audit")
    parser.add_argument("--max-pages", type=int, default=20, help="Maximum pages to crawl")
    parser.add_argument("--output-dir", default="reports", help="Directory for JSON and HTML reports")
    args = parser.parse_args()

    url = args.url or input("Enter URL to audit: ").strip()
    if not url:
        parser.error("A URL is required")

    print("\n" + "=" * 60)
    print("MetaLens Audit Results")
    print("=" * 60)

    normalized_url, pages = run_audit(url, max_pages=args.max_pages)

    print("\n" + "=" * 60)
    print(f"Pages Audited: {len(pages)}")
    print("=" * 60)

    aggregate_issues = [
        issue
        for page in pages
        for issue in page.issues
    ]
    average_score = (
        sum(page.score for page in pages) // len(pages)
        if pages
        else 100
    )

    json_path = generate_json_report(
        normalized_url,
        average_score,
        aggregate_issues,
        pages=pages,
        output_dir=args.output_dir,
    )
    html_path = generate_html_report(
        normalized_url,
        average_score,
        aggregate_issues,
        pages=pages,
        output_dir=args.output_dir,
    )
    print(f"\nJSON report: {json_path}")
    print(f"HTML report: {html_path}")


if __name__ == "__main__":
    main()
