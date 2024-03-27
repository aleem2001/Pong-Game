from turtle import Turtle

#Creating the Paddle Class
class Paddle(Turtle):
    #Creating the Paddle and defining its properties
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        #position is a tuple of (x,y) coordinates for the paddle
        self.goto(position)

    #Moving the paddle up and down
    def go_up(self):
        #Ensuring the paddle does not go out of the screen from the top
        if self.ycor() > 240:
            pass
        else:
            new_y = self.ycor() + 20
            self.goto(self.xcor(),new_y)
        
    def go_down(self):
        #Ensuring the paddle does not go out of the screen from the bottom
        if self.ycor() < -230:
            pass
        else:
            new_y = self.ycor() - 20
            self.goto(self.xcor(),new_y)