from re import S
import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = r".\day25-us_states_game\blank_states_img.gif"
screen.addshape(image)


turtle.shape(image)

data = pandas.read_csv(r".\day25-us_states_game\50_states.csv")

state_text_drawer = turtle.Turtle()
state_text_drawer.speed("fastest")
state_text_drawer.penup()
state_text_drawer.hideturtle()

states_counter = 0

game_is_on = True

while game_is_on:
    
    answer_state = screen.textinput(title=f"{states_counter}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()


    if answer_state is None:
        game_is_on = False
    elif states_counter == 50:
        game_is_on = False
    elif answer_state in data["state"].values:

        states_counter += 1
        turtle_x = data[data["state"] == answer_state]['x'].iloc[0]
        turtle_y = data[data["state"] == answer_state]['y'].iloc[0]
        data[data["state"] == answer_state].drop()
        state_text_drawer.setpos(x=turtle_x, y=turtle_y)
        state_text_drawer.write(answer_state, move=False, align="center", font=("Arial", 8, "normal"))





screen.exitonclick()