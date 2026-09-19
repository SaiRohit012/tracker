"""Job tracker v2. Default is a preview; --send explicitly enables email/state updates."""
import argparse
import asyncio
import logging
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from scraper.collectors import API_TYPES, collect
from scraper.core import Result, now
from scraper.registry import companies
from scraper.storage import open_state, merge, save, deliver, pending
from notifier.email_v2 import digest, health_alert

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--send", action="store_true")
    parser.add_argument("--baseline", action="store_true", help="Record current matches without sending; use for initial setup")
    parser.add_argument("--company", action="append", default=[], help="Name substring; repeatable")
    parser.add_argument("--api-only", action="store_true")
    parser.add_argument("--state-dir", default="data")
    parser.add_argument("--report-dir", default="reports")
    parser.add_argument("--max-emails-jobs", type=int, default=40)
    args = parser.parse_args()
    if args.send and args.baseline:
        parser.error("--send and --baseline are mutually exclusive")
    if args.max_emails_jobs < 1:
        parser.error("--max-emails-jobs must be positive")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    selected = [c for c in companies() if not args.company or any(n.lower() in c["name"].lower() for n in args.company)]
    if not selected:
        parser.error("No matching companies")
    state, legacy = open_state(args.state_dir)
    state_path = Path(args.state_dir) / "tracker_state.json"
    rows, jobs = [], []
    def record(result):
        merge(state, result, legacy)
        if args.baseline:
            for job in result.jobs:
                state["jobs"][job["id"]]["delivered_at"] = "baseline:" + now()
        rows.append(result.summary())
        jobs.extend(result.jobs)
        logging.info("%s: %s, %s total, %s matches", result.company, result.status, result.total, len(result.jobs))
        save(Path(args.report_dir) / "coverage.json", rows)
        if args.send or args.baseline:
            save(state_path, state)
    active = [c for c in selected if c["enabled"]]
    for company in selected:
        if not company["enabled"]:
            record(Result(company["name"], "disabled", detail="No verified URL"))
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(collect, c): c for c in active if c["ats"] in API_TYPES}
        for future in as_completed(futures):
            try:
                record(future.result())
            except Exception:
                # State/report errors are fatal: do not mask persistence failures as healthy scans.
                raise
    browsers = [c for c in active if c["ats"] not in API_TYPES]
    if not args.api_only and browsers:
        # Rotate the large unverified browser watchlist within the hosted-runner budget.
        if not args.company:
            count = min(len(browsers), max(1, int(os.getenv("BROWSER_COMPANIES_PER_RUN", "36"))))
            cursor = state.get("browser_cursor", 0) % len(browsers)
            ordered = browsers[cursor:] + browsers[:cursor]
            browsers = ordered[:count]
            rows.extend(Result(c["name"], "not_run", detail="Browser rotation; retained for next runs").summary() for c in ordered[count:])
            state["browser_cursor"] = (cursor + count) % len(ordered)
        from scraper.browser import collect_all
        # Checkpoint small batches so a browser crash cannot discard the whole run.
        for start in range(0, len(browsers), 6):
            try:
                batch = asyncio.run(collect_all(browsers[start:start + 6]))
            except Exception as exc:
                batch = [Result(c["name"], "failed", detail=f"Browser startup: {type(exc).__name__}") for c in browsers[start:start + 6]]
            for result in batch:
                record(result)
    elif args.api_only:
        rows.extend(Result(c["name"], "not_run", detail="--api-only").summary() for c in browsers)
    save(Path(args.report_dir) / "coverage.json", rows)
    save(Path(args.report_dir) / "matches.json", jobs)
    save(Path(args.report_dir) / "pending.json", pending(state))
    failed_delivery = False
    if args.baseline:
        # Baseline applies only to jobs observed in this run, never unrelated pending jobs.
        for job in jobs:
            state["jobs"][job["id"]]["delivered_at"] = "baseline:" + now()
        save(state_path, state)
    elif args.send:
        from scraper.link_check import validate_pending
        link_rows = validate_pending(state, pending(state)[:args.max_emails_jobs])
        save(Path(args.report_dir) / "application-link-checks.json", link_rows)
        save(state_path, state)
        failed_delivery = not deliver(state, digest, lambda s: save(state_path, s), args.max_emails_jobs,
                                      allowed_ids={r["id"] for r in link_rows})
        unhealthy = [h for h in state["health"].values() if h["status"] not in {"ok", "disabled"}
                     and h["consecutive_errors"] >= 3 and not h.get("alerted")]
        if unhealthy and health_alert(unhealthy):
            for h in unhealthy:
                h["alerted"] = True
            save(state_path, state)
    logging.info("%s companies checked; %s matches; %s pending", len(rows), len(jobs), len(pending(state)))
    return 1 if failed_delivery else 0

if __name__ == "__main__":
    raise SystemExit(main())
