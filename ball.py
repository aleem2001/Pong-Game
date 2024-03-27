from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.goto(0,0)
        self.x_move = 10            #The distance the ball moves in the x-direction
        self.y_move = 10            #The distance the ball moves in the y-direction
        self.move_speed = 0.1       #The ball's speed
    
    #Making the ball move
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)
        
    #Bouncing the ball in the y-direction, i.e in case of collision with the top and bottom walls; Essentially reversing the direction of the ball in the y-axis
    def y_bounce(self):
        self.y_move *= -1
        
    #Bouncing the ball in the x-direction, i.e in case of collision with the paddles;Essentially reversing the direction of the ball in the x-axis
    def x_bounce(self):
        self.x_move *= -1
        #increasing the speed of the ball each time it touches a paddle
        self.move_speed *= 0.9
        
    #Reset the balls position
    def reset(self):
        self.goto(0,0)
        #Resetting the ball's speed to its initial value
        self.move_speed = 0.1