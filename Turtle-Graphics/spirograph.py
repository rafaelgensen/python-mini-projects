""" Spirograph """

from turtle import Turtle, Screen
import random
import turtle as t
import math

tim = Turtle()
tim.hideturtle()
tim.speed(0)
tim.pensize(0)
t.colormode(255)

def random_color():
    """ Random Colour """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


test = [3, 5]

for a, value in enumerate(test):
    ang = 180 - (360 / value)
    for q in range (0, value):
        tim.color('white')
        tim.right(ang)
        tim.circle(100, 180)
        for i in range (0, 18):
            tim.color(random_color())
            tim.circle(70)
            tim.left(20)

SCREEN = Screen()
SCREEN.exitonclick()
