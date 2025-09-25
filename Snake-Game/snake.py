""" Snake Class"""

from turtle import Turtle
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake():
    """ Snake Class"""
    def __init__(self):
        super().__init__()
        self.segments = []
        self.start()
        self.head = self.segments[0]

    def start(self):
        """ Snake Start"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
    
    def add_segment(self, position):
        """ Add segment """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """ Extend Snake size"""
        self.add_segment(self.segments[-1].position())

    def moving(self):
        """ Snake Moving"""
        time.sleep(0.06)
        for i in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def turn_left(self):
        """ Snake Left"""
        if self.segments[0].heading() == 90:
            return self.segments[0].left(90)
        if self.segments[0].heading() == 270:
            return self.segments[0].right(90)


    def turn_right(self):
        """ Snake Right"""
        if self.segments[0].heading() == 90:
            return self.segments[0].right(90)
        if self.segments[0].heading() == 270:
            return self.segments[0].left(90)

    def turn_up(self):
        """ Snake up"""
        if self.segments[0].heading() == 0:
            return self.segments[0].left(90)
        if self.segments[0].heading() == 180:
            return self.segments[0].right(90)

    def turn_down(self):
        """ Snake down"""
        if self.segments[0].heading() == 0:
            return self.segments[0].right(90)
        if self.segments[0].heading() == 180:
            return self.segments[0].left(90)

    def reset(self):
        """ Reset Snake """
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.start()
        self.head = self.segments[0]
