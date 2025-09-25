""" Score Board """

from turtle import Turtle
import os

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """ Score Board """
    def __init__(self):
        super().__init__()
        with open(os.path.join(os.path.dirname(__file__), "data.txt"), encoding="utf-8") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.total = 0
        self.refresh()

    def refresh(self):
        """ Score Board Refresh """ 
        self.clear()
        self.write(f'Score: {self.total} High Score: {self.high_score}', \
                         align = ALIGMENT, \
                         font = FONT)

    def increase_score(self):
        """ Increase Score """
        self.total += 1
        self.refresh()

    def reset(self):
        self.high_score = max(self.high_score, self.total)
        with open(os.path.join(os.path.dirname(__file__), "data.txt"), \
                  mode = "w", encoding="utf-8") as file:
            file.write(f"{self.high_score}")
        self.total = 0
        self.refresh()
