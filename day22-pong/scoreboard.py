from turtle import Turtle

FONT = ("Courier", 45, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()


    def update_scoreboard(self) -> None:
        self.clear()
        self.goto(100, 225)
        self.write(self.p1_score, align=ALIGNMENT, font=FONT)   
        self.goto(-100, 225)
        self.write(self.p2_score, align=ALIGNMENT, font=FONT)   


    def p1_point(self) -> None:
        self.p1_score += 1
        self.update_scoreboard()

    
    def p2_point(self) -> None:
        self.p2_score += 1
        self.update_scoreboard()
