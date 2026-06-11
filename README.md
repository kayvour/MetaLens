# MetaLens

A Python-based SEO auditing tool that analyzes webpages and detects common on-page SEO issues. It helps developers, marketers, and website owners identify technical SEO problems before they impact search visibility.

## Features

### Current Checks

* Title tag auditing

  * Missing title tags
  * Empty title tags
  * Title length validation

* Meta description auditing

  * Missing meta descriptions
  * Empty meta descriptions
  * Description length validation

* H1 auditing

  * Missing H1 tags
  * Multiple H1 tags

* Canonical auditing

  * Missing canonical tags
  * Empty canonical URLs

## Project Structure

```text
src/
├── checks/
├── crawler/
├── fetcher/
├── models/
├── parser/
├── reporting/
├── scoring/
└── utils/
```

## Example Output

```text
[MEDIUM] Title is too short (14 characters)
[HIGH] Missing meta description
[HIGH] Missing canonical tag
```

## Roadmap

### Phase 1

* Title auditing
* Meta description auditing
* H1 auditing
* Canonical auditing

### Phase 2

* Open Graph validation
* Image alt text auditing
* Internal link auditing
* Robots.txt detection
* Sitemap detection

### Phase 3

* Multi-page crawling
* SEO scoring engine
* JSON reports
* HTML reports

### Phase 4

* Website-wide audits
* Crawl comparison
* Interactive dashboard

## License

MIT License
