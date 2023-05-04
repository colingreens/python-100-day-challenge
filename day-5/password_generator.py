import random
import string
from string import punctuation

letters  = string.ascii_letters
symbols = list(set(punctuation))

print("Well to the PyPassword Generator")
letters_amount = int(input("How many letters would you like?\n"))
numbers_amount = int(input("How many numbers would you like?\n"))
symbols_amount = int(input("How many symbols would you like?\n"))

password = []

for letter in range(1,letters_amount + 1):
    password.append(random.choice(letters))

for number in range(1,numbers_amount + 1):
    password.append(str(random.randint(0, 9)))

for symbol in range(1,symbols_amount + 1):
    password.append(random.choice(symbols))

random.shuffle(password)

passwordString = ""
for char in password:
    passwordString += char

print(str(passwordString))
