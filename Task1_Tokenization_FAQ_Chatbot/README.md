# Task 1 (Beginner): Tokenization and a FAQ Chatbot

CAI601400 AI Lab 6 - NLP Fundamentals

Compares whitespace vs word-like tokens on 8 inputs (punctuation, can't with straight and curly quotes, email, CS4944 version 2.1, empty string, Urdu, file name) and runs the FAQ chatbot with TF-IDF and sentence embeddings (all-MiniLM-L6-v2).

## Setup

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```
python task1_tokens.py
python task1_chatbot_check.py
python guided_chatbot.py            # TF-IDF
python guided_chatbot.py --backend embedding
```

Terminal output from my run is in `outputs/`.
