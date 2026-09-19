"""Check queued application links; access challenges are inconclusive, not closed jobs."""
from concurrent.futures import ThreadPoolExecutor
from scraper.http import session
from scraper.core import now

def check_job(job):
    result = {"id": job["id"], "url": job["url"], "checked_at": now()}
    try:
        with session() as client:
            response = client.get(job["url"], timeout=(8, 15), stream=True)
            try:
                code = response.status_code
                result["final_url"] = response.url
                if code in (404, 410):
                    status = "unavailable"
                elif code == 200:
                    status = "reachable"
                else:
                    status = "unverified"
                return result | {"status": status, "http_status": code}
            finally:
                response.close()
    except Exception as exc:
        return result | {"status": "unverified", "detail": type(exc).__name__}

def validate_pending(state, jobs):
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(check_job, jobs))
    for row in rows:
        job = state["jobs"][row["id"]]
        job["link_status"] = row["status"]
        job["link_checked_at"] = row["checked_at"]
        if row["status"] == "unavailable":
            job["active"] = False
    return rows
