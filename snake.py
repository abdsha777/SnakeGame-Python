from turtle import Turtle, Screen
import time


class Snake():
    def __init__(self):
        self.t = []
        self.size = 3
        self.create_snake()
        self.head = self.t[0]
        self.change = True

    def reset(self):
        for i in self.t:
            i.hideturtle()
        self.t.clear()
        self.__init__()

    def create_snake(self):
        for i in range(self.size):
            self.t += [Turtle('square')]
            self.t[i].pu()
            self.t[i].color('white')
            self.t[i].goto(0+(i*-20), 0)

    def extend(self):
        self.t += [Turtle('square')]
        self.t[-1].pu()
        self.t[-1].color('white')
        self.t[-1].goto(self.t[-2].position())

    def move(self):
        for i in range(len(self.t)-1, 0, -1):
            self.t[i].goto(self.t[i-1].xcor(), self.t[i-1].ycor())
        self.t[0].forward(20)

    def up(self):
        if self.change:
            self.change = False
            if self.t[0].heading() != 270:
                self.t[0].setheading(90)

    def down(self):
        if self.change:
            self.change = False
            if self.t[0].heading() != 90:
                self.t[0].setheading(270)

    def left(self):
        if self.change:
            self.change = False
            if self.t[0].heading() != 0:
                self.t[0].setheading(180)

    def right(self):
        if self.change:
            self.change = False
            if self.t[0].heading() != 180:
                self.t[0].setheading(0)
