from src.search import SearchEngine


def mock_index():
    return {
        "good": {
            "url1": {"count": 2, "positions": [0, 2]},
            "url2": {"count": 1, "positions": [1]}
        },
        "friends": {
            "url1": {"count": 1, "positions": [1]}
        }
    }


def test_print_existing(capsys):
    engine = SearchEngine(mock_index())
    engine.print_word("good")
    captured = capsys.readouterr()
    assert "url1" in captured.out


def test_print_not_found(capsys):
    engine = SearchEngine(mock_index())
    engine.print_word("unknown")
    assert "Word not found" in capsys.readouterr().out


def test_find_single_word(capsys):
    engine = SearchEngine(mock_index())
    engine.find("good")
    assert "url1" in capsys.readouterr().out


def test_find_multiple_words(capsys):
    engine = SearchEngine(mock_index())
    engine.find("good friends")
    output = capsys.readouterr().out
    assert "url1" in output
    assert "url2" not in output


def test_find_no_result(capsys):
    engine = SearchEngine(mock_index())
    engine.find("friends unknown")
    assert "No results" in capsys.readouterr().out


def test_empty_query(capsys):
    engine = SearchEngine(mock_index())
    engine.find("")
    assert "Empty query" in capsys.readouterr().out