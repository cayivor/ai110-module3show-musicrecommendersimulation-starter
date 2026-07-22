import csv
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
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    return []

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []

def load_songs(filepath: str) -> List[Dict]:
    parsed_songs = []
    
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            # Convert numerical columns from strings so we can do math on them
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = int(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            
            parsed_songs.append(row)
            
    return parsed_songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    score = 0.0
    reasons = []

    # Rule 1: Genre check
    if song['genre'] == user_prefs['favorite_genre']:
        score += 2.0
        reasons.append("Genre match (+2.0)")

    # Rule 2: Mood check
    if song['mood'] == user_prefs['favorite_mood']:
        score += 1.0
        reasons.append("Mood match (+1.0)")

    # Rule 3: Energy similarity
    energy_diff = abs(song['energy'] - user_prefs['target_energy'])
    energy_points = 1.0 - energy_diff
    
    score += energy_points
    # Round to 2 decimal places to keep the output clean
    reasons.append(f"Energy similarity (+{energy_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 3) -> List[Tuple[Dict, float, List[str]]]:
    scored_songs = []
    
    # Judge every song in the catalog
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, reasons))
        
    # Sort the list from highest score to lowest
    top_songs = sorted(scored_songs, key=lambda x: x[1], reverse=True)
    
    # Return only the top 'k' results
    return top_songs[:k]