# Task 3 (Advanced): Evaluate a Document Retrieval Chatbot

CAI601400 AI Lab 6 - NLP Fundamentals

Compares 3 chunking strategies x TF-IDF/embedding on labeled dev/test queries plus unanswerable ones; reports Hit@3, MRR@3 and runtime. Best result: sentence-aware chunks + embeddings (test Hit@3 1.0, MRR@3 0.875). Full logs in retrieval_log.csv, failures in failures.json.

## Setup

```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```
python create_dataset.py --force
python task3_retrieval.py
python document_chatbot.py
```

Terminal output from my run is in `outputs/`.

## Results (real run)

strategy,method,chunks,encode_seconds,search_seconds,dev_hit3,dev_mrr3,test_hit3,test_mrr3
window-40/overlap-0,tfidf,31,0.0043,0.000208,0.5,0.5,0.25,0.125
window-40/overlap-0,embedding,31,0.1169,6.2e-05,0.5,0.5,0.5,0.208
window-40/overlap-10,tfidf,39,0.0025,0.000161,0.25,0.25,0.25,0.125
window-40/overlap-10,embedding,39,0.1077,4.6e-05,0.25,0.125,0.25,0.125
sentence-40,tfidf,39,0.0024,0.000167,0.5,0.5,0.75,0.417
sentence-40,embedding,39,0.0912,4.4e-05,0.5,0.5,1.0,0.875
