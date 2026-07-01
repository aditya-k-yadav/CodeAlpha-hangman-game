# 🎮 Hangman 

A modular, feature-rich Hangman game built using Python. This project goes beyond a basic implementation by incorporating clean architecture, a hint system, and visual gameplay elements.

---

## 🚀 Features

* 🎯 **100+ Word Pool** for better gameplay variety
* 💡 **Hint System** (with penalty) to assist players
* 🎨 **ASCII Hangman Visuals** that update with incorrect guesses
* 🔁 **Replay Option** to play multiple rounds
* 🧠 **Input Validation** to handle invalid entries
* 🧩 **Modular Code Structure** (engine, UI, logic separation)

---

## 🏗️ Project Structure

```
hangman_project/
│
├── main.py
│
├── game/
│   ├── engine.py        # Core game logic
│   ├── words.py         # Word selection (100+ words)
│   ├── hint.py          # Hint system
│   ├── hangman_art.py   # ASCII visuals
│
├── ui/
│   └── console_ui.py    # User interaction (console)
```

---

## 🧠 Concepts Used

* Python fundamentals (loops, conditionals, functions)
* Object-Oriented Programming (class-based design)
* Modular programming (separation of concerns)
* Lists and string manipulation
* Random module

---

## ⚙️ How to Run (VS Code)

### 1. Clone or Download the Project

```bash
git clone <your-repo-link>
cd hangman_project
```

### 2. Open in VS Code

```bash
code .
```

### 3. Run the Game

```bash
python main.py
```

---

## 🎮 How to Play

1. The game selects a random word.
2. The word is displayed as underscores (`_ _ _ _`).
3. Enter one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses draw the hangman.
6. You can type `hint` to reveal a letter (costs 1 life).
7. Win by guessing the full word before running out of attempts.

---

## 🧪 Future Improvements

* 🗂️ Word categories (file-based loading)
* 💾 Score tracking using JSON
* 🎨 Colored terminal output (colorama)
* 🖥️ GUI version using Tkinter or PyQt
* 📊 Game analytics (win rate, guesses tracking)

---

## 📜 License

This project is open-source and intended for learning purposes.

---

## ⭐ Support

If you found this project useful:

* Give it a ⭐ on GitHub


---

