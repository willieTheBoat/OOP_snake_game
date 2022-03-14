from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Gold")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Times", 23, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Times", 23, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over :(", align=ALIGNMENT, font=("Times", 23, "normal"))