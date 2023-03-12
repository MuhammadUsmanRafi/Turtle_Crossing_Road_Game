import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# object of the classes
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
# action performed
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == player.finish:
        player.reset_turtle()
        scoreboard.next_level()
        car_manager.move_distance += 1

screen.exitonclick()