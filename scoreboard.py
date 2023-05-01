from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.s = 0
        with open('highscore.txt') as f:
            self.highscore = int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(
            f"SCORE : {self.s} HIGHSCORE: {self.highscore}", False, ALIGNMENT, FONT)

    def reset_game(self):
        if self.s > self.highscore:
            with open('highscore.txt', 'w') as f:
                f.write(f"{self.s}")
                self.highscore = self.s
        self.s = 0
        self.write_score()

    def update(self):
        self.s += 1
        self.write_score()
