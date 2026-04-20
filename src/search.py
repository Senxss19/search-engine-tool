class SearchEngine:
    def __init__(self, index):
        self.index = index

    def print_word(self, word):
        word = word.lower().strip()

        if not word:
            print("Empty word.")
            return

        if word not in self.index:
            print("Word not found.")
            return

        print(f"\n=== Word: {word} ===")
        for url, data in self.index[word].items():
            print(f"{url}")
            print(f"  count: {data['count']}")
            print(f"  positions: {data['positions']}")

    def find(self, query):
        words = list(set(query.lower().split()))  # remove duplicates

        if not words:
            print("Empty query.")
            return

        url_sets = []
        for word in words:
            if word not in self.index:
                print("No results found.")
                return
            url_sets.append(set(self.index[word].keys()))

        results = set.intersection(*url_sets)

        if not results:
            print("No results found.")
            return

        # ⭐ ranking by total frequency
        scored = []
        for url in results:
            score = sum(self.index[word][url]["count"] for word in words)
            scored.append((url, score))

        scored.sort(key=lambda x: x[1], reverse=True)

        print("\n=== Results (ranked) ===")
        for url, score in scored:
            print(f"{url} (score={score})")