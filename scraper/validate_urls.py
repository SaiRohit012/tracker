"""Audit endpoints without sending mail. HTTP reachability is not collection coverage."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from scraper.registry import companies
from scraper.collectors import endpoint
from scraper.http import session
from scraper.storage import save
from scraper.core import now

def check(company):
    row = {"company": company["name"], "ats": company["ats"], "checked_at": now(),
           "configured_url": company.get("url", ""), "verification": company.get("verification")}
    if not company["enabled"]:
        return row | {"status": "disabled", "detail": "Placeholder: needs verified official URL"}
    try:
        ats = company["ats"]
        url = endpoint(company) if ats in {"greenhouse", "lever", "ashby", "workday"} else company["url"].replace("{role}", "engineer")
        with session() as client:
            response = client.post(url, json={"appliedFacets": {}, "limit": 1, "offset": 0, "searchText": ""}, timeout=(8, 15)) if ats == "workday" else client.get(url, timeout=(8, 15))
        row.update(http_status=response.status_code, final_url=response.url)
        if response.status_code >= 400:
            return row | {"status": "blocked" if response.status_code in (401, 403, 429) else "failed", "detail": f"HTTP {response.status_code}"}
        if ats in {"greenhouse", "lever", "ashby", "workday"}:
            data = response.json()
            jobs = data if ats == "lever" else data.get("jobPostings" if ats == "workday" else "jobs")
            if not isinstance(jobs, list):
                raise ValueError("Expected job list missing")
            count = data.get("total", len(jobs)) if ats == "workday" else len(jobs)
            return row | {"status": "api_responding" if count else "empty_needs_verification", "jobs": count,
                          "detail": "Schema checked; confirm official ownership and run full collection"}
        return row | {"status": "reachable_unverified", "detail": "HTTP only; extraction and pagination not verified"}
    except Exception as exc:
        return row | {"status": "failed", "detail": f"{type(exc).__name__}: {exc}"[:300]}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", default="reports/url-audit.json")
    parser.add_argument("--company", action="append", default=[])
    args = parser.parse_args()
    selected = [c for c in companies() if not args.company or any(n.lower() in c["name"].lower() for n in args.company)]
    with ThreadPoolExecutor(max_workers=8) as pool:
        rows = list(pool.map(check, selected))
    save(args.json, rows)
    from collections import Counter
    print(dict(Counter(r["status"] for r in rows)))
    print(f"Saved {len(rows)} company checks to {args.json}")
    return 1 if any(r["status"] in {"failed", "blocked", "empty_needs_verification"} for r in rows) else 0

if __name__ == "__main__":
    raise SystemExit(main())
