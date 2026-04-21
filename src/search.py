import math


class SearchEngine:
    """
    Search engine supporting:
    - TF-IDF ranking
    - Boolean queries (AND / OR)
    - Phrase search
    - Query suggestions
    """

    def __init__(self, index, total_docs):
        self.index = index
        self.total_docs = total_docs

    # -------------------------
    # TF-IDF
    # -------------------------
    def compute_tfidf(self, word, url):
        """
        Safe TF-IDF computation.
        Returns 0 if the word does not appear in the document.
        """
        if url not in self.index[word]["docs"]:
            return 0

        tf = self.index[word]["docs"][url]["tf"]
        df = self.index[word]["df"]

        idf = math.log((self.total_docs + 1) / (df + 1)) + 1
        return tf * idf

    # -------------------------
    # Query parsing
    # -------------------------
    def parse_query(self, query):
        if '"' in query:
            return "PHRASE", query.replace('"', '').split()
        elif " AND " in query:
            return "AND", query.split(" AND ")
        elif " OR " in query:
            return "OR", query.split(" OR ")
        else:
            return "AND", query.split()

    # -------------------------
    # Phrase search
    # -------------------------
    def phrase_match(self, words, url):
        positions_lists = [
            self.index[word]["docs"][url]["positions"]
            for word in words
        ]

        for pos in positions_lists[0]:
            if all((pos + i) in positions_lists[i] for i in range(len(words))):
                return True
        return False

    # -------------------------
    # Suggestion
    # -------------------------
    def suggest(self, prefix):
        prefix = prefix.lower()
        return [w for w in self.index if w.startswith(prefix)][:5]

    # -------------------------
    # Print index
    # -------------------------
    def print_word(self, word):
        word = word.lower()
        if word not in self.index:
            print("Word not found.")
            return

        print(f"\n=== {word} ===")
        for url, data in self.index[word]["docs"].items():
            print(f"{url}")
            print(f"  tf: {data['tf']}")
            print(f"  positions: {data['positions']}")

    def find(self, query):
        """
        Search documents based on query.

        Supports:
        - AND / OR queries
        - Phrase search
        - TF-IDF ranking
        """

        # -------------------------
        # 1. Validate input
        # -------------------------
        if not query.strip():
            print("Empty query.")
            return

        # -------------------------
        # 2. Parse query
        # -------------------------
        mode, words = self.parse_query(query)
        words = [w.lower() for w in words]

        # remove duplicates to avoid redundant computation
        words = list(set(words))

        # -------------------------
        # 3. Collect candidate URLs
        # -------------------------
        url_sets = []

        for word in words:
            if word not in self.index:
                print("No results found.")
                return

            urls = set(self.index[word]["docs"].keys())
            url_sets.append(urls)

        # -------------------------
        # 4. Combine results
        # -------------------------
        if mode in ["AND", "PHRASE"]:
            results = set.intersection(*url_sets)
        elif mode == "OR":
            results = set.union(*url_sets)
        else:
            results = set()

        # -------------------------
        # 5. Phrase filtering
        # -------------------------
        if mode == "PHRASE":
            results = {
                url for url in results
                if self.phrase_match(words, url)
            }

        # -------------------------
        # 6. Handle no results
        # -------------------------
        if not results:
            print("No results found.")
            return

        # -------------------------
        # 7. Ranking (TF-IDF)
        # -------------------------
        scored = []

        for url in results:
            score = 0

            for word in words:
                # safe TF-IDF (avoid KeyError)
                if url in self.index[word]["docs"]:
                    score += self.compute_tfidf(word, url)

            scored.append((url, score))

        # sort by score descending
        scored.sort(key=lambda x: x[1], reverse=True)

        # -------------------------
        # 8. Output results
        # -------------------------
        print("\n=== Results ===")

        for url, score in scored:
            print(f"{url} (score={score:.4f})")