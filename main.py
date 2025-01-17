import sys
import os
import webbrowser
import shutil
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QMenuBar, QAction, QHBoxLayout, QSpacerItem, QSizePolicy, QLineEdit, QStackedWidget, QMessageBox, QCheckBox, QListWidget

class ModernButton(QPushButton):
    def __init__(self, label, parent=None):
        super().__init__(label, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                font-size: 16px;
                padding: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)







class Page1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        go_back_button = QPushButton("Go Back", self)
        go_back_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        go_back_button.clicked.connect(self.go_back)
        top_layout.addWidget(go_back_button)
        title_label = QLabel("Create Results File", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("color: #2C3E50; margin-bottom: 30px;")
        top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        top_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(top_layout)
        form_layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Name")
        self.name_input.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                color: #2C3E50;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #2980b9;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        self.university_input = QLineEdit(self)
        self.university_input.setPlaceholderText("Enter University")
        self.university_input.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                color: #2C3E50;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #2980b9;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(QLabel("University:"))
        form_layout.addWidget(self.university_input)
        self.department_input = QLineEdit(self)
        self.department_input.setPlaceholderText("Enter Department")
        self.department_input.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                color: #2C3E50;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #2980b9;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(QLabel("Department:"))
        form_layout.addWidget(self.department_input)
        self.strength_input = QLineEdit(self)
        self.strength_input.setPlaceholderText("Enter Strength of Class")
        self.strength_input.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                color: #2C3E50;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #2980b9;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(QLabel("Strength of Class:"))
        form_layout.addWidget(self.strength_input)

        self.section_input = QLineEdit(self)
        self.section_input.setPlaceholderText("Enter Section")
        self.section_input.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                color: #2C3E50;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #2980b9;
                background-color: #ffffff;
            }
        """)
        form_layout.addWidget(QLabel("Section:"))
        form_layout.addWidget(self.section_input)
        layout.addLayout(form_layout)
        # Create "Create Result File" button at center
        create_button = QPushButton("Create Result File", self)
        self.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border-radius: 10px;
                font-size: 16px;
                padding: 15px;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #1f618d;
            }
        """)
        create_button.clicked.connect(self.create_result_file)
        layout.addWidget(create_button, alignment=Qt.AlignCenter)
        self.setLayout(layout)
    def go_back(self):
        self.window().show_page(0)  
    def create_result_file(self):
        try:
            if (self.name_input.text() != "" and
                self.university_input.text() != "" and
                self.department_input.text() != "" and
                self.strength_input.text() != "" and
                self.section_input.text() != ""):

                if (self.strength_input.text().isdigit() and
                    self.name_input.text().replace(" ","").isalpha() and
                    self.university_input.text().replace(" ","").isalpha() and
                    self.department_input.text().replace(" ","").isalpha() and
                    self.section_input.text().replace(" ","").isalpha()):

                    result_folder = f"Resultcards/{self.name_input.text()}"
                    if not os.path.isdir(result_folder):
                        os.mkdir(result_folder) 
                        with open(f"{result_folder}/details.uet", "x") as r:
                            r.write(f"{self.university_input.text()}\n{self.department_input.text()}\n{self.strength_input.text()}\n{self.section_input.text()}")
                        # Writing the current result name to currentproject.uet file
                        with open("currentproject.uet", "w") as r:
                            r.write(self.name_input.text())
                        # Show success message
                        QMessageBox.information(self, "Info", "Result file created successfully.")
                        # Call the function to move to the next page (not implemented here)
                        MainPage.validate_page2(self) 
                    else:
                        QMessageBox.critical(self, "Error", "Result file already exists.")
                else:
                    QMessageBox.critical(self, "Error", "Please enter valid input.")
            else:
                QMessageBox.critical(self, "Error", "Please fill all the fields.")
        
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Value Error: {str(e)}")











class Page2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        go_back_button = QPushButton("Go Back", self)
        go_back_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        go_back_button.clicked.connect(self.go_back)
        top_layout.addWidget(go_back_button)
        title_label = QLabel("Enter Result Details", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("color: #2C3E50; margin-bottom: 30px;")
        top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        top_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(top_layout)
        form_layout = QVBoxLayout()
        self.name_input = self.create_input_field("Enter Name")
        self.rollno_input = self.create_input_field("Enter Roll No.")
        self.aict_obtain_input = self.create_input_field("AICT Obtained Marks")
        self.aict_total_input = self.create_input_field("AICT Total Marks")
        self.pf_obtain_input = self.create_input_field("PF Obtained Marks")
        self.pf_total_input = self.create_input_field("PF Total Marks")
        self.dm_obtain_input = self.create_input_field("DM Obtained Marks")
        self.dm_total_input = self.create_input_field("DM Total Marks")
        self.ap_obtain_input = self.create_input_field("AP Obtained Marks")
        self.ap_total_input = self.create_input_field("AP Total Marks")
        self.calculus_obtain_input = self.create_input_field("Calculus Obtained Marks")
        self.calculus_total_input = self.create_input_field("Calculus Total Marks")
        form_layout.addWidget(QLabel("Name:"))
        form_layout.addWidget(self.name_input)
        form_layout.addWidget(QLabel("Roll No:"))
        form_layout.addWidget(self.rollno_input)
        form_layout.addWidget(QLabel("AICT Marks:"))
        form_layout.addLayout(self.create_row(self.aict_obtain_input, self.aict_total_input))
        form_layout.addWidget(QLabel("PF Marks:"))
        form_layout.addLayout(self.create_row(self.pf_obtain_input, self.pf_total_input))
        form_layout.addWidget(QLabel("DM Marks:"))
        form_layout.addLayout(self.create_row(self.dm_obtain_input, self.dm_total_input))
        form_layout.addWidget(QLabel("AP Marks:"))
        form_layout.addLayout(self.create_row(self.ap_obtain_input, self.ap_total_input))
        form_layout.addWidget(QLabel("Calculus Marks:"))
        form_layout.addLayout(self.create_row(self.calculus_obtain_input, self.calculus_total_input))
        self.open_result_checkbox = QCheckBox("Open result file after creating", self)
        form_layout.addWidget(self.open_result_checkbox)
        create_results_button = ModernButton("Create Results", self)
        create_results_button.clicked.connect(self.create_results)
        form_layout.addWidget(create_results_button)
        layout.addLayout(form_layout)
        self.setLayout(layout)
    def create_input_field(self, placeholder):
        line_edit = QLineEdit(self)
        line_edit.setPlaceholderText(placeholder)
        line_edit.setStyleSheet("""
            QLineEdit {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
                color: #2C3E50;
                font-size: 16px;
            }
            QLineEdit:focus {
                border-color: #2980b9;
                background-color: #ffffff;
            }
        """)
        return line_edit
    def create_row(self, obtained_input, total_input):
        row_layout = QHBoxLayout()
        row_layout.addWidget(obtained_input)
        row_layout.addWidget(total_input)
        return row_layout
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
    def create_results(self):
        try:
            if self.name_input.text().replace(" ","").isalpha() and self.rollno_input.text().replace(" ","").isdigit() and self.aict_obtain_input.text().replace(" ","").isdigit() and self.aict_total_input.text().replace(" ","").isdigit() and self.pf_obtain_input.text().replace(" ","").isdigit() and self.pf_total_input.text().replace(" ","").isdigit() and self.ap_obtain_input.text().replace(" ","").isdigit() and self.ap_total_input.text().replace(" ","").isdigit() and self.dm_obtain_input.text().replace(" ","").isdigit() and self.dm_total_input.text().replace(" ","").isdigit() and self.calculus_obtain_input.text().replace(" ","").isdigit() and self.calculus_total_input.text().replace(" ","").isdigit():
                if int(self.aict_obtain_input.text())<=int(self.aict_total_input.text()) and int(self.pf_obtain_input.text())<=int(self.pf_total_input.text()) and int(self.ap_obtain_input.text())<=int(self.ap_total_input.text()) and int(self.dm_obtain_input.text())<=int(self.dm_total_input.text()) and int(self.calculus_obtain_input.text())<=int(self.calculus_total_input.text()):
                    obtain_marks = int(self.aict_obtain_input.text()) + int(self.pf_obtain_input.text()) + int(self.ap_obtain_input.text()) + int(self.dm_obtain_input.text()) + int(self.calculus_obtain_input.text())
                    total_marks = int(self.aict_total_input.text()) + int(self.pf_total_input.text()) + int(self.ap_total_input.text()) + int(self.dm_total_input.text()) + int(self.calculus_total_input.text())
                    with open("currentproject.uet","r") as r:
                        result_name = r.read()
                        with open("Resultcards/"+result_name+"/"+"details.uet","r") as d:
                            details = d.read().split("\n")
                            print(details)
                        shutil.copy("source.mb","Resultcards/"+ result_name + "/" + self.name_input.text()+".html")
                        # Opening File in Read/Write Format to remove previous content and adding the updated one.
                        with open("Resultcards/"+result_name + "/" +self.name_input.text()+".html","r+") as s:
                            before = s.read()
                            after = before.replace("<uni-name>",details[0])\
                                            .replace("<std-name>",self.name_input.text())\
                                            .replace("<sect-ion>",details[3])\
                                            .replace("<department>",details[1])\
                                            .replace("<roll-no>",details[2])\
                                            .replace("<total-marks>",str(total_marks))\
                                            .replace("<percentage-total>",str(int((obtain_marks/total_marks)*100))+"%")\
                                            .replace("<grade-total>",self.grade(obtain_marks,total_marks))\
                                            .replace("<aict-obtain>",self.aict_obtain_input.text())\
                                            .replace("<aict-total>",self.aict_total_input.text())\
                                            .replace("<aict-grade>",self.grade(self.aict_obtain_input.text(),self.aict_total_input.text()))\
                                            .replace("<pf-obtain>",self.pf_obtain_input.text())\
                                            .replace("<pf-total>",self.pf_total_input.text())\
                                            .replace("<pf-grade>",self.grade(self.pf_obtain_input.text(),self.pf_total_input.text()))\
                                            .replace("<ap-obtain>",self.ap_obtain_input.text())\
                                            .replace("<ap-total>",self.ap_total_input.text())\
                                            .replace("<ap-grade>",self.grade(self.ap_obtain_input.text(),self.ap_total_input.text()))\
                                            .replace("<dm-obtain>",self.dm_obtain_input.text())\
                                            .replace("<dm-total>",self.dm_total_input.text())\
                                            .replace("<dm-grade>",self.grade(self.dm_obtain_input.text(),self.dm_total_input.text()))\
                                            .replace("<calculus-obtain>",self.calculus_obtain_input.text())\
                                            .replace("<calculus-total>",self.calculus_total_input.text())\
                                            .replace("<calculus-grade>",self.grade(self.calculus_obtain_input.text(),self.calculus_total_input.text()))\
                                            .replace("<comments>",self.comments(self.name_input.text(),(obtain_marks/total_marks)*100))
                            print(after)
                            s.seek(0) 
                            s.write(after) 
                            if self.open_result_checkbox.isChecked():
                                webbrowser.open(os.path.dirname(os.path.abspath(__file__)) + "/" + "Resultcards/"+result_name + "/" +self.name_input.text()+".html")
                            self.name_input.clear()
                            self.rollno_input.clear()
                            self.aict_obtain_input.clear()
                            self.aict_total_input.clear()
                            self.pf_obtain_input.clear()
                            self.pf_total_input.clear()
                            self.dm_obtain_input.clear()
                            self.dm_total_input.clear()
                            self.ap_obtain_input.clear()
                            self.ap_total_input.clear()
                            self.calculus_obtain_input.clear()
                            self.calculus_total_input.clear()
                else:
                    QMessageBox.critical(self,"Error","Obtained Marks cannot be greater than total marks.")
            else:
                print("False")
                QMessageBox.critical(self,"Error","Please enter valid input")
        except ValueError:
            QMessageBox.critical(self,"Error",ValueError)
    def go_back(self):
            self.window().show_page(0) 













class Page3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        go_back_button = QPushButton("Go Back", self)
        go_back_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 14px;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        go_back_button.clicked.connect(self.go_back)
        top_layout.addWidget(go_back_button)
        title_label = QLabel("View Result Files", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setStyleSheet("color: #2C3E50; margin-bottom: 30px;")

        top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        top_layout.addWidget(title_label, alignment=Qt.AlignCenter)
        top_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(top_layout)

        self.result_files_list = QListWidget(self)
        self.result_files_list.setStyleSheet("""
            QListWidget {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
            }
            QListWidget:item {
                font-size: 16px;
                padding: 10px;
            }
            QListWidget:item:selected {
                background-color: #3498db;
                color: white;
            }
        """)
        self.results_list = QListWidget(self)
        self.results_list.setStyleSheet("""
            QListWidget {
                background-color: #ecf0f1;
                border: 2px solid #3498db;
                border-radius: 10px;
                padding: 10px;
            }
            QListWidget:item {
                font-size: 16px;
                padding: 10px;
            }
            QListWidget:item:selected {
                background-color: #3498db;
                color: white;
            }
        """)

        lists_layout = QVBoxLayout()

        result_files_label = QLabel("Result Files:", self)
        result_files_label.setFont(QFont("Arial", 14, QFont.Bold))
        result_files_label.setAlignment(Qt.AlignCenter)
        lists_layout.addWidget(result_files_label)
        lists_layout.addWidget(self.result_files_list)

        selected_results_label = QLabel("Selected Results:", self)
        selected_results_label.setFont(QFont("Arial", 14, QFont.Bold))
        selected_results_label.setAlignment(Qt.AlignCenter)
        lists_layout.addWidget(selected_results_label)
        lists_layout.addWidget(self.results_list)
        layout.addLayout(lists_layout)

        buttons_layout = QHBoxLayout()
        load_result_button = ModernButton("Load Result File", self)
        load_result_button.clicked.connect(self.load_result_file)
        open_result_button = ModernButton("Open Selected Result", self)
        open_result_button.clicked.connect(self.open_selected_result)
        buttons_layout.addWidget(load_result_button)
        buttons_layout.addWidget(open_result_button)
        buttons_layout.setAlignment(Qt.AlignCenter)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        self.load_result_files()

    def go_back(self):
        self.window().show_page(0) 

    def load_result_files(self):
        """Load the result files into the list widget."""
        if os.path.exists("Resultcards"):
            self.result_files_list.clear()
            result_files = [f for f in os.listdir("Resultcards") if os.path.isdir(os.path.join("Resultcards", f))]
            self.result_files_list.addItems(result_files)
        else:
            QMessageBox.warning(self, "Error", "Resultcards directory does not exist.")

    def load_result_file(self):
        """Load the selected result file and display the individual results."""
        selected_result_file = self.result_files_list.currentItem()
        if selected_result_file:
            result_folder = f"Resultcards/{selected_result_file.text()}"
            files = os.listdir(f"Resultcards/{selected_result_file.text()}")
            files.remove("details.uet")
            result_file = files_without_extension = [os.path.splitext(file)[0] for file in files]
            self.results_list.clear()
            if not len(result_file)==0:
                self.results_list.addItems(result_file)
        else:
            QMessageBox.warning(self, "Error", "Please select a result file to load.")

    def open_selected_result(self):
        """Open the selected result."""
        selected_result = self.results_list.currentItem()
        if selected_result:
            webbrowser.open(f"{os.getcwd()}/Resultcards/{self.result_files_list.currentItem().text()}/{selected_result.text()}.html")
        else:
            QMessageBox.warning(self, "Error", "Please select a result to open.")





class MainPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)

        title_label = QLabel("Students Result Manager", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont("Arial", 24, QFont.Bold))
        title_label.setStyleSheet("color: #2C3E50; margin-bottom: 30px;")
        layout.addWidget(title_label)

        button_layout = QHBoxLayout()

        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        button1 = ModernButton("Create Results File", self)
        button2 = ModernButton("Continue adding results", self)
        button3 = ModernButton("Lists of Results Created", self)
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)

        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        layout.addLayout(button_layout)

        button1.clicked.connect(self.show_page1)
        button2.clicked.connect(self.validate_page2)
        button3.clicked.connect(self.show_page3)
    def show_page1(self):
        self.window().show_page(1) 
    def show_page2(self):
        self.window().show_page(2)
    def show_page3(self):
        self.window().show_page(3) 
    def validate_page2(self):
        r = open("currentproject.uet","r")
        current_project = r.readline()
        r.close()
        if current_project.replace(" ","") == "":
            QMessageBox.information(self,"Error","Please Create Result File First.")
        elif not os.path.isfile(f"Resultcards/{current_project}/details.uet"):
            print(f"Resultcards/{current_project}/details.uet")
            QMessageBox.information(self,"Error","Current result file is missing or corrupt. Please create a new result file.")
        else:
            self.window().show_page(2)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Students Result Manager")
        self.setGeometry(200, 200, 800, 500)

        font = QFont("Arial", 14)
        self.setFont(font)

        self.create_menu()

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        self.stacked_widget = QStackedWidget(self)
        central_widget.setLayout(QVBoxLayout())
        central_widget.layout().addWidget(self.stacked_widget)

        self.main_page = MainPage()
        self.page1 = Page1()
        self.page2 = Page2()
        self.page3 = Page3()

        self.stacked_widget.addWidget(self.main_page)  
        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.page3)

        self.show_page(0)

    def create_menu(self):

        menubar = self.menuBar()
        menubar.setStyleSheet("""
            QMenuBar {
                background-color: #2C3E50;
                color: white;
            }
            QMenuBar::item {
                padding: 10px;
            }
            QMenuBar::item:selected {
                background-color: #34495E;
            }
            QMenu {
                background-color: #34495E;
                color: white;
            }
            QMenu::item:selected {
                background-color: #3498db;
            }
        """)

        file_menu = menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        help_menu = menubar.addMenu("Help")
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)

    def show_about(self):
        webbrowser.open("about.html")

    def show_page(self, index):
        # Switch to the page by index
        self.stacked_widget.setCurrentIndex(index)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())