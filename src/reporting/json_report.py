import json
from pathlib import Path


def generate_json_report(url, score, issues, pages=None, output_dir="reports"):
    report = {
        "url": url,
        "score": score,
        "total_issues": len(issues),
        "issues": []
    }

    if pages is not None:
        report["pages"] = [
            {
                "url": page.url,
                "score": page.score,
                "total_issues": len(page.issues),
                "issues": [
                    {
                        "severity": issue.severity,
                        "check": issue.check,
                        "message": issue.message,
                    }
                    for issue in page.issues
                ],
            }
            for page in pages
        ]

    for issue in issues:
        report["issues"].append(
            {
                "severity": issue.severity,
                "check": issue.check,
                "message": issue.message
            }
        )

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    report_path = output_path / "audit_report.json"
    with report_path.open("w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return str(report_path)
