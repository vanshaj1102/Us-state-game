import turtle
import pandas

screen = turtle.Screen()
screen.title("US States game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50 :
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 type a state " ,
                                    prompt= "guess the next state").title()

    if answer_state.upper() == "EXIT":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item() , state_data.y.item())
        t.write(answer_state)