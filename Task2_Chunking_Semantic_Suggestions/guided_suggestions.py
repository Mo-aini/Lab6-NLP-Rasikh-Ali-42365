"""6.7 Recommend related questions from the fixed FAQ list.
Run: python guided_suggestions.py [--backend tfidf|embedding]
"""
import argparse
from guided_chatbot import build_bot

parser = argparse.ArgumentParser()
parser.add_argument("--backend", choices=["tfidf", "embedding"], default="tfidf")
args = parser.parse_args()
engine = build_bot(args.backend)
for query in ["assignment upload", "forgot login", "blank"]:
    print(f"Suggested questions for {query!r} ({args.backend}):")
    for record, score in engine.search(query, k=3):
        # For TF-IDF hide zero scores (no shared words). This is NOT a semantic
        # cutoff, so for embeddings all top-3 candidates are shown with scores.
        if args.backend == "embedding" or score > 0:
            print("  ", record["id"], "|", record["question"], f"({score:.3f})")
