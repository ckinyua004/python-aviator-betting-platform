# python-aviator-betting-platform
# 🎮 Rigged Aviator Game Simulation (Python)

This is a Python simulation of the popular **Aviator betting game**, but with a twist — it's rigged.  
This version mimics how the game may favor the house by adjusting crash outcomes based on bet size and account balance.

---

## 📌 Features

- 🚀 Plane takes off with an increasing multiplier.
- 🧠 Cash out simulation at 2.0x (auto for now).
- 🎯 Rigged behavior:
  - Large bets = early crash
  - Small balance = high crash potential
  - Bet over KSh 1000 = more likely to crash below 1.5x
- 💸 Balance system to track winnings/losses
- 🔁 Loop to allow multiple rounds

---

## 🧠 Rigging Logic

| Condition                  | Effect                     |
|---------------------------|----------------------------|
| Bet > KSh 1000            | Crash likely under 1.5x    |
| Balance < KSh 500         | Higher chance of big win   |
| Normal bet & balance      | Fair-ish (randomized)      |

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed

---

## ▶️ How to Run

1. Clone the repo or copy the script.
2. Save it as `aviator.py`.
3. Run the game:

```bash
python aviator.py
# python-aviator-betting-platform
# python-aviator-betting-platform
