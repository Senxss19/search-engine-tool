# Search Engine Tool

## Author

Email: [ml21s2x@leeds.ac.uk](mailto:ml21s2x@leeds.ac.uk)  
GitHub: [https://github.com/Senxss19/search-engine-tool](https://github.com/Senxss19/search-engine-tool)  

---

## Project Overview

This project implements a simple command-line search engine in Python. It is designed to demonstrate the core principles of:

* Web crawling
* Inverted index construction
* Search query processing

The system crawls a target website, builds an inverted index containing word statistics (frequency and positions), and allows users to search for words or phrases via a command-line interface.

---

## Purpose

The purpose of this project is to:

* Understand how search engines work at a fundamental level
* Practice web scraping using Python
* Implement efficient data structures for indexing and searching
* Develop robust software with testing and error handling

---

## Project Structure

```
search-engine-tool/
│
├── src/
│   ├── crawler.py
│   ├── indexer.py
│   ├── search.py
│   └── main.py
│
├── tests/
│   ├── test_crawler.py
│   ├── test_indexer.py
│   └── test_search.py
│
├── data/
│   └── index.json
│
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Installation / Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Senxss19/search-engine-tool.git
cd search-engine-tool
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Dependencies

This project requires:

```txt
requests~=2.33.1
beautifulsoup4~=4.14.3
pytest
urllib3~=2.6.3
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## Usage (Run the Program)

Start the command-line interface:

```bash
python src/main.py
```

---

## Command Usage Examples

### 1. Build (crawl and create index)

```bash
> build
```

Crawls the website and builds the inverted index, saving it to `data/index.json`.

---

### 2. Load (load existing index)

```bash
> load
```

Loads the saved index from the file system.

---

### 3. Print (show word index)

```bash
> print good
```

Displays all pages containing the word "good", including frequency and positions.

---

### 4. Find (search query)

Single word:

```bash
> find indifference
```

Multiple words (AND query):

```bash
> find good friends
```

Returns pages that contain all query words, ranked by total frequency.

---

## Example Run

```bash
> build
Crawling: https://quotes.toscrape.com/
Crawling: https://quotes.toscrape.com/page/2/
...
Total pages: 10
Index built and saved.

> load
Index loaded.

> print good

=== Word: good ===
https://quotes.toscrape.com/
  count: 1
  positions: [76]
https://quotes.toscrape.com/page/2/
  count: 3
  positions: [24, 495, 497]
...

> find indifference

=== Results (ranked) ===
https://quotes.toscrape.com/page/2/ (score=4)

> find good friends

=== Results (ranked) ===
https://quotes.toscrape.com/page/2/ (score=8)
https://quotes.toscrape.com/page/6/ (score=2)
```

---

## Testing Instructions

Run all tests:

```bash
pytest
```

---

### Test Coverage

All tests pass successfully:

* crawler tests: 6 passed
* indexer tests: 4 passed
* search tests: 6 passed

**Total: 16 tests passed**

---

### What is Tested

The test suite covers:

* Tokenization (case normalization, punctuation handling)
* Inverted index correctness (word frequency and positions)
* Search functionality:

  * Single-word queries
  * Multi-word AND queries
  * Result ranking
* Edge cases:

  * Empty queries
  * Non-existent words
  * Duplicate query terms
* Crawler functionality:

  * HTML parsing
  * Next-page detection
  * Mocked HTTP requests (no real network dependency)

This ensures robustness, correctness, and reliability.

---

## Features Summary

The system supports:

* Case-insensitive search
* Multi-word AND queries
* Ranked results based on word frequency
* Inverted index with positional information
* Robust error handling for invalid input and network issues

---

## GenAI Usage Declaration

GenAI tools (e.g., ChatGPT / Copilot) were used to assist in this project.

They were used for:

* Understanding libraries such as requests and BeautifulSoup
* Generating initial code structure
* Debugging and improving error handling

However:

* All code was reviewed, tested, and modified independently
* Core logic (indexing, search, testing) was fully understood and implemented
* Additional edge cases and improvements were added manually

This ensures compliance with academic integrity requirements.