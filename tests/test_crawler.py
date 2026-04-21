from src.crawler import Crawler
from unittest.mock import patch

@patch("src.crawler.requests.Session.get")
def test_fetch_page(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "<html></html>"

    crawler = Crawler("http://test.com", delay=0)
    html = crawler.fetch_page("http://test.com")

    assert html is not None

def test_extract_quotes_single():
    """
    Test extracting a single quote from HTML.
    """
    crawler = Crawler("http://dummy.com")

    html = '<span class="text">Hello world</span>'
    quotes = crawler.extract_quotes(html)

    assert quotes == ["Hello world"]


def test_extract_quotes_multiple():
    """
    Test extracting multiple quotes.
    """
    crawler = Crawler("http://dummy.com")

    html = """
    <span class="text">Quote one</span>
    <span class="text">Quote two</span>
    """
    quotes = crawler.extract_quotes(html)

    assert quotes == ["Quote one", "Quote two"]


def test_extract_quotes_empty():
    """
    Test HTML with no quotes.
    """
    crawler = Crawler("http://dummy.com")

    html = "<html></html>"
    quotes = crawler.extract_quotes(html)

    assert quotes == []


def test_find_next_page_exists():
    """
    Test detection of next page link.
    """
    crawler = Crawler("http://quotes.toscrape.com")

    html = """
    <li class="next">
        <a href="/page/2/">Next</a>
    </li>
    """

    next_url = crawler.find_next_page(html, "http://quotes.toscrape.com")

    assert next_url == "http://quotes.toscrape.com/page/2/"


def test_find_next_page_none():
    """
    Test when there is no next page.
    """
    crawler = Crawler("http://dummy.com")

    html = "<html></html>"
    next_url = crawler.find_next_page(html, "http://dummy.com")

    assert next_url is None

def test_fetch_page_mock():
    """
    Test fetch_page using mocked response.
    """
    crawler = Crawler("http://dummy.com")

    with patch.object(crawler.session, "get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "<html>OK</html>"
        mock_get.return_value.raise_for_status = lambda: None

        result = crawler.fetch_page("http://dummy.com")

        assert result == "<html>OK</html>"

def test_extract_quotes():
    html = '<span class="text">Hello world</span>'
    crawler = Crawler("http://test.com", delay=0)

    quotes = crawler.extract_quotes(html)
    assert quotes == ["Hello world"]


def test_find_next_page():
    html = '<li class="next"><a href="/page/2/">Next</a></li>'
    crawler = Crawler("http://test.com", delay=0)

    next_url = crawler.find_next_page(html, "http://test.com")
    assert "page/2" in next_url

