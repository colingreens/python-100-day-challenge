# from turtle import Turtle, Screen

# tyler = Turtle()
# tyler.shape("turtle")
# tyler.color('green')
# tyler.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"


print(table)