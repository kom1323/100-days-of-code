from turtle import Turtle

ALIGHMENT = "center"
FONT = ('Courier', 16, 'normal')


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open(r"C:\Users\Omer\OneDrive\Desktop\All Projects\python projects\100-days-of-code\day20-snake\data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGHMENT, font=FONT)


    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            with open(r"C:\Users\Omer\OneDrive\Desktop\All Projects\python projects\100-days-of-code\day20-snake\data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self) -> None:
        self.score += 1
        self.update_scoreboard()



    
