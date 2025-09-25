# 🗺️ U.S. States Game

A simple and educational Python game to test your knowledge of U.S. state names and locations. Built using `turtle` graphics and `pandas`.

![Preview](us-states-game.gif)

---

## 🚀 How to Run

1. Make sure you have Python installed (**version 3.7+** recommended).
2. Clone this repository and navigate into the folder:
   ```bash
   git clone https://github.com/your-username/us-states-game.git
   cd us-states-game
   ```

3. Ensure you have the following files in the same directory:
   - `main.py` (or the script name)
   - `50_states.csv` — Contains state names and their `(x, y)` coordinates
   - `blank_states_img.gif` — A map image of the U.S. used as background

4. Install the required Python packages (only `pandas` is external):
   ```bash
   pip install pandas
   ```

5. Run the game:
   ```bash
   python main.py
   ```

---

## 🎮 How to Play

- The game will show a blank map of the United States.
- A prompt will ask you to enter the name of a state.
- If you guess correctly, the state's name will appear on the map in its correct location.
- Type `"Exit"` to end the game early. A file `states_to_learn.csv` will be created with the states you missed.

---

## 🧠 Educational Goal

This game helps improve geographic knowledge by encouraging the player to recall and identify all 50 U.S. states by name and location.

---

## 📂 Project Structure

```bash
us-states-game/
│
├── main.py                  # Main game script
├── 50_states.csv            # Contains state names and coordinates
├── blank_states_img.gif     # U.S. map image used in the game
├── states_to_learn.csv      # (Auto-generated) List of unguessed states
└── README.md                # Project documentation
```

---

## 📦 Requirements

- Python 3.7+
- `pandas`
- `turtle` (built-in)

Install dependencies with:

```bash
pip install pandas
```

---

## 📝 Notes

- The game is case-insensitive thanks to `.title()`, but spelling must be accurate.
- Works on all major operating systems (Windows, macOS, Linux).
- The file `states_to_learn.csv` can help you study the states you missed.

---

