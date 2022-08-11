from turtle import Turtle, Screen
from random import randint,choice
from colorgram import extract



colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), 
        (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168), 
        (35, 186, 109), (19, 29, 168), (13, 23, 66), (212, 135, 177),
        (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199), 
        (126, 189, 162), (8, 49, 28), (40, 132, 77), (128, 219, 232), 
        (58, 12, 25), (67, 22, 7), (114, 90, 210), (146, 216, 199), 
        (179, 17, 8), (233, 66, 34)]


tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.hideturtle()
tim.penup()
tim.speed("fastest")
print(tim.pos())
tim.setposition(-360, -300)
tim.down()


while True:
    tim.setposition(-360, -300)

    for _ in range(10):

        tim.setposition(-360, -300+70*_)
        for __ in range(11):
            
            curr_color = choice(colors)
            tim.fillcolor(curr_color)
            tim.pencolor(curr_color)

            tim.down()

            tim.begin_fill()
            tim.circle(10)
            tim.end_fill()

            tim.up()
            tim.forward(70)









screen.exitonclick()


