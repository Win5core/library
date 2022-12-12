import os

def cls():
    os.system('cls')
cls()

memberspath = ((os.path.dirname(__file__)) + "\data\members.txt")
bookspath = ((os.path.dirname(__file__)) + "\data\\books.txt")

# memberspath
try:
    with open('path' , 'r') as f:
        memberspath = f.readlines()
except FileNotFoundError:
    print("Data for not found, made a new data file")
    open(memberspath , 'w')
# bookspath
try:
    with open('path' , 'r') as f:
        bookspath = f.readlines()
except FileNotFoundError:
    print("Data for books not found, made a new data file")
    open(bookspath , 'w')
# phrase.replace("Giraffe", "Elephant")


# ................................................................................................................................

# add book/person to list
"""
i = 1
bookspath = []
while i != 0:
    x = input("\n")
    if x == "0":
        i = 0
    else:
        bookspath.append(x)
        print(bookspath)
"""










print("Welcome to my library program!\n1 Overview\n2 Manage Books\n3 Manage members\n0 Exit")
i = input("\n\nEnter a number to continue: ")

while int(i) != 0:
    if int(i) == 1:
        print("Overview")
    if int(i) == 2:
        pass



