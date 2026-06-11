def check_h1(soup):
    issues = []

    h1_tags = soup.find_all("h1")
    h1_count = len(h1_tags)

    if h1_count == 0:
        issues.append(
            Issue(
                severity = "HIGH",
                check = "H1",
                message = "Mising H1 tag"
            )
        )

    elif h1_count > 1:
        issues.append(
            Issue(
                severity = "MEDIUM",
                check = "H1",
                message = f"Multiple H1 tags found ({h1_count})"
            )
        )

    return issues
