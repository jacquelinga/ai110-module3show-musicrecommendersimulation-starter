from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        """Create a recommender with the supplied song catalog."""
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return up to k songs from the catalog."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a song matches the user's preferences."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load song records from a CSV file."""
    import csv

    numeric_fields = ("energy", "tempo_bpm", "valence", "danceability", "acousticness")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            for field in numeric_fields:
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and describe the points awarded."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("Genre match (+2)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 2.0
        reasons.append("Mood match (+2)")

    energy_points = 2.0 * (1.0 - abs(song["energy"] - user_prefs["target_energy"]))
    score += energy_points
    reasons.append(f"Energy similarity (+{energy_points:.2f})")

    return float(score), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top k songs ranked by preference score with explanations."""
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, "; ".join(reasons)))

    return sorted(scored_songs, key=lambda result: result[1], reverse=True)[:k]
