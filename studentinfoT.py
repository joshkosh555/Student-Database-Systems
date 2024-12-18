from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter.messagebox

class StudentInfo:

    def __init__(self, name=None, age=None, id_number=None, email=None, phone_number=None):
        self._name = name
        self._age = age
        self._id_number = id_number
        self._email = email
        self._phone_number = phone_number
        self.studentlist = []
        
    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def get_id_number(self):
        return self._id_number
    
    def get_email(self):
        return self._email
    
    def get_phone_number(self):
        return self._phone_number
    
    def set_name(self, name):
        self._name = name
    
    def set_age(self, age):
        self._age = age
    
    def set_id_number(self, id_number):
        self._id_number = id_number
    
    def set_email(self, email):
        self._email = email
    
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def __str__(self):
        return f"Name: {self._name}\nAge: {self._age}\nID Number: {self._id_number}\nE-mail: {self._email}\nPhone Number: {self._phone_number}"
    
    def read_file(self):
        try:
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    # Splitting the line by commas and stripping extra spaces
                    parts = line.strip().split(", ")
                    if len(parts) == 5:  # Ensure correct number of columns
                        name, age, id_number, email, phone_number = parts
                        # Create StudentInfo object and add it to the list
                        student = StudentInfo(name, age, id_number, email, phone_number)
                        self.studentlist.append(student)
        except FileNotFoundError:
            print("Error: student_data.txt not found.")

    def show_about_ui(self, about_frame, user):
        # User Attributes
        attributes = ["Name", "Age", "ID Number", "Email", "Phone Number"]
        values = [user.get_name(), user.get_age(), user.get_id_number(), user.get_email(), user.get_phone_number()]

        # Display the user's information in a grid
        for i, (attribute, value) in enumerate(zip(attributes, values)):
            Label(about_frame, text=f"{attribute}", font=("Century Gothic", 18, "bold"), bg="#E5E1DA", anchor="w").grid(row=i+1, column=0, padx=10, pady=20, sticky="w")
            Label(about_frame, text=value, font=("Century Gothic", 18, "bold"), bg="white", anchor="w").grid(row=i+1, column=1, columnspan=4, padx=10, pady=20, sticky="nsew")

