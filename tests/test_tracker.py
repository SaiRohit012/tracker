import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch, MagicMock

from scraper.core import canonical_url, eligibility, normalize, matches, salary_status, Result, extract_inr_base
from scraper.collectors import collect, convert, endpoint, salary_ashby, workday_rows, india_facet
from scraper.browser import structured_jobs, from_schema
from scraper.storage import save, load, merge, deliver, open_state, pending

C = {"name": "Example", "ats": "greenhouse", "greenhouse_id": "example", "url": "https://jobs.example.com/search?q=engineer"}

def job(**extra):
    return normalize(C, dict(title="Software Engineer", location="Bengaluru", url="/job/123", source_id="123", **extra))

class CoreTests(unittest.TestCase):
    def test_discovery_uses_observed_board_not_company_slug(self):
        from scraper.discover_sources import candidates
        values = candidates("Example", "https://example.com/careers", '<a href="https://job-boards.greenhouse.io/examplecompanyltd">Jobs</a>')
        self.assertEqual(values[0]["greenhouse_id"], "examplecompanyltd")
        self.assertEqual(candidates("Example", "https://example.com/careers", "Nothing here"), [])
    def test_base_salary_extraction_not_ctc(self):
        self.assertEqual(extract_inr_base("Base salary: INR 18–25 LPA plus equity")["min"], 1800000)
        self.assertEqual(extract_inr_base("Base pay: INR 1,800,000 - 2,500,000 per year")["max"], 2500000)
        self.assertEqual(extract_inr_base("Total compensation INR 30 LPA"), {})
        self.assertEqual(extract_inr_base("Base salary $200,000 per year"), {})
    def test_relative_links_and_job_queries(self):
        self.assertEqual(canonical_url(C["url"], "/job/123?jobId=123&utm_source=x"), "https://jobs.example.com/job/123?jobId=123")
        self.assertEqual(canonical_url("https://x.test/a/b", "../job/1"), "https://x.test/job/1")
        for value in ["javascript:alert(1)", "", "mailto:test@example.com"]:
            with self.assertRaises(ValueError):
                canonical_url(C["url"], value)

    def test_remote_is_not_india(self):
        self.assertEqual(eligibility(["Remote - United States"], remote=True), "other")
        self.assertEqual(eligibility(["Remote"], remote=True), "unknown")
        self.assertEqual(eligibility(["Indiana"]), "other")
        self.assertEqual(eligibility(["Worldwide"]), "global_remote")

    def test_same_title_different_requisitions(self):
        a = job()
        b = normalize(C, {"title": a["title"], "source_id": "456", "url": "/job/456", "location": "India"})
        self.assertNotEqual(a["id"], b["id"])

    def test_ashby_secondary_location_and_salary(self):
        c = dict(C, ats="ashby", ashby_id="example")
        raw = convert(c, {"title": "Software Engineer", "id": "x", "location": "London", "jobUrl": "/jobs/x",
                          "secondaryLocations": [{"location": "Bangalore", "address": {"addressCountry": "IND"}}]})
        self.assertTrue(matches(normalize(c, raw)))
        comp = salary_ashby({"summaryComponents": [{"compensationType": "Salary", "currencyCode": "INR", "interval": "1 YEAR", "minValue": 1800000, "maxValue": 2300000}]})
        self.assertEqual(salary_status(job(compensation=comp)), "Disclosed base range above target")

    def test_target_base_exclusive_and_unknown_visible(self):
        self.assertTrue(matches(job()))
        self.assertFalse(matches(job(compensation={"currency": "INR", "interval": "year", "max": 1650000})))
        self.assertTrue(matches(job(compensation={"currency": "INR", "interval": "year", "max": 1800000, "min": 1500000})))
        self.assertIn("overlaps", salary_status(job(compensation={"currency": "INR", "interval": "year", "max": 1800000, "min": 1500000})))
        self.assertIn("unconfirmed", salary_status(job(compensation={"currency": "USD", "interval": "year", "min": 200000})))

    def test_early_career_filter(self):
        for title in ("Senior Software Engineer", "Staff Software Engineer", "Software Engineer Intern"):
            value = job()
            value.update(title=title, seniority="senior" if "Intern" not in title else "unspecified")
            self.assertFalse(matches(value))
        value = normalize(C, {"title": "Software Engineer III", "location": "India", "url": "/job/3"})
        self.assertFalse(matches(value))

    def test_experience_is_evidence_not_invented_user_tenure(self):
        value = job(description="You have 5+ years of professional experience in software.")
        self.assertIn("5+ years", value["experience_hint"])
        self.assertTrue(matches(value))

    def test_workday_endpoint_locale(self):
        c = {"ats": "workday", "url": "https://example.wd5.myworkdayjobs.com/en-US/External/jobs?q=x"}
        self.assertEqual(endpoint(c), "https://example.wd5.myworkdayjobs.com/wday/cxs/example/External/jobs")

    def test_jsonld_graph_and_base_salary(self):
        value = {"@graph": [{"@type": "JobPosting", "title": "Software Engineer", "url": "/job/1",
                            "jobLocation": {"address": {"addressCountry": "IN"}},
                            "baseSalary": {"currency": "INR", "value": {"minValue": 1800000, "maxValue": 2200000, "unitText": "YEAR"}}}]}
        raw = from_schema(next(structured_jobs(value)))
        self.assertTrue(matches(normalize(C, raw)))
        self.assertEqual(raw["compensation"]["min"], 1800000)

class PersistenceTests(unittest.TestCase):
    @patch("scraper.link_check.check_job")
    def test_only_confirmed_missing_links_are_suppressed(self, checker):
        from scraper.link_check import validate_pending
        merge(self.state, Result("Example", jobs=[job()]))
        checker.return_value = {"id": job()["id"], "status": "unverified", "checked_at": "today"}
        validate_pending(self.state, pending(self.state))
        self.assertEqual(len(pending(self.state)), 1)
        checker.return_value = {"id": job()["id"], "status": "unavailable", "checked_at": "today"}
        validate_pending(self.state, pending(self.state))
        self.assertEqual(len(pending(self.state)), 0)

    def setUp(self):
        self.state = {"version": 2, "jobs": {}, "health": {}}

    def test_email_failure_retains_pending(self):
        merge(self.state, Result("Example", jobs=[job()], total=1))
        snapshots = []
        self.assertFalse(deliver(self.state, lambda jobs: False, lambda state: snapshots.append(True)))
        self.assertEqual(len(pending(self.state)), 1)
        self.assertTrue(deliver(self.state, lambda jobs: True, lambda state: snapshots.append(True)))
        self.assertEqual(len(pending(self.state)), 0)

    def test_delivery_cannot_pull_unchecked_replacements(self):
        a = job()
        b = normalize(C, {"title": "Software Engineer", "location": "India", "url": "/job/456", "source_id": "456"})
        merge(self.state, Result("Example", jobs=[a, b]))
        sent = []
        deliver(self.state, lambda jobs: sent.extend(jobs) or True, lambda s: None, allowed_ids={a["id"]})
        self.assertEqual([j["id"] for j in sent], [a["id"]])
        self.assertEqual(len(pending(self.state)), 1)

    def test_stale_pending_jobs_are_withheld(self):
        merge(self.state, Result("Example", jobs=[job()]))
        self.state["jobs"][job()["id"]]["last_seen"] = "2020-01-01T00:00:00+00:00"
        self.assertEqual(pending(self.state), [])

    def test_failure_and_partial_do_not_close_jobs(self):
        merge(self.state, Result("Example", jobs=[job()], total=1))
        for status in ("failed", "partial", "blocked"):
            merge(self.state, Result("Example", status))
            self.assertTrue(self.state["jobs"][job()["id"]]["active"])
        merge(self.state, Result("Example", total=0))
        self.assertFalse(self.state["jobs"][job()["id"]]["active"])

    def test_legacy_api_migration(self):
        value = job(legacy_ids=["gh_example_123"])
        merge(self.state, Result("Example", jobs=[value]), {"gh_example_123"})
        self.assertEqual(len(pending(self.state)), 0)

    def test_inventory_drop_is_suspect(self):
        merge(self.state, Result("Example", jobs=[job()], total=100))
        result = Result("Example", total=0)
        merge(self.state, result)
        self.assertEqual(result.status, "suspect")
        self.assertTrue(self.state["jobs"][job()["id"]]["active"])

    def test_corrupt_state_does_not_reset(self):
        with tempfile.TemporaryDirectory() as folder:
            save(Path(folder) / "tracker_state.json", self.state)
            state, _ = open_state(folder)
            self.assertEqual(state, self.state)
            (Path(folder) / "tracker_state.json").write_text("{broken", encoding="utf-8")
            with self.assertRaises(ValueError):
                open_state(folder)

class CollectorTests(unittest.TestCase):
    def test_workday_zero_total_on_later_pages(self):
        import time
        client = MagicMock()
        def row(n):
            return {"title": "Recruiter", "externalPath": f"/job/place/{n}", "locationsText": "India"}
        response1, response2 = MagicMock(), MagicMock()
        response1.json.return_value = {"total": 23, "jobPostings": [row(n) for n in range(20)]}
        response2.json.return_value = {"total": 0, "jobPostings": [row(n) for n in range(20, 23)]}
        client.post.side_effect = [response1, response2]
        c = dict(C, ats="workday", url="https://example.wd5.myworkdayjobs.com/External")
        result = Result("Example", source_url=endpoint(c))
        rows = workday_rows(client, c, result, time.monotonic() + 30)
        self.assertEqual((len(rows), result.pages, result.status), (23, 2, "ok"))

    def test_nested_india_facet(self):
        facets = [{"values": [{"facetParameter": "country", "values": [{"id": "123", "descriptor": "India"}]}]}]
        self.assertEqual(india_facet(facets), {"country": ["123"]})

    @patch("scraper.collectors.session")
    @patch("scraper.collectors.get_json")
    def test_bad_schema_is_failure(self, fetch, session):
        fetch.return_value = {"error": "board moved"}
        self.assertEqual(collect(C).status, "failed")

    @patch("scraper.collectors.session")
    @patch("scraper.collectors.get_json")
    def test_empty_list_is_success(self, fetch, session):
        fetch.return_value = {"jobs": []}
        self.assertEqual(collect(C).status, "ok")

    @patch("scraper.collectors.session")
    @patch("scraper.collectors.get_json")
    def test_lever_pagination(self, fetch, session):
        def row(n):
            return {"id": str(n), "text": "Software Engineer", "categories": {"location": "India"}, "hostedUrl": f"https://jobs.lever.co/x/{n}"}
        fetch.side_effect = [[row(n) for n in range(100)], [row(100)]]
        result = collect(dict(C, ats="lever", lever_id="x"))
        self.assertEqual((result.status, result.total, result.pages, len(result.jobs)), ("ok", 101, 2, 101))

    @patch("scraper.collectors.session")
    @patch("scraper.collectors.get_json")
    def test_malformed_posting_is_partial(self, fetch, session):
        fetch.return_value = {"jobs": [{"id": 1, "title": "Software Engineer", "location": {"name": "India"}}]}
        self.assertEqual(collect(C).status, "partial")

if __name__ == "__main__":
    unittest.main()
