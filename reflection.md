💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

**##1. What was broken when you started?**

The first time I ran the game, the interface loaded correctly, but the behavior of hints, scoring, and game state was inconsistent. For example, sometimes the hints were wrong: the game would display “📉 Go LOWER!” even when my guess was below the secret number, which indicated that the check_guess logic wasn’t being applied correctly or the wrong value was passed. Another issue was that the score occasionally jumped to unexpected numbers or didn’t update after submitting a guess, likely due to how update_score interacted with st.session_state.attempts. Finally, restarting the game with the “New Game 🔁” button sometimes left previous guesses in st.session_state.history or didn’t reset st.session_state.status correctly, which made repeated plays confusing. Overall, the game looked like it should work, but the state management and hint logic were glitchy and unreliable.

---

## 2. How did you use AI as a teammate?

I used VS Code Copilot extensively to understand and refactor the game logic, and I consulted ChatGPT when I wasn’t sure why certain functions behaved incorrectly. One correct AI suggestion was moving the check_guess and parse_guess functions to logic_utils.py and adjusting their inputs and outputs so they consistently returned integers and string outcomes. I verified the fix by submitting guesses in the game and checking that the hints now matched expectations every time. One misleading suggestion was when the AI proposed changing update_score to recalculate the score based on the raw input rather than validated guesses. I ran the game and saw that scores became inconsistent, so I rejected the suggestion and kept the scoring tied to validated outcomes in st.session_state. This showed me that AI can speed up debugging, but careful testing is essential.

## 3. Debugging and testing your fixes

I verified bug fixes using both manual gameplay testing and automated pytest cases. For example, I wrote a test for check_guess in test_game_logic.py to ensure that a guess of 60 against a secret of 50 returned “Too High,” a guess of 40 returned “Too Low,” and a guess of 50 returned “Win.” Running pytest confirmed that all cases passed and the logic was correct. I also submitted guesses in the live Streamlit app to confirm that the hints, score updates, and game reset behavior were correct. AI helped me design these tests by suggesting specific edge cases, like invalid input strings, boundary values, and repeated guesses, which ensured the game handled all realistic scenarios.


---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script every time the user interacts with the app, which means that any variables not stored in st.session_state will reset on each interaction. For example, without session state, attempts or score would go back to zero every time a button was clicked. To explain this to a friend, I would say: “Streamlit works like a flipbook - every click redraws the entire app. If you want information like the score or previous guesses to stick, you must store it in session state, which acts as persistent memory across reruns.” Understanding this was crucial for fixing glitches related to the New Game button and ensuring scores and history updated correctly.

---

## 5. Looking ahead: your developer habits

One habit I want to carry forward is marking problem areas with #FIXME: comments, which helped me focus on debugging and guide AI suggestions precisely. I also plan to write automated tests immediately after fixing a bug, so I can verify each fix and prevent regressions. Next time I work with AI on a coding task, I will be more deliberate in reviewing suggestions line by line rather than applying large multi-file changes at once, because even helpful AI can introduce subtle errors. I think that this project changed the way I think about AI-generated code: it reinforced that AI can significantly speed up development and debugging, but human oversight and critical testing are still essential to produce reliable, correct software.
