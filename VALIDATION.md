# Validation and scope

Prepared 19 September 2026 against repository commit `761921f5375121782f980ad7f043e844506a84be`.

## Automated checks

26 tests pass on Python 3.12, Requests 2.34.2 and Playwright 1.63.0. This includes an opt-in real Chromium test against a local two-page job-board fixture. No live email was sent.

Tests cover safe relative URLs; tracking-parameter removal without dropping job IDs; strict remote/India matching; distinct same-title requisitions; secondary locations; base salary vs CTC; target boundary and unknown salary; senior/intern exclusions; experience evidence; JSON-LD parsing; malformed/empty API responses; Lever pagination; Workday's later-page zero-total behavior; nested India facets; source discovery from observed links; failed email retention; legacy API seen-ID migration; inventory drops; corrupt-state failure; missing-link suppression; stale pending jobs; and prevention of unchecked replacement jobs entering an email batch.

Run the standard suite with `python -m unittest discover -s tests -v`. Enable the Chromium fixture with environment variable `RUN_BROWSER_TESTS=1` after installing Chromium. With no opt-in, that one fixture is skipped.

## Live checks

The 329-entry source audit recorded 43 API endpoints responding with job lists, 133 reachable custom pages needing extraction verification, 128 failed checks, 12 blocks and 13 disabled placeholders. Failures include inherited bad URLs and transient/environment-dependent network failures. Full details and exact check timestamps are in `reports/url-audit.json` and `COMPANY_AUDIT.md`.

Public API collection was exercised across every configured API source. See `reports/full-api-smoke/coverage.json` and `reports/full-api-smoke/matches.json`. The browser watchlist was not exhaustively rendered; `not_run` entries in this API-only report are intentional.

The final API preview checked 102 sources: 41 completed successfully, 2 were partial, 57 failed and 2 were blocked. It produced 98 candidate matches under the configured title/location/pay rules, including undisclosed-pay roles; this is not a claim of 98 suitable or above-target offers. The same report lists 214 browser sources not run and 13 disabled placeholders.

Workday-specific live checks successfully traversed Adobe's 109 India postings over six pages and NVIDIA's 244 India postings over thirteen pages; BrowserStack returned 34 postings over two pages. These counts are snapshots, not promises of current inventory. `reports/workday-verified/coverage.json` records these checks. Changes in role filters after a snapshot can change match counts.

Verified mappings in this upgrade include Vercel → Greenhouse, BrowserStack → Workday, Razorpay → `razorpaysoftwareprivatelimited`, Notion → Ashby, Atlan → Ashby and Anthropic → Greenhouse. The registry preserves official/hosted evidence URLs. Glean and Graviton are added with working public boards. The incorrect guessed Ashby slugs for Scale AI, Retool and Mercury from the ZIP are not installed.

The source discovery command was exercised against Razorpay's official careers page and found its actual Greenhouse board slug. Its output is in `reports/discovery-example.json`.

## Limits

- Complete job coverage is not established for every company. Custom sites still require dedicated adapters; legacy guessed URLs remain clearly identified by the audit.
- Workday uses its careers frontend endpoint, not a stable contractual public API. India country facets are discovered from live responses when available. Company time limits or large inventories can result in partial scans.
- A successful HTTP check is not proof that a job is open. Blocks and timeouts are labelled unverified. Before actual sends, confirmed 404/410 links are withheld.
- Unknown salaries are not guarantees above INR 16.5 LPA. Salary ranges may overlap the target. No CTC/equity conversion is used to claim qualifying base pay.
- Generic browser parsing is deliberately labelled partial even when it yields jobs. It does not infer India from missing location fields.
- SMTP acceptance is the delivery checkpoint; a crash immediately after acceptance can cause a duplicate on retry. State must not have concurrent local writers. GitHub Actions serializes its runs.
- The package does not contain the original app-password text, `.git`, live state, a Python environment or browser binaries. It does not change GitHub, rotate credentials or deploy itself.
