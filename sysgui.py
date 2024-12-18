from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter.messagebox

from mainmenu import mainmenuC
from search import StudentSearch
from studentinfoT import StudentInfo
from add_studyante import studentregistration
from print_studyante import printstudent

stu = StudentInfo()
stu.read_file()
addstu = studentregistration(stu.studentlist, StudentInfo)
student_search = StudentSearch()
printstu = printstudent(stu.studentlist)
attempts = 0

win = Tk()
win.geometry(f"970x800+{(win.winfo_screenwidth()-970)//2}+{(win.winfo_screenheight()-800)//2}")
win.config(bg="#B3C8CF")

def info():
    hover(0)
    pack_forget()
    cont1_div.pack(side="left", fill="both", expand=True)
def search():
    hover(1)
    pack_forget()
    cont2_div.pack(side="left", fill="both", expand=True)
    student_search.show_search_ui(cont2_div, stu)
def register():
    hover(2)
    pack_forget()
    cont3_div.pack(side="left", fill="both", expand=True)
def studentlist():
    hover(3)  # Highlight the "Registered Students" button
    pack_forget()  # Hide all other sections
    cont4_div.pack(side="left", fill="both", expand=True)  # Show the Registered Students section
def logouts():
    pass

def login_confirm():
    global user
    student_id = login_entry.get().strip()
    user = student_search.verify_login(stu.studentlist, student_id)
    
    if user:
        tkinter.messagebox.showinfo("Login Successful", f"Welcome, {user.get_name()}!")
        login_frame.pack_forget()
        main_div.pack(fill="both", expand=True)
        stu.show_about_ui(container[0], user)
    else:
        global attempts
        attempts += 1
        if attempts >= 4:
            tkinter.messagebox.showerror("Access Denied", "Too many failed attempts. Exiting...")
            win.destroy()
        else:
            tkinter.messagebox.showwarning("Login Failed", f"Invalid Student ID. Attempts left: {4 - attempts}")
    
def logout_confirm():
    tkinter.messagebox.showinfo("Logout", "You have been logged out.")
    exit()

def exit2():
    tkinter.messagebox.showinfo("Exiting...", "Come back another time.")
    exit()

def pack_forget(): 
    cont1_div.pack_forget()
    cont2_div.pack_forget()
    cont3_div.pack_forget()
    cont4_div.pack_forget()
    cont5_div.pack_forget()
    
def open_frame(frame_open, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped():
            close[i].pack_forget()
    frame_open.pack(side="right", fill="y")

def hover(active_btn):
    
    for i, btn in enumerate(btns):
        if i == active_btn:
            btn.config(bg="dodgerblue", fg="white")
        else:
            btn.config(bg="#e3e3e3", fg="black")

btns = []; container = []
func = [info, search, register, studentlist, logouts]
btn_txt = ["About You", "Search a Student", "Register", "Registered Students", "Logout"]

#login h
login_frame = Frame(win, bg="#3E5879")
login_frame.pack(fill="both", expand=True)

login_form = Frame(login_frame, bg="#F5EFE7", padx = 20, pady = 20)
login_form.place(relx=0.5, rely=0.5, anchor="center")

Label(login_form, text="Student Database System", font=("Century Gothic", 20, "bold"), bg="#F5EFE7").pack(pady=10)
Label(login_form, text="Enter Student ID:", font=("Century Gothic", 14), bg="#F5EFE7", fg="black").pack(pady=5)

login_btn = Button(login_form, text="Login", bg="skyblue", width=20, font=("Century Gothic", 20, "bold"))
exit_btn = Button(login_form, text="Exit", bg="red", width=20, font=("Century Gothic", 20, "bold"))

login_entry = Entry(login_form, font=("Century Gothic", 14), width=30)
login_entry.pack(pady=5)

login_btn.pack(pady=10), exit_btn.pack(pady=10)
login_btn.config(command = login_confirm)
exit_btn.config(command = exit2)

# menu
main_div = Frame(win, bg="#B3C8CF") 
#main_div.pack(side="left", fill="both", expand=True)

menu_div = Frame(main_div, bg="#E5E1DA") 
menu_div.pack(side="left", fill="y")

content_frame = Frame(menu_div, border=0, bg="#E5E1DA")
content_frame.pack(side="right", fill="y")

# content divs
cont1_div = Frame(main_div, bg="#F1F0E8") 
Label(cont1_div, text="About You Section", font=("Century Gothic", 16), pady=15).pack(pady=20)

cont2_div = Frame(main_div, bg="#F1F0E8")  
Label(cont2_div, text="Search a Student Section", font=("Century Gothic", 16), pady=15).pack(pady=20)

cont3_div = Frame(main_div, bg="#F1F0E8") 
Label(cont3_div, text="Register Section", font=("Century Gothic", 16), pady=15).pack(pady=20)

cont4_div = Frame(main_div, bg="#F1F0E8")  


cont5_div = Frame(main_div, bg="#F1F0E8")  
Label(cont5_div, text="Logout", font=("Century Gothic", 16), pady=15).pack(pady=20)

#label
Label(menu_div, text="Main Menu", font=("Century Gothic", 16), bg="#E5E1DA", fg="black", pady=20).pack()

for i in range(len(btn_txt)-1):
    container.append(Frame(content_frame, bg="#B3C8CF", pady=8))
    Label(container[i], text=btn_txt[i], font=("Century Gothic", 20 , "bold"), bg="#F1F0E8", width=45, anchor="center").grid(row=0, column=0, columnspan=5)

func1 = [
    partial(open_frame, container[0], [container[1], container[2], container[3]]),
    partial(open_frame, container[1], [container[0], container[2], container[3]]),
    partial(open_frame, container[2], [container[1], container[0], container[3]]),
    lambda: (open_frame(container[3], [container[0], container[1], container[2]]), printstu.show_registered_students(cont4_div, stu)),
    logout_confirm,
]

# buttons for loop
for i in range(len(btn_txt)):
    btn = Button(menu_div, text=btn_txt[i], font=("Century Gothic", 14), bg="#89A8B2", fg="black",width=20, padx=10, pady=15, command=func[i])
    btn.pack(pady=5)
    btns.append(btn)
    btns[i].config(command=func1[i])

# functions for the buttons
student_search.show_search_ui(container[1], stu)
addstu.show_reg_ui(container[2])
printstu.show_registered_students(container[3], stu)

btns[4].config(command = logout_confirm)

win.title("Student Information System - Created by Cawaling. All rights reserved.")
win.mainloop()