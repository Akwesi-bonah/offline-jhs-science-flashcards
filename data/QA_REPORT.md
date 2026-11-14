# QA report: JHS Integrated Science flashcards

Date: 2026-11-14. File: `data/jhs_flashcards.json`.

## Summary

| Item | Count |
|---|---|
| Cards reviewed | 110 (5 hand-written seed, 105 synthetic) |
| Cards edited | 7 |
| New cards added | 19 |
| Final total | 129 |

Validation: `python3 -I scripts/check_dataset.py data/jhs_flashcards.json` reports "No problems found" (129 cards, all 20-120 words, all questions end with "?", no duplicates). `scripts/export_jsonl.py` wrote 129 rows to `data/jhs_flashcards.jsonl`. No em or en dashes in the file.

Each card was checked for factual errors, false oversimplifications, Ghana-specific claims, wording for ages 12-15, and whether the answer actually answers the question. Most cards were accurate and suitable. Edited cards keep their original source with " (edited in QA)" appended.

## Cards changed

| # (index) | Name | Problem | Fix |
|---|---|---|---|
| 0 | Photosynthesis (seed) | Said chlorophyll "produces glucose". Chlorophyll traps light energy; the leaf makes the glucose. | Reworded so chlorophyll traps light and the leaf uses it to make glucose from CO2 and water. |
| 14 | Evaporation | "Usually when it is heated" implies evaporation needs heating. Evaporation happens at the surface at any temperature below boiling, and this is a common exam point (evaporation vs boiling). | Defined it as a surface change at any temperature below boiling; added "dry" to the factors. |
| 29 | Renewable energy | "Ghana generates much electricity from the Akosombo dam" overstates hydro. Today most of Ghana's electricity comes from thermal (gas/oil) plants; hydro is roughly a third. | Changed to "Ghana gets part of its electricity from hydroelectric dams such as Akosombo on the Volta River". |
| 79 | Drug abuse | "Taking medicines without a prescription" is wrong as stated: many medicines (e.g. paracetamol) are legally sold without one. | Replaced with overdosing beyond the doctor's or label's directions and taking medicine meant for someone else. |
| 89 | Insects | "Usually two pairs of wings" while listing houseflies and mosquitoes, which have only one pair. Factual error. | Most adult insects have wings; bees and grasshoppers have two pairs, flies and mosquitoes one pair. |
| 100 | Water purification | Said filtering through a clean cloth makes water safe to drink. Cloth filtering removes dirt but not germs; this is a health risk. | Boiling or chlorine kills germs; filtering removes dirt only and should be followed by boiling or treatment. |
| 102 | Seasons in Ghana | "Ghana has a rainy season and a dry season" is false for the south, which has two rainy seasons. | South: major rains about April to July, minor rains about September to November; north: one rainy season about May to October; harmattan kept. |

## Cards a teacher should check

These are not known to be wrong, but a teacher should confirm them against the current syllabus and textbooks:

- **29 Renewable energy, and new card "Akosombo hydroelectricity"**: the energy-mix wording is deliberately vague ("part of its electricity"). Confirm the teacher is happy with it, and with the claim that Lake Volta is one of the largest man-made lakes in the world.
- **102 Seasons in Ghana**: month ranges are approximate and differ slightly between textbooks.
- **22 Indicators and new card "Sobolo as an indicator"**: hibiscus (sobolo) works as an acid-base indicator, but the exact colour in base (purple, blue or green) depends on how strong the drink is. Ideally a teacher should try it in class.
- **76 Puberty**: says it "usually begins between ages 9 and 15". Typical ranges are about 8 to 13 for girls and 9 to 14 for boys; check against the textbook.
- **87 Classification**: lists "plants, animals, fungi and bacteria" as kingdoms. The Ghana JHS syllabus may use the five-kingdom system (including Protista/Protoctista); consider aligning.
- **21 Acids and bases**: describes acids as tasting sour and bases as slippery (standard textbook content). A teacher may want a line saying never to taste or touch laboratory chemicals.
- **46 Deforestation**: "reduces rainfall" is standard textbook content but is a simplification of local climate effects.
- **113 Galamsey**: names the Pra, Ankobra and Birim as affected rivers and mentions mercury use. These are widely reported, but confirm wording is appropriate for the class.
- **115 Cocoa fermentation**: "about a week" under plantain or banana leaves is typical (often 5 to 7 days); check local practice.
- **All 105 synthetic cards and 19 new cards** still carry "needs teacher review" and have not been checked by a qualified teacher.

## New cards added (19)

Source: "synthetic (Claude QA batch), needs teacher review". Category: Integrated Science.

Student-style phrasings of existing topics (different wording, not duplicate questions):

1. Why does ice melt when I hold it in my hand?
2. Why does my cutlass get rusty when I leave it outside in the rain?
3. Why do clothes on the line dry faster on a sunny, windy day?
4. Why does the Moon look full and round some nights but like a thin curve on other nights?
5. Why should I sleep under a mosquito net even when I feel healthy?
6. Why does a football always come back down when I kick it up into the air?
7. Why do I feel cool after a bath even on a hot day?
8. Why do we see lightning before we hear thunder?
9. Why can't I eat only banku every day if it fills me up?

Ghanaian-context cards:

10. Why does sobolo change colour when baking soda is added to it?
11. Why do my lips crack and my skin feel dry during harmattan?
12. How does galamsey pollute our rivers?
13. How does the Akosombo dam produce electricity?
14. Why are cocoa beans fermented and dried before they are sold?
15. Why must cassava be processed before it is eaten as gari?
16. Why do many farmers in northern Ghana grow millet and sorghum?
17. Why do I get small electric shocks from clothes or door handles during harmattan?
18. Why is it harmful to burn plastic rubbish in the house compound?
19. How is salt made at the Songor Lagoon near Ada?

## Coverage by curriculum strand

Each card is assigned to one main strand (a judgement call; some cards fit more than one).

| Strand | Cards | Of which new | Topics covered |
|---|---|---|---|
| Diversity of matter | 30 | 4 | states of matter, living things, cells, mixtures and separation, elements and compounds, acids/bases/indicators, atoms, particles, density, measurement, classification, rocks, air, rusting, physical vs chemical change, solutions |
| Cycles | 21 | 4 | food chains, decomposers, water cycle, evaporation, condensation, pollination, germination, flowers, seed dispersal, mosquito life cycle, crop rotation, weather and seasons, day and night, Moon, eclipse, cocoa processing, crops and climate |
| Systems | 16 | 0 | photosynthesis, respiration, digestive, circulatory, respiratory, skeletal, excretory systems, teeth, puberty, solar system, ecosystems, habitats |
| Forces and energy | 35 | 5 | force, friction, gravity, mass/weight, energy forms and conversion, renewable/non-renewable energy, circuits, magnets, electromagnets, light, sound, heat transfer, simple machines, work, speed, pressure, static, electrical safety, fire triangle |
| Humans and the environment | 27 | 6 | malaria, cholera, hygiene, nutrition and deficiency diseases, immunisation, HIV, drug abuse, soil erosion and conservation, fertilisers, pollution, galamsey, climate change, deforestation, waste, water safety, food processing |
| **Total** | **129** | **19** | |

## Remaining gaps

- **Systems is the thinnest strand (16 cards).** Missing: nervous system and sense organs (eye, ear), reproductive system details, plant transport (xylem/phloem), the circulatory system beyond the heart (arteries, veins, capillaries).
- **Matter:** no cards on the particulate model of liquids and gases, metals vs non-metals, the periodic table basics, simple chemical symbols and formulae, or acid-base reactions in daily life (antacids, bee and ant stings).
- **Forces and energy:** no cards on moments calculation, the lens/eye, colours and the spectrum, current/voltage/resistance basics, or solar panels in Ghana.
- **Cycles:** no carbon or nitrogen cycle cards, no life cycle of a flowering plant end to end, no cards on the menstrual cycle or life cycles of other pests (housefly, tsetse).
- **Humans and the environment:** nothing on first aid, sanitation and bilharzia/guinea worm, coastal erosion (e.g. Keta), bush fires in the savanna, or the role of forest reserves and Kakum.
- **Ghanaian context** is still concentrated in a few topics (harmattan, foods, Akosombo). More local examples in physics and chemistry cards would help.
- **Question style:** most original questions are textbook style ("What is X?"). Only 9 student-style phrasings exist; more variety (misspellings, Ghanaian English phrasing, "explain to me" requests) would make the fine-tuned model more robust.
- **Calculation practice:** only speed has a worked example; density, pressure and work could use worked number examples.
- No card has been reviewed by a qualified science teacher yet.
