from turtle import Screen
from Padle import Padle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()
r_padle = Padle(350,0)
l_padle = Padle(-350,0)

screen.listen()
screen.onkey(r_padle.up, "Up")
screen.onkey(r_padle.down, "Down")
screen.onkey(l_padle.up, "w")
screen.onkey(l_padle.down, "s")

if scoreboard.user_bet:
    scoreboard.user_bet = int(scoreboard.user_bet)
    scoreboard.write_meta()
    game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce_y()
    #Detect collision with r_paddle
    if ball.distance(r_padle) < r_padle.size and ball.xcor() > 330 and ball.xcor() < 350:
        ball.bounce_x()
    #Detect collision with l_paddle
    if ball.distance(l_padle) < l_padle.size and ball.xcor() < -330 and ball.xcor() > -350:
        ball.bounce_x()
    #Detect R padle misses
    if ball.xcor() > 380:
        ball.out_of_bounds()
        scoreboard.increase_l()
        l_padle.decrease_size(scoreboard.user_bet)
        scoreboard.write_score()
        scoreboard.write_meta()
    #Detect L padle misses
    if ball.xcor() < -380:
        ball.out_of_bounds()
        scoreboard.increase_r()
        r_padle.decrease_size(scoreboard.user_bet)
        scoreboard.write_score()
        scoreboard.write_meta()
    #Detect if someone won
    if scoreboard.l_score == scoreboard.user_bet:
        scoreboard.goto(0,0)
        scoreboard.write("Left Player Won", align="center", font=("Courier", 40, "normal"))
        game_on = False
    if scoreboard.r_score == scoreboard.user_bet:
        scoreboard.goto(0,0)
        scoreboard.write("Right Player Won", align="center", font=("Courier", 40, "normal"))
        game_on = False        
screen.exitonclick()