"""Suggest ATS migrations from a supplied official careers URL; never guess a slug."""
import argparse
import html
import re
from urllib.parse import urlsplit
from scraper.http import session
from scraper.storage import save
from scraper.validate_urls import check

def candidates(name, source, document):
    raw = html.unescape(document).replace('\\/', '/')
    found = {}
    patterns = {
        "greenhouse": r"https://(?:job-boards|boards)\.greenhouse\.io/([a-zA-Z0-9_-]+)",
        "lever": r"https://jobs\.lever\.co/([a-zA-Z0-9_-]+)",
        "ashby": r"https://jobs\.ashbyhq\.com/([a-zA-Z0-9_-]+)",
        "workday": r"https://[a-zA-Z0-9.-]+\.myworkdayjobs\.com/(?:[a-z]{2}-[A-Z]{2}/)?[a-zA-Z0-9_-]+",
    }
    for ats, pattern in patterns.items():
        for match in re.finditer(pattern, raw):
            if ats == "greenhouse" and match.group(1) == "embed":
                continue
            company = {"name": name, "ats": ats, "url": match.group(0), "enabled": True,
                       "evidence_url": source, "verification": "candidate_from_official_page"}
            if ats != "workday":
                company[ats + "_id"] = match.group(1)
            found[match.group(0)] = company
    return list(found.values())

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--name", required=True)
    parser.add_argument("--official-url", required=True)
    parser.add_argument("--json", default="reports/source-candidates.json")
    args = parser.parse_args()
    if urlsplit(args.official_url).scheme != "https":
        parser.error("Supply the company's official HTTPS careers page")
    with session() as client:
        response = client.get(args.official_url, timeout=(8, 25))
        response.raise_for_status()
    results = [{"candidate": c, "check": check(c)} for c in candidates(args.name, response.url, response.text)]
    save(args.json, results)
    print(f"{len(results)} candidates. Review company ownership before adding an override to scraper/registry.py.")

if __name__ == "__main__":
    main()
