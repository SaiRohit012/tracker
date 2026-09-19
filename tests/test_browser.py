"""Opt-in real Chromium fixture: RUN_BROWSER_TESTS=1 python -m unittest discover -s tests."""
import asyncio
import json
import os
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from scraper.browser import collect_all

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        n = "2" if self.path.startswith("/page2") else "1"
        item = {"@type": "JobPosting", "title": "Software Engineer", "url": "/job/" + n,
                "jobLocation": {"address": {"addressCountry": "IN"}},
                "baseSalary": {"currency": "INR", "value": {"minValue": 1800000, "maxValue": 2500000, "unitText": "YEAR"}}}
        next_link = '<a rel="next" href="/page2">Next</a>' if n == "1" else ""
        content = ('<html><body><script type="application/ld+json">' + json.dumps(item) + '</script><p>Page ' + n + '</p>' + next_link + '</body></html>').encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(content)
    def log_message(self, *args):
        pass

@unittest.skipUnless(os.getenv("RUN_BROWSER_TESTS") == "1", "opt-in Chromium fixture")
class BrowserTests(unittest.TestCase):
    def test_real_browser_pagination_and_links(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            url = f"http://127.0.0.1:{server.server_port}/careers"
            result = asyncio.run(collect_all([{"name": "Fixture", "ats": "playwright", "url": url}]))[0]
            self.assertEqual((result.status, result.pages, len(result.jobs)), ("partial", 2, 2))
            self.assertTrue(all(j["url"].startswith(f"http://127.0.0.1:{server.server_port}/job/") for j in result.jobs))
        finally:
            server.shutdown()
            server.server_close()
            worker.join()
