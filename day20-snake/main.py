from tkinter.messagebox import showwarning
from turtle import Screen, window_width
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from enemy import Enemy
import time


GAME_BOUNDRY = 290

screen = Screen()  



def start_game() -> None:
    screen.clearscreen()
    


    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score_board = ScoreBoard()
    enemy = Enemy()

    screen.listen()
    screen.onkey(snake.up ,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(start_game, "space")

    
    game_is_on = True

    while game_is_on:
        screen.update()
        snake.move()
        enemy.move(snake)
        time.sleep(0.08)
        screen.update()


        #Detect collision with food.git 
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score_board.increase_score()


        #Detect collision with wall.
        if (snake.head.xcor() > GAME_BOUNDRY or snake.head.xcor() < -GAME_BOUNDRY 
            or snake.head.ycor() > GAME_BOUNDRY or snake.head.ycor() < -GAME_BOUNDRY):
            score_board.reset()
            snake.reset()
            enemy.reset()


        #Detect collision with tai and enemy.
        for segment in snake.snake_body[1:]:
            if snake.head.distance(segment) < 10 or enemy.distance(segment) < 20:
                score_board.reset()
                snake.reset()
                enemy.reset()

        



start_game()



screen.exitonclick()
