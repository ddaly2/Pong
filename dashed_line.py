from turtle import Turtle

NUM_DASHES = 36
SCREEN_HEIGHT = 275
class DashedLine:

    def __init__(self):
        self.line = Turtle()
        self.line.color("white")
        self.line.width(5)
        self.line.hideturtle()

    def draw_line(self):
        self.line.penup()
        self.line.setheading(270)
        self.line.goto(0, 275)
        for _ in range(SCREEN_HEIGHT, -SCREEN_HEIGHT, -20):
            self.line.pendown()
            self.line.forward(20)
            self.line.penup()
            self.line.forward(20)




