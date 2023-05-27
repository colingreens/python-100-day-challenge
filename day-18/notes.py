from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)

tyler = Turtle()
tyler.color("green")
tyler.shape("turtle")

# for _ in range(50):
#     tyler.pendown()
#     tyler.forward(10)
#     tyler.penup()
#     tyler.forward(10)

def start_turtle(x,y):
    # for i in range(3,10):
    #     tyler.pencolor((randint(1,255),randint(1,255),randint(1,255)))
    #     for _ in range(i):
    #         tyler.forward(100)
    #         tyler.right(360/i)
    # for _ in range (200):
    #     tyler.pencolor((randint(1,255),randint(1,255),randint(1,255)))
    #     tyler.pensize(10)
    #     tyler.forward(25)
    #     tyler.speed(0)
    #     tyler.setheading(90 * randint(0,3))
    for i in range (0,360,5):
        tyler.pencolor((randint(1,255),randint(1,255),randint(1,255)))
        tyler.speed(0)
        tyler.circle(100)
        tyler.setheading(i)
        

tyler.onclick(start_turtle)
# screen.exitonclick()

screen.mainloop()