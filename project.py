import random
import turtle
from turtle import Screen,Turtle
from paddle import paddle
from scoreboard import Scoreboard
from ball import Ball
import time
#screen
list=["pico2.gif","pico3.gif"]
screen=Screen()
screen.bgpic(random.choice(list))
screen.setup(width=800,height=600)
screen.title("strike")
screen.tracer(0)

r_paddle=paddle((350,0))
l_paddle=paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

turtle.listen()
turtle.onkey(r_paddle.go_up,"Up")
turtle.onkey(r_paddle.go_down,"Down")

turtle.onkey(l_paddle.go_up,"w")
turtle.onkey(l_paddle.go_down,"s")

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#mooving ball
    if ball.ycor()>275 or ball.ycor()<-275:
        ball.bounce_y()
    #collision
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    elif ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
