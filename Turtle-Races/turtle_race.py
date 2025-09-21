""" Turtle Races!!! """

from turtle import Turtle, Screen
import random

IS_RACE_ON = False
SCREEN = Screen()
SCREEN.setup(width=500, height=400)
SCREEN.tracer(0)
user_bet = SCREEN.textinput(title="Make your bet", \
                            prompt="Which turtle will win the race? Enter a color: ")

colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
turtles = []
positions = [-125, -75, -25, 25, 75, 125]

t = Turtle()
t.hideturtle()
t.penup()
t.goto(200, 180)
t.right(90)
t.speed(0)

SCREEN.update()
SCREEN.tracer(1)

for i, value in enumerate(colors):
    turtles.append(Turtle(shape = "turtle"))
    turtles[i].color(value)
    turtles[i].penup()
    turtles[i].goto(-180, positions[i])

for i in range(0, 18):
    t.hideturtle()
    t.pendown()
    t.hideturtle()
    t.pensize(4)
    t.color('black')
    t.forward(10)
    t.color('white')
    t.forward(10)


if user_bet:
    IS_RACE_ON = True

while IS_RACE_ON:
    for i, value in enumerate(turtles):
        if value.xcor() > 185:
            if user_bet == value.pencolor():
                t.goto(-185, 50)
                t.color('black')
                t.write("Nice! You Won!", align="left", font=("Helvetica", 30, "normal"))
            IS_RACE_ON = False
            t.goto(-185, 50)
            t.color('black')
            t.write("Too bad... You lost!!", align="left", font=("Helvetica", 30, "normal"))
            t.penup()
            t.goto(-160, 0)
            t.pendown()
            t.write(f"The winner: {value.pencolor()}", align="left", font=("Helvetica", 30, "normal"))
            break
        rand_distance = random.randint(0, 10)
        value.forward(rand_distance)

SCREEN.exitonclick()
