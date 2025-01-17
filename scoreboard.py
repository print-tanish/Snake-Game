from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}","center",("Arial",24,"normal"))
        self.hideturtle()
    
       

    def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER","center",("Arial",24,"normal"))
    
    def score_increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}","center",("Arial",24,"normal"))