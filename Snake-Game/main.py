""" Snake Game """

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

SCREEN = Screen()
SCREEN.setup(width= 600, height= 600)
SCREEN.bgcolor("black")
SCREEN.title("My snake Game")
SCREEN.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
score.hideturtle()

SCREEN.listen()
SCREEN.onkey(key="Left", fun=snake.turn_left)
SCREEN.onkey(key="Right", fun=snake.turn_right)
SCREEN.onkey(key="Up", fun=snake.turn_up)
SCREEN.onkey(key="Down", fun=snake.turn_down)

GAME = True

while GAME:
    SCREEN.update()
    snake.moving()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        print(score.total)
        food.refresh()
        score.increase_score()
        snake.extend()


    # Detect collision with wall.

    if snake.head.xcor() >= 300 or \
        snake.head.xcor() <= -300 or \
        snake.head.ycor() >= 300 or \
        snake.head.ycor() <= -300:
        score.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

SCREEN.exitonclick()
