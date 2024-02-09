from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')
STARTING_SCORE = 0
SCORE_INCREMENT = 1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = STARTING_SCORE
        self.goto(-100, 200)
        self.right_score = STARTING_SCORE
        self.goto(100, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(f"{self.left_score}", font=FONT, align=ALIGNMENT)
        self.goto(100, 200)
        self.write(f"{self.right_score}", font=FONT, align=ALIGNMENT)

    def l_point(self):
        self.left_score += SCORE_INCREMENT
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.right_score += SCORE_INCREMENT
        self.clear()
        self.update_scoreboard()

