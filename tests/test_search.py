from src.search import SearchEngine

def mock_index():
    return {
        "good": {
            "df": 2,
            "docs": {
                "url1": {"tf": 2, "positions": [0, 2]},
                "url2": {"tf": 1, "positions": [1]}
            }
        },
        "friends": {
            "df": 1,
            "docs": {
                "url1": {"tf": 1, "positions": [3]}
            }
        }
    }

def test_print_existing(capsys):
    engine = SearchEngine(mock_index(), total_docs=2)
    engine.print_word("good")
    captured = capsys.readouterr()
    assert "url1" in captured.out


def test_print_not_found(capsys):
    engine = SearchEngine(mock_index(), total_docs=2)
    engine.print_word("unknown")
    assert "Word not found" in capsys.readouterr().out


def test_find_single_word(capsys):
    engine = SearchEngine(mock_index(), total_docs=2)
    engine.find("good")
    assert "url1" in capsys.readouterr().out


def test_find_multiple_words(capsys):
    engine = SearchEngine(mock_index(), total_docs=2)
    engine.find("good friends")
    output = capsys.readouterr().out
    assert "url1" in output
    assert "url2" not in output


def test_find_no_result(capsys):
    engine = SearchEngine(mock_index(), total_docs=2)
    engine.find("friends unknown")
    assert "No results" in capsys.readouterr().out


def test_empty_query(capsys):
    engine = SearchEngine(mock_index(), total_docs=2)
    engine.find("")
    assert "Empty query" in capsys.readouterr().out

def test_tfidf():
    index = {
        "hello": {
            "df": 1,
            "docs": {
                "url1": {"tf": 2, "positions": [0, 3]}
            }
        }
    }

    engine = SearchEngine(index, total_docs=2)

    score = engine.compute_tfidf("hello", "url1")
    assert score > 0