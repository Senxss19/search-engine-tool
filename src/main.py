import json
from crawler import Crawler
from indexer import Indexer
from search import SearchEngine

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
    try:
        with open(INDEX_FILE) as f:
            index = json.load(f)

        with open(META_FILE) as f:
            meta = json.load(f)

        print("Index loaded.")
        return index, meta["doc_count"]

    except:
        print("Run build first.")
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