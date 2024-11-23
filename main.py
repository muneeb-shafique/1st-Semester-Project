import os

# This function is for presentation to make program Visually Attractive
def Presentation(n):
    os.system("cls")  # To Clear the Output Screen
    os.system("color 0a") # To Change Text color to Green
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
    elif n=="create":
        print("-----------------------------------------------")
        print("|               Create Results                |")
        print("-----------------------------------------------")
    elif n=="delete":
        print("-----------------------------------------------")
        print("|               Delete Results                |")
        print("-----------------------------------------------")
    elif n=="view":
        print("-----------------------------------------------")
        print("|                 View Results                |")
        print("-----------------------------------------------")
    elif n=="add":
        print("-----------------------------------------------")
        print("|                  Add Details                |")
        print("-----------------------------------------------")
    elif n=="remove":
        print("-----------------------------------------------")
        print("|               Remove Results                |")
        print("-----------------------------------------------")

# To Create Results and Redirect to AddDetails() Function.
def CreateResult():
    Presentation("create")
    result_name = input("Enter Result Name: ")
    if not os.path.isdir("Resultcards/"+result_name):
        os.mkdir("Resultcards/"+result_name)
        input("Result Created Successfully! Press Enter to add Students Information.")
        AddDetail()
    else:
        input("Result Already Exists! Press Enter Key to go back.")
        main()

# To View the No. of Results We have created till now.
def ViewResult():
    pass

def AddDetail():
    pass

def RemoveDetail():
    pass

def DeleteResult():
    count=1
    Presentation("delete")
    print("Result Cards")
    results = os.listdir("Resultcards/")
    if len(results)!=0:
        for result in results:
            print(str(count)+") "+result)
            count+=1
        num = input("Index: ")
        
        if num != "" and num.isdigit() and int(num) < count:
            index=int(num)-1
            os.system("cls")
            print("Are you sure you want to delete",results[index],"results permanently? (Y/N)")
            sure=input()
            os.system("cls")
            if sure.upper() =='Y' or sure.upper()=="YES": 
                os.rmdir("Resultcards/"+results[index])
                print("Result Removed Successfully!")
            elif sure.upper() =='N' or sure.upper()=="NO":
                print("Deletion of",results[index],"is canceled.")
            else:
                print("Invalid Input! Press Enter Key go to back.")
        else:
            os.system("cls")
            print("Please Enter Valid Index.")
    else:
        print("No Resultcards Available")
    input()
    main()

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
    elif num=='5':
        DeleteResult()
    elif num=='6':
        About()
    elif num=='7':
        exit()
    else:
        os.system("cls") # To Clear the output Screen
        input("Invalid Number! Press Enter Key to go back.")
        main()

main()