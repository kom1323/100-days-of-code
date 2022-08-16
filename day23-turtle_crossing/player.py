from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.move_speed = MOVE_DISTANCE
        self.reset_position()
        

    def reset_position(self) -> None:
        self.goto(STARTING_POSITION)

    def check_finish(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            self.move_speed += MOVE_INCREMENT
            return True
        return False

    def move(self) -> None:
        self.forward(self.move_speed)
