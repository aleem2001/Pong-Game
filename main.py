from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Constants
RIGHT_PADDLE_POSITION = (350,0)
LEFT_PADDLE_POSITION = (-350,0)

#Creating the Screen and defining its properties
screen = Screen ()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")

#Turning off animation refresh
screen.tracer(0)

#Creating the Right and Left Paddle
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
left_paddle = Paddle(LEFT_PADDLE_POSITION)

#Listening to key strokes to move both the paddles up and down
screen.listen()

#Keystrokes to move the right paddle
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

#Keystrokes to move the left paddle
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

#Creating the ball
ball = Ball()

#Creating the scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    #Refreshing graphics
    screen.update()
    #Managing the speed of the ball
    time.sleep(ball.move_speed)
    #Moving the ball
    ball.move()
    
    #Detecting the ball's collision with the top and bottom of the screen and making it bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()         #Essentially reversing the direction of the ball in the y-axis
        
    #Detecting the ball's collision with the Paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()         #Essentially reversing the direction of the ball in the x-axis
        
    #Detecting if the paddle misses the ball and the ball goes out of the screen, if so then restarting the game with the ball in the center moving towards the other player  
    #Detect if the Right Paddle misses and adding score to the Left side
    if ball.xcor() > 380:
        ball.reset()
        ball.x_bounce()
        scoreboard.left_scores_point()
        
    #Detect if the Left Paddle misses and adding score to the Right side
    if ball.xcor() < -380:
        ball.reset()
        ball.x_bounce()
        scoreboard.right_scores_point()
        

#Does not allow the screen to vanish until it is clicked
screen.exitonclick()
