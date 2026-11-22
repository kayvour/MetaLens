from html import escape
from pathlib import Path


def generate_html_report(url, score, issues, pages=None, output_dir="reports"):
    page_sections = []
    report_pages = pages if pages is not None else []

    for page in report_pages:
        issue_html = ""
        if page.issues:
            issue_html = "".join(
                f'<div class="issue {escape(issue.severity)}">'
                f"<strong>[{escape(issue.severity)}]</strong> "
                f"{escape(issue.message)}</div>"
                for issue in page.issues
            )
        else:
            issue_html = "<p>No SEO issues found.</p>"

        page_sections.append(
            f'<section><h2><a href="{escape(page.url)}">{escape(page.url)}</a></h2>'
            f'<div class="score">SEO Score: {page.score}/100</div>'
            f'<h3>Issues Found ({len(page.issues)})</h3>{issue_html}</section>'
        )

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>MetaLens SEO Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; color: #1f2937; }}
        section {{ border-top: 1px solid #ddd; margin-top: 24px; padding-top: 8px; }}
        .score {{ font-size: 24px; font-weight: bold; margin-bottom: 16px; }}
        .issue {{ padding: 10px; margin: 10px 0; border-radius: 5px; }}
        .HIGH {{ background: #ffdddd; }}
        .MEDIUM {{ background: #fff4cc; }}
        .LOW {{ background: #ddeeff; }}
    </style>
</head>
<body>
    <h1>MetaLens SEO Audit Report</h1>
    <p><strong>URL:</strong> {escape(url)}</p>
    <div class="score">Average SEO Score: {score}/100</div>
    <h2>Issues Found ({len(issues)})</h2>
    {''.join(page_sections)}
</body>
</html>
"""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    report_path = output_path / "audit_report.html"
    report_path.write_text(html_content, encoding="utf-8")
    return str(report_path)
