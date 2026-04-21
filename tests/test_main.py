from src.main import load


def test_load_no_file(capsys):
    from src import main

    main.INDEX_FILE = "non_existent_file.json"

    index, meta = main.load()

    assert index is None


def test_load_success(tmp_path):
    import json
    from src import main

    # create fake index file
    test_file = tmp_path / "index.json"
    with open(test_file, "w") as f:
        json.dump({"test": {}}, f)

    main.INDEX_FILE = str(test_file)

    index, meta = main.load()

    assert index is not None