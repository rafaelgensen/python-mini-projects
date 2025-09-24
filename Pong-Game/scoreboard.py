""" Score Board """

from turtle import Turtle

class ScoreBoard(Turtle):
    """ Score Board """
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Update Scoreboard """
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def l_point(self):
        """ Point Left """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """ Point Right """
        self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        """ Game Over """
        self.clear()
        self.goto(0,0)
        if self.r_score > self.l_score:
            self.write("Right is the winner!", \
                       align="center", font=("Courier", 30, "normal"))
        else:
            self.write("Left is the winner!", \
                       align="center", font=("Courier", 30, "normal"))
