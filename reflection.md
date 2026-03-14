# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

The first time I ran the game, it looked like a simple number guessing game with a sidebar for difficulty and some debug info showing the secret number, attempts, and score. Right away, I noticed that the hints sometimes told me to “Go HIGHER!” even when I guessed the secret number correctly, which was confusing. Another issue was that the scoring system seemed inconsistent; sometimes I gained points for wrong guesses, and other times I lost points unexpectedly. Finally, starting a new game didn’t fully reset everything - my previous score and guess history stayed, making the game feel glitchy and unfair. Overall, the game ran without crashing, but these logic and state issues made the experience unpredictable.


## 2. How did you use AI as a teammate?

In this version of the game, several issues were corrected with the help of AI suggestions from GitHub Copilot. One improvement involved how hint messages are handled. Previously, the game sometimes displayed incorrect hints because the logic for generating messages was mixed with the comparison logic. The AI agent suggested separating the hint messages into their own function that determines the correct message based on whether the guess was too high, too low, or correct. This makes the hints consistent and easier to manage. Another fix involved resetting the game state when the player starts a new game. In the earlier version, starting a new game did not fully reset the session state, meaning values such as the score, attempt counter, and guess history could carry over from the previous round. The updated version ensures that all of these values are reset so the game truly starts fresh each time. A third improvement addressed a potential type mismatch problem. In the earlier version, the secret number could sometimes be treated as a string while the player's guess was an integer, which could lead to incorrect comparisons and misleading hints. With the help of Copilot, the logic was adjusted so that the comparison always uses numeric values, preventing type errors and ensuring that guesses are evaluated correctly.


---

## 3. Debugging and testing your fixes

To know if a bug was fixed, I decided to play the game multiple times with different guesses and watch whether the hints, scores, and resets behaved consistently. For example, I tested the hint logic manually by guessing the correct number on the first attempt, then on even and odd attempts, and verified that the hints always reflected whether I should go higher or lower. This showed me that the string conversion issue was resolved. AI helped me design the manual tests by suggesting edge cases, such as checking behavior on the last attempt or after clicking “New Game,” which ensured that all session state variables were correctly reset.


---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script from top to bottom every time a user interacts with an input or button, which is why session state is crucial for storing persistent data like the secret number, score, and attempts. Without st.session_state, every button press would reset the game to the initial state, losing all progress. I would explain this to a friend by saying, “Streamlit reruns your code every time something changes, so if you want things to remember their values, you have to put them in session state like a tiny database that lives during the session.”


---

## 5. Looking ahead: your developer habits

One habit I want to reuse is systematically documenting observed glitches before trying to fix them, including the expected behavior versus the actual behavior. It made debugging much more structured and helped me communicate problems clearly. Next time I work with AI, I would test AI suggestions more cautiously and verify them step by step instead of blindly accepting them. This project changed the way I think about AI-generated code by showing me that AI can speed up understanding and give ideas, but human judgment is absolutely essential for spotting logic errors, testing edge cases, and ensuring reliability.

