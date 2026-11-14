# Offline JHS Integrated Science revision flashcards with a fine-tuned Gemma 3 1B

Capstone project, Google DeepMind AI Research Foundations (course 08), Conversation pathway.
Author: [your name]. Date: [submission date].

> **How to use this report:** sections marked **TO FILL** must be completed by me with real
> numbers, examples or my own words after running the notebook. Nothing in the Results section
> may be estimated or invented.

---

## 1. Summary

As a student teacher from the University of Education, Winneba, I observed during my teaching
practice that most of the schools I worked in do not give students internet access, so their
students cannot use the AI study tools that better-connected students are starting to rely on.
This project tries to bring a small, curriculum-matched AI study aid to those classrooms
without the internet. I fine-tuned Gemma 3 1B with LoRA on a small dataset of Ghanaian JHS
Integrated Science question and answer flashcards, so the model answers a revision question
with a `Category:` line and a short, plain-English answer. The model is intended to be quantized
and run offline on a Raspberry Pi 4 (4 GB) classroom server, possibly alongside Kolibri, with a
teacher reviewing content before students see it.

Key results: **TO FILL** (one or two sentences after evaluation, e.g. how the fine-tuned model
compared with the base model on format and teacher ratings).

## 2. Problem statement

JHS students in rural and under-resourced Ghanaian schools have few revision materials matched to
the national curriculum, and most digital study tools need a steady internet connection and are
built for foreign curricula. During my teaching practice I saw that most schools I worked in did
not give students internet access, so online AI tools are simply out of reach for them. Students
preparing for the BECE depend on shared textbooks and limited teacher time.

The project builds a revision aid (not a teacher replacement, not a source of exam answers) for
one subject, Integrated Science, in English, that can run on low-cost local hardware with no
internet. Full version: `plan/01_problem_statement.md`.

### 2.1 Related work and context

Offline, low-cost learning servers are already used in Ghana, which shows the approach is
realistic, but none of the projects below adds a curriculum-tuned language model:

- **Kolibri (Learning Equality):** an offline-first learning platform that only needs internet for
  the initial download and can run on a Raspberry Pi as a classroom server. Learning Equality lists
  Ghana among the countries where it works with partner organisations.
- **Ghana Reads (Open Learning Exchange Ghana with World Vision):** used a Raspberry Pi server
  running the Basic eLearning Library (BeLL); the pilot was incorporated into the curriculum of
  20 schools across five districts in two regions.
- **T-TEL (Transforming Teacher Education and Learning):** gave colleges of education access to
  educational resources through low-cost Raspberry Pi computers.
- **Recent research:** a 2026 INTED paper proposes a Raspberry Pi offline server for teaching Python
  in rural Ghanaian senior high schools (a proposal, not a deployment).

This project's contribution is to add a small, fine-tuned, offline language model for JHS
Integrated Science revision to that kind of setup.

Sources: Kolibri FAQ (github.com/learningequality/kolibri-docs, docs/faq.rst);
learningequality.org/about; World Vision, Ghana Reads Quick Guide (wvi.org); Mott MacDonald,
"Transforming teacher education and learning in Ghana" (mottmac.com/article/72351/t-tel-ghana);
IATED Digital Library, ISSAHAKU2026TEA (library.iated.org/view/ISSAHAKU2026TEA).

## 3. Pathway

**Conversation (Q&A).** A student asks a question ("What is photosynthesis?") and the model
replies with a flashcard answer, using the Gemma turn format from the course labs. A small
element is borrowed from classification: each answer starts with a `Category:` label. It is not
summarization, since there is no input text to shorten. Scope is single-turn, one subject, 2 to 4
sentence answers. Details: `plan/02_pathway.md`.

## 4. Dataset

| Item | Detail |
|---|---|
| File | `data/jhs_flashcards.json` (fields: `category`, `name`, `question`, `answer`, `source`), exported to `data/jhs_flashcards.jsonl` (`prompt`, `response`) by `scripts/export_jsonl.py` |
| Size | 129 cards after QA (5 hand-written seed, 105 synthetic, 19 added during QA), per `data/QA_REPORT.md`. Check the final count before training: **TO FILL** (train: ___, test: ___ after the 80/20 split) |
| Construction | A small hand-written seed set (5 cards written by me), then expanded with an AI assistant (Claude), following the course's "seed set plus LLM expansion" approach (as in Self-Instruct, Wang et al. 2023). Every synthetic card is marked `"source": "synthetic (Claude), needs teacher review"` |
| Coverage | Public JHS Integrated Science curriculum topics: matter, mixtures, cells, energy, forces, electricity, human body and health, plants, environment, Earth and space; some local examples (e.g. sobolo as an indicator, Akosombo) |
| Quality checks | `scripts/check_dataset.py` checks missing fields, duplicate questions and answer length (20 to 120 words). An AI-assisted card-by-card QA pass (`data/QA_REPORT.md`, not a substitute for teacher review) edited 7 cards with factual problems (for example, cloth filtering was wrongly described as making water safe to drink, and Ghana was described as having only one rainy season), added 19 student-style cards, and listed cards a teacher should still check |
| Licence | CC BY 4.0 (`data/LICENSE.md`); code is MIT (`LICENSE`) |
| Data card | `plan/06_data_card.md` (Pushkarna et al. 2022 format) |

**Limitations of the data.** Most cards are AI-generated and have not yet all been reviewed by a
qualified science teacher, so they may contain errors. English only. Topic coverage is uneven.
Questions are phrased formally, while real students phrase questions in many ways. No student or
teacher voices are in the data yet. The dataset is small, so the model can learn the answer
format but cannot be relied on for facts outside it.

## 5. Method

| Setting | Value |
|---|---|
| Base model | Gemma 3 1B (`gemma3_1b`, KerasHub, JAX backend) |
| Fine-tuning | LoRA (Hu et al. 2022), `enable_lora(rank=4)` |
| Learning rate | 5e-5 |
| Epochs | 5 |
| Batch size | 1 |
| Sequence length | 256 |
| Hardware | Free Google Colab T4 GPU |
| Prompt format | `<start_of_turn>user ... <end_of_turn>` / `<start_of_turn>model ... <end_of_turn>` |
| Notebook | `notebooks/capstone_train_and_evaluate.ipynb` (instructions: `RUN_IN_COLAB.md`) |

Why these choices: a 1B model is small enough to quantize for a Raspberry Pi; LoRA trains only a
small number of extra parameters, which fits a free GPU and keeps energy use low; a short
sequence length fits short flashcard answers; 5 epochs suits a small dataset, while watching for
repetition or overfitting.

## 6. Evaluation plan

1. **Base vs fine-tuned spot checks.** The same held-out test questions are given to base Gemma 3
   1B and to the fine-tuned model. Compare format, accuracy, clarity and language level.
2. **Automatic checks** on all test answers: does the answer start with `Category:`; is it 2 to
   4 sentences and 20 to 120 words; word overlap with the reference answer (a rough signal only,
   since a correct answer can use different words).
3. **Teacher rating sheet.** A JHS science teacher rates a sample of about 20 to 30 generated
   answers from 1 to 5 on accuracy, curriculum fit, clarity and format, and notes any factual
   errors.
4. **Probe questions:** one in-dataset topic, one unseen but in-syllabus topic, one off-syllabus
   question, to see how the model behaves outside its training data.

## 7. Results

> **TO FILL after running the notebook. Paste real outputs only. Do not estimate.**

### 7.1 Training

| Epoch | Loss | Sparse categorical accuracy |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

Training time on Colab: ___ minutes. Notes (e.g. memory issues, changes made): ___

### 7.2 Automatic checks on the test set (n = ___)

| Check | Base model | Fine-tuned model |
|---|---|---|
| Starts with `Category:` (%) | | |
| 2 to 4 sentences (%) | | |
| 20 to 120 words (%) | | |
| Average word overlap with reference | | |

### 7.3 Example outputs (copy exactly from the notebook)

**Example 1 (in-dataset topic)**
- Question: ___
- Reference answer: ___
- Base model: ___
- Fine-tuned model: ___
- My comment: ___

**Example 2 (unseen but in-syllabus topic)**
- Question: ___
- Base model: ___
- Fine-tuned model: ___
- My comment: ___

**Example 3 (off-syllabus question)**
- Question: ___
- Fine-tuned model: ___
- My comment: ___

### 7.4 Teacher ratings (if completed)

Rater: [role only, no name needed]. Number of answers rated: ___

| Criterion (1 to 5) | Base model average | Fine-tuned average |
|---|---|---|
| Accuracy | | |
| Curriculum fit | | |
| Clarity | | |
| Format | | |

Errors the teacher found: ___

If teacher rating was not completed before the deadline, say so here: ___

### 7.5 Raspberry Pi (if tested)

See `deploy/RASPBERRY_PI.md`, section 7. Seconds per card: ___ (or "not yet tested").

### 7.6 What the results mean

**TO FILL** in my own words: did fine-tuning help, where did it fail, what surprised me.

## 8. Impact statement (summary)

**Positive:** students in schools without internet could revise Integrated Science offline, at
their own pace, with explanations matched to the Ghanaian curriculum; teachers could save
preparation time. A small model fine-tuned once and run locally avoids ongoing data-centre and
data-bundle costs.

**Risks:** confident wrong answers before exams; over-reliance or use as a shortcut; English-only
answers exclude some learners; uneven topic coverage; eventual e-waste.

**Values:** fairness, dignity and autonomy (teachers stay in control), and well-being, with a
tension between efficiency and accuracy. At scale, errors spread further, so scaling needs teacher
review panels and agreement from the Ghana Education Service. Full version:
`plan/04_impact_statement.md`.

## 9. Governance and sustainability (summary)

**Stakeholders** (`plan/05_stakeholders_governance_sustainability.md`): students, teachers,
parents and community, school heads and GES, with an Engage2020 engagement method for each.

**Governance** (`plan/07_governance_brief.md`):
- Existing law: follow Ghana's Data Protection Act, 2012 (Act 843) by collecting no student data.
- Bright-line rules: never used during exams; never replaces the teacher.
- Safeguards: teacher review before use, error reporting, pilot before scaling.

**Sustainability** (`plan/08_sustainability_plan.md`): fine-tune once instead of pre-training;
small model plus LoRA; 4-bit quantization for a low-power Pi; Google's 4Ms (Model, Machine,
Mechanization, Map); reuse existing devices; UPS or solar for an unreliable grid (dumsor); plan
for repair and take-back to limit e-waste; watch for rebound effects; shared responsibility in
the spirit of Ubuntu / Ukama.

## 10. Limitations and next steps

**Limitations:** small, mostly AI-generated dataset not yet fully teacher-reviewed; a 1B model
can state wrong facts confidently; English only; one subject; single-turn only; Pi deployment
not yet tested; the Keras to GGUF export path is not yet verified (see `deploy/RASPBERRY_PI.md`).

**Next steps:**
1. Teacher review of every card; fix or remove errors; retrain.
2. Add student-style question wordings and more local examples.
3. Twi explanations (with a fluent teacher reviewing them).
4. More subjects (e.g. Mathematics, Social Studies) as new categories.
5. Export, quantize and measure on the Raspberry Pi 4; if too slow, serve pre-generated,
   teacher-approved cards inside Kolibri.
6. A small pilot with one teacher and one class before any wider use.

## 11. Reflection

> **TO FILL in my own words.** Suggested prompts: What did I learn about fine-tuning and data
> quality? What would I do differently? How did my teaching practice shape the design? What is my
> responsibility as a developer if this is used with real students?

## 12. References

- Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., and Chen, W. (2022).
  LoRA: Low-Rank Adaptation of Large Language Models. *ICLR 2022*.
- Gemma Team, Google DeepMind (2025). Gemma 3 Technical Report. arXiv:2503.19786.
- Pushkarna, M., Zaldivar, A., and Kjartansson, O. (2022). Data Cards: Purposeful and Transparent
  Dataset Documentation for Responsible AI. *ACM FAccT 2022*.
- Wang, Y., Kordi, Y., Mishra, S., Liu, A., Smith, N. A., Khashabi, D., and Hajishirzi, H. (2023).
  Self-Instruct: Aligning Language Models with Self-Generated Instructions. *ACL 2023*.
- Google DeepMind. AI Research Foundations course materials (courses 01 to 08), including the
  capstone notebooks 8.8 and 8.9.
- Ghana. Data Protection Act, 2012 (Act 843).
