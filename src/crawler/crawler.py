from collections import deque
from urllib.parse import urljoin, urlparse

from fetcher.client import fetch_page
from parser.html_parser import parse_html


def crawl_website(start_url, max_pages=20):

    queue = deque([start_url])

    visited = set()

    discovered_pages = []

    while queue and len(discovered_pages) < max_pages:

        current_url = queue.popleft()

        if current_url in visited:
            continue

        visited.add(current_url)
        discovered_pages.append(current_url)

        try:

            html = fetch_page(current_url)
            soup = parse_html(html)

            for link in soup.find_all("a"):

                href = link.get("href")

                if not href:
                    continue

                absolute_url = urljoin(current_url, href)

                parsed = urlparse(absolute_url)
                start_parsed = urlparse(start_url)

                if parsed.scheme != start_parsed.scheme or parsed.netloc != start_parsed.netloc:
                    continue

                cleaned_url = (
                    parsed.scheme
                    + "://"
                    + parsed.netloc
                    + (parsed.path or "/")
                )

                if cleaned_url not in visited:
                    queue.append(cleaned_url)

        except Exception:
            continue

    return discovered_pages
