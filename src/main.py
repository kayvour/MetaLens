from fetcher.client import fetch_page
from parser.html_parser import parse.html

url = "https://www.example.com"

html = fetch_page(url)
soup = parse_html(html)

print(soup.title)
