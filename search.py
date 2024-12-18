from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter.messagebox

class StudentSearch:
    @staticmethod
    def search_student(listHere, keyword):
        for student in listHere:
            if student.get_id_number() == keyword:
                return student  # Return the student object if found
        return None

    def verify_login(self, listHere, studentid):
        for student in listHere:
            if student.get_id_number() == studentid:
                print("Login Successful!")
                return student
        else:
            print("No student found with that ID. Please try again.")
        return False

    def show_search_ui(self, search_frame, stu):
            self.lblSearchResults = Label(search_frame, text="", font=("Century Gothic", 18, "bold"), fg="red")
            self.lblSearchResults.grid(row=6, column=0, columnspan=6, padx=25, pady=15, sticky="nsew")
            self.lblSearchResults.configure(bg=search_frame.cget("bg"))

            Label(search_frame, text="Enter Student ID:", font=("Century Gothic", 18, "bold"), bg="#E5E1DA", anchor="w").grid(row=1, column=0, padx=10, pady=20, sticky="w")
            self.search_entry = Entry(search_frame, width=30, font=("Century Gothic", 18))
            self.search_entry.grid(row=1, column=1, columnspan=4, padx=10, pady=20, sticky="w")

            search_btn = Button(search_frame, text="Search", font=("Century Gothic", 18, "bold"), width=7, bg="#D8C4B6", padx=10, pady=10, command=partial(self.perform_search, stu))
            search_btn.grid(row=2, column=0, columnspan=6, pady=10)

            

    def perform_search(self, stu):
        student_id = self.search_entry.get().strip()
        
        if not student_id:
            self.lblSearchResults.config(text="Student ID is required.")
            return

        student = self.search_student(stu.studentlist, student_id)

        if student:
            self.lblSearchResults.config(text=f"{student}")
        else:
            self.lblSearchResults.config(text="Student not found.")