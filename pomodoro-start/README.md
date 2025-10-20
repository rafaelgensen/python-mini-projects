# Pomodoro Timer ⏱️🍅

A simple Pomodoro time management app built with Python and Tkinter.

## 📋 About

This is a graphical Pomodoro timer application that helps users manage their time using the Pomodoro Technique. The app cycles through work and break sessions, and includes:

- 1-minute work sessions (configurable)
- 5-minute short breaks
- 20-minute long breaks after 4 work sessions
- Reset and Start buttons
- Visual progress tracking with check marks

## 🖼️ Screenshot

![screenshot](screenshot.png) <!-- Replace with actual image if available -->

## 🧠 Pomodoro Technique Overview

1. Work for a focused session (default: 1 min for demo).
2. Take a short break (5 mins).
3. After four work sessions, take a long break (20 mins).
4. Repeat the cycle.

## 🚀 Features

- Countdown timer with GUI
- Start and reset functionality
- Visual session tracking (✔️)
- Customizable session durations
- Clean, minimal interface

## 🛠️ Tech Stack

- Python 3
- Tkinter (standard GUI library)
- PIL or image viewer (optional, for displaying the tomato image)

## ⚙️ Configuration
You can modify the session durations by changing these constants in main.py:

```python
Copiar código
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
```

## 🧾 License
This project is open-source and available under the MIT License.

## 🙌 Acknowledgements
Inspired by the Pomodoro Technique by Francesco Cirillo