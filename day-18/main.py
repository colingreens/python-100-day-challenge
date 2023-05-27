from turtle import Turtle, Screen
from random import choice

screen = Screen()
screen.colormode(255)
tyler = Turtle()
tyler.color("green")
tyler.shape("turtle")

color_list = [(238, 236, 234), (230, 226, 228), (34, 108, 167), (223, 229, 235), (227, 233, 230), (245, 77, 36), (112, 163, 211), (153, 57, 85), (219, 156, 94), (201, 60, 27), (24, 133, 55), (246, 204, 84), (190, 151, 47), (225, 119, 152), (46, 53, 121), (221, 68, 97), (113, 199, 156), (147, 37, 30), (253, 202, 0), (91, 113, 192), (74, 40, 32), (248, 153, 143), (111, 41, 49), (155, 212, 203), (53, 174, 163), (38, 31, 67), (154, 210, 219), (43, 33, 45), (35, 55, 46), (99, 93, 2)]

def start_turtle(x,y):
    for i in range(10):
        for j in range(10):
            tyler.speed(0)
            tyler.pendown()
            tyler.dot(20,choice(color_list))
            tyler.penup()
            tyler.setpos(i * 50, j * 50)

tyler.onclick(start_turtle)
screen.mainloop()