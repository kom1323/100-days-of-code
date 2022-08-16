from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        self.cars : list[Turtle] = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.generate_speed = 3



    def create_car(self) -> None:

        tim = Turtle()
        tim.penup()
        tim.shape("square")
        tim.color(random.choice(COLORS))
        tim.shapesize(stretch_wid=1, stretch_len=2)
        tim.setheading(180)
        tim.goto(300, random.randint(-250, 250))
        self.cars.append(tim)


    def generate_cars(self) -> None:

        random_num = random.randint(0,10)
        if random_num < self.generate_speed:
            for i in range(random_num):
                self.create_car()

    def move(self) -> None:

        for car in self.cars:
            car.forward(self.move_speed)
        
    def increase_speed(self) -> None:

        self.move_speed += MOVE_INCREMENT
        self.generate_speed += 1

    def delete_out_of_bounds(self) -> None:

        for car in self.cars:
            if car.xcor() < -330:
                self.cars.remove(car)
