import os

# Function to easily clear history
def clear():
    os.system('cls')

# Gets running python directory
path = os.getcwd()
# The following shows how to read all texts from the readme.txt file into a string
# If it doesn't find the file (or maybe directory),
try:
    with open(path) as f:
        lines = f.readlines()
except FileNotFoundError:
    open(path, 'w')

clear()

print("Welcome to my library program!\n1 Overview\n2 Manage Books\n3 ?\n4 Manage members")


# NEXT CHANGE: Checks if data file is ok and tells the user


# Select an option
i = input("\n\nEnter a number to continue: ")
clear()