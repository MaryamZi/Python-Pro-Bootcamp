# # Turtle - 1
# from turtle import Turtle, Screen
#
# tim = Turtle()
#
# tim.shape("turtle")
# tim.color("green")
#
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# screen = Screen()
# screen.exitonclick()

# # Turtle 2
# from turtle import Turtle, Screen
# from random import randint
#
# tim = Turtle()
#
# tim.shape("turtle")
# tim.color("green")
#
# screen = Screen()
# screen.colormode(255)
#
# for i in range(3, 11):
#     tim.pencolor((randint(1, 255), randint(1, 255), randint(1, 255)))
#     angle = 360/i
#
#     for _ in range(i):
#         tim.forward(50)
#         tim.right(angle)
#
# screen.exitonclick()

# # Turtle - 3
# from turtle import Turtle, Screen
# from random import randint
#
# tim = Turtle()
#
# tim.shape("turtle")
# tim.color("green")
# tim.speed(6)
# tim.pensize(10)
#
# screen = Screen()
# screen.colormode(255)
#
# for i in range(500):
#     tim.pencolor((randint(1, 255), randint(1, 255), randint(1, 255)))
#     tim.forward(20)
#     tim.setheading(90 * randint(0, 3))
#
# screen.exitonclick()

# # Turtle - 4
# from turtle import Turtle, Screen
# from random import randint
#
# tim = Turtle()
#
# tim.shape("turtle")
# tim.color("green")
# tim.speed(0)
#
# screen = Screen()
# screen.colormode(255)
#
# for i in range(0, 360, 10):
#     tim.setheading(i)
#     tim.pencolor((randint(1, 255), randint(1, 255), randint(1, 255)))
#     tim.circle(120)
#
# screen.exitonclick()
