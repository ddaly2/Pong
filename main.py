from turtle import Screen
from dashed_line import DashedLine
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

line = DashedLine()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
has_bounced = False
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move(1, 1)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and (ball.xcor() > 310 or ball.xcor() < -310):
        ball.hit_paddle()







screen.exitonclick()