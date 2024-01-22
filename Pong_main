from turtle import Turtle, Screen
from paddle import Paddle
from board import Board
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

board = Board()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect the paddles
    if ball.distance(r_paddle) < 37 and ball.xcor() < 360 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball out of bounds
    # If L paddle misses:
    if ball.xcor() < -380:
        ball.refresh()
        score.r_point()


    # If R paddle misses:
    if ball.xcor() > 380:
        ball.refresh()
        score.l_point()


# 1. Create the screen x
# 2. Create and move a paddle x
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall an bounce
# 6. Detect collision with paddle
# 7. Keep Score

screen.exitonclick()
