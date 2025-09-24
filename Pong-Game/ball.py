""" Paddle Ball """

from turtle import Turtle

class Ball(Turtle):
    """ Init Ball """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10


    def move(self):
        """ Move Ball """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Bounce """
        self.y_move *= -1

    def bounce_x(self):
        """ Bounce """
        self.x_move *= -1
    
    def reset_position (self):
        """ reset position """    
        self.goto(0,0)
        self.bounce_x()