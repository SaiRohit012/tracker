"""Conservative browser fallback. Partial extraction never reports full coverage."""
import asyncio
import json
import os
import re
from urllib.parse import quote_plus
from scraper.core import Result, normalize, matches, ROLE

def structured_jobs(value):
    if isinstance(value, list):
        for item in value:
            yield from structured_jobs(item)
    elif isinstance(value, dict):
        types = value.get("@type", [])
        if "JobPosting" in ([types] if isinstance(types, str) else types):
            yield value
        for key in ("@graph", "itemListElement", "item"):
            if key in value:
                yield from structured_jobs(value[key])

def from_schema(item):
    locations, countries = [], []
    locs = item.get("jobLocation") or []
    if isinstance(locs, dict):
        locs = [locs]
    for loc in locs:
        address = loc.get("address") or {}
        if isinstance(address, str):
            locations.append(address)
        else:
            locations.append(", ".join(str(address.get(k, "")) for k in ("addressLocality", "addressRegion", "addressCountry") if address.get(k)))
            countries.append(address.get("addressCountry", ""))
    requirements = item.get("applicantLocationRequirements") or []
    if isinstance(requirements, dict):
        requirements = [requirements]
    countries += [x.get("name", "") for x in requirements if isinstance(x, dict)]
    salary = item.get("baseSalary") or {}
    if isinstance(salary, list):
        salary = salary[0] if len(salary) == 1 else {}
    val = salary.get("value") or {}
    if not isinstance(val, dict):
        val = {"value": val}
    identifier = item.get("identifier") or {}
    return {"title": item.get("title"), "url": item.get("url"),
            "source_id": identifier.get("value") if isinstance(identifier, dict) else identifier,
            "locations": locations, "countries": countries,
            "remote": item.get("jobLocationType") == "TELECOMMUTE",
            "description": item.get("description"), "published_at": item.get("datePosted"),
            "compensation": {"currency": salary.get("currency"), "interval": str(val.get("unitText", "")).lower(),
                             "min": val.get("minValue", val.get("value")), "max": val.get("maxValue", val.get("value")),
                             "evidence": "employer_disclosed"} if salary else {}}

# Resolve links in the browser using DOM URL semantics, not string concatenation.
CARDS = """() => Array.from(document.querySelectorAll('a[href]')).map(a => {
 const card = a.closest('li, tr, article, [class*="job-card"], [class*="posting"], [data-job-id]');
 return {title: (a.innerText || '').trim(), url: a.href, card: card ? card.innerText : ''};
}).filter(x => /\\/(job|jobs|position|positions|opening|openings|careers|role)(\\/|[-?])/i.test(x.url))"""

async def one(browser, company):
    result = Result(company["name"], status="partial", source_url=company["url"])
    context = await browser.new_context()
    page = await context.new_page()
    page.set_default_timeout(12000)
    found, visited = {}, set()
    try:
        # Fetch broad results, then filter locally. Custom sites can configure selectors.
        await page.goto(company["url"].replace("{role}", quote_plus("engineer")), wait_until="domcontentloaded", timeout=25000)
        for page_number in range(int(os.getenv("BROWSER_MAX_PAGES", "12"))):
            await page.wait_for_timeout(1200)
            body = await page.locator("body").inner_text()
            if re.search(r"verify you are human|access denied|captcha|just a moment", body[:4000], re.I):
                result.status, result.detail = "blocked", "Access challenge; no bypass attempted"
                break
            signature = await page.locator("body").inner_text()
            if signature in visited:
                result.detail = "Pagination repeated content"
                break
            visited.add(signature)
            result.pages += 1
            for blob in await page.locator('script[type="application/ld+json"]').all_text_contents():
                try:
                    for item in structured_jobs(json.loads(blob)):
                        raw = from_schema(item)
                        job = normalize(company, raw)
                        found[job["url"]] = job
                except (ValueError, TypeError, AttributeError):
                    pass
            cards = await page.evaluate(CARDS)
            for card in cards:
                if not ROLE.search(card["title"]) or len(card["title"]) > 250:
                    continue
                try:
                    # A card may include a description; don't infer geography from arbitrary text.
                    job = normalize(company, {"title": card["title"], "url": card["url"]})
                    if job["url"] not in found:
                        found[job["url"]] = job
                except ValueError:
                    pass
            selector = company.get("next_selector", 'a[rel="next"], button[aria-label="Next"], button[aria-label="Next page"], a[aria-label="Next page"]')
            next_button = page.locator(selector).first
            if not await next_button.count() or not await next_button.is_visible() or not await next_button.is_enabled() or await next_button.get_attribute("aria-disabled") == "true":
                result.detail = "Generic extraction; site-specific pagination/coverage not verified"
                break
            await next_button.click()
        # Fetch detail pages for role candidates to obtain structured location/salary evidence.
        candidates = list(found.values())
        cap = int(os.getenv("BROWSER_MAX_DETAILS", "30"))
        for job in candidates[:cap]:
            if job["eligibility"] != "unknown":
                continue
            try:
                response = await page.goto(job["url"], wait_until="domcontentloaded", timeout=18000)
                if response and response.status >= 400:
                    continue
                for blob in await page.locator('script[type="application/ld+json"]').all_text_contents():
                    for item in structured_jobs(json.loads(blob)):
                        raw = from_schema(item)
                        raw["url"] = raw.get("url") or job["url"]
                        enhanced = normalize(company, raw)
                        if enhanced["url"] == job["url"]:
                            found[job["url"]] = enhanced
            except Exception:
                continue
        result.total = len(found)
        result.jobs = [j for j in found.values() if matches(j)]
        if not found and result.status != "blocked":
            result.status, result.detail = "unverified", "No structured postings extracted; not proof of zero openings"
        elif len(candidates) > cap:
            result.detail += f"; detail limit {cap}/{len(candidates)}"
    except Exception as exc:
        result.status, result.detail = "failed", f"{type(exc).__name__}: {exc}"[:350]
    finally:
        await context.close()
    return result

async def collect_all(companies):
    from playwright.async_api import async_playwright
    semaphore = asyncio.Semaphore(3)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        async def bounded(company):
            async with semaphore:
                try:
                    return await asyncio.wait_for(one(browser, company), timeout=int(os.getenv("BROWSER_COMPANY_SECONDS", "90")))
                except Exception as exc:
                    return Result(company["name"], "failed", detail=f"Browser budget/error: {type(exc).__name__}")
        try:
            return await asyncio.gather(*(bounded(c) for c in companies))
        finally:
            await browser.close()
