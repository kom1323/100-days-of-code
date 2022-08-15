from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


p1_paddle = Paddle("p1")
p2_paddle = Paddle("p2")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(p1_paddle.move_up, "Up")
screen.onkeypress(p1_paddle.move_down, "Down")
screen.onkeypress(p2_paddle.move_up, "w")
screen.onkeypress(p2_paddle.move_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    #Ball bounce off walls
    if ball.ycor() < -270 or ball.ycor() > 280:
        ball.bounce_y()


    #Detect collision with r_paddle
    if (ball.distance(p1_paddle) < 50 and ball.xcor() > 320
        or ball.distance(p2_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    #Detect out of bounds on the right
    if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.p2_point()

    #Detect out of bounds on the left
    if ball.xcor() < -390:
            ball.reset_position()
            scoreboard.p1_point()





screen.exitonclick()