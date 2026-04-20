import re
from collections import defaultdict


class Indexer:
    """
    Responsible for building the inverted index.
    """

    def __init__(self):
        # Structure: word -> url -> {count, positions}
        self.index = defaultdict(lambda: defaultdict(lambda: {"count": 0, "positions": []}))

    def tokenize(self, text):
        """
        Convert text into normalized tokens.
        - Lowercase
        - Remove punctuation
        """
        text = text.lower()
        words = re.findall(r"\b[a-z]+\b", text)
        return words

    def add_page(self, url, text):
        """
        Add a page's content to the index.
        """
        words = self.tokenize(text)

        for position, word in enumerate(words):
            self.index[word][url]["count"] += 1
            self.index[word][url]["positions"].append(position)

    def build_index(self, pages):
        """
        Build index from all pages.
        pages: dict {url: text}
        """
        for url, text in pages.items():
            self.add_page(url, text)

        return self.index