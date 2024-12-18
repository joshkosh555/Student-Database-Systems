from mainmenu import mainmenuC
from search import StudentSearch
from studentinfoT import StudentInfo
from add_studyante import studentregistration
from print_studyante import printstudent


stu = StudentInfo()
stu.read_file()
addstu = studentregistration(stu.studentlist, StudentInfo)
student_search = StudentSearch()
printstu = printstudent()

mainmenu = mainmenuC(stu.studentlist, addstu, student_search, printstu)  

attempts = 0
while attempts < 4:
    print("="*10, "Login - Students InfoSys", "="*10)
    login_check = input("Enter Students ID:")
    user = student_search.verify_login(stu.studentlist, login_check)
    if user:
        mainmenu.mainm(stu.studentlist, user)  
        break  
    else:
        attempts += 1
        print("Wrong Student ID")
if attempts == 4:
    print("Too many failed attempts. Exiting...")
    exit()