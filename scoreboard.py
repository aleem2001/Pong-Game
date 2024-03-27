from turtle import Turtle

#Constants
FONT = ("Courier",70,"normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        #Calling update_scoreboard() to print it
        self.update_scoreboard()
        
    def update_scoreboard(self):
        #Clearing the score before updating
        self.clear()
        #Writing the Left side score
        self.goto(-100, 200)
        self.write(self.left_score, align='center', font=FONT)
        
        #Writing the Right side score
        self.goto(100, 200)
        self.write(self.right_score, align='center', font=FONT)
        
    #Updating Left sides score
    def left_scores_point(self):
        self.left_score += 1
        #Calling update_scoreboard() to print updated scoreboard
        self.update_scoreboard()
        
    #Updating Right sides score    
    def right_scores_point(self):
        self.right_score += 1
        #Calling update_scoreboard() to print updated scoreboard
        self.update_scoreboard()