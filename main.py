import os
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import shutil


def DeleteResult():
    count=1
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


# Main application class
class MultiPageApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Student Result Form")
        self.geometry("850x600")
        self.configure(bg="white")

        # Initialize the frames for different pages
        self.page1 = tk.Frame(self)
        self.page2 = tk.Frame(self)
        self.page3 = tk.Frame(self)

        self.setup_menubar()
        self.setup_page1()
        self.setup_page2()
        self.setup_page3()

        self.show_page1()

    def setup_menubar(self):
        """Setup the menubar with options."""
        menubar = tk.Menu(self)

        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

        # Add the menubar to the window
        self.config(menu=menubar)

    def show_about(self):
        """Display an About messagebox."""
        webbrowser.open("about.html")

    def show_page1(self):
        self.page1.pack(fill="both", expand=True)
        self.page2.pack_forget()
        self.page3.pack_forget()

    def show_page2(self):
        self.page1.pack_forget()
        self.page2.pack(fill="both", expand=True)
        self.page3.pack_forget()

    def show_page3(self):
        self.page1.pack_forget()
        self.page2.pack_forget()
        self.page3.pack(fill="both", expand=True)






    def CreateResult(self):
        """Create result file and save details."""
        try:
            if self.resultname_entry.get()!=0 and self.uni_entry.get()!="" and self.dep_entry.get()!="" and self.strength_entry.get()!="" and self.section_entry.get()!="":
                if self.strength_entry.get().isdigit() and self.resultname_entry.get().isalpha and self.uni_entry.get().isalpha and self.dep_entry.get().isalpha and self.strength_entry.get().isalpha:
                    if not os.path.isdir("Resultcards/" + self.resultname_entry.get()):  
                        os.mkdir("Resultcards/" + self.resultname_entry.get())
                        with open("Resultcards/" + self.resultname_entry.get() + "/details.uet", "x") as r:
                            r.write(self.uni_entry.get() + "\n" + self.dep_entry.get() + "\n" + self.strength_entry.get() + "\n" + self.section_entry.get())
                        with open("currentproject.uet","w") as r:
                            r.write(self.resultname_entry.get())
                        messagebox.showinfo("Info","Result file created successfully.")
                        self.show_page2()
                    else:
                        messagebox.showerror("Error","Result file already exists.")
                else:
                    messagebox.showerror("Error","Please enter valid input.")
            else:
                messagebox.showerror("Error","Please fill all the feilds.")
        except ValueError:
            messagebox.showerror("Error",ValueError)




    def setup_page3(self):
        """Setup Page 1 (Main menu) with buttons"""
        self.page3.configure(bg="white")
        # Modern header
        header_frame = tk.Frame(self.page3, bg="#2980b9", pady=10)
        header_frame.pack(fill="x")
        ttk.Label(header_frame, text="Create Result File", font=("Arial", 22, "bold"), foreground="white", background="#2980b9").pack()

        form_frame = tk.Frame(self.page3, bg="#ffffff")
        form_frame.pack(pady=20)

        ttk.Label(form_frame, text="Name:", font=("Arial", 12), background="white").grid(row=0, column=0, sticky="e", padx=20, pady=10)
        self.resultname_entry = self.create_modern_entry(form_frame)  # This should be a Tkinter entry widget
        self.resultname_entry.grid(row=0, column=1, padx=20, pady=10)

        ttk.Label(form_frame, text="University:", font=("Arial", 12), background="white").grid(row=1, column=0, sticky="e", padx=20, pady=10)
        self.uni_entry = self.create_modern_entry(form_frame)
        self.uni_entry.grid(row=1, column=1, padx=20, pady=10)

        ttk.Label(form_frame, text="Department:", font=("Arial", 12), background="white").grid(row=2, column=0, sticky="e", padx=20, pady=10)
        self.dep_entry = self.create_modern_entry(form_frame)
        self.dep_entry.grid(row=2, column=1, padx=20, pady=10)

        ttk.Label(form_frame, text="Strength of Class:", font=("Arial", 12), background="white").grid(row=3, column=0, sticky="e", padx=20, pady=10)
        self.strength_entry = self.create_modern_entry(form_frame)
        self.strength_entry.grid(row=3, column=1, padx=20, pady=10)

        ttk.Label(form_frame, text="Section:", font=("Arial", 12), background="white").grid(row=4, column=0, sticky="e", padx=20, pady=10)
        self.section_entry = self.create_modern_entry(form_frame)
        self.section_entry.grid(row=4, column=1, padx=20, pady=10)

        # Now use self.CreateResult directly
        self.create_button = self.create_modern_button(self.page3, "Create Result", command=self.CreateResult)
        self.create_button.pack(pady=20, padx=50, fill='x')










    def setup_page1(self):
        """Setup Page 1 (Main menu) with buttons"""
        
        # Header
        ttk.Label(self.page1, text="Student Result Form", font=("Arial", 24, "bold")).pack(pady=20)

        # Create Buttons for navigation with modern styles
        self.create_button = self.create_modern_button(self.page1, "Create Result", self.show_page3)
        self.create_button.pack(pady=20, padx=50, fill='x')

        # Another button with placeholder
        self.view_button = self.create_modern_button(self.page1, "View Results", command=self.show_page2)
        self.view_button.pack(pady=20, padx=50, fill='x')





    def create_modern_button(self, parent, text, command):
        """Creates a modern-styled button"""
        button = ttk.Button(parent, text=text, command=command)
        style = ttk.Style()
        style.configure("TButton",
                        font=("Arial", 14, "bold"),
                        padding=15,
                        relief="flat",
                        width=20,
                        background="#2980b9",
                        foreground="#2980b9")
        button.configure(style="TButton")

        # Custom Button Hover Effect
        button.bind("<Enter>", lambda e: self.on_hover(button))
        button.bind("<Leave>", lambda e: self.on_leave(button))

        return button

    def on_hover(self, button):
        """Change button background color on hover"""
        button.configure(style="TButtonHover")

    def on_leave(self, button):
        """Revert button background color when not hovered"""
        button.configure(style="TButton")







    








    def setup_page2(self):
        """Setup Page 2 (Form page)"""
        self.page2.configure(bg="white")
        # Modern header
        header_frame = tk.Frame(self.page2, bg="#2980b9", pady=10)
        header_frame.pack(fill="x")
        ttk.Label(header_frame, text="Create Student Result", font=("Arial", 22, "bold"), foreground="white", background="#2980b9").pack()

        # Form layout with a modern feel
        form_frame = tk.Frame(self.page2, bg="#ffffff")
        form_frame.pack(pady=20)

        # Name
        ttk.Label(form_frame, text="Name:", font=("Arial", 12), background="white").grid(row=0, column=0, sticky="e", padx=20, pady=10)
        self.name_entry = self.create_modern_entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=20, pady=10)

        # Roll No
        ttk.Label(form_frame, text="Roll No:", font=("Arial", 12), background="white").grid(row=3, column=0, sticky="e", padx=20, pady=10)
        self.roll_no_entry = self.create_modern_entry(form_frame)
        self.roll_no_entry.grid(row=3, column=1, padx=20, pady=10)

        # Subject Marks
        self.create_marks_input(form_frame)

        # Create Result Button with modern styling
        self.create_button = self.create_modern_button(self.page2, "Create Result",command=self.CreateFile)
        self.create_button.pack(pady=20, padx=50, fill='x')

    def create_modern_entry(self, parent):
        """Create a modern-styled entry (textbox)"""
        entry = ttk.Entry(parent, font=("Arial", 12), width=30)
        entry.configure(style="TEntry")

        # Add internal padding for a better look
        entry.grid(ipadx=10, ipady=5)

        return entry

    def create_marks_input(self, form_frame):
        subjects = ["AICT", "PF", "AP", "DM", "Calculus"]
        for i, subject in enumerate(subjects):
            ttk.Label(form_frame, text=f"{subject} Marks:", font=("Arial", 12), background="white").grid(row=4 + i, column=0, sticky="e", padx=20, pady=10)
            obtained_entry = self.create_modern_entry(form_frame)
            obtained_entry.grid(row=4 + i, column=1, padx=10, pady=10)

            total_entry = self.create_modern_entry(form_frame)
            total_entry.grid(row=4 + i, column=2, padx=10, pady=10)

            setattr(self, f"{subject.lower()}_obtained_entry", obtained_entry)
            setattr(self, f"{subject.lower()}_total_entry", total_entry)

    def grade(self,obtain,total):
        percentage = (obtain/total)*100
        if percentage>=90:
            return "A"
        elif percentage>=80:
            return "B"
        elif percentage>=70:
            return "C"
        elif percentage>=60:
            return "D"
        elif percentage>=50:
            return "F"

    def CreateFile(self):
        """Create result file and save details."""
        try:
            #Validation to ensure that no textbox is empty
            if self.name_entry.get().isalpha() and self.roll_no_entry.get().isdigit() and self.aict_obtained_entry.get().isdigit() and self.aict_total_entry.get().isdigit() and self.pf_obtained_entry.get().isdigit() and self.pf_total_entry.get().isdigit() and self.ap_obtained_entry.get().isdigit() and self.ap_total_entry.get().isdigit() and self.dm_obtained_entry.get().isdigit() and self.dm_total_entry.get().isdigit() and self.calculus_obtained_entry.get().isdigit() and self.calculus_total_entry.get().isdigit():
                # Ensuring that the input is valid
                if int(self.aict_obtained_entry.get())<=int(self.aict_total_entry.get()) and int(self.pf_obtained_entry.get())<=int(self.pf_total_entry.get()) and int(self.ap_obtained_entry.get())<=int(self.ap_total_entry.get()) and int(self.dm_obtained_entry.get())<=int(self.dm_total_entry.get()) and int(self.calculus_obtained_entry.get())<=int(self.calculus_total_entry.get()):
                    # Calculating Total Obtained and Max Marks
                    obtain_marks = int(self.aict_obtained_entry.get()) + int(self.pf_obtained_entry.get()) + int(self.ap_obtained_entry.get()) + int(self.dm_obtained_entry.get()) + int(self.calculus_obtained_entry.get())
                    total_marks = int(self.aict_total_entry.get()) + int(self.pf_total_entry.get()) + int(self.ap_total_entry.get()) + int(self.dm_total_entry.get()) + int(self.calculus_total_entry.get())
                    # Opening currentproject.uet file in order to get the name of result file we are currently working on
                    with open("currentproject.uet","r") as r:
                        # Reading data from details.uet file to get the details related to students
                        with open("Resultcards/"+r.read()+"/"+"details.uet","r") as d:
                            details = d.read().split("\n")  # Converting Details in the form of list
                            print(details)
                        # Copying Result Source from current directory to Results Folder
                        shutil.copy("source.mb","Resultcards/"+ r.read() + "/" + self.name_entry.get()+".html")

                        with open("Resultcards/"+r.read()+self.name_entry.get()+".html","r+") as s:
                            before = s.read()
                            after = before.replace("<uni-name>",details[0]).replace("<std-name>",self.name_entry.get()).replace("<sect-ion>",details[3]).replace("<department>",details[1]).replace("<roll-no>",details[2]).replace("<total-marks>",str(total_marks)).replace("<percentage-total>",str((obtain_marks/total_marks)*100)).replace("<grade-total>",self.grade(obtain_marks,total_marks))
                            print(after)
                            s.seek(0)  # Move cursor back to the beginning of the file
                            s.write(after)  # Write modified content
                else:
                    messagebox.showerror("Error","Obtained Marks cannot be greater than total marks.")
            else:
                messagebox.showerror("Error","Please enter valid input")
        except ValueError:
            messagebox.showerror("Error",ValueError)



# Run the application
if __name__ == "__main__":
    app = MultiPageApp()
    app.mainloop()
