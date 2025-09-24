""" Main module pong game """

from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

SCREEN = Screen()
SCREEN.bgcolor("black")
SCREEN.setup(width=800, height=600)
SCREEN.title("Pong")
SCREEN.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

SCREEN.update()

SCREEN.listen()
SCREEN.onkey(paddle_r.go_up, "Up")
SCREEN.onkey(paddle_r.go_down, "Down")
SCREEN.onkey(paddle_l.go_up, "W")
SCREEN.onkey(paddle_l.go_down, "S")

game_on = True
speed = 0.08

while game_on:
    SCREEN.update()
    time.sleep(speed)
    ball.move()

    # Detect collision with wall
    if ball.xcor() >= 380:
        print("ponto do time esquerdo")
        score.l_point()
        ball.reset_position()
        speed = 0.08
    if ball.xcor() <= -380:
        print("ponto do time direito")
        score.r_point()
        ball.reset_position()
        speed = 0.08
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()
    # Detect collision with paddle_r
    if ball.distance(paddle_r) < 60 and ball.xcor() > 320 or \
        ball.distance(paddle_l) < 60 and ball.xcor() < -320 :
        ball.bounce_x()
        speed *= 0.8

    if max(score.l_score, score.r_score) >= 3:
        score.game_over()
        break

SCREEN.exitonclick()
