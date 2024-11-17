from turtle import Screen
from snake import Snake
import time 
from food import Food
from scoreboard import Scoreboard
screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
   screen.update()
   time.sleep(0.1)

   snake.move()

   if snake.segments[0].distance(food)<10:
      food.refresh()
      snake.extend()
      scoreboard.score_increase()
   if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()<-280 or snake.segments[0].ycor()>280:
      game_is_on=False
      scoreboard.game_over()
   for segment in snake.segments:
      if segment==snake.segments[0]:
         pass
      
      if snake.segments[0].distance(segment)<10:
         game_is_on=False
         scoreboard.game_over()
 

 
   