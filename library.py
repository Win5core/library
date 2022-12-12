import os

def cls():
    os.system('cls')

path = os.path.dirname(__file__)

people = (path + "\data\people.txt")

cls()

# phrase.replace("Giraffe", "Elephant")

try:
    with open('path' , 'r') as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = False



print("Welcome to my library program!\n1 Overview\n2 Manage Books\n3 Manage members\n0 Exit")


# NEXT CHANGE: Checks if data file is ok and tells the user


i = input("\n\nEnter a number to continue: ")

while int(i) != 0:
    if int(i) == 1:
        print("Overview")
    if int(i) == 2:
        pass



