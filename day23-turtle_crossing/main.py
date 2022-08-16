import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.move, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)

    car_manager.generate_cars()

    car_manager.move()
    car_manager.delete_out_of_bounds()
    screen.update()

    #Detect collision with cars
    for car in car_manager.cars:
        if (player.distance(car) < 35 and player.ycor() < car.ycor() + 10 and player.ycor() > car.ycor() - 10
            or player.distance(car) < 25):
            player.reset_position()
            scoreboard.game_over()
            screen.exitonclick()


    if player.check_finish():
        player.reset_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    screen.update()

