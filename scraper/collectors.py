"""Public board collection with schema checks, pagination and explicit failures."""
from urllib.parse import urlsplit, quote
import os
import time
import requests
from scraper.core import Result, matches, normalize, ROLE, INDIA
from scraper.http import get_json, session

API_TYPES = {"greenhouse", "lever", "ashby", "workday"}

def india_facet(facets):
    for facet in facets:
        values = facet.get("values", [])
        selected = [v["id"] for v in values if v.get("descriptor", "").lower() == "india" and v.get("id")]
        if selected and facet.get("facetParameter"):
            return {facet["facetParameter"]: selected}
        nested = india_facet(values)
        if nested:
            return nested
    return {}

def workday_rows(client, company, result, deadline):
    root = result.source_url.rsplit("/jobs", 1)[0]
    applied = {}
    def fetch(offset):
        response = client.post(result.source_url, json={"appliedFacets": applied, "limit": 20,
                               "offset": offset, "searchText": ""}, timeout=(8, 25))
        response.raise_for_status()
        data = response.json()
        if not isinstance(data.get("jobPostings"), list) or not isinstance(data.get("total"), int):
            raise ValueError("Unexpected Workday schema")
        return data
    first = fetch(0)
    if os.getenv("INCLUDE_OVERSEAS", "false").lower() != "true":
        applied = india_facet(first.get("facets", []))
        if applied:
            first = fetch(0)
            result.scope = "India country facet"
    expected = first["total"]  # Later Workday pages often return total=0, not a new total.
    rows, seen = [], set()
    for offset in range(0, 50000, 20):
        if time.monotonic() > deadline:
            result.status, result.detail = "partial", "Workday time budget exceeded"
            break
        try:
            data = first if offset == 0 else fetch(offset)
            batch = data["jobPostings"]
            result.pages += 1
            if not batch and offset < expected:
                raise ValueError("Workday returned an incomplete page")
            for item in batch:
                path = item.get("externalPath", "")
                if not path or path in seen:
                    raise ValueError("Missing/duplicate Workday requisition path")
                seen.add(path)
                host = urlsplit(company["url"])
                site = root.rsplit("/", 1)[1]
                item["_url"] = f"https://{host.netloc}/en-US/{site}{path}"
                rows.append(item)
            if offset + len(batch) >= expected:
                if expected >= 2000:
                    result.status, result.detail = "partial", "Possible Workday server result cap"
                break
        except Exception as exc:
            if not rows:
                raise
            result.status, result.detail = "partial", f"Workday pagination: {type(exc).__name__}"
            break
    else:
        result.status, result.detail = "partial", "Workday pagination safety limit"
    for item in rows:
        location = item.get("locationsText", "")
        if not ROLE.search(item.get("title", "")):
            continue
        from scraper.core import SENIOR
        if os.getenv("EXCLUDE_SENIOR", "true").lower() == "true" and SENIOR.search(item.get("title", "")):
            continue
        if not (INDIA.search(location) or not location or "locations" in location.lower() or os.getenv("INCLUDE_OVERSEAS", "false").lower() == "true"):
            continue
        if time.monotonic() > deadline:
            result.status, result.detail = "partial", "Workday details time budget exceeded"
            break
        try:
            detail = get_json(client, root + item["externalPath"]).get("jobPostingInfo", {})
            if not detail:
                raise ValueError("Missing jobPostingInfo")
            item["locationsText"] = "; ".join([detail.get("location", location)] + (detail.get("additionalLocations") or []))
            item["_description"] = detail.get("jobDescription", "")
            item["_url"] = detail.get("externalUrl") or item["_url"]
        except Exception:
            result.status, result.detail = "partial", "Some Workday job details unavailable"
    return rows

def endpoint(company):
    ats = company["ats"]
    if ats == "greenhouse":
        return f"https://boards-api.greenhouse.io/v1/boards/{quote(company['greenhouse_id'], safe='')}/jobs?content=true"
    if ats == "lever":
        host = "api.eu.lever.co" if company.get("lever_region") == "eu" else "api.lever.co"
        return f"https://{host}/v0/postings/{quote(company['lever_id'], safe='')}?mode=json"
    if ats == "ashby":
        return f"https://api.ashbyhq.com/posting-api/job-board/{quote(company['ashby_id'], safe='')}?includeCompensation=true"
    if ats == "workday":
        parts = urlsplit(company["url"])
        if not (parts.hostname or "").endswith(".myworkdayjobs.com"):
            raise ValueError("Not a Workday careers tenant")
        paths = [p for p in parts.path.split("/") if p]
        if paths and len(paths[0]) == 5 and paths[0][2] == "-":
            paths.pop(0)
        if not paths:
            raise ValueError("Missing Workday site")
        return f"https://{parts.netloc}/wday/cxs/{parts.hostname.split('.')[0]}/{paths[0]}/jobs"
    raise ValueError(f"Unsupported ATS {ats}")

def salary_ashby(data):
    data = data or {}
    salaries = [x for x in data.get("summaryComponents", []) if x.get("compensationType") == "Salary"]
    pay = salaries[0] if len(salaries) == 1 else {}
    return {"summary": data.get("compensationTierSummary", ""),
            "currency": pay.get("currencyCode"), "min": pay.get("minValue"), "max": pay.get("maxValue"),
            "interval": "year" if pay.get("interval") == "1 YEAR" else pay.get("interval"),
            "evidence": "employer_disclosed", "raw": data} if data else {}

def convert(company, item):
    ats = company["ats"]
    if ats == "greenhouse":
        return {"title": item.get("title"), "location": (item.get("location") or {}).get("name", ""),
                "url": item.get("absolute_url"), "source_id": item.get("id"), "description": item.get("content"),
                "legacy_ids": [f"gh_{company['greenhouse_id']}_{item.get('id')}"]}
    if ats == "lever":
        cats, sal = item.get("categories") or {}, item.get("salaryRange") or {}
        compensation = {"currency": sal.get("currency"), "min": sal.get("min"), "max": sal.get("max"),
                        "interval": "year" if sal.get("interval") in ("per-year-salary", "year") else sal.get("interval"),
                        "evidence": "employer_disclosed", "raw": sal} if sal else {}
        return {"title": item.get("text"), "locations": cats.get("allLocations") or [cats.get("location", "")],
                "url": item.get("hostedUrl"), "source_id": item.get("id"), "compensation": compensation,
                "description": (item.get("descriptionPlain") or "") + " " + " ".join(x.get("content", "") for x in item.get("lists", [])),
                "remote": item.get("workplaceType") == "remote",
                "legacy_ids": [f"lv_{company['lever_id']}_{item.get('id')}"]}
    if ats == "ashby":
        secondary = item.get("secondaryLocations") or []
        address = (item.get("address") or {}).get("postalAddress") or {}
        return {"title": item.get("title"), "source_id": item.get("id"),
                "locations": [item.get("location", "")] + [x.get("location", "") for x in secondary],
                "countries": [address.get("addressCountry", "")] + [(x.get("address") or {}).get("addressCountry", "") for x in secondary],
                "url": item.get("jobUrl") or item.get("applyUrl"), "description": item.get("descriptionPlain"),
                "remote": item.get("isRemote", False), "compensation": salary_ashby(item.get("compensation")),
                "published_at": item.get("publishedAt"),
                "legacy_ids": [f"ab_{company['ashby_id']}_{item.get('id')}"]}
    return {"title": item.get("title"), "location": item.get("locationsText", ""),
            "url": item.get("_url"), "source_id": item.get("externalPath"), "description": item.get("_description", "")}

def collect(company):
    result = Result(company["name"])
    rows, invalid = [], 0
    deadline = time.monotonic() + int(os.getenv("API_COMPANY_SECONDS", "120"))
    try:
        result.source_url = endpoint(company)
        with session() as client:
            ats = company["ats"]
            if ats in {"greenhouse", "ashby"}:
                data = get_json(client, result.source_url)
                if not isinstance(data, dict) or not isinstance(data.get("jobs"), list):
                    raise ValueError("Unexpected schema: jobs list missing")
                rows, result.pages = data["jobs"], 1
            elif ats == "lever":
                for offset in range(0, 50000, 100):
                    if time.monotonic() > deadline:
                        result.status, result.detail = "partial", "API time budget exceeded"
                        break
                    batch = get_json(client, result.source_url, params={"skip": offset, "limit": 100})
                    if not isinstance(batch, list):
                        raise ValueError("Unexpected Lever schema")
                    if batch and rows and batch[0].get("id") == rows[0].get("id"):
                        raise ValueError("Pagination repeated its first page")
                    rows.extend(batch)
                    result.pages += 1
                    if len(batch) < 100:
                        break
                else:
                    result.status, result.detail = "partial", "Lever pagination safety limit"
            else:
                rows = workday_rows(client, company, result, deadline)
        seen = set()
        for item in rows:
            if item.get("isListed") is False:
                continue
            try:
                job = normalize(company, convert(company, item))
                if matches(job) and job["id"] not in seen:
                    result.jobs.append(job)
                    seen.add(job["id"])
            except (ValueError, TypeError, KeyError):
                invalid += 1
        result.total = len(rows)
        if invalid:
            result.status, result.detail = "partial", f"{invalid} malformed postings"
    except requests.HTTPError as exc:
        result.status = "blocked" if exc.response.status_code in (401, 403, 429) else "failed"
        result.detail = f"HTTP {exc.response.status_code}"
    except Exception as exc:
        result.status, result.detail = "failed", f"{type(exc).__name__}: {exc}"[:350]
    return result
