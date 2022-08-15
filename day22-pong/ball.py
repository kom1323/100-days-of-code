from turtle import Turtle

BALL_START_POS = (0, 0)



class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(BALL_START_POS)
        self.x_move = 10
        self.y_move = 10

    

    def move(self) -> None:
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self) -> None:
        self.y_move *= -1

    def bounce_x(self) -> None:
        self.x_move *= -1.25
        

    def reset_position(self) -> None:
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.bounce_x()
