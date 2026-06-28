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


def main():
    url = input("Enter URL to audit: ").strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    discovered_pages = crawl_website(url)
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

    print("\n")
    print("=" * 60)
    print("MetaLens Audit Results")
    print("=" * 60)

    for page in pages:

        print(f"\nURL: {page.url}")
        print(f"SEO Score: {page.score}/100")

        if not page.issues:
            print("No SEO issues found.")
        else:
            for issue in page.issues:
                print(f"[{issue.severity}] {issue.message}")

        print(f"Total Issues Found: {len(page.issues)}")

    print("\n" + "=" * 60)
    print(f"Pages Audited: {len(pages)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
