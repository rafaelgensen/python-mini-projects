""" Etch-A-Sketch """

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.speed(10)
tim.pensize(2)
tim.color('green')
SCREEN = Screen()

def move_forwards():
    """ Move Forwards """
    tim.forward(10)

def rotate_left():
    """" Rotate Left"""
    tim.left(10)

def rotate_right():
    """" Rotate Left"""
    tim.right(10)

def move_backwards():
    """ Move Backwards """
    tim.backward(10)

def clear():
    """ Clear """
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

SCREEN.listen()
SCREEN.onkey(key="W", fun=move_forwards)
SCREEN.onkey(key="A", fun=rotate_left)
SCREEN.onkey(key="D", fun=rotate_right)
SCREEN.onkey(key="S", fun=move_backwards)
SCREEN.onkey(key="space", fun=clear)
SCREEN.exitonclick()
