print("Welcome to Treasure Island. Your mission is to find the treasure")
first_choice = input("Left or Right ")

if first_choice == "right":
    print("Good")
    second_choice = input("Swim or Walk ")
    if second_choice == "swim":
        print("good")
        door = int(input("Which door 1 2 or 3? "))
        if door < 2:
            print("good")
        else:
            print("wrong")
    else:
        print("Wrong")
else:
    print("Wrong")
