# Technical proposal (Conversation pathway)

Follows the capstone notebooks 8.8 (Stage 2: prepare data) and 8.9 (Stage 3: train and evaluate).

## Task
Single-turn Q&A. Input: a JHS Integrated Science revision question. Output: a flashcard answer,
`Category: Integrated Science` on the first line, then 2 to 4 plain-English sentences.

## Data (Stage 2, notebook 8.8)
- Source: question and answer pairs written by me from public JHS Integrated Science curriculum
  topics (no copied textbook or past-paper text). Teacher review of a sample for accuracy.
- Size: 150 to 300 pairs, spread across curriculum strands (diversity of matter, cycles,
  systems, forces and energy, humans and the environment).
- Storage: `data/jhs_flashcards.json` (category, name, question, answer), exported by
  `scripts/export_jsonl.py` to `data/jhs_flashcards.jsonl` with the `prompt` / `response`
  columns the capstone notebooks expect.
- Cleaning: `clean_html` and `clean_unicode` from 8.8 (mostly a no-op for hand-written data),
  keep `response_original`, check duplicates and length with `scripts/check_dataset.py`.
- Split: 80% train / 20% test (`train_test_split(test_size=0.2)`), saved as
  `conversational_training_data.jsonl` and `conversational_test_data.jsonl` on Google Drive.
- Formatting: Gemma turn format (`<start_of_turn>user ... <end_of_turn>` /
  `<start_of_turn>model ... <end_of_turn>`), as in course 05.

## Model and training (Stage 3, notebook 8.9)
- Base model: Gemma 3 1B (`gemma3_1b`), Keras / JAX on a free Colab T4 GPU.
- PEFT: LoRA via `model.backbone.enable_lora(rank=4)` (try 8 if underfitting).
- Hyperparameters (start from the notebook defaults): learning rate 5e-5, 3 epochs,
  batch size 1, sequence length about 256 to 400. If memory allows nothing larger, use gradient
  accumulation (course 07) for an effective batch of 4 to 8.
- Monitor: loss each epoch plus generations for fixed prompts (one in-dataset topic, one
  unseen but in-syllabus topic, one off-syllabus topic).

## Evaluation
1. Manual spot checks on the held-out test questions: format (Category line, length), factual
   accuracy, age-appropriate language, no invented facts.
2. Systematic human evaluation: a JHS science teacher rates a random sample of about 30
   generated cards on accuracy, curriculum fit and clarity (1 to 5 scale); compare base Gemma 3
   1B vs the fine-tuned model on the same questions.
3. Iterate: fix weak topics in the data, adjust epochs or learning rate, re-evaluate.

## Deployment demo (optional, after the capstone core)
Export the LoRA-merged model, quantize to 4-bit, and run offline on a Raspberry Pi 4 (4 GB) with
llama.cpp or Ollama; measure seconds per card. Optionally serve alongside Kolibri.

## Risks to the technical plan
- Hallucinated facts at small data sizes: mitigated by teacher review and keeping answers short.
- Overfitting to phrasing: vary question wording in the dataset.
- Pi latency: keep answers short; fall back to pre-generated, teacher-approved cards if needed.
