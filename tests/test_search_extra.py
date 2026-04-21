from src.search import SearchEngine

def test_print_word_output(capsys):
    index = {
        "test": {
            "df": 1,
            "docs": {"url1": {"tf": 1, "positions": [0]}}
        }
    }

    engine = SearchEngine(index, 1)
    engine.print_word("test")

    captured = capsys.readouterr()
    assert "url1" in captured.out

def mock_index():
    return {
        "life": {
            "df": 2,
            "docs": {
                "url1": {"tf": 2, "positions": [0, 2]},
                "url2": {"tf": 1, "positions": [1]}
            }
        },
        "love": {
            "df": 1,
            "docs": {
                "url1": {"tf": 1, "positions": [5]}
            }
        }
    }


def test_or_query(capsys):
    engine = SearchEngine(mock_index(), 2)
    engine.find("life OR love")
    captured = capsys.readouterr()
    assert "url1" in captured.out


def test_phrase_not_found(capsys):
    engine = SearchEngine(mock_index(), 2)
    engine.find('"life love"')
    captured = capsys.readouterr()
    assert "No results" in captured.out


def test_suggestion():
    engine = SearchEngine(mock_index(), 2)
    result = engine.suggest("li")
    assert "life" in result


def test_empty_query(capsys):
    engine = SearchEngine(mock_index(), 2)
    engine.find("")
    captured = capsys.readouterr()
    assert "Empty query" in captured.out