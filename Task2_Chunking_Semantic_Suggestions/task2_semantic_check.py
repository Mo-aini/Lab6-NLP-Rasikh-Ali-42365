"""Task 2: semantic suggestions over chunk records - TF-IDF vs real sentence embeddings.
Run: python task2_semantic_check.py
"""
from task2_chunks import make_chunks, load_task2_docs, LABELED
from lab6_search import Retriever, show_hits

# 1) Manual wiring check
texts = {"it": "A forgotten password can be reset using the recovery link.",
         "assessment": "Assignments are uploaded through the learning portal."}
records = make_chunks(texts, "sentence")
for backend in ["tfidf", "embedding"]:
    engine = Retriever(records, backend)
    print("Backend:", backend)
    show_hits(engine.search("How can I regain access to my account?", k=2))
print()

# 2) Chunk records from the Task 2 corpus, three paraphrased queries
docs = load_task2_docs()
chunks = make_chunks(docs, "sentence")
engines = {b: Retriever(chunks, b) for b in ["tfidf", "embedding"]}
paraphrases = [
    ("I was unwell, can I get more time for my assignment?", "handbook_late"),
    ("I can't remember how to sign in to my account", "it_password"),
    ("my printouts come out with nothing on them", "printer_help"),
]
for query, expected_doc in paraphrases:
    print("=" * 70)
    print("Query:", query, "| expected document:", expected_doc)
    for backend, engine in engines.items():
        hits = engine.search(query, k=3)
        print(f"  [{backend}]" + ("  no candidates (no shared vocabulary)" if not hits else ""))
        for rank, (r, score) in enumerate(hits, 1):
            mark = "<- expected doc" if r["doc"] == expected_doc else ""
            print(f"   {rank}. {r['id']} score={score:.3f} chars {r['start']}-{r['end']} {mark}")
            print("      evidence:", r["text"][:160] + ("..." if len(r["text"]) > 160 else ""))
