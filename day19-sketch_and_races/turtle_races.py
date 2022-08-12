from calendar import c
from turtle import Turtle, Screen
from random import choice,randint


is_race_on = False
screen = Screen()
screen.setup(width = 500,height = 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]





def create_turtles(timmies):

    for tim in range(6):
        trtl = Turtle(shape="turtle")
        trtl.penup()
        trtl.color(colors[tim])
        trtl.goto(x= -230, y = -50 + 30*tim)
        timmies.append(trtl)

def game_loop():

    user_bet = screen.textinput(title = "Make your bet", prompt = f"which turtle will win the race? Enter a color from the list\n {colors}: ")

    timmies = []
    create_turtles(timmies)

    if user_bet:
        is_race_on = True


    while is_race_on:

        for turtle in timmies:
            random_distance = randint(0, 50)
            turtle.forward(random_distance)

            if turtle.xcor() > 230:
                winning_color = turtle.pencolor() 
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")       
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")   

                again = screen.textinput(title= f"The {winning_color} turtle is the winner!", prompt= "Do you want to go again? ('yes/'no'):")

                if again == 'yes':
                    screen.clearscreen()
                    game_loop()
                else:
                    screen.bye()
                    return

                    
            

game_loop()



