row1 = ["🚀","🌽","❤️"]
row2 = ["👑","🤣","👽"]
row3 = ["👀","🤡","🪲"]
map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? 💰(int = column then row) 12 = column 1 row 2 ")

column = int(position[0])
row = int(position[1])

map[row-1][column-1] = "💰"
print(f"{row1}\n{row2}\n{row3}")