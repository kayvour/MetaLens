import json

def generate_json_report(url, score, issues):

    report = {
        "url": url,
        "score": score,
        "total_issues": len(issues),
        "issues": []
    }

    for issue in issues:
        report["issues"].append(
            {
                "severity": issue.severity,
                "check": issue.check,
                "message": issue.message
            }
        )

    with open("reports/audit_report.json", "w") as file:
        json.dump(report, file, indent=4)
    
    return report

