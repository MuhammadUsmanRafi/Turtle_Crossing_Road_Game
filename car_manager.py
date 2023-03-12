from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(0, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = random.randint(-240, 240)
            new_car.setposition(300, random_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.move_distance)

