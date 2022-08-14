from turtle import Turtle

ALIGHMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.write(f"Score: {self.score}", align=ALIGHMENT, font=FONT)


    def game_over(self) -> None:
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGHMENT, font=FONT)


    def increase_score(self) -> None:
        self.clear()
        self.score += 1
        self.update_scoreboard()



    
