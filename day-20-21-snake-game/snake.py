from turtle import Turtle

UP_HEADING = 90
DOWN_HEADING = 270
LEFT_HEADING = 180
RIGHT_HEADING = 0

UP = "Up"
DOWN = "Down"
LEFT = "Left"
RIGHT = "Right"

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def move(self):
        for segment_index in range(len(self.snake_segments) - 1, 0, -1):
            preceding_segment = self.snake_segments[segment_index - 1]
            self.snake_segments[segment_index].goto(preceding_segment.xcor(), preceding_segment.ycor())

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_HEADING:
            self.head.setheading(UP_HEADING)
        self.move()

    def down(self):
        if self.head.heading() != UP_HEADING:
            self.head.setheading(DOWN_HEADING)
        self.move()

    def left(self):
        if self.head.heading() != RIGHT_HEADING:
            self.head.setheading(LEFT_HEADING)
        self.move()

    def right(self):
        if self.head.heading() != LEFT_HEADING:
            self.head.setheading(RIGHT_HEADING)
        self.move()

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.snake_segments.append(snake_segment)

    def extend(self):
        tail_position = self.snake_segments[-1].position()
        self.add_segment(tail_position)

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for x in [0, -20, -40]:
            self.add_segment((x, 0))

