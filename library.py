import os

def clear():
    os.system('cls')

path = os.getcwd()

# path = (os.getcwd() + "\\file.txt")

clear()

# phrase.replase("Giraffe", "Elephant")

"""
try:
    with open('path') as f:
        lines = f.readlines()
except FileNotFoundError:
    print("")
"""
i = "x"
while i == 0:
    print(" Welcome to my library program!\n1 Overview\n2 Manage Books\n3 Manage members")

# NEXT CHANGE: Checks if data file is ok and tells the user

i = input("\n\nEnter a number to continue: ")
clear()
