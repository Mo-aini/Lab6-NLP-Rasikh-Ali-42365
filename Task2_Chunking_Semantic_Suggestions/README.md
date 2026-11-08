# Task 2 (Intermediate): Chunking and Semantic Suggestions

CAI601400 AI Lab 6 - NLP Fundamentals

Fixed word-window (40 words, overlap 0 and 10) vs sentence-aware chunking (40-word budget) with source ids and character offsets. Boundary tests pass: empty text, short document, invalid overlap, a 95-word sentence falling back to windows, offsets matching the source.

## Setup

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```
python task2_chunks.py
python task2_semantic_check.py
python guided_suggestions.py --backend embedding
```

Terminal output from my run is in `outputs/`.
