# Sustainability and environmental justice plan (Course 07 format)

> Status: draft for me to check and put into my own words where needed. No energy or carbon
> figures are given here because none have been measured yet; measured values (training time on
> Colab, Pi power draw) go in `PROJECT_REPORT.md` once available.

## Three-level table

| Level | Action | Environmental impact | Who benefits | Who might lose out |
|---|---|---|---|---|
| **Developer** (me) | Fine-tune an existing small model (Gemma 3 1B) once with LoRA rank 4 on a free Colab GPU; no pre-training; short sequence length (256); a few epochs only; quantize to 4-bit so it runs on a low-power Raspberry Pi 4 | Much less compute than pre-training or full fine-tuning; one short training run; inference on a low-power local device instead of a data centre | Schools (low running cost); the wider public (less data-centre demand) | Accuracy may be lower than a larger model, so students could get weaker answers if review is skipped |
| **Stakeholder** (teachers, school heads, parents, local repairers) | Reuse phones and laptops students and schools already have; run the Pi from a UPS or small solar panel where possible because of dumsor (unreliable grid power); agree simple usage hours | Avoids buying new devices; adds a small, steady electricity load; batteries and Pis eventually become e-waste | Students without internet; teachers who save preparation time | Schools with no devices or no power at all; people near informal e-waste sites if devices are dumped |
| **Organisational** (deploying school, district, GES or NGO partner) | Own the hardware; plan repair, reuse and take-back of Pis, SD cards, SSDs and batteries; decide whether to scale only after a pilot; share the dataset and model openly so others do not retrain from scratch | Fewer duplicate training runs across organisations; responsible end-of-life handling reduces e-waste harm | Other schools and developers who reuse the work | Organisations that must fund maintenance; rural schools left out if scaling follows money instead of need |

## Mini-plan (target 250 to 300 words)

**Who decides about resource use.** I decide how the model is trained: one small model, fine-tuned
once with LoRA, then quantized, instead of pre-training or calling a cloud model for every
question. Google's 4Ms guide these choices: an efficient **Model** (1B parameters, LoRA), an
efficient **Machine** (a Colab GPU for one short run, then a low-power Pi), **Mechanization**
(shared cloud infrastructure for training rather than my own hardware) and **Map** (where the
compute runs; I cannot choose the Colab data-centre location, which I note as a limit). The
school head and teachers decide deployment: how many Pis, when they run and how they are powered.

**How benefits and risks are distributed.** The main benefit goes to students in schools without
internet, who are usually left out of AI tools. The costs are a small electricity load on a
fragile grid (dumsor) and future e-waste. In Ghana, e-waste often ends up in informal
recycling sites where nearby communities carry the health burden, so the plan must not shift
harm onto them. A rebound effect is also possible: if the tool works well, schools may buy many
new devices or keep them on all day, cancelling the efficiency gains. Reusing existing devices
and setting usage hours limits this.

**Who is responsible.** I am responsible for an efficient model, honest documentation and open
sharing. The deploying school or organisation is responsible for power, repair, and taking back
devices at end of life. Following Ubuntu or Ukama ("I am because we are"; everything is
connected), responsibility is shared: students, teachers, parents and the wider community
should all have a say, and benefits for one school should not create burdens for another
community.

(My own additions or changes:)
