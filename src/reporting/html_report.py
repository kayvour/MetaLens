def generate_html_report(url, score, issues):

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>MetaLens SEO Report</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 40px;
            }}

            h1 {{
                color: #333;
            }}

            .score {{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }}

            .issue {{
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
            }}

            .HIGH {{
                background-color: #ffdddd;
            }}

            .MEDIUM {{
                background-color: #fff4cc;
            }}

            .LOW {{
                background-color: #ddeeff;
            }}
        </style>
    </head>
    <body>

        <h1>Metalens SEO Audit Report</h1>
        <p><strong>URL:</strong> {url}</p>

        <div class = "score">
            SEO Score: {score}/100
        </div>

        <h2>Issues Found ({len(issues)})</h2>
    """

    if not issues:
        html_content += "<p>No SEO issues found.</p>"

    else:
        for issue in issues:
            html_content += f"""
            <div class = "issue {issue.severity}">
                <strong>[{issue.severity}]</strong>
                {issue.message}
            </div>
            """

    html_content += """
    </body>
    </html>
    """

    with open("reports/audit_report.html", "w", encoding="utf-8") as file:
        file.write(html_content)
