# Problem statement (draft v2, capstone)

## The problem
Junior high school (JHS) students in rural and under-resourced Ghanaian schools have too few
revision materials that match the national curriculum, and the digital study tools that exist
usually need a steady internet connection and are built around foreign curricula. Students
preparing for the Basic Education Certificate Examination (BECE) therefore depend heavily on
shared textbooks and limited teacher time.

## Context
- Many rural schools have unreliable or expensive internet and frequent power cuts.
- Students increasingly have access to shared phones or old laptops, even where internet is poor.
- Teachers carry large classes and cannot write individual revision material for every topic.
- **First-hand observation:** as a student teacher from the University of Education, Winneba,
  I noticed during my teaching practice that most of the schools I worked in do not give
  students internet access, so students cannot use online AI study tools at all, even though
  these tools are becoming common elsewhere. This widens the gap between those students and
  better-connected schools.

## What this project will do (scope)
Fine-tune Gemma 3 1B with LoRA to generate short, accurate revision flashcards (a category plus
a 2 to 4 sentence answer) for the JHS **Integrated Science** curriculum, written in plain
English. The model will be quantized to run **offline on a Raspberry Pi 4 (4 GB)** acting as a
classroom server, so students can revise from nearby devices without internet.

## Boundaries (what it will NOT do)
- It is a revision aid, not a teacher replacement and not a source of exam answers.
- One subject first (Integrated Science); other subjects and Twi explanations are future work.
- It will not collect students' personal data.
- Teachers review the card set before classroom use.

## Why it is needed and realistic
- It targets a real gap (curriculum-matched, offline revision) using low-cost hardware.
- Fine-tuning an existing small model once, with LoRA, keeps compute, cost and energy low,
  instead of training a new model or relying on cloud data centres.
- A 150 to 300 card dataset, written from public curriculum topics, is achievable in the
  capstone timeframe.

## Who it is for
JHS students (main users), supported by their teachers; parents and school heads are secondary
stakeholders.

## Success looks like
Teachers rate most generated cards as accurate, on-curriculum and age-appropriate; the model runs
offline on the Pi 4 within an acceptable wait time for a short card.

## Feedback from explaining it to someone
- Who I explained it to:
- Questions they asked ("Why?", "Who is this for?"):
- Gaps I fixed:
