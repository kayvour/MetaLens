from models.issue import Issue

def check_alt_text(soup):
    issues = []
    images = soup.find_all("img")
    missing_alt_count = 0

    for image in images:
        alt_text = image.get("alt", "").strip()

        if not alt_text:
            missing_alt_count += 1

    if missing_alt_count > 0:
        issues.append(
            Issue(
                severity = "MEDIUM",
                check = "Images",
                message = f"{missing_alt_count} images are missing alt text."
            )
        )
    
    return issues
