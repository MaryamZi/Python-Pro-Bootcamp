import time
from turtle import Screen
from food import Food
from snake import Snake
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

head = snake.snake_segments[0]

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if head.distance(food) < 20:
        snake.extend()
        score_board.increase_score()
        food.generate_at_new_location()

    x = head.xcor()
    y = head.ycor()
    if x > 280 or x < -280 or y > 280 or y < -280:
        score_board.reset()
        snake.reset()
        head = snake.snake_segments[0]
        continue

    for segment in snake.snake_segments[1:]:
        if head.distance(segment) < 5:
            score_board.reset()
            snake.reset()
            head = snake.snake_segments[0]
            continue

screen.exitonclick()
