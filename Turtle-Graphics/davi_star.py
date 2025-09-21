""" Davi Star """ 

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.speed(10)
tim.pensize(1)

colours = [
    "medium slate blue",
    "turquoise",
    "dark orange",
    "deep pink",
    "lime green",
    "crimson",
    "sky blue",
    "orchid",
    "salmon"]

for a in range (0, 6):
    for i in range (3, 20):
        ang = 360 / i
        tim.color(random.choice(colours))
        for q in range (0, i):
            tim.left(ang)
            tim.forward(50)
    tim.right(60)
    tim.forward(50)

SCREEN = Screen()
SCREEN.exitonclick()
