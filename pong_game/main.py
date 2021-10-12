## Class of pong and create 2 pongs; 
# Class of Score to create 2 scores, 
# Line in hte middle; 
# ball can be its own class (turtle)

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.tracer(0)

paddle_right = Paddle("right")
paddle_left = Paddle("left")


score_right = Scoreboard(position="right")
score_left = Scoreboard(position="left")

for _ in range (11):
    ball = Ball()
    play_on = True

    while play_on:
        screen.listen()
        time.sleep(ball.turtle_speed)
        
        screen.onkeypress(paddle_right.move_paddle_up, "Up")
        screen.onkeypress(paddle_right.move_paddle_down, "Down")
        screen.onkeypress(paddle_left.move_paddle_up, "w")
        screen.onkeypress(paddle_left.move_paddle_down, "s")
        
        ball.move()

        if (
            ball.ycor() > 280 or 
            ball.ycor() < -280       
            ):             
            
            ball.deflect(angle = 360)

        if ((
            ball.ycor() > paddle_right.paddle_position_bottom() and 
            ball.ycor() < paddle_right.paddle_position_top() and 
            ball.xcor() > 370) or

            ball.ycor() > paddle_left.paddle_position_bottom() and 
            ball.ycor() < paddle_left.paddle_position_top() and 
            ball.xcor() < -370):

            ball.deflect(angle = 180)

        if ball.xcor() < -400:
            score_right.win()
            play_on = False
            ball.hideturtle()
               
        if ball.xcor() > +400:
            score_left.win()
            play_on = False
            ball.hideturtle()


        screen.update()

screen.exitonclick()
