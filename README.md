# MetaLens

A Python-based SEO auditing tool that analyzes webpages and detects common on-page SEO issues. It helps developers, marketers, and website owners identify technical SEO problems before they impact search visibility.

## Features

### ✅ Implemented Checks

* **Title Tag Auditing**
  * Missing title tags
  * Empty title tags
  * Title length validation

* **Meta Description Auditing**
  * Missing meta descriptions
  * Empty meta descriptions
  * Description length validation

* **H1 Tag Auditing**
  * Missing H1 tags
  * Multiple H1 tags

* **Canonical Tag Auditing**
  * Missing canonical tags
  * Empty canonical URLs

* **Open Graph Validation**
  * Validates OG meta tags for social sharing

* **Image Alt Text Auditing**
  * Detects missing alt attributes on images
  * Validates alt text completeness

* **Internal Link Auditing**
  * Analyzes internal link structure
  * Detects broken or invalid links

* **Robots.txt Detection**
  * Checks for robots.txt file presence

### ✅ Implemented Features

* **Web Crawler**
  * Multi-page crawling capabilities
  * Internal link discovery
  * URL normalization and management

* **HTTP Client**
  * Custom headers support
  * Page fetching with error handling

* **HTML Parser**
  * BeautifulSoup-based HTML parsing
  * Metadata and content extraction

* **SEO Scoring Engine**
  * Automated scoring based on issue severity
  * Weighted penalty system (HIGH: 15pts, MEDIUM: 8pts, LOW: 3pts)

* **Multiple Report Formats**
  * JSON reports for data integration
  * HTML reports for visual inspection
  * Console output for quick feedback

* **Audit Results & Models**
  * Comprehensive data models for issues, pages, and audit results
  * Structured issue tracking with severity levels

## Project Structure

```text
src/
├── checks/              # All SEO check implementations
├── crawler/             # Website crawling logic
├── fetcher/             # HTTP client and headers
├── models/              # Data models (Issue, Page, AuditResult)
├── parser/              # HTML parsing and extraction
├── reporting/           # Report generation (JSON, HTML, Console)
├── scoring/             # SEO score calculation
└── utils/               # Constants, helpers, and logging
```

## Example Output

```text
[MEDIUM] Title is too short (14 characters)
[HIGH] Missing meta description
[HIGH] Missing canonical tag
[MEDIUM] Image missing alt text: /images/header.png
[LOW] Internal link unreachable: /discontinued-page
```

## Usage

```bash
# Run a single page audit
python src/main.py

# Or use the examples
python examples/single_page_audit.py
python examples/website_audit.py
```

## Roadmap

### ✅ Phase 1 - Completed

* Title auditing
* Meta description auditing
* H1 auditing
* Canonical auditing

### ✅ Phase 2 - Completed

* Open Graph validation
* Image alt text auditing
* Internal link auditing
* Robots.txt detection

### ✅ Phase 3 - Completed

* Multi-page crawling
* SEO scoring engine
* JSON reports
* HTML reports

### Phase 4 - Upcoming

* Website-wide audits with comparison
* Crawl comparison and historical tracking
* Interactive dashboard
* Sitemap detection and validation

## License

MIT License
