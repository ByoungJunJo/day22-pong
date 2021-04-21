from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong ")

# Turn off the animation
screen.tracer(0)

# Create paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create the ball and make it move
ball = Ball()

# Create the scoreboard
scoreboard = Scoreboard()

# Move the paddles using keyboard
screen.listen()
screen.onkey(fun=r_paddle.go_up, key='Up')
screen.onkey(fun=r_paddle.go_down, key='Down')
screen.onkey(fun=l_paddle.go_up, key='w')
screen.onkey(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with top & bottom walls (only y coordinates).
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # Detect when the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()
    # Detect when the left paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()






screen.exitonclick()