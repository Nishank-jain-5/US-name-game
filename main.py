import turtle
import pandas as pd

count = 0
data = pd.read_csv("50_states.csv")
states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()


screen = turtle.Screen()
screen.title("U.S. state game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


game_is_on = True

gussed_state = []

while game_is_on:

    user = screen.textinput(title=f"{count}/50 States correct",prompt="Enter Name of the State of the US").title()

    if user == "Exit":
        missing_state = []
        for st in states:
            if st not in gussed_state:
                missing_state.append(st)
        
        # create csv file of missing state
        missing_state_dataframe = pd.DataFrame(missing_state)
        missing_state_dataframe.to_csv("missing_state.csv")
        break

    tur = turtle.Turtle()

    if user in states:

        if user not in gussed_state:
            count = count + 1

            if count>50:
                game_is_on = False

            Index = states.index(user)
            tur.penup()
            tur.goto(x[Index], y[Index])
            tur.write(f"{user}")
            tur.hideturtle()
            gussed_state.append(user)
