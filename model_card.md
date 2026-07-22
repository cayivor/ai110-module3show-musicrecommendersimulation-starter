# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  
One major limitation discovered during stress testing is the algorithm's vulnerability to "genre silos" and strict string-matching failures. Because the scoring logic heavily weights the categorical genre match (+2.0 points) using strict text equivalency, users might miss highly relevant tracks if their profile requests "LoFi Chill" but the dataset is labeled simply as "Lofi". Additionally, this heavy categorization weight creates a filter bubble where cross-genre songs with the exact target energy and mood are mathematically suppressed in favor of weaker acoustic matches that happen to share the preferred genre tag.
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.
### Stress Test Results

During evaluation, I tested four distinct user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an adversarial "High-Energy Sad Classical" curveball. The biggest surprise was an unintended string-matching failure in the Chill Lofi profile. The system searched for "LoFi Chill", but the dataset used "Lofi", meaning the top song missed out on the +2.0 genre bonus. However, the system still successfully ranked the correct track ("Coffee Shop Rain") as number one because the continuous energy and mood mathematical fallbacks worked perfectly to pull it to the top.

### Profile Comparisons

*   **High-Energy Pop vs. Deep Intense Rock:** Both profiles requested massive energy targets (0.90 and 0.95). However, the recommendations were completely distinct. The algorithm successfully used the Genre and Mood categorical anchors to separate the users, proving the system can differentiate between "upbeat dance energy" and "heavy aggressive energy."
*   **Chill Lofi vs. Deep Intense Rock:** These outputs demonstrated the power of the `energy_similarity` formula. While the Rock profile pulled tracks near 1.00 energy, the Lofi profile completely abandoned those tracks, successfully identifying and elevating slow, low-energy tracks (Energy ~0.20). This proves the absolute difference math effectively measures and matches the listener's target vibe, even when text filters fail.
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
