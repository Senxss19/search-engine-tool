import json
from crawler import Crawler
from indexer import Indexer
from search import SearchEngine

INDEX_FILE = "data/index.json"
BASE_URL = "https://quotes.toscrape.com/"


def build():
    """
    Crawl website and build index.
    """
    crawler = Crawler(BASE_URL)
    pages = crawler.crawl()

    indexer = Indexer()
    index = indexer.build_index(pages)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)

    print("Index built and saved.")


def load():
    """
    Load index from file.
    """
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            index = json.load(f)
        print("Index loaded.")
        return index
    except FileNotFoundError:
        print("Index file not found. Run 'build' first.")
        return None


def main():
    index = None
    engine = None

    while True:
        command = input("> ").strip()

        if command == "build":
            build()

        elif command == "load":
            index = load()
            if index:
                engine = SearchEngine(index)

        elif command.startswith("print "):
            if not engine:
                print("Load index first.")
                continue
            word = command.split(" ", 1)[1]
            engine.print_word(word)

        elif command.startswith("find "):
            if not engine:
                print("Load index first.")
                continue
            query = command.split(" ", 1)[1]
            engine.find(query)

        elif command == "exit":
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()