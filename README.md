# day22-pong
## Problem 
Create a Pong game using Python library, [Turtle](https://docs.python.org/3/library/turtle.html).
## Solutions
1. Create the screen
```
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong ")
```
2. Create and move the paddle
```
# First let's create the right paddle
r_paddle = Paddle((350, 0))

# Make a class in a seperate file: paddle.py

from turtle import Turtle
STEPS = 20

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + STEPS
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - STEPS
        self.goto(self.xcor(), new_y)
```
3. Create another paddle
```
l_paddle = Paddle((-350, 0))
```
Thanks to the class I created above, I don't need to create another long lines of code.

4. Create the ball & make it move
```
# In main.py
ball = Ball()

# Make a class, Ball

from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

```
5. Detect collision with wall and bounce 
```
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with top & bottom walls (only y coordinates).
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()
```
6. Detect collision with paddle (`ball.distance(paddle)`)
```
if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
    ball.bounce_x()
```
7. Detect when paddle missles
```
# Detect when the right paddle misses
if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.increase_left_score()
# Detect when the left paddle misses
elif ball.xcor() < -380:
    ball.reset_position()
    scoreboard.increase_right_score()
```
8. Keep score
```
# Create a class, Scoreboard

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 230)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} vs {self.r_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.clear()
        self.l_score += 1
        self.update_scoreboard()

    def increase_right_score(self):
        self.clear()
        self.r_score += 1
        self.update_scoreboard()
```
## 3 Key Lessons:
1. Break down the problem
2. Get stuck? Define the problem
3. Make re-usuable codes (day 21's code helped me a lot to complete the day 22 project with minimum guidance from Angela)
