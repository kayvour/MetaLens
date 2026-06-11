from models.issue import Issue

def check_canonical(soup):
    issues = []

    canonical_tag = soup.find("link", rel="canonical")

    if not canonical_tag:
        issues.append(
            Issue(
                severity = "HIGH",
                check = "Canonical",
                message = "Missing canonical tag"
            )
        )
        return issues

    canonical_url = canonical_tag.get("href", "").strip()

    if not canonical_url:
        issues.append(
            Issue(
                severity = "HIGH",
                check = "Canonical",
                message = "Canonical tag is empty"
            )
        )

    return issues
    