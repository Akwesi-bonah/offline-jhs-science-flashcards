# Model card: JHS Integrated Science flashcard model (Gemma 3 1B + LoRA)

Structure follows the Hugging Face model card template (model details, uses, bias/risks/limitations,
training details, evaluation). Results are filled in after training; nothing here is measured yet.

## Model details
- **Base model:** Gemma 3 1B (`gemma3_1b`, pre-trained, not instruction-tuned), Google DeepMind.
- **Adaptation:** LoRA (rank 4) via KerasHub, JAX backend; base weights frozen.
- **Task:** single-turn question answering that returns a revision flashcard:
  `Category: Integrated Science` then a 2 to 4 sentence answer.
- **Developer:** the project author (student teacher, University of Education, Winneba), as a
  Google DeepMind AI Research Foundations capstone project, 2026.
- **Licence:** project code MIT; dataset CC BY 4.0; Gemma weights are governed by Google's Gemma
  terms of use and are not redistributed in this repository.

## Uses
- **Direct use:** offline revision support for Ghanaian JHS students in Integrated Science, run on
  a classroom Raspberry Pi 4 or a laptop, under a teacher's supervision.
- **Downstream use:** teachers generating draft revision cards that they review before sharing.
- **Out-of-scope use:** exam answering or use during exams; replacing a teacher; medical,
  safety or legal advice; subjects or languages not in the training data; unsupervised use with
  students before teacher review of the dataset and outputs.

## Bias, risks and limitations
- Small dataset (129 cards), 124 of them AI-generated and not yet reviewed by a qualified teacher.
- English only; students who learn best in Twi or other Ghanaian languages are not served.
- Uneven topic coverage (the "systems" strand is thinnest); answers outside covered topics rely on
  the base model's knowledge and may be wrong or invented.
- A 1B model can state errors confidently; every output should be treated as a draft.
- **Recommendation:** teacher review of the dataset and a sample of outputs before any classroom use;
  keep an error log; pilot with one class first.

## Training details
- **Data:** `data/jhs_flashcards.jsonl` (prompt/response), 80/20 train/test split, random seed 812.
- **Format:** Gemma turn markers `<start_of_turn>user ... <end_of_turn>` /
  `<start_of_turn>model ... <end_of_turn>`.
- **Hyperparameters:** learning rate 5e-5, 5 epochs, batch size 1, sequence length 256, LoRA rank 4.
- **Hardware:** Google Colab, NVIDIA T4 GPU. Training time: TO FILL.

## Evaluation
- **Test data:** the 20% held-out split (n = TO FILL).
- **Methods:** base vs fine-tuned spot checks on the same prompts; automatic checks (starts with
  `Category:`, 20 to 120 words, token-overlap F1 vs reference); teacher ratings (1 to 5) for
  accuracy, curriculum fit and clarity on a sample.
- **Results:** TO FILL from `results/` (see PROJECT_REPORT.md section 7).

## Environmental impact
- One short LoRA fine-tune of a 1B model on a free cloud T4; no pre-training. Planned offline
  inference on a low-power Raspberry Pi 4. Energy not measured. See `plan/08_sustainability_plan.md`.
