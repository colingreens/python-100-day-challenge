from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(
    title="Make your bet.", prompt="Which turtle will win? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []

for x in range(0, len(colors)):
    temp_turtle = Turtle(shape="turtle")
    temp_turtle.color(colors[x])
    temp_turtle.penup()
    temp_turtle.goto(x=(-230), y=((250 / len(colors) * x) - (400 - 250) / 2))
    turtle_list.append(temp_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            print(turtle.pencolor())
            is_race_on = False
            if turtle.pencolor() == user_bet:
                print("congrats you won!")
            else:
                print("you lose!")

        turtle.forward(randint(0, 10))


screen.exitonclick()
