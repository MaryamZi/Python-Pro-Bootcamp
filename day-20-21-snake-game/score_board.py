from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT_CENTER = "center"


class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        with open("./high_score.txt") as file:
            self.high_score = int(file.read())
        self.color("White")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT_CENTER, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./high_score.txt", mode='w') as file:
                file.write(self.high_score.__str__())
        self.score = 0
        self.update_scoreboard()
