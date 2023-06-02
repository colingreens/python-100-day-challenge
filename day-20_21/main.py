import time
from food import Food
from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_is_on = True
score = 0
while game_is_on:
    screen.update()
    time.sleep(0.11)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score = score + 1
        snake.extend()
        scoreboard.update_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any segment in tail:
    # trigger game_over


screen.exitonclick()
