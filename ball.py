from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_direction = 2
        self.y_direction = 2

    def move(self, x, y):
        new_x = self.xcor() + self.x_direction
        new_y = self.ycor() + self.y_direction
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_direction *= -1

    def x_redirect(self):
        self.x_direction *= -1

    def go_home(self):
        self.goto(0, 0)
        self.x_redirect()






