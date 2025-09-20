# Coffee Machine ☕️

A Python-based **Coffee Machine Simulator** that models real-world behavior of a coffee machine:  
handling ingredients, processing coins, checking resources, and serving drinks.

This project applies **Object-Oriented Programming (OOP)** with multiple classes, each responsible for a specific part of the machine.

---

## 📂 Project Structure

```
Coffee-Machine/
│── coffee_maker.py # Handles resources and making coffee
│── money_machine.py # Manages coins and transactions
│── menu.py # Defines drinks and menu
│── main.py # Entry point for the program
│── README.md # Documentation
``` 

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/coffee-machine.git
   cd coffee-machine
   ```

2. Run the program:

python main.py

## 🧩 How It Works

MenuItem class: Defines a drink (name, ingredients, cost).
Menu class: Stores available drinks, retrieves names, and finds drinks by user input.
CoffeeMaker class: Keeps track of resources (water, milk, coffee) and checks if a drink can be made.
MoneyMachine class: Processes coins, verifies payment, and manages profits.
main.py: Runs the machine loop, taking user orders and coordinating all other classes.

## ✨ Example Gameplay

What would you like? (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickles?: 0
How many pennies?: 0
Here is $7.5 in change.
Here is your latte ☕️. Enjoy!!

What would you like? (espresso/latte/cappuccino): report
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5

## 🛠️ Features

Tracks machine resources (water, milk, coffee)
Accepts coins and calculates change
Checks if resources are sufficient before making a drink
Supports multiple drink types (latte, espresso, cappuccino)
Reports current resources and money earned
Loop-based system that keeps running until turned off

## 📌 Future Improvements

Save machine state to a file (so resources/money persist across runs)
Add new drinks to the menu dynamically
Handle invalid coin inputs gracefully
Extend to a GUI or web interface