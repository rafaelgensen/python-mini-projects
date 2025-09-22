""" Score Board """

from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """ Score Board """
    def __init__(self):
        super().__init__()
        self.score = Turtle()
        self.score.hideturtle()
        self.score.penup()
        self.score.color('white')
        self.score.goto(0, 260)
        self.total = 0
        self.refresh()

    def refresh(self):
        """ Score Board Refresh """ 
        self.total += 1
        self.score.clear()
        self.score.write(f'Score: {self.total - 1}', \
                         align = ALIGMENT, \
                         font = FONT)

    def game_over(self):
        """ GAME OVER """
        self.score.goto(0,0)
        self.score.write(f'GAME OVER', \
                    align = ALIGMENT, \
                    font = FONT)
        