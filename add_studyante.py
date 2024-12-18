from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter.messagebox

class studentregistration:
    def __init__(self, studentlist, studinfo):
        self.studentlist = studentlist 
        self.studinfo = studinfo  

    def add_student(self, name=None, age=None, id_number=None, email=None, phone_number=None):
        if not name:
            print("\n=== Add New Student ===")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            id_number = input("Enter Student ID: ")
            email = input("Enter Email Address: ")
            phone_number = input("Enter Phone Number: ")

        new_student = self.studinfo(name, age, id_number, email, phone_number)
        
        self.studentlist.append(new_student)
        
        self.write_to_file(new_student)
        
        print(f"\nAdded student {name} to the list.")
        
        return new_student

    def write_to_file(self, student):
        try:
            with open("student_data.txt", "a+") as file:
                file.write(f"{student.get_name()}, {student.get_age()}, {student.get_id_number()}, {student.get_email()}, {student.get_phone_number()}\n")
                print(f"Student {student.get_name()} has been saved to the database.")
        except Exception as e:
            print(f"Error writing to file: {e}")

    def show_reg_ui(self, reg_frame):
        self.lblErrors = Label(reg_frame, text="", font=("Century Gothic", 18, "bold"), fg="red")
        self.lblErrors.grid(row=7, column=0, columnspan=6, padx=25, pady=15)
        self.lblErrors.configure(bg=reg_frame.cget("bg"))

        self.reg_txt = ["Name", "Age", "ID Number", "Email", "Phone Number"]
        self.reg_entry = [] 

        for i, field in enumerate(self.reg_txt):
            Label(reg_frame, text=field, font=("Century Gothic", 18, "bold",),bg="#E5E1DA", anchor="w").grid(row=i+1, column=0, padx=10, pady=20, sticky="w")
            
            entry = Entry(reg_frame, width=30, font=("Century Gothic", 18))
            entry.grid(row=i+1, column=1, padx=10, pady=20, columnspan=4)
            self.reg_entry.append(entry)

        reg_btn = Button(reg_frame, text="Register", font=("Century Gothic", 18, "bold"), width=7, 
                        bg="#D8C4B6", command=self.check_entries, padx=10, pady=10)
        reg_btn.grid(row=len(self.reg_txt)+1, column=0, columnspan=5, pady=10)

    def check_entries(self):
        errors = []
        for i, entry in enumerate(self.reg_entry):
            if not entry.get().strip(): 
                errors.append(f"- {self.reg_txt[i]} is required")

        if errors:
            self.lblErrors.config(text="The following errors occurred:\n" + "\n".join(errors))
        else:
            name = self.reg_entry[0].get().strip()
            age = self.reg_entry[1].get().strip()
            id_number = self.reg_entry[2].get().strip()
            email = self.reg_entry[3].get().strip()
            phone_number = self.reg_entry[4].get().strip()

            self.add_student(name, age, id_number, email, phone_number) 
            tkinter.messagebox.showinfo("Registration Success", f"Student '{name}' has been successfully registered.")
            
            for entry in self.reg_entry:
                entry.delete(0, END)

            self.lblErrors.config(text="")