from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.x = self.xcor()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update(0)

    def update(self, increment):
        self.clear()
        self.goto(self.x,280)
        self.score += increment
        self.write(f"Scoreboard: {self.score}", True, align="center")

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", True, align="center")