"""6.1 Tokenization and conservative normalization (guided example + experiment).
Run: python guided_tokens.py
"""
import re

for text in ["I can't submit CS4944 late!", "rasikh.ali@example.edu", "", "یہ ایک مثال ہے"]:
    whitespace = text.split()
    words = re.findall(r"\b\w+\b", text)
    print("Original:", repr(text))
    print("  Whitespace:", whitespace, len(whitespace))
    print("  Word-like:", words, len(words))
