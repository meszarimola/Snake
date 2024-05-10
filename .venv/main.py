import time
from turtle import (Screen, Turtle)
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")

game_is_on = True
while game_is_on:
	screen.update()
	time.sleep(0.1)
	snake.move_snake()

	if (snake.head.distance(food) < 15):
		food.refresh()
		scoreboard.increase_score()
		snake.extend()

	if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		game_is_on = False
		scoreboard.game_over()

	for segment in snake.segments[2::1]:
			if snake.head.distance(segment) < 10:
				game_is_on = False
				scoreboard.game_over()
screen.exitonclick()
