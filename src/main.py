"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    high_energy_pop = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
    }
    chill_lofi = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.3,
    }
    intense_rock = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.9,
    }
    profiles = [
        ("High-Energy Pop", high_energy_pop),
        ("Chill Lofi", chill_lofi),
        ("Intense Rock", intense_rock),
    ]

    for profile_name, user_prefs in profiles:
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\n{profile_name} - Top 5 recommendations:\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
