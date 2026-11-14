# Pathway choice

**Primary pathway: Conversation (Q&A).**

The model receives a student's question ("What is photosynthesis?") and responds with a
flashcard answer. That is a question-and-response behaviour, the conversation pathway's
primary behaviour, and the same `<start_of_turn>user ... <start_of_turn>model ...` format used
in the course's Africa Galore labs.

**Secondary element (borrowed from Classification):** each answer starts with a
`Category:` label (e.g. Integrated Science, later other subjects). This is a small labelling
step inside the answer, not a separate classifier, so the project stays in one pathway.

**Not summarization:** the model writes short answers from its knowledge plus fine-tuning, it
does not shorten a given input text.

Scope stays narrow: one subject, single-turn Q&A (no multi-turn chat), 2 to 4 sentence answers.
