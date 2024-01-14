from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.4, stretch_len=0.4)
        self.coordinates = 0
        self.penup()

    def random_spawn(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.coordinates = (x, y)
        self.goto(x=x, y=y)
