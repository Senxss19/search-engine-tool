import requests
from unittest.mock import patch, MagicMock
from src.crawler import Crawler


# -------------------------
# Test: fetch_page success
# -------------------------
@patch("src.crawler.requests.Session.get")
def test_fetch_page_success(mock_get):
    mock_response = MagicMock()
    mock_response.text = "<html>OK</html>"
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    crawler = Crawler("http://test.com", delay=0)
    html = crawler.fetch_page("http://test.com")

    assert html == "<html>OK</html>"


# -------------------------
# Test: fetch_page timeout retry
# -------------------------
@patch("src.crawler.requests.Session.get")
def test_fetch_page_timeout(mock_get):
    # simulate real timeout exception
    mock_get.side_effect = requests.exceptions.Timeout()

    crawler = Crawler("http://test.com", delay=0)
    html = crawler.fetch_page("http://test.com")


    assert html is None


# -------------------------
# Test: extract_quotes empty
# -------------------------
def test_extract_quotes_empty():
    crawler = Crawler("http://test.com", delay=0)
    result = crawler.extract_quotes("<html></html>")
    assert result == []


# -------------------------
# Test: find_next_page none
# -------------------------
def test_find_next_page_none():
    crawler = Crawler("http://test.com", delay=0)
    html = "<html></html>"
    assert crawler.find_next_page(html, "http://test.com") is None


# -------------------------
# Test: crawl loop stops when fetch fails
# -------------------------
@patch("src.crawler.Crawler.fetch_page")
def test_crawl_stops_on_fail(mock_fetch):
    mock_fetch.return_value = None

    crawler = Crawler("http://test.com", delay=0)
    pages = crawler.crawl()

    assert pages == {}

# -------------------------
# Retry then success (cover retry branch)
# -------------------------
@patch("src.crawler.requests.Session.get")
def test_fetch_page_retry_then_success(mock_get):
    mock_response = MagicMock()
    mock_response.text = "OK"
    mock_response.raise_for_status.return_value = None

    # first timeout, then success
    mock_get.side_effect = [
        requests.exceptions.Timeout(),
        mock_response
    ]

    crawler = Crawler("http://test.com", delay=0)
    result = crawler.fetch_page("http://test.com")

    assert result == "OK"


# -------------------------
# RequestException branch
# -------------------------
@patch("src.crawler.requests.Session.get")
def test_fetch_page_request_exception(mock_get):
    mock_get.side_effect = requests.exceptions.RequestException("Error")

    crawler = Crawler("http://test.com", delay=0)
    result = crawler.fetch_page("http://test.com")

    assert result is None


# -------------------------
# Crawl multiple pages (next page loop)
# -------------------------
@patch("src.crawler.Crawler.fetch_page")
def test_crawl_multiple_pages(mock_fetch):
    html_page1 = '''
        <span class="text">Quote1</span>
        <li class="next"><a href="/page/2/">Next</a></li>
    '''
    html_page2 = '''
        <span class="text">Quote2</span>
    '''

    mock_fetch.side_effect = [html_page1, html_page2]

    crawler = Crawler("http://test.com", delay=0)
    pages = crawler.crawl()

    assert len(pages) == 2