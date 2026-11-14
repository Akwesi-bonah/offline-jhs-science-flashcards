# Data Card: JHS Integrated Science revision flashcards (draft v2)

| Field | Response |
|---|---|
| **Input versus output** | Input: a text revision question a JHS student might ask in English (e.g. "What is photosynthesis?"). Output: a text flashcard, `Category: Integrated Science` on the first line, then a 2 to 4 sentence answer in plain English. |
| **Classification problem** | None as the main task (Conversation pathway). The only label is the `Category` line, currently a single value (Integrated Science); more subjects can be added later. |
| **Labeling** | Answers are the "labels". 5 seed cards were hand-written by me; 45 were generated with an AI assistant (Claude) and marked `"source": "synthetic (Claude), needs teacher review"`. All answers are checked automatically for format, duplicates and length (`scripts/check_dataset.py`). **Pending:** a JHS science teacher reviews every synthetic card for accuracy and curriculum fit before training. |
| **Data creation** | Written from public JHS Integrated Science curriculum topics (cells, matter, mixtures, energy, forces, electricity, human body, health, plants, environment, Earth and space). No interviews or recordings; no personal data. Synthetic augmentation followed the course's "seed set + LLM expansion" approach. Target: 100 to 200 pairs for the first training run. |
| **Web collection ethics** | No web scraping. No textbook, past-question or website text copied, to avoid copyright problems; answers are original wording of common scientific facts. AI-generated content is labelled as such. Intended licence for the dataset: CC BY 4.0. |
| **Bias and representation** | English only, so students who learn best in Twi or other Ghanaian languages are not served yet. Topic coverage is uneven (whatever was written first is better covered). Examples are mostly general; few local examples (sobolo as an indicator, kenkey meal, Akosombo, galamsey-polluted water, salt pans) so far. Questions are phrased formally; real students phrase questions in many ways. No student or teacher voices in the data yet. |
| **Values and community alignment** | Reflects fairness (offline access for rural schools), dignity and autonomy (teachers review and control content), and well-being (accuracy over volume). Accountability: teacher review before use, an error log for wrong cards, and sharing the dataset openly so others can check it. |

## Known limitations (affects scope)
- Until teacher review is done, the model must not be used with real students.
- Single subject, single-turn Q&A, English only.
- Synthetic answers may carry the generating model's style and blind spots.

## Next improvements
- Teacher review of all synthetic cards; fix or remove errors.
- Add more local examples and paraphrased question wordings (student-style questions).
- Grow to 100 to 200 cards with balanced coverage across curriculum strands.
