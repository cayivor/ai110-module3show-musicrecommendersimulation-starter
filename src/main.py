"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile

    user_prefs = {
        "favorite_genre": "Classical",
        "favorite_mood": "Sad",
        "target_energy": 0.95 
    }
    
    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    recommendations = recommend_songs(user_prefs, songs, k=3)
    
    for i, (song, score, reasons) in enumerate(recommendations, 1):
        print(f"{i}. {song['title']} by {song['artist']} (Score: {score:.2f})")
        reasons_string = ", ".join(reasons)
        print(f"   Why: {reasons_string}\n")


if __name__ == "__main__":
    main()
