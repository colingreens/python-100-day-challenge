#requirements
#1. Print Report of Current water,coffee,milk, money
#2. Check if resources are sufficient
#3. Process Coins
#4 Check transaction successfull
#4 Make Coffee! 

MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

coffe_order = {
    "water":0,
    "milk":0,
    "coffee":0
}

def can_make_coffee(selection):
    coffee = MENU[selection]["ingredients"]
    waterNeeded = coffee["water"]
    milkNeeded = coffee.get("milk", 0) 
    coffeeNeeded = coffee["coffee"]

    coffe_order["water"] = waterNeeded
    coffe_order["milk"] = milkNeeded
    coffe_order["coffee"] = coffeeNeeded

    currentWater = resources["water"]
    currentMilk = resources["milk"]
    currentCoffee = resources["coffee"]

    if waterNeeded > currentWater:
        print("Sorry not enough water in machine")
        return False
    elif milkNeeded > currentMilk:
        print("Sorry not enough milk in machine")
        return False
    elif coffeeNeeded > currentCoffee:
        print("Sorry not enough coffee in machine")
        return False
    else:        
        return True

def can_process_money(selection):
    quarters = int(input("How many quarters did you put in?"))
    dollar_amount = round(quarters * 25 / 100,2)
    amount_needed = MENU[selection]["cost"]

    change_back = dollar_amount - amount_needed

    if change_back < 0:
        print("Sorry put in more money next time")
        return False
    
    if change_back > 0:
        print(f"Here's your change of {change_back}")
    
    resources["money"] += dollar_amount 


def make_coffee(selection):
    print(f"Enjoy your {selection}")
    resources["water"] -= coffe_order["water"]
    resources["milk"] -= coffe_order["milk"]
    resources["coffee"] -= coffe_order["coffee"]

isOn = True

while isOn == True:
    selection = input("What would you like? espresso/latte/cappuccino\n").lower()

    if selection == "off":
        isOn = False
        continue

    if selection == "report":
        print(resources)
        continue

    if MENU.get(selection) == None:
        print("Invalid Input")
        continue

    if can_make_coffee(selection) and can_process_money(selection):
        make_coffee(selection)