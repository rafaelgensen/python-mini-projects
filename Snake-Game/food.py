""" Snake Foods """

from turtle import Turtle
import random

class Food(Turtle):
    """ Snake Foods """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        """ relocate food """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        return self.goto(random_x, random_y)
    