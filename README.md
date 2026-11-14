# Offline JHS revision flashcards on a Raspberry Pi 4

Capstone project for Google DeepMind AI Research Foundations (course 08, Conversation pathway).

## What this is

During teaching practice as a student teacher (University of Education, Winneba), I saw that
most of the schools I worked in do not give students internet access, so their students cannot
use online AI study tools. This project fine-tunes **Gemma 3 1B** with **LoRA** (on Google Colab)
on a small set of Ghanaian JHS **Integrated Science** question and answer flashcards. The goal is
a model that answers a revision question with a `Category:` line and a 2 to 4 sentence,
plain-English answer, and that can be quantized to run **offline on a Raspberry Pi 4 (4 GB)**
classroom server, possibly alongside Kolibri.

It is a revision aid only: it does not replace teachers, it is not used during exams, it collects
no student data, and teachers review content before students use it.

## Folder map

| Path | What it is |
|---|---|
| `PROJECT_REPORT.md` | The capstone submission report (results to be filled in after running) |
| `MODEL_CARD.md` | Model card (Hugging Face template sections): uses, out-of-scope uses, risks, training, evaluation |
| `results/` | Where to save notebook outputs (loss plot, comparison CSV, teacher rating sheet) |
| `plan/01_problem_statement.md` to `plan/08_sustainability_plan.md` | Problem, pathway, technical proposal, impact, stakeholders, data card, governance brief, sustainability plan |
| `data/jhs_flashcards.json` | The dataset (`category`, `name`, `question`, `answer`, `source`). Same core fields as the course's Africa Galore QA set |
| `data/jhs_flashcards.jsonl` | Export with `prompt` / `response` columns for the capstone notebooks |
| `data/QA_REPORT.md` | Results of the dataset quality check and cards a teacher should review |
| `data/LICENSE.md` | Dataset licence (CC BY 4.0) |
| `scripts/check_dataset.py` | Checks missing fields, duplicate questions and answer length |
| `scripts/export_jsonl.py` | Converts the JSON dataset to the JSONL the notebooks expect |
| `notebooks/capstone_train_and_evaluate.ipynb` | Colab notebook: prepare data, fine-tune with LoRA, evaluate |
| `RUN_IN_COLAB.md` | Step-by-step instructions for running in Colab |
| `deploy/RASPBERRY_PI.md` | Plan for running offline on a Raspberry Pi 4 with Kolibri (not yet tested) |
| `LICENSE` | MIT licence for the code |

## How to run

1. Check and export the data (on any computer with Python 3):

       python3 scripts/check_dataset.py data/jhs_flashcards.json
       python3 scripts/export_jsonl.py data/jhs_flashcards.json data/jhs_flashcards.jsonl

2. Open `notebooks/capstone_train_and_evaluate.ipynb` in Google Colab with a T4 GPU and follow
   `RUN_IN_COLAB.md` (Kaggle credentials are needed to download Gemma, as in the course labs).
3. Paste the real training numbers and example outputs into the Results section of
   `PROJECT_REPORT.md`.
4. Optional: follow `deploy/RASPBERRY_PI.md` to test on a Raspberry Pi.

Model weights and checkpoints are not stored in this repository (see `.gitignore`).

## Dataset rules

- Write answers in your own words from the curriculum topics. Do not copy textbooks or past papers.
- 2 to 4 sentences (20 to 120 words), plain English a JHS student understands.
- One subject first (Integrated Science), then add more categories.
- Mark AI-generated cards in the `source` field; a teacher reviews them before classroom use.
- Target: 150 to 300 cards over time. Keep about 20% aside for evaluation (the notebooks use an
  80/20 split).
- No personal data about students or teachers.

## Licence

- Code: MIT (`LICENSE`).
- Dataset: CC BY 4.0 (`data/LICENSE.md`). Most cards are AI-assisted and still need review by a
  qualified teacher.
- Gemma 3 model weights are not included and are covered by Google's Gemma terms of use.

## Status

- Dataset: 129 cards after a QA pass; teacher review still pending.
- Training and evaluation: notebook ready; results not yet recorded.
- Raspberry Pi deployment: planned, not yet tested.
- Governance brief and sustainability plan: drafted; personal story and reflections still to be
  written by the author.
