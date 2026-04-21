import json
from unittest.mock import patch, MagicMock
from src import main


# -------------------------
# Test: build() writes files
# -------------------------
@patch("src.main.Crawler")
@patch("src.main.Indexer")
def test_build(mock_indexer, mock_crawler, tmp_path):
    # mock crawler
    mock_crawler.return_value.crawl.return_value = {
        "url1": "hello world"
    }

    # mock indexer
    mock_indexer.return_value.build_index.return_value = (
        {"hello": {}}, 1
    )

    # redirect file paths
    main.INDEX_FILE = tmp_path / "index.json"
    main.META_FILE = tmp_path / "meta.json"

    main.build()

    assert main.INDEX_FILE.exists()
    assert main.META_FILE.exists()


# -------------------------
# Test: load success
# -------------------------
def test_load_success(tmp_path):
    test_file = tmp_path / "index.json"

    with open(test_file, "w") as f:
        json.dump({"test": {}}, f)

    main.INDEX_FILE = test_file

    index, meta = main.load()

    assert index is not None


# -------------------------
# Test: CLI commands
# -------------------------
@patch("builtins.input", side_effect=["exit"])
def test_main_exit(mock_input):
    main.main()  # just ensure it runs without crash


# -------------------------
# Test: unknown command
# -------------------------
@patch("builtins.input", side_effect=["unknown", "exit"])
def test_main_unknown(mock_input, capsys):
    from src import main

    main.main()

    captured = capsys.readouterr()
    assert "Unknown command" in captured.out

@patch("builtins.input", side_effect=["load", "exit"])
@patch("src.main.load", return_value=({"test": {}}, 1))
def test_main_load(mock_load, mock_input):
    main.main()

# -------------------------
# Test print command
# -------------------------
@patch("builtins.input", side_effect=["load", "print test", "exit"])
@patch("src.main.load", return_value=({"test": {"df":1,"docs":{"url":{"tf":1,"positions":[0]}}}}, 1))
def test_main_print(mock_load, mock_input):
    main.main()


# -------------------------
# Test find command
# -------------------------
@patch("builtins.input", side_effect=["load", "find test", "exit"])
@patch("src.main.load", return_value=({"test": {"df":1,"docs":{"url":{"tf":1,"positions":[0]}}}}, 1))
def test_main_find(mock_load, mock_input):
    main.main()


# -------------------------
# Test suggest command
# -------------------------
@patch("builtins.input", side_effect=["load", "suggest te", "exit"])
@patch("src.main.load", return_value=({"test": {"df":1,"docs":{"url":{"tf":1,"positions":[0]}}}}, 1))
def test_main_suggest(mock_load, mock_input):
    main.main()