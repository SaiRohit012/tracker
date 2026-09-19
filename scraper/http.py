import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def session():
    client = requests.Session()
    retry = Retry(total=2, backoff_factor=0.7, status_forcelist=[429, 500, 502, 503, 504],
                  allowed_methods=["GET"], respect_retry_after_header=False)
    client.mount("https://", HTTPAdapter(max_retries=retry))
    client.headers["User-Agent"] = "JobTracker/2.0 (personal job alerts; public careers data)"
    return client

def get_json(client, url, **kwargs):
    response = client.get(url, timeout=(8, 25), **kwargs)
    response.raise_for_status()
    return response.json()
