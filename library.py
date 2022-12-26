# Making a short command to use cls
import os
def cls():
    os.system('cls')
cls()

# Importing paths as a string to variable
memberspath = ((os.path.dirname(__file__)) + "\data\members.txt")
bookspath = ((os.path.dirname(__file__)) + "\data\\books.txt")
path = ((os.path.dirname(__file__)) + "\data")

# Data file checker
if os.path.exists(path) == False:
    os.mkdir(path)
if os.path.isfile(memberspath) == False:
        open(memberspath , 'w')
if os.path.isfile(bookspath) == False:
        open(bookspath , 'w')

# Menus
def menu0():
    cls()
    print("Welcome to my library program!\n1 Overview\n2 Manage Books\n3 Manage members\n0 Exit")
def menu2():
    cls()
    print("1 View list of books\n2 Add a new book\n3 Remove a book\n0 Return to previous menu")
def menu3():
    cls()
    print("1 View list of members\n2 Add a new member\n3 Remove a member\n0 Return to previous menu")
i0 = ()
i1 = ()
i2 = ()
i3 = ()

while i0 != 0:
    menu0()
    i0 = int(input("\nEnter a number: "))
    if i0 == 1:
        # Menu1
        print("option 1")
    elif i0 == 2:
        # Books menu (menu2)
        while i2 !=0:
            menu2()
            try:
                i2 = int(input("\nEnter a number: "))
            except ValueError:
                pass
            if i2 == 1:
                cls()
                with open(bookspath) as file: 
                    while (line := file.readline().rstrip()): 
                        print(line)
                input("\nPress enter to continue")
            elif i2 == 2:
                    cls()
                    books = []
                    with open(bookspath) as file: 
                        for line in file: 
                            books.append(line.rstrip())
                    newbook = (str(input("Enter the name: ")))
                    books.append(newbook)
                    file = open(bookspath,'w')
                    for book in books:
                        file.write(book + "\n")
                    file.close()
                    input("Done! Press enter to continue")
            elif i2 == 3:
                cls()
                books = []
                with open(bookspath) as file: 
                    for line in file: 
                        books.append(line.rstrip())
                x = int(0)
                while x == 0:
                    bookremove = str(input("Enter the name or enter 0 to cancel: "))
                    if bookremove == str(0):
                        x = int(1)
                    else:
                        try:
                            books.remove(bookremove)
                            x = int(1)
                            file = open(bookspath,'w')
                            for book in books:
                                file.write(book + "\n")
                            file.close()
                            input("\nDone! Press enter to continue")
                        except ValueError:
                            print("Book not found")
            elif i3 == 0:
                i0 = ()
                pass
            else:
                cls()
                menu3()
                i2 = int(input("\nInvalid number! Enter again: "))
    elif i0 == 3:
        # Members menu (menu3)
        while i3 !=0:
            menu3()
            try:
                i3 = int(input("\nEnter a number: "))
            except ValueError:
                pass
            if i3 == 1:
                cls()
                with open(memberspath) as file: 
                    while (line := file.readline().rstrip()): 
                        print(line)
                input("\nPress enter to continue")
            elif i3 == 2:
                    cls()
                    members = []
                    with open(memberspath) as file: 
                        for line in file: 
                            members.append(line.rstrip())
                    newmember = (str(input("Enter the name: ")))
                    members.append(newmember)
                    file = open(memberspath,'w')
                    for member in members:
                        file.write(member + "\n")
                    file.close()
                    input("Done! Press enter to continue")
            elif i3 == 3:
                cls()
                members = []
                with open(memberspath) as file: 
                    for line in file: 
                        members.append(line.rstrip())
                x = int(0)
                while x == 0:
                    memberremove = str(input("Enter the name or enter 0 to cancel: "))
                    if memberremove == str(0):
                        x = int(1)
                    else:
                        try:
                            members.remove(memberremove)
                            x = int(1)
                            file = open(memberspath,'w')
                            for member in members:
                                file.write(member + "\n")
                            file.close()
                            input("\nDone! Press enter to continue")
                        except ValueError:
                            print("Member not found")
            elif i3 == 0:
                i0 = ()
                pass
            else:
                cls()
                menu3()
                i2 = int(input("\nInvalid number! Enter again: "))
    elif i0 == 0:
        cls()
        print("Thanks for using the program!\n")
    else:
        menu0()
        i0 = int(input("\nInvalid number! Enter again: "))
