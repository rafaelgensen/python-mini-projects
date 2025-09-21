""" Random Walk  """

from turtle import Turtle, Screen
import random
import turtle as t

tim = Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.speed(0)
tim.pensize(5)
t.colormode(255)

def random_color():
    """ Random Colour """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]

for i in range (0, 400):
    tim.color(random_color())
    tim.setheading(random.choice(directions))
    tim.forward(random.choice([10, 20, 30]))


SCREEN = Screen()
SCREEN.exitonclick()
