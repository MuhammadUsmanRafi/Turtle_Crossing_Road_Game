from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.score()

    def score(self):
        self.goto(-290, 260)
        self.write(f"level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
