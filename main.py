from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

score_board = Scoreboard()
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
    time.sleep(.009)
    ball.move(1, 1)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50) and (ball.xcor() > 330 or ball.xcor() < -330):
        ball.x_redirect()

    if ball.xcor() > 400:
        score_board.l_point()
        ball.go_home()

    if ball.xcor() < -400:
        score_board.r_point()
        ball.go_home()







screen.exitonclick()