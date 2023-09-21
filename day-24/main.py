#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as file:
    names = [name.rstrip() for name in file]

with open('./Input/Letters/starting_letter.txt', 'r') as f:
    starting_letter = f.read()

for name in names:
    named_letter = starting_letter.replace("[name]",name)
    f = open(f"./Output/ReadyToSend/{name}.txt","w")
    f.write(named_letter)