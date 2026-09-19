"""Atomic local state. Corrupt state fails loudly instead of re-sending everything."""
import json
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path
from scraper.core import now, rank

def load(path, default):
    path = Path(path)
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else default

def save(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(temporary, path)

def open_state(directory):
    state = load(Path(directory) / "tracker_state.json", {"version": 2, "jobs": {}, "health": {}})
    if state.get("version") != 2 or not isinstance(state.get("jobs"), dict):
        raise ValueError("Unsupported/corrupt tracker state; restore a backup")
    legacy = set(load(Path(directory) / "seen_jobs.json", []))
    return state, legacy

def merge(state, result, legacy=()):
    previous = state["health"].get(result.company, {})
    # Large unexplained drops deserve inspection, even with a syntactically valid API response.
    previous_total = previous.get("total", 0)
    if result.status == "ok" and previous_total >= 20 and result.total < previous_total * 0.2:
        result.status = "suspect"
        result.detail = f"Inventory fell from {previous_total} to {result.total}; verify source"
    health = result.summary()
    health["consecutive_errors"] = 0 if result.status == "ok" else previous.get("consecutive_errors", 0) + 1
    health["last_success"] = result.checked_at if result.status == "ok" else previous.get("last_success")
    health["alerted"] = previous.get("alerted", False) if result.status != "ok" else False
    state["health"][result.company] = health
    returned = set()
    for job in result.jobs:
        returned.add(job["id"])
        existing = state["jobs"].get(job["id"], {})
        # Canonical URL dedup also bridges a company switching ATS or source-ID formats.
        if not existing:
            existing = next((v for v in state["jobs"].values() if v["company"] == job["company"] and v["url"] == job["url"]), {})
            if existing and existing["id"] != job["id"]:
                existing["active"] = False
        delivered = existing.get("delivered_at")
        if not delivered and any(x in legacy for x in job.get("legacy_ids", [])):
            delivered = "legacy"
        state["jobs"][job["id"]] = dict(job, first_seen=existing.get("first_seen", now()),
                                         last_seen=now(), active=True, delivered_at=delivered)
    # Only a complete successful scan can retire absent matches. Failures never close jobs.
    if result.status == "ok":
        for key, job in state["jobs"].items():
            if job["company"] == result.company and key not in returned:
                job["active"] = False

def pending(state):
    from scraper.core import matches
    cutoff = datetime.now(timezone.utc) - timedelta(days=7)
    return sorted([j for j in state["jobs"].values() if j.get("active") and not j.get("delivered_at")
                   and datetime.fromisoformat(j["last_seen"]) >= cutoff and matches(j)], key=rank, reverse=True)

def deliver(state, sender, save_state, limit=40, allowed_ids=None):
    batch = [j for j in pending(state) if allowed_ids is None or j["id"] in allowed_ids][:limit]
    if not batch:
        return True
    # Save the pending outbox before attempting SMTP, so unsuccessful sends survive.
    save_state(state)
    if not sender(batch):
        return False
    for job in batch:
        state["jobs"][job["id"]]["delivered_at"] = now()
    save_state(state)
    return True
