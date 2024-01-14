from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen = Screen()
screen.setup(width=500, height=400)

for ci in range(len(colors)):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[ci])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=75-ci*30)
    turtles.append(new_turtle)

is_race_on = False
user_guess = screen.textinput(title="Take a guess", prompt=f"Which turtle will win the race {colors}?").lower()

if user_guess in colors:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 250:
            winner_color = turtle.pencolor()
            if winner_color == user_guess:
                print(f"Congratulations! '{user_guess}', and therefore you, won!")
            else:
                print(f"Try again! '{winner_color}' won.")
            is_race_on = False
            break
        turtle.forward(randint(0, 10))

screen.exitonclick()
