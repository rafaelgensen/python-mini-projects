# Quiz Game 🎮

A simple **True/False Quiz Game** built in Python.  
This project demonstrates object-oriented programming (OOP) concepts such as classes, objects, and encapsulation, while keeping the logic modular and easy to extend.

---

## 📂 Project Structure

Quiz-Game/
│── art.py # ASCII art / title screen
│── data.py # Quiz questions data
│── main.py # Entry point for the game
│── question_model.py # Defines the Question class
│── quiz_brain.py # Handles the quiz logic
│── README.md # Documentation

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/quiz-game.git
   cd quiz-game
   ```

2. Run the game:
   python main.py

## 🧩 How It Works

Question class: Represents each question with its text and answer.

QuizBrain class: Controls the flow of the quiz (asking questions, checking answers, tracking score).

main.py: Initializes the game, loads the questions, and starts the quiz loop.

data.py: Provides the question set. You can add more questions here.

art.py: Optional ASCII art to display at the start of the game.

## ✨ Example Gameplay

Q.1: The Earth is flat (True/False)?: false
You got it right!
The correct answer was: False.
Your current score is: 1/1

Q.2: Python is a programming language (True/False)?: true
You got it right!
The correct answer was: True.
Your current score is: 2/2

## 🛠️ Features

Object-Oriented Design

Modular code (easy to extend with new features)

Simple and interactive CLI game

Tracks score dynamically

## 📌 Future Improvements

Add multiple-choice questions

Store questions in an external JSON/CSV file

Build a GUI version with Tkinter or PyQt

Fetch questions dynamically from an API