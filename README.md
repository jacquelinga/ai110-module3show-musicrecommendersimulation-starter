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
Music recommendation systems use users listening habits and song characteristisc to predict what they might enjoy. some systems compare users with similar interests, others base their recommendations based on genre, mood, energy and tempo. Mine will use a content based approace that compares song attributes with a users preferences. I gave grenre and mood equal importance becuase both the style and feeling matter in my opinion. energy, valence and tempo will help determine how closely a song matches the users taste. each song will recieve a score and the songs with the highest scores will be recommended first. Each song stores its ID, title, artist, genre, mood, energy, templo, valence, daceability, and acoustiness. these descrive the song and help the recommender compare. the users tatse stores their favorite genre, mood, energy level and whether they prefer acousic music. the recommender uses these preferences to determine which songs are the best matches. 
My recipe:
my recommender uses a weighted scoring system to compare each song with the users preferences. Genre(+2), Mood(+2), energy(0-2). energy is calculated using 2*(1-abs(song_energy-target_energy)) each song received a max of 6 points. the system evaluates every song in the file, sorts them from highest to lowest score and recommends the best matches. 
Some potential biases are that my recommendor may overlook songs from other categories and only focus on the users favorite genre. 

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

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
Top recommendations:

Sunrise City - Score: 5.96
Because: Genre match (+2); Mood match (+2); Energy similarity (+1.96)

Rooftop Lights - Score: 3.92
Because: Mood match (+2); Energy similarity (+1.92)

Gym Hero - Score: 3.74
Because: Genre match (+2); Energy similarity (+1.74)

Velvet Weekend - Score: 1.98
Because: Energy similarity (+1.98)

Night Drive Loop - Score: 1.90
Because: Energy similarity (+1.90)

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



