import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class Crawler:
    def __init__(self, base_url, delay=6):
        self.base_url = base_url
        self.delay = delay
        self.last_request_time = 0

        self.session = requests.Session()
        self.session.trust_env = False  # disable proxy

    def fetch_page(self, url):
        elapsed = time.time() - self.last_request_time
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)

        headers = {"User-Agent": "Mozilla/5.0"}
        retries = 3

        for attempt in range(retries):
            try:
                response = self.session.get(
                    url,
                    headers=headers,
                    timeout=20,
                    verify=False
                )
                response.raise_for_status()
                self.last_request_time = time.time()
                return response.text

            except requests.exceptions.Timeout:
                print(f"[Retry {attempt+1}] Timeout: {url}")

            except requests.RequestException as e:
                print(f"Error: {url} -> {e}")
                break

        return None

    def extract_quotes(self, html):
        soup = BeautifulSoup(html, "html.parser")
        quotes = soup.find_all("span", class_="text")
        return [q.get_text() for q in quotes]

    def find_next_page(self, html, current_url):
        soup = BeautifulSoup(html, "html.parser")
        next_btn = soup.find("li", class_="next")
        if next_btn:
            return urljoin(current_url, next_btn.find("a")["href"])
        return None

    def crawl(self):
        pages = {}
        current_url = self.base_url

        while current_url:
            print(f"Crawling: {current_url}")
            html = self.fetch_page(current_url)

            if not html:
                print(f"Skipping {current_url}")
                break

            text = " ".join(self.extract_quotes(html))
            if text.strip():
                pages[current_url] = text

            current_url = self.find_next_page(html, current_url)

        print(f"Total pages: {len(pages)}")
        return pages