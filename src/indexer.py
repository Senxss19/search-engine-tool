import re
from collections import defaultdict


class Indexer:
    """
    Responsible for building the inverted index.
    """

    def __init__(self):
        """"
        Structure:
        word -> {
            "df": document_frequency,
            "docs": {
                url: {
                    "tf": term_frequency,
                    "positions": [...]
                }
            }
        }
        """
        self.index = defaultdict(lambda: {
            "df": 0,
            "docs": defaultdict(lambda: {"tf": 0, "positions": []})
        })
        self.doc_count = 0

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
        seen_words = set()

        for pos, word in enumerate(words):
            entry = self.index[word]["docs"][url]
            entry["tf"] += 1
            entry["positions"].append(pos)

            if word not in seen_words:
                self.index[word]["df"] += 1
                seen_words.add(word)

        self.doc_count += 1

    def build_index(self, pages):
        """
        Build index from all pages.
        pages: dict {url: text}
        """
        for url, text in pages.items():
            self.add_page(url, text)

        return self.index