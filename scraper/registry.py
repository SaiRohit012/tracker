"""Original watchlist plus evidence-backed overrides; no fabricated board slugs."""
from scraper.companies import COMPANIES as ORIGINAL

# Official career pages / hosted boards inspected in September 2026.
VERIFIED = [
    {"name": "BrowserStack", "ats": "workday", "url": "https://browserstack.wd3.myworkdayjobs.com/External", "evidence_url": "https://www.browserstack.com/careers"},
    {"name": "Razorpay", "ats": "greenhouse", "greenhouse_id": "razorpaysoftwareprivatelimited", "url": "https://job-boards.greenhouse.io/razorpaysoftwareprivatelimited", "evidence_url": "https://razorpay.com/jobs/"},
    {"name": "Notion India", "ats": "ashby", "ashby_id": "notion", "url": "https://jobs.ashbyhq.com/notion", "evidence_url": "https://www.notion.com/careers"},
    {"name": "Atlan", "ats": "ashby", "ashby_id": "atlan", "url": "https://jobs.ashbyhq.com/atlan", "evidence_url": "https://jobs.ashbyhq.com/atlan"},
    {"name": "Anthropic", "ats": "greenhouse", "greenhouse_id": "anthropic", "url": "https://job-boards.greenhouse.io/anthropic", "evidence_url": "https://job-boards.greenhouse.io/anthropic"},
    {"name": "OpenAI", "ats": "ashby", "ashby_id": "openai", "url": "https://jobs.ashbyhq.com/openai", "evidence_url": "https://openai.com/careers/search/"},
    {"name": "Perplexity", "ats": "ashby", "ashby_id": "perplexity", "url": "https://jobs.ashbyhq.com/perplexity", "evidence_url": "https://www.perplexity.ai/careers"},
    {"name": "Linear", "ats": "ashby", "ashby_id": "linear", "url": "https://jobs.ashbyhq.com/linear", "evidence_url": "https://linear.app/careers"},
    {"name": "Ramp", "ats": "ashby", "ashby_id": "ramp", "url": "https://jobs.ashbyhq.com/ramp", "evidence_url": "https://ramp.com/careers"},
    {"name": "Vercel", "ats": "greenhouse", "greenhouse_id": "vercel", "url": "https://job-boards.greenhouse.io/vercel", "evidence_url": "https://vercel.com/careers"},
    {"name": "Glean", "ats": "greenhouse", "greenhouse_id": "gleanwork", "url": "https://job-boards.greenhouse.io/gleanwork", "evidence_url": "https://www.glean.com/careers"},
    {"name": "Graviton Research Capital", "ats": "greenhouse", "greenhouse_id": "gravitonresearchcapital", "url": "https://job-boards.greenhouse.io/gravitonresearchcapital", "evidence_url": "https://boards.greenhouse.io/embed/job_board?for=gravitonresearchcapital"},
]

def companies():
    entries = {c["name"]: dict(c, verification="legacy_unverified") for c in ORIGINAL}
    for company in VERIFIED:
        entries[company["name"]] = dict(company, verification="board_checked", verified_on="2026-09-19")
    for c in entries.values():
        c["enabled"] = bool(c.get("url")) and "(unconfirmed)" not in c["name"]
    return list(entries.values())
