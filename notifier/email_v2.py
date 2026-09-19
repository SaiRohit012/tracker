"""Escaped email content and explicit SMTP acceptance results."""
import html
import logging
import os
import smtplib
from email.message import EmailMessage
from scraper.core import salary_status

def send(subject, body):
    sender = os.getenv("SENDER_EMAIL", "n8nworkflow2026@gmail.com")
    recipient = os.getenv("RECIPIENT_EMAIL", "shaiksairohit@gmail.com")
    password = os.getenv("GMAIL_APP_PASSWORD", "")
    if not password:
        logging.error("GMAIL_APP_PASSWORD missing; pending messages retained")
        return False
    message = EmailMessage()
    message["Subject"], message["From"], message["To"] = subject, sender, recipient
    message.set_content("Your job tracker report is available in the HTML part of this email.")
    message.add_alternative(body, subtype="html")
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=30) as server:
            server.login(sender, password.replace(" ", ""))
            refused = server.send_message(message)
        return not refused
    except Exception as exc:
        logging.error("Email failed: %s; message retained for retry", type(exc).__name__)
        return False

def digest(jobs):
    esc = lambda value: html.escape(str(value or ""), quote=True)
    rows = []
    for job in jobs:
        comp = job.get("compensation", {})
        pay = comp.get("summary") or (f"{comp.get('currency')} {comp.get('min')}–{comp.get('max')} / {comp.get('interval')}" if comp.get("currency") else "Not disclosed")
        rows.append(f'<tr><td>{esc(job["company"])}</td><td>{esc(job["title"])}<br>{esc(job.get("experience_hint", "Review requirements"))}</td>'
                    f'<td>{esc(job["location"])}</td><td>{esc(pay)}<br>{esc(salary_status(job))}</td>'
                    f'<td><a href="{esc(job["url"])}">Official job</a><br>{esc(job.get("link_status", "unverified"))}</td></tr>')
    body = '<h2>Job opportunities</h2><p>Target: early career, India / eligible remote, base above ₹16.5 LPA. Unknown salaries require confirmation.</p><table border="1" cellpadding="8"><tr><th>Company</th><th>Role</th><th>Location</th><th>Compensation</th><th>Link</th></tr>' + "".join(rows) + '</table><p>Employer-disclosed ranges are not a guaranteed offer. Check work eligibility and requirements in each posting.</p>'
    return send(f"[Job Tracker] {len(jobs)} opportunities", body)

def health_alert(entries):
    body = "<h2>Sources need attention</h2><ul>" + "".join(
        f"<li>{html.escape(x['company'])}: {html.escape(x['status'])} — {html.escape(x['detail'])}</li>" for x in entries) + "</ul><p>See the latest Actions coverage report for every company's status.</p>"
    return send(f"[Job Tracker] {len(entries)} sources need attention", body)
