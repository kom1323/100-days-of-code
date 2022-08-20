from turtle import Turtle
MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self) -> None:
        self.snake_body = []
        self.create_snake()
        self.head: Turtle
       

        
    def reset(self) -> None:

        for seg in self.snake_body:
            seg.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()


    def create_snake(self) -> None:
        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.snake_body[0]

    
    def add_segment(self,position) -> None:
        tim = Turtle(shape="square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.snake_body.append(tim)


    def extend(self) -> None:
        #add a new segment to the snake.
        self.add_segment(self.snake_body[-1].position())

    def move(self) -> None:
        body_len = len(self.snake_body)
        for body_num in range(body_len - 1, 0, -1):
            new_x = self.snake_body[body_num - 1].xcor()
            new_y = self.snake_body[body_num - 1].ycor()
            self.snake_body[body_num].goto(new_x, new_y)
        
        self.head.forward(MOVE_DISTANCE)


    def up(self) -> None:
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)
        
    def down(self) -> None:
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)
        
    def left(self) -> None:
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
        

    def right(self) -> None:
        if self.head.heading() != WEST:
            self.head.setheading(EAST)
        