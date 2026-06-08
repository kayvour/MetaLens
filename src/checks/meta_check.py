from models.issue import Issue


def check_meta_description(soup):
    issues = []

    meta_tag = soup.find("meta", attrs={"name": "description"})

    if not meta_tag:
        issues.append(
            Issue(
                severity="HIGH",
                check="Meta Description",
                message="Missing meta description"
            )
        )
        return issues

    description = meta_tag.get("content", "").strip()

    if not description:
        issues.append(
            Issue(
                severity="HIGH",
                check="Meta Description",
                message="Empty meta description"
            )
        )
        return issues

    description_length = len(description)

    if description_length < 120:
        issues.append(
            Issue(
                severity="MEDIUM",
                check="Meta Description",
                message=f"Meta description too short ({description_length} characters)"
            )
        )

    elif description_length > 160:
        issues.append(
            Issue(
                severity="LOW",
                check="Meta Description",
                message=f"Meta description too long ({description_length} characters)"
            )
        )

    return issues
