import os

# This function is for presentation to make program Visually Attractive
def Presentation(n):
    os.system("cls")  # To Clear the Output Screen
    if n=="main":
        print("-----------------------------------------------")
        print("| Welcome to Students Grade Management System |")
        print("-----------------------------------------------")
        print("1. Create Result Cards")
        print("2. View Result Cards")
        print("3. Add Student Details")
        print("4. Remove Student Details")
        print("5. Delete Result Cards")
        print("6. About")
        print("7. Exit")

def CreateResult():
    pass

def ViewResult():
    pass

def AddDetail():
    pass

def RemoveDetail():
    pass

def About():
    pass

# Main Function: From where our program Starts
def main():
    Presentation("main")
    num=input("Enter Number: ")
    if num=='1':
        CreateResult()
    elif num=='2':
        ViewResult()
    elif num=='3':
        AddDetail()
    elif num=='4':
        RemoveDetail()
    elif num=='6':
        About()
    elif num=='7':
        exit()
    else:
        os.system("cls") # To Clear the output Screen
        input("Invalid Number! Press Enter Key to go back.")
        main()

main()