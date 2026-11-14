# Deploying on a Raspberry Pi 4 (4 GB): offline classroom server

Status: **not yet tested on real hardware.** This is a plan with the commands I expect to use.
All speed and memory numbers are **to be measured**. Steps that I have not verified are marked
"unverified".

Goal: a Raspberry Pi 4 (4 GB) in the classroom that works with no internet, serving
(a) Kolibri, the offline learning platform, and (b) the fine-tuned Gemma 3 1B flashcard model,
or, if the model is too slow or not ready, a set of pre-generated, teacher-approved cards.

---

## 1. Hardware

| Item | Why |
|---|---|
| Raspberry Pi 4 Model B, 4 GB | Enough memory for a 4-bit 1B model plus Kolibri (to be measured) |
| Official 5.1 V 3 A USB-C power supply | Under-powered Pis throttle and corrupt storage |
| USB 3 SSD (preferred) or a good 32 GB+ microSD card | SSD is faster and survives power cuts better than SD cards |
| Case with heatsink and fan | Model inference keeps the CPU busy; without cooling it throttles |
| Small UPS or power bank with pass-through, or solar kit (optional) | Power cuts (dumsor) can corrupt storage mid-write |
| Wi-Fi (built in) or a cheap router | Students connect from phones or laptops on a local network, no internet needed |

## 2. Operating system

1. Use **Raspberry Pi Imager** (https://www.raspberrypi.com/software/) to write
   **Raspberry Pi OS (64-bit), Lite or Desktop** to the SSD or SD card. 64-bit is required:
   Ollama and modern llama.cpp builds target arm64.
2. In Imager's settings, set a hostname (e.g. `scipi`), a user and password, and enable SSH.
3. Boot, then update (this step needs internet once, e.g. at home or via a phone hotspot):

       sudo apt update && sudo apt full-upgrade -y
       sudo reboot

4. Check temperature and throttling while testing later:

       vcgencmd measure_temp
       vcgencmd get_throttled     # 0x0 means no throttling or under-voltage

5. Optional: add swap only as a safety net (heavy swapping on an SD card is slow and wears it).

## 3. Kolibri (offline learning platform)

Follow the official instructions, which cover Raspberry Pi OS and Debian-based systems:

- Kolibri install docs: https://kolibri.readthedocs.io/en/latest/install/
- Downloads: https://learningequality.org/download/

After installing, Kolibri normally serves on port 8080: open `http://scipi.local:8080` (or the
Pi's IP address) from a phone on the same network. Import content channels while the Pi still
has internet, or from a USB drive. Kolibri does not run the language model; it is the place where
the approved flashcards and other learning resources live.

## 4. Running the model

There are two common ways to run a small model on a Pi. Both need the model in **GGUF** format,
quantized to 4-bit (for example `Q4_K_M`).

### 4a. First, test with the base model (easy, needs internet once)

This checks whether the Pi is fast enough before any conversion work.

    curl -fsSL https://ollama.com/install.sh | sh
    ollama run gemma3:1b "What is photosynthesis? Answer in 2 to 4 sentences."

Record: seconds to first word, seconds per card, memory use (`free -h`), temperature. All
**to be measured**.

### 4b. Getting my fine-tuned model into GGUF (the hard part)

The model is trained in **Keras / KerasHub** (JAX backend) in Colab. llama.cpp and Ollama do not
read Keras files. The path is:

    Keras model with LoRA  ->  Hugging Face Transformers format (safetensors)  ->  GGUF  ->  4-bit GGUF

**Step 1: Keras to Hugging Face format (unverified).** Research findings, stated honestly:

- Recent KerasHub releases (0.23.0 and later) added export to the Hugging Face Transformers
  format. The KerasHub source has an exporter for Gemma 3
  (`keras_hub/src/utils/transformers/export/gemma3.py`) and an entry point
  `export_to_safetensors(keras_model, path)` in `hf_exporter.py`. The release notes describe a
  `export_to_transformers(...)` method on models.
- I have **not** confirmed: (1) which KerasHub version Colab installs for the course notebooks,
  (2) the exact method name in that version, (3) whether LoRA weights are merged into the base
  weights during export. In Keras 3, a layer with LoRA enabled computes its effective kernel as
  the base kernel plus the scaled LoRA update, so an exporter that reads the effective kernel
  should include the fine-tuning, but this must be checked.
- How to check: after export, load the folder with `transformers` in Colab, ask the same 5 test
  questions, and compare with the Keras model's answers. If they match the fine-tuned answers
  (not the base model's), the LoRA update was included.

Sketch to try in Colab (adjust to the installed version; unverified):

    # in the training notebook, after fine-tuning
    !pip install -U keras-hub
    gemma_lm.export_to_transformers("hf_export/")        # name may differ by version
    # or:
    # from keras_hub.src.utils.transformers.export.hf_exporter import export_to_safetensors
    # export_to_safetensors(gemma_lm, "hf_export/")

If export fails or drops the LoRA update, alternatives are: re-run the same fine-tune in
Hugging Face `transformers` + `peft` (then `merge_and_unload()` and save), or use the fallback in
section 5.

**Step 2: Hugging Face to GGUF and quantize** (do this on Colab or a laptop, not the Pi):

    git clone https://github.com/ggml-org/llama.cpp
    pip install -r llama.cpp/requirements.txt
    python llama.cpp/convert_hf_to_gguf.py hf_export/ --outfile jhs-gemma3-1b-f16.gguf --outtype f16
    # build llama.cpp (cmake) to get llama-quantize, then:
    ./llama.cpp/build/bin/llama-quantize jhs-gemma3-1b-f16.gguf jhs-gemma3-1b-Q4_K_M.gguf Q4_K_M

Copy `jhs-gemma3-1b-Q4_K_M.gguf` to the Pi with a USB drive or `scp`. Re-run the 5 test
questions on the quantized model, because 4-bit quantization can change answers.

### 4c. Serve on the Pi

**Option A: Ollama.** Create a file called `Modelfile` next to the GGUF:

    FROM ./jhs-gemma3-1b-Q4_K_M.gguf
    TEMPLATE """<start_of_turn>user
    {{ .Prompt }}<end_of_turn>
    <start_of_turn>model
    """
    PARAMETER stop "<end_of_turn>"
    PARAMETER num_predict 160
    PARAMETER temperature 0.2

Then:

    ollama create jhs-flashcards -f Modelfile
    ollama run jhs-flashcards "What is an indicator?"

**Option B: llama.cpp server** (build llama.cpp on the Pi with cmake):

    ./build/bin/llama-server -m jhs-gemma3-1b-Q4_K_M.gguf --host 0.0.0.0 --port 8081 -c 512 -n 160

It provides a simple web page and an HTTP API on port 8081 for devices on the local network.

Keep answers short (`num_predict` / `-n` around 160 tokens) so cards come back in a reasonable
time. A low temperature keeps answers closer to the training style.

## 5. Fallback: pre-generated, teacher-approved cards inside Kolibri

If the model is too slow on the Pi, cannot be exported, or is not yet approved, students can
still benefit:

1. On Colab, use the fine-tuned model to generate cards for the full list of syllabus questions.
2. A science teacher reviews every card (accept, correct or reject), using the rating sheet.
3. Put the approved cards into a simple offline HTML page or PDF, and add it to a Kolibri
   channel with **Kolibri Studio** (https://studio.learningequality.org/), or import it into
   Kolibri as a document.
4. Students revise from Kolibri with no model running on the Pi at all.

This fallback is actually the safest option for a first pilot, because every card a student sees
has been checked by a teacher.

## 6. Classroom rules (from the governance brief)

- No student accounts or personal data are needed for the flashcards; do not log names.
- Switch the model off (or block access) during tests and exams.
- Keep a paper or on-screen error form next to the Pi; the teacher fixes reported cards.

## 7. Measurements to record (to be measured)

| Measurement | Base `gemma3:1b` | Fine-tuned Q4_K_M |
|---|---|---|
| Model file size | | |
| RAM used while answering (`free -h`) | | |
| Seconds to first word | | |
| Seconds for a full card | | |
| CPU temperature after 10 questions | | |
| Throttling seen? (`vcgencmd get_throttled`) | | |
| Works alongside Kolibri at the same time? | | |
