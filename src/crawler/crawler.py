from urllib.parse import urlparse, urljoin

def crawl_website(soup, base_url):
    """
    Find all internal links.
    """

    pages = set()

    parsed_base = urlparse(base_url)
    base_netloc = parsed_base.netloc
    base_scheme = parsed_base.scheme

    for link in soup.find_all("a"):
        href = link.get("href")

        if not href:
            continue

        absolute_url = urljoin(base_url, href)
        parsed = urlparse(absolute_url)

        if parsed.scheme != base_scheme or parsed.netloc != base_netloc:
            continue

        cleaned_url = parsed.scheme + "://" + parsed.netloc + parsed.path
        pages.add(cleaned_url)
        
    return sorted(pages)
