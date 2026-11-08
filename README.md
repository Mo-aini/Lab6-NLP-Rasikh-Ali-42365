# Lab 6 — Rasikh Ali (42365)

CAI601400 AI Lab 6 — NLP Fundamentals: tokenization, embeddings, chunking and document retrieval.

📄 **Report:** [PDF](report/Lab6_Report_Rasikh_Ali_42365.pdf) · [DOCX](report/Lab6_Report_Rasikh_Ali_42365.docx)

## Setup (any task)

Each task folder is self-contained. From inside the folder:

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The embedding backend uses `sentence-transformers/all-MiniLM-L6-v2` on CPU (downloaded on first run). The TF-IDF backend needs no download. Terminal output from my own runs is saved in each task's `outputs/` folder.

## Task 1 (Beginner) — Tokenization & FAQ Chatbot

Folder: [`Task1_Tokenization_FAQ_Chatbot`](Task1_Tokenization_FAQ_Chatbot)

- `task1_tokens.py` compares whitespace tokens, Unicode word-like regex tokens and the encoder's sub-word tokens on 8 tricky inputs (punctuation, `can't` with straight and curly apostrophes, an email, `CS4944 version 2.1`, an empty string, Urdu text, a file name).
- `guided_chatbot.py` is a command-line FAQ chatbot that matches a question to the closest FAQ (TF-IDF or sentence embeddings) and answers with its source, a "possible matches" list for unsure cases, and a fallback for unrelated questions.
- `task1_chatbot_check.py` runs behaviour checks (exact match, empty input, off-topic, ambiguous) plus a scripted transcript.
- `lab6_search.py` is the shared retrieval helper (`Retriever` with `tfidf` / `embedding` backends).

```bash
cd Task1_Tokenization_FAQ_Chatbot
python task1_tokens.py              # add --no-model to skip the encoder tokenizer
python task1_chatbot_check.py
python guided_chatbot.py            # TF-IDF
python guided_chatbot.py --backend embedding
```

## Task 2 (Intermediate) — Chunking & Semantic Suggestions

Folder: [`Task2_Chunking_Semantic_Suggestions`](Task2_Chunking_Semantic_Suggestions)

- `task2_chunks.py` compares fixed word windows (40 words, overlap 0 and 10) with sentence-aware chunking (40-word budget); every chunk keeps its source id and character offsets. Boundary tests: empty text, a short document, invalid overlap, a 95-word sentence falling back to windows, and offsets matching the source.
- `task2_semantic_check.py` builds semantic suggestions over the chunk records and compares TF-IDF with real sentence embeddings on labeled queries.
- `guided_suggestions.py` recommends related questions from the FAQ list; `guided_embeddings.py` and `guided_chunks.py` are the guided examples (cosine similarity, chunking with metadata).
- `create_dataset.py` writes the synthetic `corpus.json` / `queries.json` used here and in Task 3.

```bash
cd Task2_Chunking_Semantic_Suggestions
python task2_chunks.py
python task2_semantic_check.py
python guided_suggestions.py --backend embedding
```

## Task 3 (Advanced) — Document Retrieval Chatbot Evaluation

Folder: [`Task3_Document_Retrieval_Chatbot`](Task3_Document_Retrieval_Chatbot)

- `task3_retrieval.py` evaluates 3 chunking strategies × 2 retrieval methods (TF-IDF, embeddings) on labeled dev/test queries plus unanswerable ones, reporting Hit@3, MRR@3 and runtime. It writes `results_summary.csv`, `retrieval_log.csv`, `failures.json`, and picks the best configuration on dev data only (`selected_config.json`).
- `document_chatbot.py` is an interactive evidence assistant that uses the selected configuration and answers with the source chunk.
- `guided_metrics.py` (Hit@3 / MRR@3) and `guided_limits.py` (CPU setup and model input limits) are the guided examples.

```bash
cd Task3_Document_Retrieval_Chatbot
python create_dataset.py --force
python task3_retrieval.py
python document_chatbot.py
```

**Results (my run):** sentence-aware chunks + embeddings gave the best test result — Hit@3 **1.0**, MRR@3 **0.875**. The rule fixed on dev data (best dev MRR@3, then Hit@3, then fewer chunks) picked window-40/overlap-0 + embeddings because four configurations tied on dev, so that is the configuration `document_chatbot.py` loads from `selected_config.json`.

| Strategy | Method | Chunks | Dev Hit@3 | Dev MRR@3 | Test Hit@3 | Test MRR@3 |
|---|---|---|---|---|---|---|
| window-40 / overlap-0 | TF-IDF | 31 | 0.50 | 0.500 | 0.25 | 0.125 |
| window-40 / overlap-0 | Embedding | 31 | 0.50 | 0.500 | 0.50 | 0.208 |
| window-40 / overlap-10 | TF-IDF | 39 | 0.25 | 0.250 | 0.25 | 0.125 |
| window-40 / overlap-10 | Embedding | 39 | 0.25 | 0.125 | 0.25 | 0.125 |
| sentence-40 | TF-IDF | 39 | 0.50 | 0.500 | 0.75 | 0.417 |
| sentence-40 | Embedding | 39 | 0.50 | 0.500 | 1.00 | 0.875 |

All corpus text is synthetic teaching data, not real university policy.
