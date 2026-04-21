from src.indexer import Indexer


def test_tokenize_basic():
    idx = Indexer()
    text = "Hello, WORLD!"
    assert idx.tokenize(text) == ["hello", "world"]


def test_tokenize_empty():
    idx = Indexer()
    assert idx.tokenize("") == []


def test_build_index_counts():
    idx = Indexer()
    pages = {"url1": "good good", "url2": "good"}
    index, doc_count = idx.build_index(pages)

    assert index["good"]["docs"]["url1"]["tf"] == 2
    assert index["good"]["df"] == 2


def test_positions():
    idx = Indexer()
    pages = {"url1": "a b a"}
    index, _ = idx.build_index(pages)

    assert index["a"]["docs"]["url1"]["positions"] == [0, 2]