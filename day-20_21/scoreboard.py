from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 260)
        self.pendown()
        self.score = 0

    def write_score(self):
        self.write(
            f"Your Score: {self.score}", align="center", font=("Arial", 24, "normal")
        )

    def update_score(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 24, "normal"))
