# Install this upgrade

This package replaces the original runner and adds tested collectors, explicit coverage reporting and a persistent notification queue. It is configured for early-career India roles with **base above INR 16.5 lakh/year**. Unknown salary is retained and labelled; it is not a confirmed above-target offer.

1. Back up your existing repo.
2. Extract the ZIP into the repo root and replace matching files. Include `.github`, `.env.example` and `.gitignore`. **Keep your existing `data/` folder**; the ZIP intentionally does not include production state.
3. Install Python 3.11+ and run:

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m unittest discover -s tests -v
python main.py --api-only
```

4. Inspect `reports/matches.json` and `reports/coverage.json`. This preview sends nothing.
5. Choose the first live run:
   - `python main.py --baseline`: record current jobs without alerts, then alert on future jobs.
   - `python main.py --send`: start sending existing eligible jobs, up to 40 per run.
6. In GitHub, retain/configure the `GMAIL_APP_PASSWORD` secret. The sender and recipient defaults from your repo are retained. Rotate the password if the one previously published in the README was real.
7. Commit/upload the code. In Actions, use **Job Tracker → Run workflow → preview/baseline/send**. Scheduled runs use send mode. Review the uploaded reports.

Your exact internship durations were missing from the message. The package therefore filters senior titles and shows experience evidence without claiming exact eligibility. You can change preferences through environment variables or GitHub repository variables; see README.md.

API sources are checked each run. Browser sources rotate in groups of 36 so the large watchlist fits an hourly Actions run. These generic sources remain partial/unverified until their extraction is independently checked. The audit includes remaining broken URLs; this package does **not** claim working coverage of all 329 entries.

Files to read: `README.md` for settings and limitations, `VALIDATION.md` for testing, `COMPANY_AUDIT.md` for every company's source check, and `scraper/registry.py` for verified source overrides.
