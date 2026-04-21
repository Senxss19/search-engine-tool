import re
from collections import defaultdict


class Indexer:
    """
    Builds an inverted index with:
    - term frequency (tf)
    - document frequency (df)
    - positional information
    """

    def __init__(self):
        self.index = defaultdict(lambda: {
            "df": 0,
            "docs": defaultdict(lambda: {"tf": 0, "positions": []})
        })
        self.doc_count = 0

    def tokenize(self, text):
        """
        Normalize text into tokens:
        - lowercase
        - remove punctuation
        """
        text = text.lower()
        return re.findall(r"\b[a-z]+\b", text)

    def add_page(self, url, text):
        """
        Add a single page to the index.
        """
        words = self.tokenize(text)
        seen = set()

        for pos, word in enumerate(words):
            entry = self.index[word]["docs"][url]
            entry["tf"] += 1
            entry["positions"].append(pos)

            if word not in seen:
                self.index[word]["df"] += 1
                seen.add(word)

        self.doc_count += 1

    def build_index(self, pages):
        """
        Build index from all pages.
        """
        for url, text in pages.items():
            self.add_page(url, text)

        return self.index, self.doc_count