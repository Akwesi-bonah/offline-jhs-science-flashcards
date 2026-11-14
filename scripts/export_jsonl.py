"""Export the flashcard dataset to the prompt/response JSONL used by the capstone notebooks.

Usage: python3 scripts/export_jsonl.py data/jhs_flashcards.json data/jhs_flashcards.jsonl
"""
import json
import sys


def main(src: str, dst: str) -> None:
    with open(src, encoding="utf-8") as f:
        cards = json.load(f)
    with open(dst, "w", encoding="utf-8") as out:
        for card in cards:
            row = {
                "prompt": card["question"].strip(),
                "response": f"Category: {card['category']}\n{card['answer'].strip()}",
                "meta": {"topic": card["name"], "category": card["category"]},
            }
            out.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"Wrote {len(cards)} rows to {dst}")


if __name__ == "__main__":
    main(*(sys.argv[1:3] if len(sys.argv) > 2 else ("data/jhs_flashcards.json", "data/jhs_flashcards.jsonl")))
