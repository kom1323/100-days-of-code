from turtle import Turtle
import random
GRID_CONSTANT = 20


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.sample(range(-280, 280, 20), 1)[0]
        random_y = random.sample(range(-280, 280, 20), 1)[0]
        self.goto(random_x, random_y)      