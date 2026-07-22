# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
Modern streaming platforms rely on a hybrid recommendation architecture, blending collaborative filtering—which analyzes the listening behavior of similar user communities—with content-based filtering, which examines the acoustic properties of the audio itself. To build a highly focused prototype, this simulation prioritizes a pure content-based engine. It calculates the mathematical distance between a listener's target taste profile and a track's specific acoustic features to serve the closest possible match. Under the hood, the Song models evaluate genre, energy, valence, and tempo_bpm, while the UserProfile tracks parallel target variables (preferred_genre, target_energy, target_valence, and target_tempo) to define the user's desired vibe.


he recommendation engine calculates a compatibility score for each track based on a combination of strict categorical filters and continuous acoustic feature mapping. Each song starts at a baseline score of 0.0 and is evaluated against the user's taste profile using the following weights:

Genre Anchor (+2.0 points): An exact string match with the user's favorite_genre. This acts as the primary baseline, as genre heavily dictates the structural acoustic profile and instrumentation of a song.

Mood Modifier (+1.0 point): An exact string match with the user's favorite_mood. This serves as a secondary weight to align the track's emotional intent.

Energy Proximity (Up to +1.0 point): A dynamic similarity score calculated using the absolute difference between the track's energy and the user's target energy (1.0 - | Song Energy - Target Energy |). This ensures tracks with the closest acoustic "vibe" receive the highest fractional bonus.

Known Biases & Limitations
Because the algorithm heavily weights exact genre matches, the system has a strong categorical bias. It risks operating in a "genre silo," potentially rejecting highly relevant cross-genre tracks that perfectly match the listener's energy and mood targets but fail the strict genre string comparison. This means a user seeking a relaxed vibe might miss out on a perfectly calm R&B track simply because their profile is set to LoFi.
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


## Sample Recommendation Output

```text
Top recommendations:

1. Neon Nights by SynthWave (Score: 1.00)
   Why: Energy similarity (+1.00)

2. Sunrise City by Neon Echo (Score: 0.97)
   Why: Energy similarity (+0.97)

3. Storm Runner by Voltline (Score: 0.94)
   Why: Energy similarity (+0.94)



