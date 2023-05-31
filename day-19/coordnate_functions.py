from turtle import Turtle, Screen

tyler = Turtle()
screen = Screen()


def move_forwards():
    tyler.forward(10)


def move_backwards():
    tyler.backward(10)


def move_left():
    tyler.left(30)


def move_right():
    tyler.right(30)


def reset():
    tyler.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)
screen.exitonclick()
