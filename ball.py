from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.x_direction = 10
        self.y_direction = 10

    def move(self, x, y):
        new_x = self.xcor() + x * self.x_direction
        new_y = self.ycor() + y * self.y_direction
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_direction *= -1

    def hit_paddle(self):
        self.x_direction *= -1






