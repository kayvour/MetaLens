from models.issue import Issue

def check_open_graph(soup):
    issues = []

    required_tags = [
        "og:title",
        "og:description",
        "og:image"
    ]

    for tag in required_tags:
        og__tag = soup.find("meta", attrs={"property": tag})

        if not og__tag:
            issues.append(
                Issue(
                    severity = "MEDIUM",
                    check = "Open Graph",
                    message = f"Missing {tag}"
                )
            )

    return issues
