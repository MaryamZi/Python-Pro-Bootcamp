import pandas
import turtle

screen = turtle.Screen()
screen.title("The States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("./50_states.csv")

state_names = data.state.to_list()
state_count = len(state_names)

guessed_states = []

while len(guessed_states) < state_count:
    # answer = input(f"{len(guessed_states)}/{state_count} Guess the state").title()
    answer = screen.textinput(title=f"{len(guessed_states)}/{state_count} Guess the state", prompt="Guess:").title()

    if answer == "Exit":
        states_to_learn = []

        for state in state_names:
            if state not in guessed_states:
                states_to_learn.append(state)

        data_frame = pandas.DataFrame(states_to_learn)
        data_frame.to_csv("./states_to_learn.csv")
        break

    if answer in state_names:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row = data[data.state == answer]
        t.goto(int(row.x), int(row.y))
        t.write(row.state.state())
        guessed_states.append(answer)

screen.exitonclick()