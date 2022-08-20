from tabnanny import check
from turtle import Turtle, Vec2D
from snake import Snake
import math


ENEMY_START = (-280, 0)





class Enemy(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("orange")
        self.penup()
        self.reset()

    def move(self, snake: Snake) -> None:
        self.setheading(self.towards(snake.head))
        self.forward(5)



    def reset(self) -> None:
        self.goto(ENEMY_START)
        