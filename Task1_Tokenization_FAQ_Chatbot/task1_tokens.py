"""Task 1 (Beginner): compare whitespace, Unicode word-like regex and model sub-word tokens.
Run: python task1_tokens.py          (add --no-model to skip the encoder tokenizer)
"""
import re
import sys

samples = [
    ("punctuation", "AI, search!"),
    ("contraction (straight ')", "I can't log in."),
    ("contraction (curly \u2019)", "I can\u2019t log in."),
    ("email", "help@example.com"),
    ("course code + version", "CS4944 version 2.1"),
    ("empty string", ""),
    ("Urdu", "یہ ایک مثال ہے"),
    ("identifier/file name", "CS4944_42365_Lab6.pdf"),
]


def whitespace_tokens(text):
    return text.split()


def wordlike_tokens(text):
    # Unicode-aware letter/number runs. NOT a linguistic or multilingual tokenizer.
    return re.findall(r"\b\w+\b", text, flags=re.UNICODE)


def aggressive_normalize(text):
    # A risky normalization: lowercase and delete punctuation.
    return re.sub(r"[^\w\s]", "", text.lower())


for label, text in samples:
    ws, words = whitespace_tokens(text), wordlike_tokens(text)
    print(f"\n[{label}] original={text!r}")
    print("   whitespace:", ws, len(ws))
    print("   word-like :", words, len(words))
assert wordlike_tokens("") == [] and whitespace_tokens("") == []

print("\nNormalization risk (original kept separately from the search copy):")
for text in ["I can't log in.", "CS4944 version 2.1", "help@example.com"]:
    print(f"   {text!r} -> {aggressive_normalize(text)!r}")

if "--no-model" not in sys.argv:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    print("\nModel sub-word tokens (all-MiniLM-L6-v2 WordPiece tokenizer):")
    for label, text in samples:
        if label in ("punctuation", "contraction (straight ')", "email",
                     "course code + version", "Urdu"):
            toks = model.tokenizer.tokenize(text)
            ids = model.tokenizer(text, truncation=False)["input_ids"]
            print(f"   [{label}] {text!r}: {toks} ({len(toks)} sub-words, "
                  f"{len(ids)} ids incl. [CLS]/[SEP])")
