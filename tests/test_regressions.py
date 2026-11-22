import sys
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from checks.link_check import check_links
from crawler import crawler as crawler_module
from models.issue import Issue
from models.page import Page
from reporting.html_report import generate_html_report
from reporting.json_report import generate_json_report


def test_crawl_website_ignores_external_domains_with_same_prefix(monkeypatch):
    html_pages = {
        "https://example.com": "<a href='/about'>About</a><a href='https://example.com.evil.com/'>Evil</a>",
        "https://example.com/about": "<html></html>",
    }

    monkeypatch.setattr(crawler_module, "fetch_page", lambda url: html_pages[url])
    monkeypatch.setattr(crawler_module, "parse_html", lambda html: BeautifulSoup(html, "html.parser"))

    discovered = crawler_module.crawl_website("https://example.com", max_pages=5)

    assert discovered == ["https://example.com", "https://example.com/about"]


def test_check_links_reports_empty_and_placeholder_hrefs():
    soup = BeautifulSoup(
        "<a href=''>Empty</a><a href='#'>Placeholder</a><a>Missing</a>",
        "html.parser",
    )

    issues = check_links(soup)
    messages = {issue.message for issue in issues}

    assert "1 empty href link(s)" in messages
    assert "1 placeholder link(s)" in messages
    assert "1 missing href attribute(s)" in messages


def test_report_generation_writes_json_and_html(tmp_path):
    issue = Issue(
        severity="HIGH",
        check="title",
        message="Missing title",
    )
    page = Page(url="https://example.com", score=85, issues=[issue])

    json_path = generate_json_report(
        "https://example.com",
        85,
        [issue],
        pages=[page],
        output_dir=str(tmp_path),
    )
    html_path = generate_html_report(
        "https://example.com",
        85,
        [issue],
        pages=[page],
        output_dir=str(tmp_path),
    )

    assert Path(json_path).is_file()
    assert Path(html_path).is_file()
    assert "Missing title" in Path(json_path).read_text(encoding="utf-8")
    assert "Missing title" in Path(html_path).read_text(encoding="utf-8")
