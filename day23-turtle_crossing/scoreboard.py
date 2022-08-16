from turtle import Turtle
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self) -> None:

        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230, 260)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"level: {self.level}", align= "center", font=FONT)
        

    def game_over(self) -> None:
        self.goto(0, 100)
        self.write("Game Over", align= "center", font=FONT)

    def increase_level(self) -> None:
        self.level += 1
        self.update_scoreboard()

