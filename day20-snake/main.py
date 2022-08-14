from turtle import Screen, window_width
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

GAME_BOUNDRY = 290

screen = Screen()   
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_is_on = True

while game_is_on:
    time.sleep(0.08)
    screen.update()


    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()


    #Detect collision with wall.
    if (snake.head.xcor() > GAME_BOUNDRY or snake.head.xcor() < -GAME_BOUNDRY 
        or snake.head.ycor() > GAME_BOUNDRY or snake.head.ycor() < -GAME_BOUNDRY):
        print(snake.head.pos())
        game_is_on = False
        score_board.game_over()


    #Detect collision with tail.
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()
    screen.update()

    snake.move()

screen.exitonclick()