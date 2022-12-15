import os

def cls():
    os.system('cls')
cls()
memberspath = ((os.path.dirname(__file__)) + "\data\members.txt")
bookspath = ((os.path.dirname(__file__)) + "\data\\books.txt")
path = ((os.path.dirname(__file__)) + "\data")

# memberspath
try:
    print("Creating path...")
    os.mkdir(path)
except FileExistsError:
    print("Path already exists!")
try:
    with open(memberspath , 'r') as f:
        members = f.readlines
        print("wut")
except FileNotFoundError:
    print("Members data not found, made a new data file")
    open(memberspath , 'w')
        
# bookspath , needs edit
"""
try:
    print("Creating path...")
    os.mkdir(path)
except FileExistsError:
    print("Path already exists!")
try:
    with open(memberspath , 'r') as f:
        members = f.readlines
        print("wut")
except FileNotFoundError:
    print("Members data not found, made a new data file")
    open(memberspath , 'w')
"""

# ................................................................................................................................

# add book/person to list
"""
i = 1
books = []
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
        # print("Overview")
        pass
    if int(i) == 2:
        pass
cls()


