print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15 "))
people_split = int(input("How many people to split the bill? "))

total_amt = total_bill * (1 + tip_percentage / 100)
per_person = round(total_amt / people_split, 2)

print(f"Each person should pay: ${per_person}")