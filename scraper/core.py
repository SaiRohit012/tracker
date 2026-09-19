"""Shared conservative normalization and explicit collection health."""
from __future__ import annotations
import hashlib
import html
import os
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from urllib.parse import parse_qsl, urlencode, urljoin, urlsplit, urlunsplit

def now():
    return datetime.now(timezone.utc).isoformat()

def text(value):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", str(value or "")))).strip()

def canonical_url(base, href):
    url = urlsplit(urljoin(base, href or ""))
    if url.scheme not in ("http", "https") or not url.netloc or not href:
        raise ValueError("Missing or unsafe job URL")
    query = [(k, v) for k, v in parse_qsl(url.query, keep_blank_values=True)
             if not k.lower().startswith("utm_") and k.lower() not in {"gh_src", "source", "ref"}]
    return urlunsplit((url.scheme, url.netloc.lower(), url.path, urlencode(sorted(query)), ""))

ROLE = re.compile(r"\b(sde[ -]?[123]?|swe[ -]?[123]?|software|developer|backend|frontend|full[ -]?stack|"
                  r"machine learning|ml engineer|ai engineer|ai scientist|data (engineer|scientist|analyst)|"
                  r"devops|cloud engineer|site reliability|platform engineer|support engineer|"
                  r"member of technical staff|amts|mts|quantitative (researcher|developer)|quant (researcher|developer))\b", re.I)
INDIA = re.compile(r"\b(india|bengaluru|bangalore|hyderabad|mumbai|pune|gurugram|gurgaon|noida|chennai|kolkata|delhi)\b", re.I)
SENIOR = re.compile(r"\b(senior|sr\.?|staff|principal|lead|manager|director|head|architect|sde[ -]?3|swe[ -]?3|engineer (?:iii|iv|v|3|4|5))\b", re.I)

def eligibility(locations, countries=(), remote=False):
    locations = " ; ".join(str(x) for x in locations if x)
    if INDIA.search(locations) or any(str(c).upper() in {"IN", "IND", "INDIA"} for c in countries):
        return "india"
    if re.search(r"\b(worldwide|anywhere in the world|global remote)\b", locations, re.I):
        return "global_remote"
    if not locations or (remote and locations.lower().strip() == "remote"):
        return "unknown"
    return "other"

@dataclass
class Result:
    company: str
    status: str = "ok"
    jobs: list = field(default_factory=list)
    total: int = 0
    pages: int = 0
    detail: str = ""
    source_url: str = ""
    checked_at: str = field(default_factory=now)
    scope: str = "whole board"
    def summary(self):
        return {k: v for k, v in vars(self).items() if k != "jobs"} | {"matched": len(self.jobs)}

def normalize(company, raw):
    title = text(raw.get("title"))
    if not title:
        raise ValueError("Job missing title")
    url = canonical_url(company.get("url", ""), raw.get("url"))
    source_id = str(raw.get("source_id") or "")
    source = raw.get("source", company["ats"])
    identity = company["name"].lower() + ":" + source + ":" + (source_id or url)
    key = hashlib.sha256(identity.encode()).hexdigest()[:32]
    locations = raw.get("locations") or [raw.get("location", "")]
    eligible = eligibility(locations, raw.get("countries", []), raw.get("remote", False))
    compensation = raw.get("compensation") or extract_inr_base(text(raw.get("description")))
    requirements = re.search(r"\b(\d{1,2})\+?\s*(?:-|–|to)?\s*(?:\d{1,2})?\s*years?\s+(?:of\s+)?(?:professional\s+|relevant\s+|software development\s+|software engineering\s+)?experience\b", text(raw.get("description")), re.I)
    return {"id": key, "company": company["name"], "title": title, "url": url,
            "location": "; ".join(x for x in locations if x) or "Unknown", "eligibility": eligible,
            "description": text(raw.get("description"))[:16000], "source": source, "source_id": source_id,
            "compensation": compensation, "published_at": raw.get("published_at"),
            "fetched_at": now(), "legacy_ids": raw.get("legacy_ids", []),
            "experience_hint": requirements.group(0) if requirements else "Not extracted; review posting",
            "seniority": "senior" if SENIOR.search(title) else "unspecified"}

def extract_inr_base(description):
    # Only explicit annual base salary evidence; never infer CTC from a company name.
    number = r"([\d,]+(?:\.\d+)?)"
    pattern = re.compile(r"\bbase (?:salary|pay)\b[^.;]{0,50}?(?:INR|₹|Rs\.?)[ ]*" + number +
                         r"(?:\s*[-–—]\s*(?:INR|₹|Rs\.?)?\s*" + number + r")?\s*"
                         r"(lpa|lakhs? per (?:annum|year)|lakhs? annually|per year|per annum|annually)", re.I)
    match = pattern.search(description)
    if not match:
        return {}
    low, high, unit = match.groups()
    scale = 100000 if unit.lower().startswith(("lpa", "lakh")) else 1
    lo = float(low.replace(",", "")) * scale
    hi = float((high or low).replace(",", "")) * scale
    if lo <= 0 or hi < lo:
        return {}
    return {"currency": "INR", "interval": "year", "min": lo, "max": hi,
            "evidence": "employer_disclosed_text", "summary": match.group(0)}

def matches(job):
    if not ROLE.search(job["title"]):
        return False
    allowed = {"india", "global_remote"}
    if os.getenv("INCLUDE_UNKNOWN_LOCATION", "false").lower() == "true":
        allowed.add("unknown")
    if os.getenv("INCLUDE_OVERSEAS", "false").lower() == "true":
        allowed.add("other")
    if job["eligibility"] not in allowed:
        return False
    if os.getenv("EXCLUDE_SENIOR", "true").lower() == "true" and job["seniority"] == "senior":
        return False
    if os.getenv("INCLUDE_INTERNSHIPS", "false").lower() != "true" and re.search(r"\b(intern|internship)\b", job["title"], re.I):
        return False
    minimum = float(os.getenv("MIN_ANNUAL_INR", "1650000"))
    comp = job["compensation"]
    if comp.get("currency") == "INR" and comp.get("interval") == "year" and comp.get("max") is not None:
        if float(comp["max"]) <= minimum:
            return False
    return True

def salary_status(job):
    comp = job.get("compensation", {})
    target = float(os.getenv("MIN_ANNUAL_INR", "1650000"))
    if comp.get("currency") == "INR" and comp.get("interval") == "year":
        if comp.get("min") is not None and float(comp["min"]) > target:
            return "Disclosed base range above target"
        if comp.get("max") is not None and float(comp["max"]) > target:
            return "Range overlaps target; confirm offered base"
    return "Base salary unconfirmed for target"

def rank(job):
    comp = job.get("compensation", {})
    comparable = comp.get("currency") == "INR" and comp.get("interval") == "year"
    hint = re.match(r"(\d+)", job.get("experience_hint", ""))
    early = not hint or int(hint.group(1)) <= 2
    return (early, job["eligibility"] == "india", comparable,
            float(comp.get("min") or 0) if comparable else 0, job.get("published_at") or "")
