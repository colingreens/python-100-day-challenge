current_age = int(input("What is your current age?\n"))

years_left = 90 - current_age
months_left = years_left * 12
weeks_left = months_left * 52

print(f"You have:\n{years_left} years.\n{months_left} months.\n{weeks_left} weeks left to live.")