from models.issue import Issue

def check_title(soup):
    issues = []

    title_tag = soup.find('title')
    if not title_tag:
        issues.append(
            Issue(
                severity = "HIGH",
                check = "Title",
                message = "Missing title tag"
            )
        )
        return issues

    title_text = title_tag.get_text().strip()
    if not title_text:
        issues.append(
            Issue(
                severity = "HIGH",
                check = "Title",
                message = "Empty title tag"
            )
        )

    title_length = len(title_text)
    if title_length < 30:
        issues.append(
            Issue(
                severity = "MEDIUM",
                check = "Title",
                message = f"Title is too short ({title_length} characters)"
            )
        )
    elif title_length > 60:
        issues.append(
            Issue(
                severity = "MEDIUM",
                check = "Title",
                message = f"Title is too long ({title_length} characters)"
            )
        )

    return issues
