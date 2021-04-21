from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 230)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} vs {self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()