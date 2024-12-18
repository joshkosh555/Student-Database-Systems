from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter.messagebox

class printstudent:
    def __init__(self, students=None):
        self.students = students if students else []
    def print_allstudents(self, studentlist):
        print("\n==================== ALL STUDENT'S INFORMATION ====================")
        for student in studentlist:
            print(f"\n{student}")
        print("\n==================== NOTHING FOLLOWS ====================")
        
    def show_registered_students(self, container, studentinfo):
        for widget in container.winfo_children():
            widget.destroy()

        columns = ("ID", "Name", "Age", "Email", "Phone Number")
        tree = ttk.Treeview(container, columns=columns, show="headings", height=15)
        tree.pack(fill="both", expand=True, padx=54, pady=15, anchor="center")

        tree.heading("ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Email", text="Email")
        tree.heading("Phone Number", text="Phone Number")

        tree.column("ID", width=100, anchor="center")
        tree.column("Name", width=150, anchor="w")
        tree.column("Age", width=50, anchor="center")
        tree.column("Email", width=150, anchor="w")
        tree.column("Phone Number", width=150, anchor="w")

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        for student in studentinfo.studentlist:
            tree.insert("", "end", values=(student.get_id_number(), student.get_name(), student.get_age(), student.get_email(), student.get_phone_number(),),)

        Button(container, text="Refresh", command=lambda: self.show_registered_students(container, studentinfo), bg="#D8C4B6", font=("Century Gothic", 18, "bold"), padx=10, pady=5,).pack(pady=10)