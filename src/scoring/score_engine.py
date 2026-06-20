def calculate_score(issues):
    score = 100

    penalties = {
        "HIGH": 15,
        "MEDIUM": 8,
        "LOW": 3
    }

    for issue in issues:
        score -= penatlties.get(issue.severity, 0)

    return max(score, 0)
