import json
from src.crawler import Crawler
from src.indexer import Indexer
from src.search import SearchEngine

INDEX_FILE = "data/index.json"
META_FILE = "data/meta.json"
BASE_URL = "https://quotes.toscrape.com/"


def build():
    crawler = Crawler(BASE_URL)
    pages = crawler.crawl()

    indexer = Indexer()
    index, doc_count = indexer.build_index(pages)

    with open(INDEX_FILE, "w") as f:
        json.dump(index, f)

    with open(META_FILE, "w") as f:
        json.dump({"doc_count": doc_count}, f)

    print("Index built.")


def load():
    """
    Load index from file system.
    Returns:
        (index, metadata)
    """
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        print("Index loaded.")
        return data, {}   # keep interface consistent

    except FileNotFoundError:
        print("Index file not found. Run 'build' first.")
        return None, None


def main():
    engine = None

    while True:
        cmd = input("> ").strip()

        if cmd == "build":
            build()

        elif cmd == "load":
            index, doc_count = load()
            if index:
                engine = SearchEngine(index, doc_count)

        elif cmd.startswith("print "):
            engine.print_word(cmd.split(" ", 1)[1])

        elif cmd.startswith("find "):
            engine.find(cmd.split(" ", 1)[1])

        elif cmd.startswith("suggest "):
            print(engine.suggest(cmd.split(" ", 1)[1]))

        elif cmd == "exit":
            break

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()