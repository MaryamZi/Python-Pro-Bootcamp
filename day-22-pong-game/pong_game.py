import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

score_board = ScoreBoard()
ball = Ball()

r_paddle = Paddle((350, 0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle((-350, 0))
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True


while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    ycor = ball.ycor()
    if ycor > 280 or ycor < -280:
        ball.bounce_y()

    xcor = ball.xcor()
    if (ball.distance(r_paddle) < 50 and xcor > 320) or (ball.distance(l_paddle) < 50 and xcor < -320):
        ball.bounce_x()

    if xcor > 380:
        ball.reset_position()
        score_board.l_point()

    elif xcor < -380:
        ball.reset_position()
        score_board.r_point()


screen.exitonclick()