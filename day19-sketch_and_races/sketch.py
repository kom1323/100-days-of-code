from turtle import Turtle, Screen



def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def clear_screen():
    tim.reset()
    

tim = Turtle()
screen = Screen()
screen.listen()
screen.onkeypress(move_forward,"w")
screen.onkeypress(move_backward,"s")
screen.onkeypress(rotate_left,"a")
screen.onkeypress(rotate_right,"d")
screen.onkey(clear_screen, "c")




screen.exitonclick()