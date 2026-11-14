"""Check the capstone flashcard dataset before fine-tuning.

Usage: python3 scripts/check_dataset.py data/jhs_flashcards.json
"""
import json
import sys
from collections import Counter

REQUIRED = ("category", "name", "question", "answer")
MIN_WORDS, MAX_WORDS = 20, 120  # keep answers short enough for a flashcard


def main(path: str) -> int:
    with open(path, encoding="utf-8") as f:
        cards = json.load(f)

    problems = []
    questions = Counter()
    for i, card in enumerate(cards):
        missing = [k for k in REQUIRED if not str(card.get(k, "")).strip()]
        if missing:
            problems.append(f"card {i}: missing {', '.join(missing)}")
            continue
        q = card["question"].strip()
        questions[q.lower()] += 1
        if not q.endswith("?"):
            problems.append(f"card {i} ({card['name']}): question should end with '?'")
        words = len(card["answer"].split())
        if not MIN_WORDS <= words <= MAX_WORDS:
            problems.append(
                f"card {i} ({card['name']}): answer has {words} words "
                f"(aim for {MIN_WORDS}-{MAX_WORDS})"
            )

    for q, n in questions.items():
        if n > 1:
            problems.append(f"duplicate question ({n}x): {q}")

    print(f"{len(cards)} cards")
    for cat, n in Counter(c.get("category", "?") for c in cards).most_common():
        print(f"  {cat}: {n}")
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nNo problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "data/jhs_flashcards.json"))
