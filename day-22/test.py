import csv

active_days = []

with open("./ragbrai_training.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        miles = int(row[1])
        if miles > 0:
            active_days.append(miles)


print("Active Miles\n")
print(f"Total Miles: {sum(active_days)}\n")
print(f"Total Days: {len(active_days)}\n")
print(f"Average Miles Per Day: {sum(active_days)/len(active_days)}")
