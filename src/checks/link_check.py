from models.issue import Issue


def check_links(soup):
    issues = []
    links = soup.find_all("a")

    missing_href_count = 0
    empty_href_count = 0
    placeholder_href_count = 0

    for link in links:
        if not link.has_attr("href"):
            missing_href_count += 1
            continue

        href = link.get("href", "").strip()

        if not href:
            empty_href_count += 1

        elif href == "#":
            placeholder_href_count += 1

    if missing_href_count > 0:
        issues.append(
            Issue(
                severity="MEDIUM",
                check="Links",
                message=f"{missing_href_count} missing href attribute(s)",
            )
        )

    if empty_href_count > 0:
        issues.append(
            Issue(
                severity="MEDIUM",
                check="Links",
                message=f"{empty_href_count} empty href link(s)",
            )
        )

    if placeholder_href_count > 0:
        issues.append(
            Issue(
                severity="LOW",
                check="Links",
                message=f"{placeholder_href_count} placeholder link(s)",
            )
        )

    return issues
