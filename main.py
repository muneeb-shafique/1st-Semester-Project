import os
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

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
                for item in os.listdir("Resultcards/"+results[index]+"/"):
                    os.remove("Resultcards/"+results[index]+"/"+item)
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

def About():
    subprocess.Popen(["notepad.exe","about.txt"])


# Function to create the result
def create_result():
    try:
        # Get values from the entry fields
        name = name_entry.get()
        section = section_entry.get()
        department = department_entry.get()
        roll_no = roll_no_entry.get()
        aict_obtained = int(aict_obtained_entry.get())
        aict_total = int(aict_total_entry.get())

        pf_obtained = int(pf_obtained_entry.get())
        pf_total = int(pf_total_entry.get())

        ap_obtained = int(ap_obtained_entry.get())
        ap_total = int(ap_total_entry.get())

        dm_obtained = int(dm_obtained_entry.get())
        dm_total = int(dm_total_entry.get())

        calculus_obtained = int(calculus_obtained_entry.get())
        calculus_total = int(calculus_total_entry.get())

        # Calculate total marks and percentage
        total_marks = (aict_obtained + pf_obtained + ap_obtained + dm_obtained + calculus_obtained)
        total_max_marks = (aict_total + pf_total + ap_total + dm_total + calculus_total)
        percentage = (total_marks / total_max_marks) * 100

        # Display result in a pop-up
        result_text = (f"Name: {name}\n"
                       f"Section: {section}\n"
                       f"Department: {department}\n"
                       f"Roll No: {roll_no}\n"
                       f"Total Marks: {total_marks}/{total_max_marks}\n"
                       f"Percentage: {percentage:.2f}%")
        
        messagebox.showinfo("Student Result", result_text)
    
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for marks.")

# Main Window
root = tk.Tk()
root.title("Student Result Form")
root.geometry("600x600")
root.configure(bg="white")

# Menu Bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Adding 'File' menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Adding 'Insert' menu
about_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About")

# Style for ttk widgets (modern look)
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="white")
style.configure("TEntry", font=("Arial", 12), padding=5, relief="flat", fieldbackground="#ecf0f1", foreground="black")
style.configure("TButton", font=("Arial", 12, "bold"), background="#3498db", foreground="white", relief="flat", padding=10)
style.map("TButton", background=[('active', '#2980b9')])

# Labels and Entry Widgets
# Name, Section, Department, Roll No.
ttk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=20, pady=10)
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=20, pady=10, ipadx=10)

ttk.Label(root, text="Section:").grid(row=1, column=0, sticky="e", padx=20, pady=10)
section_entry = ttk.Entry(root)
section_entry.grid(row=1, column=1, padx=20, pady=10, ipadx=10)

ttk.Label(root, text="Department:").grid(row=2, column=0, sticky="e", padx=20, pady=10)
department_entry = ttk.Entry(root)
department_entry.grid(row=2, column=1, padx=20, pady=10, ipadx=10)

ttk.Label(root, text="Roll No:").grid(row=3, column=0, sticky="e", padx=20, pady=10)
roll_no_entry = ttk.Entry(root)
roll_no_entry.grid(row=3, column=1, padx=20, pady=10, ipadx=10)

# Subject Marks Entry Section
ttk.Label(root, text="AICT Marks:").grid(row=4, column=0, padx=20, pady=10)
aict_obtained_entry = ttk.Entry(root)
aict_obtained_entry.grid(row=4, column=1, padx=10, pady=10, ipadx=10)
aict_total_entry = ttk.Entry(root)
aict_total_entry.grid(row=4, column=2, padx=10, pady=10, ipadx=10)

ttk.Label(root, text="PF Marks:").grid(row=5, column=0, padx=20, pady=10)
pf_obtained_entry = ttk.Entry(root)
pf_obtained_entry.grid(row=5, column=1, padx=10, pady=10, ipadx=10)
pf_total_entry = ttk.Entry(root)
pf_total_entry.grid(row=5, column=2, padx=10, pady=10, ipadx=10)

ttk.Label(root, text="AP Marks:").grid(row=6, column=0, padx=20, pady=10)
ap_obtained_entry = ttk.Entry(root)
ap_obtained_entry.grid(row=6, column=1, padx=10, pady=10, ipadx=10)
ap_total_entry = ttk.Entry(root)
ap_total_entry.grid(row=6, column=2, padx=10, pady=10, ipadx=10)

ttk.Label(root, text="DM Marks:").grid(row=7, column=0, padx=20, pady=10)
dm_obtained_entry = ttk.Entry(root)
dm_obtained_entry.grid(row=7, column=1, padx=10, pady=10, ipadx=10)
dm_total_entry = ttk.Entry(root)
dm_total_entry.grid(row=7, column=2, padx=10, pady=10, ipadx=10)

ttk.Label(root, text="Calculus Marks:").grid(row=8, column=0, padx=20, pady=10)
calculus_obtained_entry = ttk.Entry(root)
calculus_obtained_entry.grid(row=8, column=1, padx=10, pady=10, ipadx=10)
calculus_total_entry = ttk.Entry(root)
calculus_total_entry.grid(row=8, column=2, padx=10, pady=10, ipadx=10)

# "Create Result" Button
create_button = ttk.Button(root, text="Create Result", command=create_result)
create_button.grid(row=9, column=0, columnspan=3, pady=30)

# Run the application
root.mainloop()
