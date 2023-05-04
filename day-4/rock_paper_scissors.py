import random

player_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

rock = "🪨"
paper = "📃"
scissors = "✂️"

options_list = [rock, paper, scissors]

print(f"Player throws {options_list[player_choice]}\n")
print(f"Computer throws {options_list[computer_choice]}")

if player_choice == computer_choice:
    print("Draw! Throw again")
elif player_choice == 1 and computer_choice == 2:
    print("Computer Wins!")
elif player_choice == 2 and computer_choice == 3:
    print("Computer Wins!")
elif player_choice == 3 and computer_choice == 1:
    print("Computer Wins!")
else:
    print("Player wins!")


