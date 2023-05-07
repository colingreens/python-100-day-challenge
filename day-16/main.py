from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine =  MoneyMachine()

isOn = True

while isOn == True:
    selection = input(f"What would you like {menu.get_items()}").lower()

    if selection == "off":
        isOn = False
        continue

    if selection == "report":
        coffeeMaker.report()
        moneyMachine.report()
        continue

    order = menu.find_drink(selection)

    if order != None:
        if coffeeMaker.is_resource_sufficient(order):
            if moneyMachine.make_payment(order.cost):
                coffeeMaker.make_coffee(order)


    

    

