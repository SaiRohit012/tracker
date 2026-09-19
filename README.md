# Job Tracker v2

Personal job alerts for early-career software/data roles in India and explicitly worldwide remote roles. Target: **base salary above INR 16,50,000 per year**. Unknown salary remains visible and is labelled unconfirmed. Bonus/equity are never counted toward the base threshold. Senior-titled jobs and internships are excluded by default. Duration of prior internships was not supplied; no exact years-of-experience eligibility is claimed.

Simple experience phrases from job descriptions are shown in alerts. Roles mentioning more than two years are ranked lower, not automatically excluded: descriptions can mix mandatory and preferred requirements. Check the actual posting against your experience.

## Install / upgrade

1. Back up your repository. Extract this package into the repository root, replacing matching code files, including the hidden `.github` folder. Do **not** delete your existing `data/seen_jobs.json` or `data/scraper_health.json`. This package intentionally excludes your live state.
2. Use Python 3.11 or later: `python -m pip install -r requirements.txt` then `python -m playwright install chromium`. Linux CI uses `python -m playwright install --with-deps chromium`.
3. Run `python -m unittest discover -s tests -v`.
4. Preview: `python main.py --api-only`. Reports are written under `reports/`; no email or persistent state changes occur. Full preview: `python main.py`.
5. Review `reports/matches.json` and `reports/coverage.json`. To suppress an initial flood of existing matches, run `python main.py --baseline` once. To receive them instead, use `python main.py --send`; at most 40 pending jobs are sent per run.
6. Configure `GMAIL_APP_PASSWORD` in GitHub Actions secrets. The existing sender/recipient defaults are retained; optional `SENDER_EMAIL` and `RECIPIENT_EMAIL` repository variables override them. Set other preferences through repository variables or shell environment variables (see `.env.example`). `.env` files are not automatically loaded.
7. Push your code and manually run the Job Tracker workflow. The supplied workflow runs hourly at minute 17 and persists state even if email fails. API sources run every time; up to 36 browser sources rotate per run (about seven runs for the current watchlist), so the job fits the hosted runner budget. Set `BROWSER_COMPANIES_PER_RUN` for a different budget, or use `--company` for an explicit selection. The validator runs weekly and on manual dispatch. No deployment or push was performed when preparing this package.

The previous public README contained an apparent app password. If real, revoke it and create a replacement. This package removes it from documentation; it cannot revoke it or remove old Git history.

## What changed

- Public Greenhouse, Lever and Ashby adapters with explicit schema checks, bounded transient retries and Lever pagination; documented Greenhouse board host.
- Workday careers frontend adapter with offset pagination and detail enrichment for relevant India/multiple-location postings. This endpoint is **not** a guaranteed stable public API; unsupported tenants are reported as failed.
- Stable source IDs/canonical URLs instead of title-only deduplication. Original Greenhouse/Lever seen IDs migrate. Old browser title IDs cannot be safely mapped: use `--baseline` to prevent a one-time refreshed browser digest.
- Atomic state, a persistent pending queue, and delivered status only after SMTP acceptance. Delivery is at-least-once: a crash between SMTP acceptance and state save can duplicate an email. No claim of exactly-once delivery.
- Official structured salary ranges retained where available (Ashby, Lever, JSON-LD). INR annual base is compared with your target; foreign currency, undisclosed pay, and ambiguous multi-tier compensation remain unconfirmed. No inferred company salary guarantees.
- India matching uses location/country evidence, including Ashby secondary locations. Remote-US does not pass as India. Unknown locations are excluded unless enabled. Visa, citizenship, experience and legal work eligibility still require reading the posting.
- Generic browser fallback resolves URLs correctly, follows recognized next-page controls, reads JobPosting JSON-LD and inspects a bounded number of details. Generic coverage is always partial/unverified, never advertised as complete. Sources with no structured location may yield no alerts until a dedicated parser is added.
- Per-company total counts, pages, matched counts, exact statuses and last successful collection; large inventory drops are flagged. Only successful complete scans can retire absent matches. Notifications retry independently of new collection.
- Registry preserves original watchlist with explicit unverified status and disables empty placeholders. New verified sources include Glean and Graviton, plus verified additions from the ZIP. Vercel uses Greenhouse; guessed Scale AI/Retool/Mercury Ashby boards are not added.

## Commands

```
python main.py --company Glean --company Graviton
python main.py --api-only --baseline
python main.py --send --max-emails-jobs 40
python -m scraper.validate_urls --json reports/url-audit.json
python -m scraper.validate_urls --company Vercel
python -m scraper.discover_sources --name Razorpay --official-url https://razorpay.com/jobs/
```

`--company` takes case-insensitive substrings. Preview writes reports only. `--baseline` writes state without email. `--send` writes state and can send email. Do not run simultaneous local writers against the same state directory. GitHub Actions uses a concurrency group to serialize scheduled/manual runs.

## Configuration

Set `MIN_ANNUAL_INR` (default 1650000), `EXCLUDE_SENIOR` (true), `INCLUDE_INTERNSHIPS` (false), `INCLUDE_OVERSEAS` (false), or `INCLUDE_UNKNOWN_LOCATION` (false) as environment variables. A known INR annual maximum **at or below** the threshold is excluded; an overlapping range is labelled accordingly, not treated as a guaranteed qualifying offer. Lack of salary data does not exclude a potentially valuable role. Rank prioritizes India eligibility and disclosed comparable INR base; it does not rank companies by guessed pay.

Edit `scraper/registry.py` for verified overrides/additions. The old `scraper/companies.py` is retained as a legacy candidate list; its comments are historical claims, not current verification. Do not edit the old `scraper/config.py` to change v2 settings; `.env.example` documents the active settings. Unused old scraper/notifier files may remain after overlaying the upgrade, but the new runner does not import them.

## Understanding reliability reports

`ok` = API collection completed and schema validated; `partial` = bounded/incomplete extraction; `suspect` = major inventory drop; `blocked` = access denied/rate limited; `failed` = network/schema/parser failure; `unverified` = no trusted extraction evidence; `disabled` = placeholder. A board with zero postings can be legitimate, but the URL audit flags it for ownership/source verification. `reachable_unverified` only means the careers page responded. HTTP status alone cannot prove complete coverage.

Inspect the bundled `reports/url-audit.json` for point-in-time checks and `VALIDATION.md` for the verification performed. Scores/counts describe checked sources, not a guarantee of all companies' jobs. The large legacy watchlist still needs verified mappings or dedicated parsers for some companies.

Before sending, queued job URLs are checked: HTTP 404/410 is suppressed, while blocks/timeouts remain explicitly unverified. HTTP 200 only establishes reachability, not that an employer is still accepting applications. Pending jobs not observed for seven days are withheld until seen again. Source discovery reads actual ATS links from an official page and proposes registry changes for review; it cannot identify every embedded/custom recruitment system.

Official references: [Greenhouse](https://docs.greenhouse.io/job-board.html), [Lever](https://github.com/lever/postings-api), [Ashby](https://developers.ashbyhq.com/docs/public-job-posting-api).
