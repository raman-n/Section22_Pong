from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.set_heading()
        self.turtle_speed = 0.005


    
    def set_heading(self):
        self.setheading(random.randint(0, 360))

    def move(self):
        self.forward(1)
    
    def deflect(self, angle:int):
        self.setheading(angle - self.heading())

