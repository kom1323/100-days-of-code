from turtle import Turtle

STARTING_P1_LOCATION = (350, 0)
STARTING_P2_LOCATION = (-360, 0)


class Paddle(Turtle):

    def __init__(self, player_num: str) -> None:
        super().__init__()
        self.create_paddle(player_num)
        


    def create_paddle(self, player_num: str) -> None:
        
        if player_num == "p1":
            pos = STARTING_P1_LOCATION
        else:
            pos = STARTING_P2_LOCATION


        
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(pos)
    

    def move_up(self):
        self.sety(self.ycor()  + 15)
        
        
    
    def move_down(self):
        self.sety(self.ycor() - 15)
        