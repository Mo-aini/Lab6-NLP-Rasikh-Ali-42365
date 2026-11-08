"""Task 1: FAQ chatbot behaviour checks + a scripted transcript (TF-IDF backend).
Run: python task1_chatbot_check.py
"""
from guided_chatbot import build_bot, reply, FAQ

engine = build_bot()
assert "it_help.txt" in reply(engine, "How do I reset my password?")
assert reply(engine, "") == "Please enter a question."
assert "No matching FAQ" in reply(engine, "volcano geology")
assert "Possible matches" in reply(engine, "password recovery")
# the two added FAQs
assert "printer_help" in reply(engine, "What should I do if the printer prints blank pages?")
assert "it_password" in reply(engine, "How do I connect to campus Wi-Fi?")
print("FAQ behaviour checks passed (", len(FAQ), "FAQs )\n")

for query in ["How do I reset my password?",          # exact answer
              "What should I do if the printer prints blank pages?",  # added FAQ, exact
              "printer shows empty paper",            # suggestion response
              "wifi not working",                     # suggestion response
              "",                                     # empty input
              "volcano geology"]:                     # unsupported input
    print("You:", repr(query))
    print("Bot:", reply(engine, query))
    print()
