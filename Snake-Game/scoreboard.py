""" Score Board """

from turtle import Turtle

ALIGMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """ Score Board """
    def __init__(self):
        super().__init__()
        self.high_score = 0
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

#    def game_over(self):
#        """ GAME OVER """
#        self.goto(0,0)
#        self.write('GAME OVER', \
#                    align = ALIGMENT, \
#                    font = FONT)

    def reset(self):
        self.high_score = max(self.high_score, self.total)
        self.total = 0
        self.refresh()

