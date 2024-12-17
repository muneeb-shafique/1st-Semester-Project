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
class MultiPageApp(tk.Tk):  # Define a class that inherits from tk.Tk to create the main app window
    def __init__(self):  # Initialize the constructor for the MultiPageApp class
        super().__init__()  # Call the constructor of the parent class (tk.Tk) to initialize the window

        self.title("Student Result Form")  # Set the title of the window
        self.geometry("850x650")  # Define the dimensions of the window (850px by 650px)
        self.configure(bg="white")  # Set the background color of the window to white

        # Set the minimum window size to 850x650 pixels to prevent resizing smaller
        self.wm_minsize(850, 650)  

        # Initialize the frames for different pages (page1, page2, and page3)
        self.page1 = tk.Frame(self)  # Create a Frame widget for page1
        self.page2 = tk.Frame(self)  # Create a Frame widget for page2
        self.page3 = tk.Frame(self)  # Create a Frame widget for page3

        self.setup_menubar()  # Call the setup_menubar method to create a menubar for the app
        self.setup_page1()  # Call the setup_page1 method to set up the first page
        self.setup_page2()  # Call the setup_page2 method to set up the second page
        self.setup_page3()  # Call the setup_page3 method to set up the third page

        self.show_page1()  # Display the first page by default when the app starts

    def setup_menubar(self):  # Define the setup_menubar method
        """Setup the menubar with options."""  # Comment explaining the purpose of this method
        menubar = tk.Menu(self)  # Create a menubar widget


        # File Menu
        file_menu = tk.Menu(menubar, tearoff=0)  # Create a menu for file options (tearoff=0 disables tearing off the menu)
        file_menu.add_command(label="Exit", command=self.quit)  # Add an "Exit" option that will close the application when selected
        menubar.add_cascade(label="File", menu=file_menu)  # Add the file_menu to the menubar with the label "File"

        # Help Menu 
        help_menu = tk.Menu(menubar, tearoff=0)  # Create a menu for help options (tearoff=0 disables tearing off the menu)
        help_menu.add_command(label="About", command=self.show_about)  # Add an "About" option that will show an about message when selected
        menubar.add_cascade(label="Help", menu=help_menu)  # Add the help_menu to the menubar with the label "Help"

        # Add the menubar to the window  # Comment indicating that the menubar is being added to the window
        self.config(menu=menubar)  # Configure the main window to display the menubar

    def show_about(self):  # Define the method to show the "About" information
        """Display an About messagebox."""  # Comment explaining the method's functionality
        webbrowser.open("about.html")  # Open the "about.html" file in the default web browser when the "About" menu is clicked

    def show_page1(self):  # Define the method to display the first page (page1)
        self.page1.pack(fill="both", expand=True)  # Pack the page1 frame into the window to make it visible (expand to fill available space)
        self.page2.pack_forget()  # Hide the page2 frame if it's currently displayed
        self.page3.pack_forget()  # Hide the page3 frame if it's currently displayed

    def show_page2(self):  # Define the method to display the second page (page2)
        self.page1.pack_forget()  # Hide the page1 frame if it's currently displayed
        self.page2.pack(fill="both", expand=True)  # Pack the page2 frame into the window to make it visible
        self.page3.pack_forget()  # Hide the page3 frame if it's currently displayed

    def show_page3(self):  # Define the method to display the third page (page3)
        self.page1.pack_forget()  # Hide the page1 frame if it's currently displayed
        self.page2.pack_forget()  # Hide the page2 frame if it's currently displayed
        self.page3.pack(fill="both", expand=True)  # Pack the page3 frame into the window to make it visible







    def CreateResult(self):
        """Create result file and save details."""
        # Try Method to Handle Unexpected Errors
        try:
            # Validating that no feild is empty
            if self.resultname_entry.get()!="" and self.uni_entry.get()!="" and self.dep_entry.get()!="" and self.strength_entry.get()!="" and self.section_entry.get()!="":
                # Validating that the data given in textboxes is correct.
                if self.strength_entry.get().isdigit() and self.resultname_entry.get().isalpha() and self.uni_entry.get().isalpha() and self.dep_entry.get().isalpha() and self.strength_entry.get().isalpha():
                    # Checking if there is already a Result Folder or not
                    if not os.path.isdir("Resultcards/" + self.resultname_entry.get()):  
                        os.mkdir("Resultcards/" + self.resultname_entry.get())  # Create a new Result Folder
                        # Creating a new file details.uet in Results Folder
                        with open("Resultcards/" + self.resultname_entry.get() + "/details.uet", "x") as r:
                            # Writing Data in detials.uet file
                            r.write(self.uni_entry.get() + "\n" + self.dep_entry.get() + "\n" + self.strength_entry.get() + "\n" + self.section_entry.get())
                        with open("currentproject.uet","w") as r:   # Opening currentproject.uet file
                            r.write(self.resultname_entry.get())    # Reading Result File Name from currentproject.uet file
                        messagebox.showinfo("Info","Result file created successfully.")
                        self.show_page2()   # Displaying Page 2
                    else:
                        messagebox.showerror("Error","Result file already exists.")
                else:
                    messagebox.showerror("Error","Please enter valid input.")
            else:
                messagebox.showerror("Error","Please fill all the feilds.")
        except ValueError:
            messagebox.showerror("Error",ValueError)




    def setup_page3(self):  # Define the setup method for the third page
        """Setup Page 1 (Main menu) with buttons"""  # Comment describing the purpose of this method
        self.page3.configure(bg="white")  # Set the background color of page3 to white

        # Modern header section for the page
        header_frame = tk.Frame(self.page3, bg="#2980b9", pady=10)  # Create a frame for the header with a blue background and padding
        header_frame.pack(fill="x")  # Pack the header frame horizontally across the window
        ttk.Label(header_frame, text="Create Result File", font=("Arial", 22, "bold"), foreground="white", background="#2980b9").pack()  # Create a label with white text on a blue background inside the header frame

        # Create the form frame where user input fields will be placed
        form_frame = tk.Frame(self.page3, bg="#ffffff")  # Create a frame for the form with a white background
        form_frame.pack(pady=20)  # Pack the form frame with vertical padding of 20

        # Create and position the "Name" label and entry field
        ttk.Label(form_frame, text="Name:", font=("Arial", 12), background="white").grid(row=0, column=0, sticky="e", padx=20, pady=10)  # Label with text "Name" aligned to the right
        self.resultname_entry = self.create_modern_entry(form_frame)  # Create an entry widget for "Name"
        self.resultname_entry.grid(row=0, column=1, padx=20, pady=10)  # Place the entry widget in the grid at row 0, column 1

        # Create and position the "University" label and entry field
        ttk.Label(form_frame, text="University:", font=("Arial", 12), background="white").grid(row=1, column=0, sticky="e", padx=20, pady=10)  # Label with text "University"
        self.uni_entry = self.create_modern_entry(form_frame)  # Create an entry widget for "University"
        self.uni_entry.grid(row=1, column=1, padx=20, pady=10)  # Place the entry widget in the grid at row 1, column 1

        # Create and position the "Department" label and entry field
        ttk.Label(form_frame, text="Department:", font=("Arial", 12), background="white").grid(row=2, column=0, sticky="e", padx=20, pady=10)  # Label with text "Department"
        self.dep_entry = self.create_modern_entry(form_frame)  # Create an entry widget for "Department"
        self.dep_entry.grid(row=2, column=1, padx=20, pady=10)  # Place the entry widget in the grid at row 2, column 1

        # Create and position the "Strength of Class" label and entry field
        ttk.Label(form_frame, text="Strength of Class:", font=("Arial", 12), background="white").grid(row=3, column=0, sticky="e", padx=20, pady=10)  # Label with text "Strength of Class"
        self.strength_entry = self.create_modern_entry(form_frame)  # Create an entry widget for "Strength of Class"
        self.strength_entry.grid(row=3, column=1, padx=20, pady=10)  # Place the entry widget in the grid at row 3, column 1

        # Create and position the "Section" label and entry field
        ttk.Label(form_frame, text="Section:", font=("Arial", 12), background="white").grid(row=4, column=0, sticky="e", padx=20, pady=10)  # Label with text "Section"
        self.section_entry = self.create_modern_entry(form_frame)  # Create an entry widget for "Section"
        self.section_entry.grid(row=4, column=1, padx=20, pady=10)  # Place the entry widget in the grid at row 4, column 1

        # Create and position the "Create Result" button
        self.create_button = self.create_modern_button(self.page3, "Create Result", command=self.CreateResult)  # Create a button with the text "Create Result" and bind the action to the CreateResult method
        self.create_button.pack(pady=20, padx=50, fill='x')  # Pack the button with vertical padding of 20, horizontal padding of 50, and make it fill the width of the window











    def setup_page1(self):
        """Setup Page 1 (Main menu) with buttons"""
        
        # Header
        ttk.Label(self.page1, text="Student Result Form", font=("Arial", 24, "bold")).pack(pady=20)

        # Create Buttons for navigation with modern styles
        self.create_button = self.create_modern_button(self.page1, "Create Result", self.show_page3)
        self.create_button.pack(pady=20, padx=50, fill='x')

        # Another button with placeholder
        self.view_button = self.create_modern_button(self.page1, "Continue Adding Results", command=self.show_page2)
        self.view_button.pack(pady=20, padx=50, fill='x')

        # Another button with placeholder
        self.view_button = self.create_modern_button(self.page1, "List of results created", command=self.show_page2)
        self.view_button.pack(pady=20, padx=50, fill='x')





    def create_modern_button(self, parent, text, command):  # Define the method to create a modern-styled button
        """Creates a modern-styled button"""  # Comment describing the method
        button = ttk.Button(parent, text=text, command=command)  # Create the button with the provided text and command
        style = ttk.Style()  # Create a Style object to customize the appearance of the button
        style.configure("TButton",  # Configure the button's style
                        font=("Arial", 14, "bold"),  # Set the font to Arial, size 14, bold
                        padding=15,  # Add padding inside the button
                        relief="flat",  # Remove the default border (flat relief)
                        width=20,  # Set the button width to 20 characters
                        background="#2980b9",  # Set the background color to a shade of blue
                        foreground="#2980b9")  # Set the text color to the same blue
        button.configure(style="TButton")  # Apply the "TButton" style to the button

        style.configure("TButtonHover",
                        background="#3498db",  # Set a lighter blue background when hovered
                        foreground="white")  # Set the text color to white on hover
        button.configure(style="TButton")
        style.configure("Custom.TCheckbutton", background="white", font=("Arial", 16))  # Configure a custom style for Checkbuttons (unused here)

        # Custom Button Hover Effect
        button.bind("<Enter>", lambda e: self.on_hover(button))  # Bind the <Enter> event to trigger the hover effect
        button.bind("<Leave>", lambda e: self.on_leave(button))  # Bind the <Leave> event to revert the hover effect

        return button  # Return the button object

    def on_hover(self, button):  # Define the method to handle the hover effect
        """Change button background color on hover"""  # Comment describing the hover effect method
        button.configure(style="TButtonHover")  # Change the button's style to "TButtonHover" when hovered

    def on_leave(self, button):  # Define the method to revert the hover effect
        """Revert button background color when not hovered"""  # Comment explaining the revert action
        button.configure(style="TButton")  # Revert the button's style back to the default "TButton" when the hover ends



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


        self.var = tk.IntVar()
        style = ttk.Style()
        style.configure("TCheckbutton",
                    background="white",  # Set the background to white
                    font=("Arial", 16))   # Set the font style

        # Create the checkbox with the customized style
        checkbox = ttk.Checkbutton(form_frame, text="Open result after creating", variable=self.var, style="TCheckbutton")
        checkbox.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="w")

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
        percentage = (int(obtain)/int(total))*100
        if percentage>=90:
            return "A"
        elif percentage>=80:
            return "B"
        elif percentage>=70:
            return "C"
        elif percentage>=60:
            return "D"
        elif percentage>=50:
            return "E"
        elif percentage<50:
            return "F"
        
    def comments(self,name,percentage):
        if percentage>=90:
            return f"Congratulations on achieving an A grade, {name}! Your dedication, hard work, and commitment to excellence are clearly reflected in your performance. Keep up the fantastic effort, and continue striving for greatness in all that you do."
        elif percentage >=80:
            return f"Congratulations on earning a B grade, {name}! You've shown a solid understanding of the material and have worked hard throughout the term. Keep building on your strengths and continue to push yourself to achieve even greater success next time."
        elif percentage>=70:
            return f"You've done well to earn a C grade, {name}, but there's still room for improvement. Make sure to review areas where you struggled, and consider seeking additional support if necessary. Consistent effort and a positive mindset will help you make progress and achieve better results next time."
        elif percentage>=60:
            return f"You've earned a D grade, {name}, and while you've made some effort, there's a clear need for improvement in understanding the material. I encourage you to review the topics you found difficult, ask questions, and seek extra help if needed. With more dedication, you can improve your performance."
        elif percentage>=50:
            return f"{name}, your performance this term was below expectations, and there were significant gaps in your understanding of the material. It's important to dedicate more time to studying and seek help to address the areas of difficulty. I encourage you to take advantage of additional resources, such as tutoring or review sessions, to improve your grasp of the subject. With focused effort and support, you can make progress and perform better moving forward."
        elif percentage<50:
            return f"{name}, your performance this term was below expectations, with significant gaps in understanding the material. I recommend seeking extra help or tutoring to address these challenges. With more effort and support, you can improve. Please take this opportunity to focus on your learning and reach out for assistance."

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
                        result_name = r.read()
                        # Reading data from details.uet file to get the details related to students
                        with open("Resultcards/"+result_name+"/"+"details.uet","r") as d:
                            details = d.read().split("\n")  # Converting Details in the form of list
                            print(details)
                        # Copying Result Source from current directory to Results Folder
                        shutil.copy("source.mb","Resultcards/"+ result_name + "/" + self.name_entry.get()+".html")
                        # Opening File in Read/Write Format to remove previous content and adding the updated one.
                        with open("Resultcards/"+result_name + "/" +self.name_entry.get()+".html","r+") as s:
                            before = s.read()
                            # Replacing Dummy Text with Actual Data for HTML file
                            after = before.replace("<uni-name>",details[0])\
                                            .replace("<std-name>",self.name_entry.get())\
                                            .replace("<sect-ion>",details[3])\
                                            .replace("<department>",details[1])\
                                            .replace("<roll-no>",details[2])\
                                            .replace("<total-marks>",str(total_marks))\
                                            .replace("<percentage-total>",str(int((obtain_marks/total_marks)*100))+"%")\
                                            .replace("<grade-total>",self.grade(obtain_marks,total_marks))\
                                            .replace("<aict-obtain>",self.aict_obtained_entry.get())\
                                            .replace("<aict-total>",self.aict_total_entry.get())\
                                            .replace("<aict-grade>",self.grade(self.aict_obtained_entry.get(),self.aict_total_entry.get()))\
                                            .replace("<pf-obtain>",self.pf_obtained_entry.get())\
                                            .replace("<pf-total>",self.pf_total_entry.get())\
                                            .replace("<pf-grade>",self.grade(self.pf_obtained_entry.get(),self.pf_total_entry.get()))\
                                            .replace("<ap-obtain>",self.ap_obtained_entry.get())\
                                            .replace("<ap-total>",self.ap_total_entry.get())\
                                            .replace("<ap-grade>",self.grade(self.ap_obtained_entry.get(),self.ap_total_entry.get()))\
                                            .replace("<dm-obtain>",self.dm_obtained_entry.get())\
                                            .replace("<dm-total>",self.dm_total_entry.get())\
                                            .replace("<dm-grade>",self.grade(self.dm_obtained_entry.get(),self.dm_total_entry.get()))\
                                            .replace("<calculus-obtain>",self.calculus_obtained_entry.get())\
                                            .replace("<calculus-total>",self.calculus_total_entry.get())\
                                            .replace("<calculus-grade>",self.grade(self.calculus_obtained_entry.get(),self.calculus_total_entry.get()))\
                                            .replace("<comments>",self.comments(self.name_entry.get(),(obtain_marks/total_marks)*100))
                            print(after)
                            s.seek(0)  # Move cursor back to the beginning of the file
                            s.write(after)  # Write modified content
                            if self.var.get():
                                webbrowser.open(os.path.dirname(os.path.abspath(__file__)) + "/" + "Resultcards/"+result_name + "/" +self.name_entry.get()+".html")
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