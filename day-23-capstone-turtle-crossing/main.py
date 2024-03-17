import random
import time
from turtle import Screen
from car_manager import CarManager
from player import Player, FINISH_LINE_Y
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:
        car_manager.create_new_car()

    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_on = False
            score_board.end_game()

    if player.ycor() > FINISH_LINE_Y:
        player.go_to_start()
        car_manager.increase_car_speed()
        score_board.level_up()

screen.exitonclick()
