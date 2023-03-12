from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.finish = FINISH_LINE_Y

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.setposition(STARTING_POSITION)
