
from turtle import Turtle
start_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
up=90
down=270
right=0
left=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    
    def create_snake(self):
        for position in start_position:
            new_segment=Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)
  
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
           self.segments[seg_num].goto(self.segments[seg_num-1].xcor(),self.segments[seg_num-1].ycor())
       
        self.segments[0].forward(move_distance)
    def up(self):
        if self.segments[0].heading()!=down:
         self.segments[0].setheading(90)
    def down(self):
        if self.segments[0].heading()!=up:
         self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading()!=left:
         self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading()!=right:
         self.segments[0].setheading(180)
          


        


