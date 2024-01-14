from snake import Snake
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game.')
screen.tracer(0)

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)

food.random_spawn()

while game_is_on:
    snake.move_snake()
    if snake.segments[0].distance(food) < 17:
        snake.increase_tail()
        scoreboard.update_score()
        food.random_spawn()
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280:
        game_is_on = False
        scoreboard.game_over()
    elif snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()
