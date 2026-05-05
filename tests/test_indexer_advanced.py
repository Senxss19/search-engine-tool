from src.indexer import Indexer


# -------------------------
# Test: add_page basic functionality
# -------------------------
def test_add_page_basic():
    idx = Indexer()
    idx.add_page("url1", "hello world hello")

    assert idx.index["hello"]["docs"]["url1"]["tf"] == 2
    assert idx.index["hello"]["df"] == 1
    assert idx.index["world"]["df"] == 1


# -------------------------
# Test: add_page positions
# -------------------------
def test_add_page_positions():
    idx = Indexer()
    idx.add_page("url1", "a b a")

    positions = idx.index["a"]["docs"]["url1"]["positions"]
    assert positions == [0, 2]


# -------------------------
# Test: df should count per document (not per occurrence)
# -------------------------
def test_df_not_duplicated():
    idx = Indexer()
    idx.add_page("url1", "test test test")

    # df should be 1 even though word appears multiple times
    assert idx.index["test"]["df"] == 1


# -------------------------
# Test: multiple documents increase df
# -------------------------
def test_df_multiple_docs():
    idx = Indexer()
    idx.add_page("url1", "hello")
    idx.add_page("url2", "hello")

    assert idx.index["hello"]["df"] == 2


# -------------------------
# Test: build_index empty input
# -------------------------
def test_build_index_empty():
    idx = Indexer()
    index, total_docs = idx.build_index({})

    assert index == {}
    assert total_docs == 0


# -------------------------
# Test: build_index multiple words
# -------------------------
def test_build_index_multiple_words():
    idx = Indexer()
    pages = {
        "url1": "a b c",
        "url2": "b c d"
    }

    index, _ = idx.build_index(pages)

    assert index["b"]["df"] == 2
    assert index["a"]["df"] == 1
    assert index["d"]["df"] == 1


# -------------------------
# Test: build_index positions correctness
# -------------------------
def test_build_index_positions():
    idx = Indexer()
    pages = {"url1": "x y x y"}

    index, _ = idx.build_index(pages)

    assert index["x"]["docs"]["url1"]["positions"] == [0, 2]
    assert index["y"]["docs"]["url1"]["positions"] == [1, 3]


# -------------------------
# Test: tokenize removes punctuation
# -------------------------
def test_tokenize_punctuation():
    idx = Indexer()
    text = "Hello!!! This, is a test..."
    tokens = idx.tokenize(text)

    assert tokens == ["hello", "this", "is", "a", "test"]


# -------------------------
# Test: tokenize numbers removed
# -------------------------
def test_tokenize_numbers():
    idx = Indexer()
    text = "abc123 456def"
    tokens = idx.tokenize(text)

    assert tokens == ["abc", "def"]


# -------------------------
# Test: mixed case normalization
# -------------------------
def test_tokenize_case_insensitive():
    idx = Indexer()
    text = "Apple apple APPLE"
    tokens = idx.tokenize(text)

    assert tokens == ["apple", "apple", "apple"]