# 🔍 Search Engine Tool  
![CI](https://github.com/Senxss19/search-engine-tool/actions/workflows/test.yml/badge.svg)
![GitHub stars](https://img.shields.io/github/stars/Senxss19/search-engine-tool?style=social)
![GitHub forks](https://img.shields.io/github/forks/Senxss19/search-engine-tool?style=social)
![GitHub issues](https://img.shields.io/github/issues/Senxss19/search-engine-tool)
![GitHub license](https://img.shields.io/github/license/Senxss19/search-engine-tool)

![Python](https://img.shields.io/badge/python-3.12-blue)
![pytest](https://img.shields.io/badge/tests-pytest-green)
![coverage](https://img.shields.io/badge/coverage-90%25-brightgreen)

![Last Commit](https://img.shields.io/github/last-commit/Senxss19/search-engine-tool)
![Repo Size](https://img.shields.io/github/repo-size/Senxss19/search-engine-tool)

A mini search engine built in Python that demonstrates core information retrieval techniques, including web crawling, inverted indexing, and advanced query processing.

---

## 👤 Author

- Email: ml21s2x@leeds.ac.uk  
- GitHub: https://github.com/Senxss19/search-engine-tool  

---

## 📌 Project Overview

This project implements a command-line search engine capable of:

- Crawling a website with politeness constraints
- Building an inverted index with positional information
- Supporting advanced search queries
- Ranking results using TF-IDF

The system is designed to simulate how real-world search engines process and retrieve information.

---

## 🧠 Key Features

### 🔹 Core Features
- Web crawler with politeness delay (6 seconds)
- Inverted index with:
  - term frequency (TF)
  - document frequency (DF)
  - word positions
- Case-insensitive tokenization

---

### 🔹 Advanced Features (High-Distinction Level)

- ✅ **TF-IDF Ranking**
- ✅ **Boolean Queries**
  - AND (default)
  - OR
- ✅ **Phrase Search**
  - `"exact phrase"`
- ✅ **Query Suggestions**
  - Prefix-based suggestions
- ✅ **Efficient Query Processing**

---

## 🏗️ System Architecture

```

```
    +-------------+
    |  Crawler    |
    +-------------+
           ↓
    +-------------+
    |  Indexer    |
    +-------------+
           ↓
    +-------------+
    | SearchEngine|
    +-------------+
           ↓
    +-------------+
    |    CLI      |
    +-------------+
```

```

---

## 📂 Project Structure

```

search-engine-tool/
│
├── src/
│   ├── crawler.py       # Web crawling logic
│   ├── indexer.py       # Inverted index construction
│   ├── search.py        # Query processing & ranking
│   └── main.py          # CLI interface
│
├── tests/               # Unit tests (pytest)
├── data/                # Stored index files
├── requirements.txt
├── pytest.ini
└── README.md

````

---

## ⚙️ Installation

```bash
git clone https://github.com/Senxss19/search-engine-tool.git
cd search-engine-tool
python -m venv venv
````

Activate:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the CLI:

```bash
python src/main.py
```

---

## 💻 Commands

### Build index

```bash
> build
```

### Load index

```bash
> load
```

### Print word statistics

```bash
> print good
```

### Search queries

```bash
> find good friends          # AND query
> find life OR love          # OR query
> find "life is beautiful"   # Phrase search
```

### Suggestions

```bash
> suggest li
```

---

## 📊 Ranking Algorithm

The system uses **TF-IDF (Term Frequency – Inverse Document Frequency)**:

* TF measures how often a term appears in a document
* IDF measures how rare the term is across documents

Final score:

```
score = Σ TF(word, doc) × log(N / DF(word))
```

This improves ranking quality compared to simple frequency-based scoring.

---

## 🧪 Testing

Run tests:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=src --cov-report=term
```

---

## 📈 Test Coverage

* ✔ Unit tests for all modules
* ✔ Mocked HTTP requests (no real network dependency)
* ✔ CLI interaction testing
* ✔ Edge case handling

**Coverage: >90%**

---

## 🧠 Design Decisions

* Used **inverted index** for efficient retrieval (O(1) lookup per term)
* Stored **positions** to support phrase queries
* Used **set operations** for Boolean queries
* Applied **TF-IDF** for better ranking quality
* Designed modular architecture for extensibility

---

## ⚡ Performance Considerations

* Query time complexity:

  * AND: O(n)
  * OR: O(n)
* Index lookup: O(1)
* Optimized by avoiding redundant computations

---

## 🤖 GenAI Usage & Critical Evaluation

GenAI tools (e.g., ChatGPT / Copilot) were used during development.

### Where GenAI Helped

* Understanding APIs (requests, BeautifulSoup)
* Suggesting initial architecture ideas
* Providing debugging hints

### Limitations of GenAI

* Generated code was sometimes incorrect or inefficient
* Did not consider edge cases (e.g., phrase matching, missing keys)
* Required significant manual correction

### My Approach

* All AI-generated code was reviewed and rewritten where necessary
* Core algorithms (indexing, TF-IDF, search logic) were implemented independently
* Additional tests were added beyond AI suggestions

### Reflection

Using GenAI accelerated development but required critical evaluation to ensure correctness and understanding.

---

## 🔄 Future Improvements

* BM25 ranking algorithm
* Web-based interface
* Parallel crawling
* Better autocomplete (trie-based)

---

## 🏷️ Versioning

This project follows **Semantic Versioning (SemVer)**:

- v1.0.0 – Initial implementation (crawler, index, basic search)
- v1.1.0 – Added TF-IDF ranking, boolean queries, and phrase search
- v2.0.0 – Improved testing, coverage (>90%), and system robustness

Releases are available on GitHub:
- v2.0.0: https://github.com/Senxss19/search-engine-tool/releases/tag/v2.0.0
- v1.1.0: https://github.com/Senxss19/search-engine-tool/releases/tag/v1.1.0
- v1.0.0: https://github.com/Senxss19/search-engine-tool/releases/tag/v1.0.0

---

## 📜 License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this software with proper attribution.