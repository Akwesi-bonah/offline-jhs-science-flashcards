# Running the capstone notebooks (Conversation pathway)

## Quick path: one notebook (recommended)
`notebooks/capstone_train_and_evaluate.ipynb` does everything below (8.8 and 8.9) in one go:
clean, split, format, base-model test, LoRA training, evaluation, teacher sheet, saving.

1. Colab: File > Upload notebook > `notebooks/capstone_train_and_evaluate.ipynb`.
2. Runtime > Change runtime type > **T4 GPU**. Kaggle secrets `KAGGLE_USERNAME`, `KAGGLE_KEY`
   set with Notebook access on.
3. Runtime > Run all. In section 2 a file picker appears: choose `data/jhs_flashcards.jsonl`.
   (Or put it at `MyDrive/jhs_flashcards.jsonl` and set `USE_DRIVE = True` in section 2.)
4. Downloads at the end: `human_eval_sheet.csv` (for the teacher), `human_eval_key.csv`
   (keep, it says which rows are base vs fine-tuned) and `jhs_capstone_outputs.zip`
   (splits, scores, side-by-side table, training curves, LoRA weights, run config).
5. Fill in the Iteration and Reflection cells (section 11) in your own words.

The step-by-step instructions below are for working inside the official 8.8 / 8.9 lab notebooks.

## 0. Upload
Upload `data/jhs_flashcards.jsonl` to Google Drive: `MyDrive/jhs_flashcards.jsonl`.
Runtime → Change runtime type → **T4 GPU**. Kaggle secrets `KAGGLE_USERNAME`, `KAGGLE_KEY` set
(same as course 05/07 labs).

## 1. Notebook 8.8 (Stage 2: prepare data)
- Activity 1, load:
  ```python
  filepath = "/content/drive/MyDrive/jhs_flashcards.jsonl"
  df = pd.read_json(filepath, lines=True)
  display(df.head()); print(df.columns.tolist(), len(df))
  ```
  Columns are already `prompt`, `response` (plus `meta`), as the notebook expects.
- Activity 2, clean: run the notebook's `clean_html` / `clean_unicode` on `df["response"]`
  (little will change; the data is hand-checked). Keep `response_original`.
- Activity 3, split: `train_test_split(df, test_size=0.2, random_state=812)`.
- Activity 4, format: the notebook's function maps `row["prompt"]` → `"input"` and
  `row["response"]` → `"output"` and writes `conversational_training_data.jsonl` and
  `conversational_test_data.jsonl` to Drive. Use it unchanged.

## 2. Notebook 8.9 (Stage 3: train and evaluate)
- Activity 1: load the two JSONL files exactly as in the worked example (`to_dict("records")`).
- Activity 2: use the worked example's `format_io_as_turns(example["input"], example["output"])`
  unchanged; `data = {"prompts": inputs, "responses": targets}`.
- Load `gemma3_1b`, then **test the base model first** on 5 test prompts (save the outputs).
- Activity 3, suggested first run:
  ```python
  lora_rank = 4          # try 8 later if answers stay generic
  learning_rate = 5e-5
  num_epochs = 5         # small dataset; watch for repetition / overfitting
  batch_size = 1
  sequence_length = 256  # answers are short; saves T4 memory
  ```
  Watch loss and sparse categorical accuracy each epoch.
- Activity 4, evaluate: spot-check the same test prompts (base vs fine-tuned), then a teacher
  scores ~20-30 answers 1-5 for accuracy, curriculum fit, clarity, and format. Record in a table.
- Activity 5, iterate: fix weak topics in `data/jhs_flashcards.json`, re-export, re-run.
- Activity 6, reflect: your own words.

## If something breaks
- Out of memory: lower `sequence_length` to 192, keep `batch_size = 1`, rank 4; or load with
  `dtype="bfloat16"` (course 07).
- Paste the full error message to Claude.
